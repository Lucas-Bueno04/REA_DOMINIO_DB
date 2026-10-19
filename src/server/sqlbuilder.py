"""Gerador de SELECT a partir do modelo de entidades (semente da camada de consulta, Fase 4).

Princípios de segurança:
  * Identificadores (tabelas, colunas, aliases) vêm SOMENTE do modelo YAML validado — nunca do chamador.
  * Valores do chamador entram SEMPRE como parâmetros `?`.
  * Só gera SELECT. Paginação por `TOP n START AT m` (SQL Anywhere).
  * Filtro de empresa e filtros obrigatórios (`acesso`) são exigidos antes de gerar o SQL.
"""
import pathlib
import re

import yaml

RAIZ = pathlib.Path(__file__).resolve().parents[2]
_CARREGADOR = getattr(yaml, "CSafeLoader", yaml.SafeLoader)      # libyaml em C quando disponível: o carregamento do modelo cai de ~7 s para ~1 s
MODULOS = RAIZ / "src" / "model" / "modulos"
OWNER = "bethadba"
LIMITE_PADRAO, LIMITE_MAXIMO = 50, 500
_IDENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


class ErroConsulta(ValueError):
    pass


def carregar_modelo() -> tuple[dict, dict]:
    """Devolve (entidades, dominios) de todos os módulos."""
    ents, doms = {}, {}
    for arq in sorted(MODULOS.glob("*.yaml")):
        txt = arq.read_text(encoding="utf-8")
        d = yaml.load(txt, Loader=_CARREGADOR)
        gerado = "Gerado em lote" in txt[:200]      # módulos gerados por scripts/mapear_lote.py (regras = fatos medidos, sem curadoria)
        doms.update(d.get("dominios", {}))
        for n, e in d.get("entidades", {}).items():
            e["_modulo"] = d["modulo"]
            e["_gerada"] = gerado
            ents[n] = e
    return ents, doms


def _ident(x: str) -> str:
    if not _IDENT.match(x):
        raise ErroConsulta(f"identificador inválido no modelo: {x!r}")
    return x


def _real(v) -> str:
    return v["coluna"] if isinstance(v, dict) else v


def _escape_like(v: str) -> str:
    return v.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")


def _condicao(expr: str, op: str, valor, params: list) -> str:
    if op == "eq":
        params.append(valor); return f"{expr} = ?"
    if op in ("in", "in_pad"):           # in_pad = lista já expandida pelo motor com as variantes de brancos de CHAR (até 3 por valor pedido)
        if not isinstance(valor, (list, tuple)) or not valor:
            raise ErroConsulta("operador 'in' exige lista não vazia")
        if len(valor) > (500 if op == "in" else 1500):
            raise ErroConsulta("operador 'in' aceita no máximo 500 valores")
        params.extend(valor); return f"{expr} IN ({','.join('?' * len(valor))})"
    if op == "entre":
        if not isinstance(valor, (list, tuple)) or len(valor) != 2:
            raise ErroConsulta("operador 'entre' exige [inicio, fim]")
        params.extend(valor); return f"{expr} BETWEEN ? AND ?"
    if op == "branco":
        return f"TRIM({expr}) = ''"
    if op == "gte":
        params.append(valor); return f"{expr} >= ?"
    if op == "lte":
        params.append(valor); return f"{expr} <= ?"
    if op == "contem":
        params.append(f"%{_escape_like(str(valor))}%"); return f"{expr} LIKE ? ESCAPE '\\'"
    if op == "prefixo":
        params.append(f"{_escape_like(str(valor))}%"); return f"{expr} LIKE ? ESCAPE '\\'"
    raise ErroConsulta(f"operador desconhecido: {op}")


