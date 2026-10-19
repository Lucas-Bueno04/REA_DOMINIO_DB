"""Bateria de validação das ferramentas da biblioteca (SOMENTE LEITURA: só chama as ferramentas, que só fazem SELECT).

Para cada entidade (uma tabela) roda, contra o banco real:
  esquema     a tool MCP é montada (assinatura tipada → JSON Schema) sem erro
  descricao   a descrição que o modelo de IA lê tem tamanho útil e cita a tabela
  entrada     a ferramenta recusa entrada inválida (sem obrigatórios, parâmetro desconhecido) com mensagem acionável
  execucao    com uma amostra real (empresa/filtros obrigatórios) devolve JSON serializável
  campos      os campos devolvidos são os declarados no modelo
  credenciais nenhuma coluna de credencial sai
  filtro      filtrar por um valor lido da própria linha devolve essa linha (o filtro faz o que diz)
  paginacao   a 2ª página existe e não repete a 1ª linha
  obter       (quando existe) a chave de uma linha recupera a mesma linha
Resultado gravado em data/biblioteca_estado.db (status por ferramenta). Falha = alguma checagem obrigatória falhou.
"""
from __future__ import annotations

import datetime
import decimal
import importlib.util
import json
import pathlib
import re
import time
import uuid

from biblioteca import estado
from biblioteca.base import Ferramenta, como_funcao, validar_argumentos
from biblioteca.contexto import RAIZ

OBRIGATORIAS = ("esquema", "descricao", "entrada", "execucao", "campos", "credenciais", "filtro", "paginacao", "obter", "totais")


