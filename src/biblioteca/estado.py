"""Acompanhamento da biblioteca: resultado da validação de cada ferramenta (SQLite local data/biblioteca_estado.db) e visão por tabela para o portal.

O status de cada tabela é DERIVADO (não se edita à mão): existe o arquivo da tabela na biblioteca? as ferramentas passaram na bateria de validação?
  sem_ferramenta : tabela do banco sem arquivo na biblioteca (ainda não modelada em entidade, vazia ou ignorada)
  gerada         : há ferramenta(s) padrão geradas do modelo, ainda não validadas
  validada       : todas as ferramentas da tabela passaram na bateria (esquema, descrição, execução real, filtro, paginação, credenciais)
  curada         : validada E construída sobre uma entidade CURADA à mão (regras de negócio conferidas com os dados) ou com ferramentas de caso de uso
  falhou         : alguma ferramenta falhou na bateria (veja os checks)
  revisada       : validada e revisada por um agente independente (nota registrada)
"""
from __future__ import annotations

import datetime
import json
import pathlib
import sqlite3

RAIZ = pathlib.Path(__file__).resolve().parents[2]
DB = RAIZ / "data" / "biblioteca_estado.db"

DDL = """
create table if not exists ferramenta (
  nome text primary key, tabela text, entidade text, modulo text, tipo text, gerada integer,
  status text not null default 'nao_validada',      -- nao_validada | validada | falhou
  checks text, ms integer, linhas integer, validada_em text, nota_revisao text, revisor text
);
create index if not exists ix_ferr_tabela on ferramenta(tabela);
create table if not exists amostra (
  entidade text primary key, empresa text, filtros text, criada_em text
);
create table if not exists historico (
  dia text primary key, ferramentas integer, validadas integer, falhas integer, tabelas integer, tabelas_validadas integer
);
"""


def agora() -> str:
    return datetime.datetime.now().isoformat(timespec="seconds")


def abrir() -> sqlite3.Connection:
    DB.parent.mkdir(exist_ok=True)
    c = sqlite3.connect(DB, timeout=30, check_same_thread=False)
    c.row_factory = sqlite3.Row
    c.executescript(DDL)
    return c


def sincronizar(c: sqlite3.Connection, biblioteca) -> None:
    """Garante uma linha por ferramenta existente (mantém resultados anteriores) e remove as que deixaram de existir."""
    existentes = {r["nome"] for r in c.execute("select nome from ferramenta")}
    for f in biblioteca.ferramentas.values():
        tabela = f.tabelas[0] if f.tabelas else None
        if f.nome in existentes:
            c.execute("update ferramenta set tabela=?, entidade=?, modulo=?, tipo=?, gerada=? where nome=?", (tabela, f.entidade, f.modulo, f.tipo, int(f.gerada), f.nome))
        else:
            c.execute("insert into ferramenta(nome, tabela, entidade, modulo, tipo, gerada) values (?,?,?,?,?,?)", (f.nome, tabela, f.entidade, f.modulo, f.tipo, int(f.gerada)))
    # Só apaga o que sumiu quando a biblioteca carregou INTEIRA: uma carga quebrada (erro de sintaxe no meio de uma edição) tem poucas ferramentas e apagaria
    # resultados de validação e vereditos de revisão de todo o resto (já aconteceu).
    sumiram = existentes - set(biblioteca.ferramentas)
    if sumiram and not biblioteca.erros and len(sumiram) <= max(50, 0.05 * len(existentes)):
        for nome in sumiram:
            c.execute("delete from ferramenta where nome=?", (nome,))
    c.commit()


def gravar_resultado(c: sqlite3.Connection, nome: str, ok: bool, checks: dict, ms: int, linhas: int | None) -> None:
    c.execute("update ferramenta set status=?, checks=?, ms=?, linhas=?, validada_em=? where nome=?",
              ("validada" if ok else "falhou", json.dumps(checks, ensure_ascii=False), ms, linhas, agora(), nome))
    c.commit()


