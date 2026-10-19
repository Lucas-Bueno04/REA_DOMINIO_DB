"""Dados do acompanhamento da BIBLIOTECA de tools MCP para o portal: quais tabelas já viraram ferramentas de consulta e em que estágio
(gerada → validada → curada/revisada). Só leitura: lê o registro da biblioteca e data/biblioteca_estado.db (gravado por scripts/validar_biblioteca.py)."""
from __future__ import annotations

import json
import threading

from biblioteca import estado
from biblioteca.registro import carregar
from plataforma import dados as dd

_TRAVA = threading.Lock()
_pronto = False


def _sincronizar(c):
    global _pronto
    with _TRAVA:
        if not _pronto:
            estado.sincronizar(c, carregar())
            _pronto = True


def painel() -> dict:
    b = carregar()
    c = estado.abrir()
    try:
        _sincronizar(c)
        plat = {t["t"]: t for t in dd.lista_tabelas()}
        por_tab: dict[str, list] = {}
        for r in c.execute("select * from ferramenta"):
            por_tab.setdefault((r["tabela"] or "").lower(), []).append(r)
        tabs = []
        for t, fs in sorted(por_tab.items()):
            p = plat.get(t, {})
            tabs.append({"t": t, "nome": p.get("nome", t), "modulo": fs[0]["modulo"], "dep": p.get("dep", ""), "linhas": p.get("linhas"), "status_mapa": p.get("status"),
                         "status": estado.status_tabela(fs), "ferramentas": [{"nome": f["nome"], "tipo": f["tipo"], "status": f["status"], "ms": f["ms"]} for f in fs],
                         "falhas": [f["nome"] for f in fs if f["status"] == "falhou"], "revisada": all((f["nota_revisao"] or "").startswith("[aprovada]") for f in fs)})
        sem = [{"t": t, "nome": p["nome"], "dep": p["dep"], "linhas": p["linhas"], "status_mapa": p["status"]} for t, p in plat.items()
               if t not in por_tab and p["status"] not in ("vazia", "ignorada", "bloqueada")]
        r = estado.resumo(c)
        r["por_status"]["sem_ferramenta"] = len(sem)
        hist = [dict(x) for x in c.execute("select * from historico order by dia")]
        return {"resumo": r, "tabelas": tabs, "sem_ferramenta": sem, "historico": hist, "erros_carga": b.erros,
                "por_tipo": {t: sum(1 for f in b.ferramentas.values() if f.tipo == t) for t in {f.tipo for f in b.ferramentas.values()}}}
    finally:
        c.close()


def ferramenta(nome: str) -> dict:
    f = carregar().ferramentas.get(nome)
    if not f:
        raise KeyError(nome)
    c = estado.abrir()
    try:
        r = c.execute("select * from ferramenta where nome=?", (nome,)).fetchone()
        return {"nome": f.nome, "tipo": f.tipo, "modulo": f.modulo, "tabelas": f.tabelas, "titulo": f.titulo, "descricao": f.descricao, "gerada": f.gerada,
                "parametros": [{"nome": p.nome, "obrigatorio": p.obrigatorio, "padrao": p.padrao, "descricao": p.descricao} for p in f.parametros],
                "exemplos": f.exemplos, "status": r["status"] if r else "nao_validada", "checks": json.loads(r["checks"]) if r and r["checks"] else {},
                "ms": r["ms"] if r else None, "validada_em": r["validada_em"] if r else None, "revisao": r["nota_revisao"] if r else None, "revisor": r["revisor"] if r else None}
    finally:
        c.close()