def _scripts():
    spec = importlib.util.spec_from_file_location("tme", RAIZ / "scripts" / "testar_motor_entidades.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


_TME = None


def montar_amostra(e: dict) -> tuple:
    """(empresa, filtros, nota) usando o mesmo critério da fumaça das entidades (empresa mediana + um dos filtros obrigatórios)."""
    global _TME
    _TME = _TME or _scripts()
    return _TME.montar_chamada(e)


def _nat(v):
    return _TME.nat(v) if _TME else v


def _eq(a, b) -> bool:
    if isinstance(a, str) or isinstance(b, str):
        return str(a).strip().casefold() == str(b).strip().casefold()          # o banco compara texto sem diferenciar maiúsculas
    try:
        return abs(float(a) - float(b)) < 1e-9
    except Exception:
        return a == b


def validar_entidade(motor, entidade: str, ferramentas: list[Ferramenta], amostra: dict | None) -> dict[str, tuple[bool, dict, int, int | None]]:
    """Valida todas as ferramentas geradas de uma entidade. Devolve {nome_da_ferramenta: (ok, checks, ms, linhas)}."""
    e = motor.ents[entidade]
    cons = next(f for f in ferramentas if f.tipo == "consultar")
    obt = next((f for f in ferramentas if f.tipo == "obter"), None)
    res: dict[str, dict] = {f.nome: {} for f in ferramentas}
    ms: dict[str, int] = {f.nome: 0 for f in ferramentas}
    linhas_n: dict[str, int | None] = {f.nome: None for f in ferramentas}

    def marca(f, nome, ok, msg=""):
        res[f.nome][nome] = {"ok": bool(ok), "msg": msg[:300]}

    # ---- esquema + descrição + entrada (não tocam o banco)
    for f in ferramentas:
        try:
            fn = como_funcao(f, lambda: None)
            from mcp.server.mcpserver import MCPServer
            MCPServer("v").add_tool(fn, name=f.nome, description=f.descricao)
            marca(f, "esquema", True)
        except Exception as ex:
            marca(f, "esquema", False, f"{type(ex).__name__}: {ex}")
        d = f.descricao
        marca(f, "descricao", 150 <= len(d) <= 9000 and e["tabela"].lower() in d.lower(), f"{len(d)} caracteres")
        try:
            erro_vazio = False
            if any(p.obrigatorio for p in f.parametros):
                try:
                    validar_argumentos(f, {})
                except ValueError:
                    erro_vazio = True
            else:
                erro_vazio = True
            try:
                validar_argumentos(f, {"parametro_inexistente_xyz": 1})
                erro_param = False
            except ValueError as ex:
                erro_param = "não existe" in str(ex)
            marca(f, "entrada", erro_vazio and erro_param)
        except Exception as ex:
            marca(f, "entrada", False, repr(ex))

    # ---- execução real
    if amostra is None:
        emp, filt, nota = montar_amostra(e)
        if nota:
            marca(cons, "execucao", True, "sem_dados: " + nota)
            for nome in ("campos", "credenciais", "filtro", "paginacao"):
                marca(cons, nome, True, "sem_dados")
            for o in ferramentas:
                if o.tipo in ("obter", "totais"):
                    marca(o, "execucao", True, "sem_dados")
                    marca(o, "obter" if o.tipo == "obter" else "totais", True, "sem_dados")
            return {f.nome: (all(v["ok"] for v in res[f.nome].values()), res[f.nome], 0, 0) for f in ferramentas}
        amostra = {"empresa": emp, "filtros": filt}
    emp, filt = amostra["empresa"], amostra["filtros"]
    base = dict(filt_para_args(e, filt))
    if emp is not None:
        base["empresa"] = emp
    t0 = time.time()
    try:
        r = cons.executar(motor, **validar_argumentos(cons, {**base, "limite": 5}))
        json.dumps(r, default=str)
        linhas = r["linhas"]
        ms[cons.nome] = round((time.time() - t0) * 1000)
        linhas_n[cons.nome] = len(linhas)
        marca(cons, "execucao", isinstance(linhas, list), f"{len(linhas)} linhas em {ms[cons.nome]} ms")
    except Exception as ex:
        marca(cons, "execucao", False, f"{type(ex).__name__}: {str(ex)[:250]}")
        for nome in ("campos", "credenciais", "filtro", "paginacao"):
            marca(cons, nome, False, "dependia da execução")
        for o in ferramentas:
            if o.tipo in ("obter", "totais"):
                marca(o, "execucao", False, "dependia da execução de consultar")
                marca(o, "obter" if o.tipo == "obter" else "totais", False, "dependia da execução de consultar")
        return {f.nome: (all(v["ok"] for v in res[f.nome].values()), res[f.nome], ms[f.nome], linhas_n[f.nome]) for f in ferramentas}

    # ---- campos e credenciais
    if linhas:
        esperados = set(e["colunas"]) | set(e.get("calculadas", {})) | set(e.get("coalescidas", {}))
        for v in e.get("vinculos", {}).values():
            esperados |= set(v["colunas"])
        extra = set(linhas[0]) - esperados
        marca(cons, "campos", not extra, f"campos fora do modelo: {sorted(extra)[:5]}" if extra else "")
        real = {api: (v["coluna"] if isinstance(v, dict) else v) for api, v in e["colunas"].items()}        # o nome do campo é derivado do comentário; a credencial se julga pela COLUNA do banco
        cred = [k for k in linhas[0] if motor.re_cred.search(real.get(k, k)) and real.get(k, k).lower() not in motor.cred_excecoes]
        marca(cons, "credenciais", not cred, f"colunas de credencial expostas: {cred}" if cred else "")
    else:
        marca(cons, "campos", True, "sem_dados")
        marca(cons, "credenciais", True, "sem_dados")

    # ---- filtro: usar um valor lido da própria linha
    marca(cons, "filtro", True, "sem filtro de igualdade testável")
    if linhas:
        reais = {api: (v["coluna"] if isinstance(v, dict) else v) for api, v in e["colunas"].items()}
        for fnome, f in e.get("filtros", {}).items():
            if isinstance(f["coluna"], list) or "eq" not in f["ops"] or fnome == "periodo":
                continue
            api = next((a for a, c in reais.items() if c.lower() == f["coluna"].lower()), None)
            val = linhas[0].get(api) if api else None
            if val is None or isinstance(val, (float, bool)):
                continue
            ci = motor._colunas(e["tabela"])
            tipo = next((c["tipo"] for c in ci if c["nome"].lower() == f["coluna"].lower()), "")
            if tipo.lower().startswith(("decimal", "numeric", "double", "float", "real", "long varchar", "long binary", "binary", "image", "xml", "uniqueidentifier")):
                continue
            from biblioteca.entidades import nome_param
            try:
                r2 = cons.executar(motor, **validar_argumentos(cons, {**base, nome_param(fnome): val, "limite": 20}))
                l2 = r2["linhas"]
                ok = bool(l2) and all(_eq(x.get(api), val) for x in l2)
                marca(cons, "filtro", ok, f"filtro {fnome}={val!r}: {len(l2)} linhas" + ("" if ok else " (nem todas casam)"))
            except Exception as ex:
                marca(cons, "filtro", False, f"filtro {fnome}: {type(ex).__name__}: {str(ex)[:200]}")
            break

    # ---- paginação
    marca(cons, "paginacao", True, "menos de uma página")
    if len(linhas) == 5:
        try:
            r3 = cons.executar(motor, **validar_argumentos(cons, {**base, "limite": 5, "offset": 5}))
            l3 = r3["linhas"]
            if l3:
                ok = l3 != linhas
                if not ok:      # linhas idênticas (a entidade não expõe a chave inteira): vale se o total do filtro passa de uma página
                    ok = (cons.executar(motor, **validar_argumentos(cons, {**base, "limite": 1, "contar": True})).get("total") or 0) > 5
                marca(cons, "paginacao", ok, f"2ª página com {len(l3)} linhas")
            else:        # a tabela pode ter exatamente 5 linhas no filtro: confere pelo total
                tot = cons.executar(motor, **validar_argumentos(cons, {**base, "limite": 1, "contar": True})).get("total")
                marca(cons, "paginacao", tot == 5, f"2ª página vazia; total do filtro = {tot}")
        except Exception as ex:
            marca(cons, "paginacao", False, f"{type(ex).__name__}: {str(ex)[:200]}")

    # ---- obter
    if obt:
        marca(obt, "execucao", True, "ver obter")
        if not linhas:
            marca(obt, "obter", True, "sem_dados")
        else:
            try:
                from biblioteca.entidades import chave_para_filtros, nome_param
                chave = chave_para_filtros(e)
                reais = {api: (v["coluna"] if isinstance(v, dict) else v) for api, v in e["colunas"].items()}
                args = {}
                if e["acesso"].get("empresa"):
                    args["empresa"] = emp
                faltou = False
                for k, fn_ in chave.items():
                    api = next((a for a, c in reais.items() if c.lower() == k.lower()), None)
                    if api is None or linhas[0].get(api) is None:
                        faltou = True
                        break
                    args[nome_param(fn_)] = linhas[0][api]
                if faltou:
                    marca(obt, "obter", True, "chave com campo nulo/não exposto na linha de amostra")
                else:
                    t1 = time.time()
                    ro = obt.executar(motor, **validar_argumentos(obt, args))
                    ms[obt.nome] = round((time.time() - t1) * 1000)
                    linhas_n[obt.nome] = 1 if ro["encontrado"] else 0
                    marca(obt, "obter", ro["encontrado"] and not ro.get("aviso"), ro.get("aviso") or ("" if ro["encontrado"] else "chave da própria linha não foi encontrada"))
            except Exception as ex:
                marca(obt, "obter", False, f"{type(ex).__name__}: {str(ex)[:250]}")
    # ---- totais: os números do agrupamento fecham com a contagem da consulta
    tot = next((f for f in ferramentas if f.tipo == "totais"), None)
    if tot:
        marca(tot, "execucao", True, "ver totais")
        try:
            ex = dict(tot.exemplos[0]["argumentos"])
            args_t = {**{k: v for k, v in base.items() if k in {p.nome for p in tot.parametros}}, "agrupar_por": ex.get("agrupar_por"), "metricas": ex.get("metricas"), "limite": 500}
            t1 = time.time()
            rt = tot.executar(motor, **validar_argumentos(tot, args_t))
            ms[tot.nome] = round((time.time() - t1) * 1000)
            json.dumps(rt, default=str)
            geral = rt["total_geral"]["linhas"]
            soma = sum(g["linhas"] for g in rt["grupos"])
            rc = cons.executar(motor, **validar_argumentos(cons, {**base, "limite": 1, "contar": True}))
            fecha_grupos = rt["truncado"] or soma == geral
            marca(tot, "totais", fecha_grupos and geral == rc.get("total"), f"total_geral={geral} contagem={rc.get('total')} soma_dos_grupos={soma}{' (truncado)' if rt['truncado'] else ''}")
            linhas_n[tot.nome] = geral
        except Exception as ex:
            marca(tot, "totais", False, f"{type(ex).__name__}: {str(ex)[:250]}")
    return {f.nome: (all(res[f.nome].get(k, {"ok": True})["ok"] for k in OBRIGATORIAS), res[f.nome], ms[f.nome], linhas_n[f.nome]) for f in ferramentas}


def filt_para_args(e: dict, filt: dict) -> dict:
    """Traduz os filtros da amostra (nomes do modelo) para parâmetros da ferramenta."""
    from biblioteca.entidades import nome_param
    return {("periodo" if k == "periodo" else nome_param(k)): v for k, v in (filt or {}).items()}


def validar_caso_de_uso(motor, f: Ferramenta) -> tuple[bool, dict, int, int | None]:
    """Bateria de um caso de uso: esquema, descrição (com fontes e conferência), entrada, execução real com argumentos de teste e fontes existentes no catálogo."""
    checks: dict[str, dict] = {}

    def marca(nome, ok, msg=""):
        checks[nome] = {"ok": bool(ok), "msg": msg[:300]}

    try:
        from mcp.server.mcpserver import MCPServer
        MCPServer("v").add_tool(como_funcao(f, lambda: None), name=f.nome, description=f.descricao)
        marca("esquema", True)
    except Exception as ex:
        marca("esquema", False, f"{type(ex).__name__}: {ex}")
    marca("descricao", 200 <= len(f.descricao) <= 9000 and "FONTES" in f.descricao and "CONFERÊNCIA" in f.descricao, f"{len(f.descricao)} caracteres")
    try:
        validar_argumentos(f, {})
        marca("entrada", not any(p.obrigatorio for p in f.parametros), "aceitou entrada vazia")
    except ValueError:
        try:
            validar_argumentos(f, {"parametro_inexistente_xyz": 1})
            marca("entrada", False, "aceitou parâmetro desconhecido")
        except ValueError:
            marca("entrada", True)
    ausentes = [t for t in f.tabelas if t not in motor._tab]
    marca("fontes", not ausentes, f"tabelas-fonte inexistentes no catálogo: {ausentes}" if ausentes else "")
    ms = 0
    if f.teste is None:
        marca("execucao", False, "caso de uso sem teste automático definido")
    else:
        try:
            args = f.teste(motor) if callable(f.teste) else f.teste
            t0 = time.time()
            r = f.executar(motor, **validar_argumentos(f, args))
            ms = round((time.time() - t0) * 1000)
            json.dumps(r, default=str)
            marca("execucao", isinstance(r, dict) and not r.get("erro"), f"ok em {ms} ms com {json.dumps(args, default=str)[:120]}")
        except Exception as ex:
            marca("execucao", False, f"{type(ex).__name__}: {str(ex)[:250]}")
    return all(v["ok"] for v in checks.values()), checks, ms, None