def montar_balancete(empresa: int, data_inicial, data_final, filial=None) -> tuple[str, list]:
    """Balancete de verificação por conta analítica (consulta agregada, modelo contabil.yaml → consultas.balancete).

    Saldo = débitos − créditos (positivo = devedor). A conta é resolvida pelo PLANO do lançamento (codi_emp_plano).
    Retorna (sql, params). Todos os valores entram como parâmetros.
    """
    filt_fil = " AND fili_lan = ?" if filial is not None else ""
    lado = ("SELECT codi_emp_plano AS plano, {c} AS conta, data_lan AS dt, {d} AS deb, {k} AS cre "
            f"FROM {OWNER}.ctlancto WHERE codi_emp = ? AND {{c}} <> 0 AND data_lan <= ?{filt_fil}")
    params = []
    for _ in range(2):
        params += [int(empresa), data_final] + ([int(filial)] if filial is not None else [])
    # ordem dos '?' no SQL final: (débito: emp, fim, [fil]) (crédito: emp, fim, [fil]) (saldo anterior: ini) (débitos: ini) (créditos: ini)
    params += [data_inicial, data_inicial, data_inicial]
    sql = (
        "SELECT m.plano AS plano_empresa, m.conta AS conta_codigo, c.clas_cta AS classificacao, c.nome_cta AS nome, c.tipo_cta AS tipo, "
        "SUM(CASE WHEN m.dt < ? THEN m.deb - m.cre ELSE 0 END) AS saldo_anterior, "
        "SUM(CASE WHEN m.dt >= ? THEN m.deb ELSE 0 END) AS debitos, "
        "SUM(CASE WHEN m.dt >= ? THEN m.cre ELSE 0 END) AS creditos "
        "FROM (" + lado.format(c="cdeb_lan", d="vlor_lan", k="0") + " UNION ALL " + lado.format(c="ccre_lan", d="0", k="vlor_lan") + ") m "
        f"LEFT JOIN {OWNER}.ctcontas c ON c.codi_emp = m.plano AND c.codi_cta = m.conta "
        "GROUP BY m.plano, m.conta, c.clas_cta, c.nome_cta, c.tipo_cta "
        "ORDER BY c.clas_cta, m.conta")
    # os '?' dos SUM(...) vêm ANTES do FROM no texto; reordena os parâmetros para a ordem textual
    ini = params[-3:]
    params = ini + params[:-3]
    return sql, params


def montar_contas_a_receber(escritorio: int, *, vencimento_de=None, vencimento_ate=None, situacao=None,
                            cliente_codigo=None, limite=LIMITE_PADRAO, offset=0, contar=False) -> tuple[str, list]:
    """Contas a receber de Honorários: saldo por parcela (modelo honorarios.yaml → consultas.contas_a_receber).

    faturado = Σ valor dos itens da parcela; recebido = Σ valor LÍQUIDO dos recebimentos; saldo = faturado − recebido.
    situacao: 'aberta' (saldo > 0), 'quitada' (saldo = 0) ou 'inconsistente' (saldo < 0). Todos os valores entram como parâmetros.
    """
    if situacao not in (None, "aberta", "quitada", "inconsistente"):
        raise ErroConsulta("situacao deve ser 'aberta', 'quitada' ou 'inconsistente'")
    params = [int(escritorio)] * 3
    onde = ""
    if vencimento_de is not None:
        onde += " AND p.vencimento >= ?"; params.append(vencimento_de)
    if vencimento_ate is not None:
        onde += " AND p.vencimento <= ?"; params.append(vencimento_ate)
    if cliente_codigo is not None:
        onde += " AND f.i_cliente = ?"; params.append(int(cliente_codigo))
    interna = (
        "SELECT p.i_faturamento AS faturamento_codigo, p.i_parcela AS parcela, f.i_cliente AS cliente_codigo, c.nome AS cliente_nome, "
        "f.competencia AS competencia, p.vencimento AS vencimento, COALESCE(it.faturado, 0) AS faturado, COALESCE(rc.recebido, 0) AS recebido, "
        "COALESCE(it.faturado, 0) - COALESCE(rc.recebido, 0) AS saldo "
        f"FROM {OWNER}.hrfaturamento_parcela p "
        f"JOIN {OWNER}.hrfaturamento f ON f.codi_emp = p.codi_emp AND f.i_faturamento = p.i_faturamento "
        f"LEFT JOIN {OWNER}.hrcliente c ON c.codi_emp = f.codi_emp AND c.i_cliente = f.i_cliente "
        f"LEFT JOIN (SELECT i_faturamento, i_parcela, SUM(valor) AS faturado FROM {OWNER}.hrfaturamento_parcela_item WHERE codi_emp = ? GROUP BY i_faturamento, i_parcela) it "
        "ON it.i_faturamento = p.i_faturamento AND it.i_parcela = p.i_parcela "
        f"LEFT JOIN (SELECT i_faturamento, i_parcela, SUM(valor) AS recebido FROM {OWNER}.hrrecebimento WHERE codi_emp = ? GROUP BY i_faturamento, i_parcela) rc "
        "ON rc.i_faturamento = p.i_faturamento AND rc.i_parcela = p.i_parcela "
        f"WHERE p.codi_emp = ?{onde}")
    filtro_sit = {"aberta": " WHERE x.saldo > 0.005", "quitada": " WHERE ABS(x.saldo) <= 0.005",
                  "inconsistente": " WHERE x.saldo < -0.005", None: ""}[situacao]
    if contar:
        return f"SELECT COUNT(*) AS total FROM ({interna}) x{filtro_sit}", params
    limite = min(int(limite or LIMITE_PADRAO), LIMITE_MAXIMO)
    offset = max(int(offset or 0), 0)
    sql = (f"SELECT TOP {limite} START AT {offset + 1} x.*, "
           "CASE WHEN x.saldo > 0.005 THEN 'aberta' WHEN x.saldo < -0.005 THEN 'inconsistente' ELSE 'quitada' END AS situacao "
           f"FROM ({interna}) x{filtro_sit} ORDER BY x.vencimento, x.faturamento_codigo, x.parcela")
    return sql, params