def gravar_revisao(c: sqlite3.Connection, nome: str, nota: str, revisor: str) -> None:
    c.execute("update ferramenta set nota_revisao=?, revisor=? where nome=?", (nota, revisor, nome))
    c.commit()


def amostra(c: sqlite3.Connection, entidade: str) -> dict | None:
    r = c.execute("select empresa, filtros from amostra where entidade=?", (entidade,)).fetchone()
    return {"empresa": json.loads(r["empresa"]), "filtros": json.loads(r["filtros"])} if r else None


def gravar_amostra(c: sqlite3.Connection, entidade: str, empresa, filtros: dict) -> None:
    c.execute("insert or replace into amostra values (?,?,?,?)", (entidade, json.dumps(empresa), json.dumps(filtros, default=str), agora()))
    c.commit()


def status_tabela(ferrs: list[sqlite3.Row]) -> str:
    if not ferrs:
        return "sem_ferramenta"
    if any(f["status"] == "falhou" for f in ferrs):
        return "falhou"
    if all(f["status"] == "validada" for f in ferrs):
        if any(not f["gerada"] for f in ferrs):
            return "curada"
        if all((f["nota_revisao"] or "").startswith("[aprovada]") for f in ferrs):
            return "revisada"
        return "validada"
    return "gerada"


ORDEM_STATUS = ["curada", "revisada", "validada", "gerada", "falhou", "sem_ferramenta"]


def resumo(c: sqlite3.Connection, tabelas_banco: list[dict] | None = None) -> dict:
    """Visão para o portal. `tabelas_banco` = lista da plataforma (nome, departamento, status, linhas) para mostrar o que ainda NÃO tem ferramenta."""
    por_tab: dict[str, list] = {}
    for r in c.execute("select * from ferramenta"):
        por_tab.setdefault((r["tabela"] or "").lower(), []).append(r)
    tabs = []
    for t, fs in por_tab.items():
        tabs.append({"tabela": t, "modulo": fs[0]["modulo"], "status": status_tabela(fs), "ferramentas": [f["nome"] for f in fs],
                     "falhas": [f["nome"] for f in fs if f["status"] == "falhou"]})
    cont = {s: 0 for s in ORDEM_STATUS}
    for t in tabs:
        cont[t["status"]] += 1
    if tabelas_banco is not None:
        com = set(por_tab)
        for tb in tabelas_banco:
            n = (tb.get("tabela") or tb.get("nome") or "").lower()
            if n and n not in com and tb.get("status") not in ("vazia", "ignorada", "bloqueada"):
                cont["sem_ferramenta"] += 1
    mods: dict[str, dict] = {}
    for t in tabs:
        m = mods.setdefault(t["modulo"] or "?", {s: 0 for s in ORDEM_STATUS} | {"total": 0})
        m[t["status"]] += 1
        m["total"] += 1
    tot = c.execute("select count(*) n, sum(status='validada') v, sum(status='falhou') f from ferramenta").fetchone()
    return {"ferramentas": tot["n"], "ferramentas_validadas": tot["v"] or 0, "ferramentas_com_falha": tot["f"] or 0, "tabelas": len(tabs),
            "por_status": cont, "por_modulo": mods, "ordem_status": ORDEM_STATUS}


def snapshot_hoje(c: sqlite3.Connection, r: dict | None = None) -> dict:
    r = r or resumo(c)
    dia = datetime.date.today().isoformat()
    ps = r["por_status"]
    val = ps["validada"] + ps["curada"] + ps["revisada"]
    c.execute("insert or replace into historico values (?,?,?,?,?,?)", (dia, r["ferramentas"], r["ferramentas_validadas"], r["ferramentas_com_falha"], r["tabelas"], val))
    c.commit()
    return {"dia": dia, "ferramentas": r["ferramentas"], "validadas": r["ferramentas_validadas"], "falhas": r["ferramentas_com_falha"], "tabelas": r["tabelas"], "tabelas_validadas": val}
