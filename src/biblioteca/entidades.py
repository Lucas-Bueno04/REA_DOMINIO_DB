"""Constrói as ferramentas MCP de uma entidade do modelo (uma tabela): `<entidade>_consultar` (genérica, com filtros, ordenação e paginação) e
`<entidade>_obter` (um registro pela chave). A descrição que o modelo de IA lê é montada do próprio modelo (o que é a tabela, filtros, domínios,
regras de negócio, privacidade, exemplos), então muda junto com os YAML sem reescrever arquivos.
"""
from __future__ import annotations

import json
import keyword
import re
from typing import Any

from biblioteca.base import Ferramenta, Param, nome_seguro
from biblioteca.contexto import contexto
from server import sqlbuilder as sb
from server.motor import ErroUso

RESERVADOS = {"empresa", "colunas", "ordem", "limite", "offset", "contar", "decodificar"}
OPS_TEXTO = {"eq": "igual", "in": "lista de valores", "entre": "{\"entre\":[a,b]}", "gte": "{\"gte\":v}", "lte": "{\"lte\":v}",
             "contem": "{\"contem\":\"x\"}", "prefixo": "{\"prefixo\":\"x\"}"}
VOLUME = {"pequeno": "pequena (até alguns milhares de linhas)", "medio": "média", "grande": "GRANDE (milhões de linhas: use filtros e limite)"}


def _liso(txt: str | None) -> str:
    return re.sub(r"\s+", " ", (txt or "").strip())


def _corta(txt: str, n: int) -> str:
    """Corta em n caracteres, preferindo terminar numa frase/vírgula completa em vez de no meio da palavra."""
    if len(txt) <= n:
        return txt
    c = txt[: n - 1]
    k = max(c.rfind(". "), c.rfind("; "), c.rfind(", "))
    return (c[: k + 1] if k > n * 0.6 else c).rstrip() + " […]"