def _preparar(ent: dict, filtros: dict):
    """Valida os filtros obrigatórios e monta (tabela, joins, where, params, usar_vinculo). Compartilhado por montar() e montar_agregado()."""
    ac = ent.get("acesso", {})
    emp_col = ac.get("empresa")
    if emp_col and "empresa" not in filtros:
        raise ErroConsulta("filtro 'empresa' é obrigatório para esta entidade")
    exige = ac.get("exige_algum")
    if exige and not any(k in filtros for k in exige):
        raise ErroConsulta(f"informe ao menos um dos filtros: {', '.join(exige)}")

    tabela = _ident(ent["tabela"])
    joins, usados = [], set()
    where, params = [], []

    def usar_vinculo(nome):
        if nome in usados:
            return
        v = ent["vinculos"][nome]
        cond = " AND ".join(f"t.{_ident(l)} = v_{nome}.{_ident(r)}" for l, r in v["liga"].items())
        joins.append(f"LEFT JOIN {OWNER}.{_ident(v['tabela'])} v_{nome} ON {cond}")
        usados.add(nome)

    if emp_col:
        op, val = ("eq", filtros["empresa"]) if not isinstance(filtros["empresa"], tuple) else filtros["empresa"]
        where.append(_condicao(f"t.{_ident(emp_col)}", op, val, params))
    for nome, spec in filtros.items():
        if nome == "empresa":
            continue
        op, val = spec
        if nome == "periodo" and ac.get("periodo"):
            per = ac["periodo"]
            if isinstance(per, dict):
                usar_vinculo(per["vinculo"])
                expr = f"v_{per['vinculo']}.{_ident(per['coluna'])}"
            else:
                expr = f"t.{_ident(per)}"
        else:
            f = ent.get("filtros", {}).get(nome)
            if not f:
                raise ErroConsulta(f"filtro desconhecido: {nome}")
            if op not in f["ops"] and not (op == "branco" and "eq" in f["ops"]) and not (op == "in_pad" and ("eq" in f["ops"] or "in" in f["ops"])):
                raise ErroConsulta(f"operador '{op}' não permitido em '{nome}' (permitidos: {f['ops']})")
            if isinstance(f["coluna"], list):       # várias colunas: a condição vale em QUALQUER uma (OR)
                partes = [_condicao(f"t.{_ident(c)}", op, val, params) for c in f["coluna"]]
                where.append("(" + " OR ".join(partes) + ")")
                continue
            expr = f"t.{_ident(f['coluna'])}"
        where.append(_condicao(expr, op, val, params))

    return tabela, joins, where, params, usar_vinculo