def _norm_t(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


FORTE = re.compile(r"(^|_)(cpf|nascimento|email|e_mail|telefone|fone|endereco|logradouro|salario|remuneracao|liquido|nit|login|usuario|ip|maquina|estacao)(_|$)|numero_do_pis|pis_pasep")
FRACO = re.compile(r"(^|_)nome(_|$)")
PESSOA = re.compile(r"empregad|socio|cliente|fornecedor|pessoa|dependente|responsavel|contador|usuario|salari|funcion|contribuinte|locat|prestador|beneficiario|autonomo|favorecid|procurador")
SENTINELA = "DATAS SENTINELA: 1900-01-01 (não informada), 2050-12-31, 2100-01-31 e 3000-12-01 (sem fim) são valores padrão do sistema, não datas reais."


def _col(v) -> str:
    return v["coluna"] if isinstance(v, dict) else v


def nome_param(nome: str) -> str:
    """Nome do parâmetro da ferramenta para o filtro `nome` (evita colisão com os parâmetros fixos e com palavras reservadas do Python)."""
    if nome in RESERVADOS or keyword.iskeyword(nome) or not nome.isidentifier():
        return f"filtro_{re.sub(r'[^a-zA-Z0-9_]', '_', nome)}"
    return nome


def legenda_dominio(ctx, nome: str, maximo: int = 10) -> str:
    d = ctx.doms.get(nome) or {}
    vals = d.get("valores") or {}
    if not vals:
        return ""
    itens = [f"{k}={v}" for k, v in list(vals.items())[:maximo]]
    mais = f", … (+{len(vals) - maximo})" if len(vals) > maximo else ""
    conf = d.get("confirmado")
    aviso = "" if conf is True else " [significado NÃO confirmado: hipótese]" if conf is False else " [parcialmente confirmado]"
    return f"Códigos: {', '.join(itens)}{mais}{aviso}"


def _descricao_filtro(ctx, e: dict, nome: str, f: dict) -> str:
    cols = f["coluna"] if isinstance(f["coluna"], list) else [f["coluna"]]
    tipos = []
    for c in cols:
        ci = ctx.coluna(e["tabela"], c)
        tipos.append(f"{c} ({ci.get('tipo', '?')})")
    ops = ", ".join(OPS_TEXTO.get(o, o) for o in f["ops"])
    igual = "eq" in f["ops"] or "in" in f["ops"]
    txt = f"Filtra {' OU '.join(tipos)}. Aceita: " + ("valor simples (igualdade)" + (", " if ops else "") if igual else "SOMENTE os operadores abaixo (igualdade NÃO é aceita neste filtro): ") + ops + "."
    dom = next((v.get("dominio") for v in e["colunas"].values() if isinstance(v, dict) and _col(v).lower() == cols[0].lower() and v.get("dominio")), None)
    if dom:
        txt += " " + legenda_dominio(ctx, dom)
    ci = ctx.coluna(e["tabela"], cols[0])
    if ci.get("comentario"):
        txt += f" ({_liso(ci['comentario'])})"
    if ci.get("tipo") in ("date", "timestamp", "datetime"):
        txt += " Datas no formato AAAA-MM-DD."
    return txt


def _amostra_real(entidade: str) -> dict | None:
    """Empresa e filtros com que a validação obteve dados desta tabela (data/biblioteca_estado.db); None se ainda não houver."""
    global _AMOSTRAS
    if _AMOSTRAS is None:
        _AMOSTRAS = {}
        try:
            from biblioteca import estado
            c = estado.abrir()
            for r in c.execute("select entidade, empresa, filtros from amostra"):
                _AMOSTRAS[r["entidade"]] = {"empresa": json.loads(r["empresa"]), "filtros": json.loads(r["filtros"])}
            c.close()
        except Exception:
            pass
    return _AMOSTRAS.get(entidade)


_AMOSTRAS = None


def _exemplo(e: dict, nome_tool: str) -> dict:
    ac = e.get("acesso", {})
    args: dict[str, Any] = {}
    am = _amostra_real(nome_tool)
    if am:
        if am["empresa"] is not None:
            args["empresa"] = am["empresa"]
        for k, v in (am["filtros"] or {}).items():
            args["periodo" if k == "periodo" else nome_param(k)] = {"de": "2025-01-01", "ate": "2025-01-31"} if k == "periodo" else v
        args["limite"] = 20
        return {"descricao": "Chamada que devolveu dados na validação (ajuste empresa e filtros)", "argumentos": args}
    if ac.get("empresa"):
        args["empresa"] = 1
    for x in ac.get("exige_algum", [])[:1]:
        args["periodo" if x == "periodo" else nome_param(x)] = {"de": "2025-01-01", "ate": "2025-01-31"} if x == "periodo" else "<valor>"
    if not ac.get("exige_algum") and ac.get("periodo"):
        args["periodo"] = {"de": "2025-01-01", "ate": "2025-01-31"}
    args["limite"] = 20
    return {"descricao": "Primeira página dos registros (ajuste empresa e período)", "argumentos": args}


def _bloco_acesso(e: dict) -> list[str]:
    ac = e.get("acesso", {})
    out = []
    if ac.get("empresa"):
        out.append(f"OBRIGATÓRIO: 'empresa' (código da empresa na coluna {ac['empresa']}).")
    else:
        out.append("Tabela global (não depende de empresa): NÃO informe 'empresa'.")
    if ac.get("exige_algum"):
        nomes = ", ".join(nome_param(x) for x in ac["exige_algum"])
        out.append(f"OBRIGATÓRIO também: ao menos UM destes filtros (protege tabela de {VOLUME.get(ac.get('volume'), 'grande')}): {nomes}.")
    if ac.get("periodo"):
        per = ac["periodo"]
        col_per = f"{per['vinculo']}.{per['coluna']}" if isinstance(per, dict) else per
        out.append("Parâmetro 'periodo' = {\"de\":\"AAAA-MM-DD\",\"ate\":\"AAAA-MM-DD\"} filtra pela coluna " + str(col_per) + ". Linhas com essa coluna VAZIA nunca aparecem num filtro de período; "
                   "se a tabela tiver outro campo de competência ou data de referência (veja CAMPOS), prefira o filtro dele.")
    return out


def descricao_consultar(nome: str, e: dict) -> str:
    ctx = contexto()
    gerada = e.get("_gerada", False)
    tab = e["tabela"]
    linhas = ctx.linhas(tab)
    cab = f"{e.get('titulo', nome)} — tabela {tab} (módulo {e['_modulo']}" + (", ~" + f"{linhas:,}".replace(",", ".") + " linhas" if linhas else "") + ")."
    p = [cab]
    desc = _liso(e.get("descricao"))
    com_tab = _liso((ctx.tabelas.get(tab.lower()) or {}).get("comentario"))
    if desc:
        p.append("O QUE É: " + _corta(desc, 700))
    if com_tab and _norm_t(com_tab) not in _norm_t(desc + " " + e.get("titulo", "")):
        p.append("COMENTÁRIO DO BANCO SOBRE A TABELA: " + _corta(com_tab, 300))
    p.append("QUANDO USAR: para listar, filtrar e paginar registros desta tabela" + (" e entender seus códigos" if e.get("filtros") else "") + ". Para UM registro pela chave, use a ferramenta *_obter correspondente (quando existir).")
    p.extend(_bloco_acesso(e))
    filtros = e.get("filtros", {})
    if filtros:
        nomes = ", ".join(nome_param(n) for n in filtros)
        p.append("FILTROS: " + nomes + ". Cada filtro aceita um valor simples, uma lista ou um operador (ver o parâmetro).")
    campos = [c for c in e["colunas"]]
    calc = list(e.get("calculadas", {}))
    p.append("CAMPOS: " + _corta(", ".join(campos + calc), 1500) + ". Use 'colunas' para pedir só alguns; 'decodificar=true' acrescenta <campo>_descricao nos códigos.")
    enr = [c for v in e.get("vinculos", {}).values() for c in v["colunas"]]
    if enr:
        p.append("CAMPOS DE VÍNCULO (vêm de outras tabelas, preenchidos sozinhos): " + _corta(", ".join(enr), 400) + ".")
    am = _amostra_real(nome)
    if am and am["empresa"] is not None:
        p.append(f"EXEMPLO COM DADOS: a empresa {am['empresa']} tem registros nesta tabela (use para testar).")
    regras = e.get("regras") or []
    if regras:
        rtxt = " | ".join(_corta(_liso(r), 350) for r in regras[:5])
        p.append(("REGRAS DE NEGÓCIO (conferidas nos dados): " if not gerada else "FATOS MEDIDOS NOS DADOS: ") + rtxt + (f" (+{len(regras) - 5} regras: veja descrever_entidade)" if len(regras) > 5 else ""))
    if e.get("privacidade"):
        p.append("PRIVACIDADE: " + _corta(_liso(e["privacidade"]), 300))
    sens = [a for a, v in e["colunas"].items() if isinstance(v, dict) and v.get("sensivel")]
    if sens:
        p.append("CAMPOS SENSÍVEIS (dado pessoal/financeiro; use só se a pergunta exigir): " + ", ".join(sens[:40]) + ("…" if len(sens) > 40 else ""))
    pessoa_tab = bool(PESSOA.search(_norm_t(tab + " " + e.get("titulo", ""))))
    todos = campos + enr
    pess = [c for c in todos if c not in sens and (FORTE.search(c) or (pessoa_tab and FRACO.search(c)))]
    if pess:
        p.append("POSSÍVEIS DADOS PESSOAIS/FINANCEIROS (os dados saem em claro; devolva só o que a pergunta exigir): " + ", ".join(pess[:30]) + ("…" if len(pess) > 30 else "") + ".")
    reais_l = {str(_col(v)).lower() for v in e["colunas"].values()}
    if "i_empregados" in reais_l or "foempregados" in {v["tabela"].lower() for v in e.get("vinculos", {}).values()}:
        p.append("PRIVACIDADE (folha): as linhas são de empregados identificáveis; evite listar pessoas sem necessidade.")
    datas = [c for c in e["colunas"].values() if (ctx.coluna(tab, _col(c)).get("tipo") or "").lower().startswith(("date", "timestamp"))]
    if datas:
        p.append(SENTINELA)
    chars = [f for f in e.get("filtros", {}).values() if not isinstance(f["coluna"], list) and (ctx.coluna(tab, f["coluna"]).get("tipo") or "").lower() == "char" and int(ctx.coluna(tab, f["coluna"]).get("tamanho") or 0) > 1]
    if chars:
        p.append("TEXTO: informe os códigos sem espaços (o servidor testa as variantes com brancos); na resposta, códigos de texto podem vir com espaços à esquerda.")
    if len(campos) <= 2:
        p.append("UTILIDADE LIMITADA: a tabela expõe só " + str(len(campos)) + " campo(s) (tabela de apoio/ligação); ela NÃO traz o conteúdo que o nome pode sugerir (XML, arquivo, etc.).")
    p.append("CONFIANÇA: " + ("modelo GERADO em lote (colunas e filtros medidos no banco; significados de códigos sem legenda NÃO são confirmados)." if gerada
                             else "modelo CURADO à mão e conciliado com os dados."))
    p.append("Somente leitura. Resposta paginada: use 'proximo_offset' para a página seguinte (limite máx. 500).")
    return "\n".join(p)


def parametros_consultar(nome: str, e: dict) -> tuple[list[Param], dict[str, str]]:
    ctx = contexto()
    ac = e.get("acesso", {})
    ps: list[Param] = []
    mapa: dict[str, str] = {}
    if ac.get("empresa"):
        ps.append(Param("empresa", f"Código da empresa (coluna {ac['empresa']}). Número ou lista de números.", int | list[int], obrigatorio=True))
    if ac.get("periodo"):
        ps.append(Param("periodo", "Período por data de referência: {\"de\":\"AAAA-MM-DD\",\"ate\":\"AAAA-MM-DD\"} (um dos dois basta).", dict | None))
        mapa["periodo"] = "periodo"
    for fn_, f in e.get("filtros", {}).items():
        if fn_ == "periodo" and ac.get("periodo"):
            continue                       # o parâmetro 'periodo' padrão já cobre
        pn = nome_param(fn_)
        mapa[pn] = fn_
        ps.append(Param(pn, _corta(_descricao_filtro(ctx, e, fn_, f), 500), Any))
    ps += [
        Param("colunas", "Campos desejados (padrão: todos). Veja CAMPOS na descrição.", list[str] | None),
        Param("ordem", "Ordenação, ex.: [\"data desc\", \"numero\"] (campos da entidade).", list[str] | None),
        Param("limite", "Linhas por página (1 a 500).", int, padrao=50, minimo=1, maximo=500),
        Param("offset", "Quantas linhas pular (use proximo_offset da resposta anterior).", int, padrao=0, minimo=0),
        Param("contar", "true devolve também o total de linhas do filtro (mais lento em tabelas grandes).", bool, padrao=False),
        Param("decodificar", "true acrescenta <campo>_descricao com o significado dos códigos conhecidos.", bool, padrao=False),
    ]
    return ps, mapa


def _executor_consultar(entidade: str, mapa: dict[str, str]):
    def run(motor, **kw):
        e = motor.ents[entidade]
        empresa = kw.pop("empresa", None)
        meta = {k: kw.pop(k) for k in ("colunas", "ordem", "limite", "offset", "contar", "decodificar") if k in kw}
        filtros = {mapa[k]: v for k, v in kw.items() if v is not None and k in mapa}
        ac = e.get("acesso", {})
        if ac.get("exige_algum") and not any(x in filtros for x in ac["exige_algum"]):
            raise ErroUso("Informe ao menos um destes filtros: " + ", ".join(nome_param(x) for x in ac["exige_algum"]) + ".")
        return motor.consultar_entidade(entidade, empresa, filtros or None, meta.get("colunas"), meta.get("ordem"), meta.get("limite") or 50,
                                        meta.get("offset") or 0, bool(meta.get("contar")), bool(meta.get("decodificar")))
    return run


def chave_para_filtros(e: dict) -> dict[str, str] | None:
    """Mapa {campo_da_chave: nome_do_filtro_eq} se TODA coluna da chave (exceto a de empresa) tem filtro de igualdade; senão None."""
    emp = (e.get("acesso", {}).get("empresa") or "").lower()
    out = {}
    for k in e["chave"]:
        if k.lower() == emp:
            continue
        fn_ = next((n for n, f in e.get("filtros", {}).items() if not isinstance(f["coluna"], list) and f["coluna"].lower() == k.lower() and "eq" in f["ops"]), None)
        if not fn_:
            return None
        out[k] = fn_
    return out or None


def ferramenta_consultar(nome: str, e: dict) -> Ferramenta:
    ps, mapa = parametros_consultar(nome, e)
    return Ferramenta(nome=nome_seguro(nome, "consultar"), descricao=descricao_consultar(nome, e), parametros=ps,
                      executar=_executor_consultar(nome, mapa), tipo="consultar", modulo=e["_modulo"], tabelas=[e["tabela"].lower()],
                      entidade=nome, titulo=f"Consultar {e.get('titulo', nome)}", gerada=e.get("_gerada", True), exemplos=[_exemplo(e, nome)])


def ferramenta_obter(nome: str, e: dict) -> Ferramenta | None:
    chave = chave_para_filtros(e)
    if not chave:
        return None
    ac = e.get("acesso", {})
    ps: list[Param] = []
    if ac.get("empresa"):
        ps.append(Param("empresa", f"Código da empresa (coluna {ac['empresa']}).", int, obrigatorio=True))
    mapa = {}
    for k, fn_ in chave.items():
        pn = nome_param(fn_)
        mapa[pn] = fn_
        ps.append(Param(pn, _corta(_descricao_filtro(contexto(), e, fn_, e["filtros"][fn_]), 400), Any, obrigatorio=True))
    desc = (f"{e.get('titulo', nome)} — obtém UM registro pela chave ({', '.join(e['chave'])}) da tabela {e['tabela']}. "
            f"Use quando já souber a chave (ex.: veio de outra consulta); para listar/filtrar use {nome_seguro(nome, 'consultar')}. "
            "Devolve {encontrado, registro}; sem registro, encontrado=false. Somente leitura.")

    def run(motor, **kw):
        empresa = kw.pop("empresa", None)
        filtros = {mapa[k]: v for k, v in kw.items() if k in mapa}
        r = motor.consultar_entidade(nome, empresa, filtros, None, None, 2, 0, False, True)
        linhas = r["linhas"]
        return {"entidade": nome, "tabela": e["tabela"], "encontrado": bool(linhas), "registro": linhas[0] if linhas else None,
                "aviso": "a chave retornou mais de um registro; confira os parâmetros" if len(linhas) > 1 else None}

    return Ferramenta(nome=nome_seguro(nome, "obter"), descricao=desc, parametros=ps, executar=run, tipo="obter", modulo=e["_modulo"],
                      tabelas=[e["tabela"].lower()], entidade=nome, titulo=f"Obter {e.get('titulo', nome)}", gerada=e.get("_gerada", True),
                      exemplos=[{"descricao": "Um registro pela chave", "argumentos": {**({"empresa": 1} if ac.get("empresa") else {}), **{nome_param(f): "<valor>" for f in chave.values()}}}])


def somaveis(e: dict) -> list[str]:
    ctx = contexto()
    cols = {k: v for k, v in ctx._cols.get(e["tabela"].lower(), {}).items()}
    return sb.campos_somaveis(e, cols) + list(e.get("calculadas", {}))


def ferramenta_totais(nome: str, e: dict) -> Ferramenta | None:
    """Totais por grupo (contagem + soma/média/mín/máx de campos numéricos), o caso de uso mais frequente sobre tabelas de movimento."""
    mets = [m for m in somaveis(e) if m not in e.get("calculadas", {})]
    if not mets:
        return None
    ctx = contexto()
    ps, mapa = parametros_consultar(nome, e)
    base = [p for p in ps if p.nome not in ("colunas", "ordem", "offset", "contar", "decodificar")]
    reais = {a: _col(v) for a, v in e["colunas"].items()}
    datas = [a for a, c in reais.items() if (ctx.coluna(e["tabela"], c).get("tipo") or "").lower().startswith(("date", "timestamp"))]
    agrup = [(f"{a}:mes" if a in datas else a) for a in list(e["colunas"])[:60] if a not in mets]
    base = [p for p in base if p.nome != "limite"]
    base += [
        Param("agrupar_por", "Campos para agrupar (veja CAMPOS PARA AGRUPAR). Datas exigem granularidade (campo:mes, campo:ano ou campo:dia); os demais campos entram sem sufixo. "
                             "Vazio = um total geral.", list[str] | None),
        Param("metricas", "Campos numéricos a totalizar (veja CAMPOS SOMÁVEIS na descrição). Vazio = só a contagem de linhas.", list[str] | None),
        Param("funcao", "soma | media | minimo | maximo (aplicada a todas as métricas).", str, padrao="soma"),
        Param("limite", "Máximo de grupos (1 a 500).", int, padrao=100, minimo=1, maximo=500),
        Param("decrescente", "true ordena os grupos do maior para o menor valor do agrupamento (ex.: meses mais recentes primeiro).", bool, padrao=False),
    ]
    com_dominio_t = [a for a, v in e["colunas"].items() if isinstance(v, dict) and v.get("dominio") and a not in mets]
    desc = (f"{e.get('titulo', nome)} — TOTAIS por grupo da tabela {e['tabela']} (módulo {e['_modulo']}). "
            "QUANDO USAR: perguntas de soma, contagem, média ou evolução desta tabela (totais por mês, por tipo, por situação...); evita trazer milhares de linhas. "
            + " ".join(_bloco_acesso(e)) + " "
            "CAMPOS SOMÁVEIS: " + ", ".join(mets) + ". "
            "CAMPOS PARA AGRUPAR: " + _corta(", ".join(agrup), 900) + ". "
            "Os filtros são os mesmos de " + nome_seguro(nome, "consultar") + ". Devolve {grupos, total_geral, truncado}; cada grupo traz 'linhas' (contagem) e a métrica como <funcao>_<campo>. "
            "ATENÇÃO: o total_geral soma tudo SEM SINAL e sem excluir exceções (cancelados, estornos, entrada x saída, débito x crédito): quando a tabela tiver um campo de natureza/tipo "
            + (f"({', '.join(com_dominio_t[:4])}) " if com_dominio_t else "") + "agrupe também por ele para não misturar sinais, e filtre o que não deve entrar. "
            + ("REGRAS DA TABELA QUE AFETAM OS TOTAIS: " + " | ".join(_corta(_liso(r), 450) for r in (e.get("regras") or [])[:4]) + ". " if e.get("regras") and not e.get("_gerada") else "")
            + "Somente leitura.")

    def run(motor, **kw):
        empresa = kw.pop("empresa", None)
        meta = {k: kw.pop(k, None) for k in ("agrupar_por", "metricas", "funcao", "limite", "decrescente")}
        filtros = {mapa[k]: v for k, v in kw.items() if v is not None and k in mapa}
        ac = e.get("acesso", {})
        if ac.get("exige_algum") and not any(x in filtros for x in ac["exige_algum"]):
            raise ErroUso("Informe ao menos um destes filtros: " + ", ".join(nome_param(x) for x in ac["exige_algum"]) + ".")
        return motor.agregar_entidade(nome, empresa, filtros or None, meta["agrupar_por"], meta["metricas"], meta["funcao"] or "soma", meta["limite"] or 100, bool(meta["decrescente"]))

    exemplo = _exemplo(e, nome)["argumentos"]
    exemplo.pop("limite", None)
    com_dominio = [a for a, v in e["colunas"].items() if isinstance(v, dict) and v.get("dominio") and a not in mets]
    escolha = next((a for a in agrup if a.endswith(":mes")), None) or (com_dominio[0] if com_dominio else (agrup[0] if agrup else None))
    exemplo.update({"agrupar_por": [escolha] if escolha else [], "metricas": mets[:1]})
    for q in base:
        if q.nome == "agrupar_por" and escolha:
            q.descricao += f" Exemplo desta tabela: [\"{escolha}\"]."
        if q.nome == "metricas":
            q.descricao += f" Exemplo: [\"{mets[0]}\"]."
    return Ferramenta(nome=nome_seguro(nome, "totais"), descricao=desc, parametros=base, executar=run, tipo="totais", modulo=e["_modulo"], tabelas=[e["tabela"].lower()],
                      entidade=nome, titulo=f"Totais de {e.get('titulo', nome)}", gerada=e.get("_gerada", True),
                      exemplos=[{"descricao": "Total por mês do primeiro campo somável", "argumentos": exemplo}])


def ferramentas_da_entidade(nome: str) -> list[Ferramenta]:
    e = contexto().ents[nome]
    out = [ferramenta_consultar(nome, e)]
    for f in (ferramenta_obter(nome, e), ferramenta_totais(nome, e)):
        if f:
            out.append(f)
    return out