def montar(ent: dict, filtros: dict, *, colunas=None, limite=LIMITE_PADRAO, offset=0,
           ordem=None, vinculos=True, contar=False) -> tuple[str, list]:
    """filtros = {nome_filtro: (op, valor)}  ou  {'empresa': valor}  ou  {'periodo': (op, valor)}.

    Retorna (sql, params). Lança ErroConsulta se faltar filtro obrigatório ou algo for inválido.
    """
    tabela, joins, where, params, usar_vinculo = _preparar(ent, filtros)
    ac = ent.get("acesso", {})

    if contar:
        sql = f"SELECT COUNT(*) AS total FROM {OWNER}.{tabela} t " + " ".join(joins)
    else:
        limite = min(int(limite or LIMITE_PADRAO), LIMITE_MAXIMO)
        offset = max(int(offset or 0), 0)
        sel = []
        calc = ent.get("calculadas", {})
        coal = ent.get("coalescidas", {})
        escolhidas = colunas or (list(ent["colunas"]) + list(calc) + list(coal))
        for api in escolhidas:
            if api in calc:       # coluna calculada: expressão aritmética declarada no modelo (validada), só com colunas da tabela
                expr = re.sub(r"[A-Za-z_][A-Za-z0-9_]*", lambda m: f"t.{_ident(m.group(0))}", calc[api])
                sel.append(f"{expr} AS {_ident(api)}")
            elif api in coal:     # primeiro valor não nulo entre colunas de vínculos ("vinculo.coluna") e, opcionalmente, um literal 'X'
                partes = []
                for item in coal[api]:
                    if item.startswith("'"):
                        if not re.fullmatch(r"'[A-Za-z0-9 ]*'", item):
                            raise ErroConsulta(f"literal inválido no modelo: {item!r}")
                        partes.append(item)
                    else:
                        vn, vc = item.split(".")
                        usar_vinculo(_ident(vn))
                        partes.append(f"v_{vn}.{_ident(vc)}")
                sel.append(f"COALESCE({', '.join(partes)}) AS {_ident(api)}")
            elif api in ent["colunas"]:
                sel.append(f"t.{_ident(_real(ent['colunas'][api]))} AS {_ident(api)}")
            else:
                achou = False
                for vn, v in ent.get("vinculos", {}).items():
                    if api in v["colunas"]:
                        usar_vinculo(vn)
                        sel.append(f"v_{vn}.{_ident(v['colunas'][api])} AS {_ident(api)}")
                        achou = True
                        break
                if not achou:
                    raise ErroConsulta(f"coluna desconhecida: {api}")
        if colunas is None and vinculos:
            for vn, v in ent.get("vinculos", {}).items():
                usar_vinculo(vn)
                for api, real in v["colunas"].items():
                    sel.append(f"v_{vn}.{_ident(real)} AS {_ident(api)}")
        ord_ = ordem or ent.get("ordem") or [[c, "asc"] for c in ent["chave"]]
        order = ", ".join(f"t.{_ident(c)} {'DESC' if str(d).lower() == 'desc' else 'ASC'}" for c, d in ord_)
        # desempate determinístico pela chave, para a paginação não repetir/pular linhas
        extras = [c for c in ent["chave"] if c not in {c2 for c2, _ in ord_}]
        if extras:
            order += ", " + ", ".join(f"t.{_ident(c)} ASC" for c in extras)
        sql = (f"SELECT TOP {limite} START AT {offset + 1} " + ", ".join(sel) +
               f" FROM {OWNER}.{tabela} t " + " ".join(joins))
    if where:
        sql += " WHERE " + " AND ".join(where)
    if not contar:
        sql += " ORDER BY " + order
    return re.sub(r"\s+", " ", sql).strip(), params


# ------------------------------------------------------------------------------------------------ agregação (totais por grupo)
FUNCOES_AGREGADAS = {"soma": "SUM", "media": "AVG", "minimo": "MIN", "maximo": "MAX"}
GRANULARIDADES = {"mes": "YYYY-MM", "ano": "YYYY", "dia": "YYYY-MM-DD"}


def montar_agregado(ent: dict, filtros: dict, *, agrupar: list[tuple[str, str | None]], metricas: list[tuple[str, str]], limite: int = LIMITE_PADRAO,
                    ordem_desc: bool = False) -> tuple[str, list]:
    """SELECT agregado: `agrupar` = [(campo_api, granularidade|None)], `metricas` = [(funcao, campo_api)] (+ sempre COUNT(*) AS linhas). Sem agrupar = um total geral.
    Os campos vêm do modelo; as funções e granularidades de listas fechadas; os valores dos filtros como parâmetros."""
    tabela, joins, where, params, _ = _preparar(ent, filtros)
    reais = {api: _real(v) for api, v in ent["colunas"].items()}
    sel, grp = [], []
    for api, gran in agrupar:
        if api not in reais:
            raise ErroConsulta(f"campo de agrupamento desconhecido: {api}")
        expr = f"t.{_ident(reais[api])}"
        if gran:
            if gran not in GRANULARIDADES:
                raise ErroConsulta(f"granularidade desconhecida: {gran} (use mes, ano ou dia)")
            expr = f"DATEFORMAT({expr}, '{GRANULARIDADES[gran]}')"
        sel.append(f"{expr} AS {_ident(api)}")
        grp.append(expr)
    sel.append("COUNT(*) AS linhas")
    for fn, api in metricas:
        if fn not in FUNCOES_AGREGADAS:
            raise ErroConsulta(f"função desconhecida: {fn} (use {', '.join(FUNCOES_AGREGADAS)})")
        if api not in reais:
            raise ErroConsulta(f"campo de métrica desconhecido: {api}")
        sel.append(f"{FUNCOES_AGREGADAS[fn]}(t.{_ident(reais[api])}) AS {_ident(fn + '_' + api)}")
    limite = max(1, min(int(limite or LIMITE_PADRAO), LIMITE_MAXIMO))
    sql = f"SELECT TOP {limite} " + ", ".join(sel) + f" FROM {OWNER}.{tabela} t " + " ".join(joins)
    if where:
        sql += " WHERE " + " AND ".join(where)
    if grp:
        sql += " GROUP BY " + ", ".join(grp) + " ORDER BY " + ", ".join(f"{i + 1} {'DESC' if ordem_desc else 'ASC'}" for i in range(len(grp)))
    return re.sub(r"\s+", " ", sql).strip(), params


_NAO_SOMAVEL = re.compile(r"(^|_)(numero|codigo|serie|sequencial|sequencia|chave|ordem|ano|mes|dia|cnpj|cpf|cep|telefone|ddd|nsu|protocolo|ibge|competencia|versao|"
                          r"aliquota|taxa|percentual|perc|fator|coeficiente|indice|cae|cnae|data|numerica|reducao|cadbases|cst|cfop|ncm|id|conta|grupo|parcelar|flag|tipo)(_|$)")
_SOMAVEL = re.compile(r"valor|saldo|total|base|quant|qtd|montante|preco|custo|receita|despesa|credito|debito|imposto|juros|multa|desconto|dias|horas|retid|pago|apurad|devido|liquido|bruto|"
                      r"lucro|prejuizo|faturamento|rendimento|salario|remuneracao|provento|encargo|tarifa|abatimento|deducao|acrescimo|ressarcimento|estoque|contabil|produtos|frete|seguro")


_FORTE_SOMAVEL = re.compile(r"(^|_)(valor|valores|saldo|total|quantidade|qtd|dias|horas)(_|$)")


def campos_somaveis(ent: dict, colunas_catalogo: dict[str, dict]) -> list[str]:
    """Campos da entidade que somam com sentido: numéricos cujo nome indica valor/quantidade (valor, saldo, total, base, dias...) e que não são chave, código com domínio,
    identificador (número, série, sequencial...), alíquota/percentual, data serial ou código fiscal. `colunas_catalogo` = {coluna_em_minusculas: {"tipo": ...}}."""
    chave = {c.lower() for c in ent["chave"]}
    out = []
    for api, v in ent["colunas"].items():
        real = _real(v).lower()
        c = colunas_catalogo.get(real)
        if not c or real in chave or (isinstance(v, dict) and v.get("dominio")) or not (_FORTE_SOMAVEL.search(api) or (_SOMAVEL.search(api) and not _NAO_SOMAVEL.search(api))):
            continue
        if (c.get("tipo") or "").lower().startswith(("decimal", "numeric", "double", "float", "real", "money", "integer", "smallint", "bigint")):
            out.append(api)
    return out
