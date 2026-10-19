"""Contexto somente-leitura que a biblioteca usa para montar descrições: modelo (entidades e domínios) + catálogo local (SQLite). Não toca no banco Domínio."""
from __future__ import annotations

import functools
import pathlib
import sqlite3

from server.sqlbuilder import carregar_modelo

RAIZ = pathlib.Path(__file__).resolve().parents[2]
CATALOGO = RAIZ / "data" / "catalog" / "dominio_catalog.db"


class Contexto:
    def __init__(self):
        self.ents, self.doms = carregar_modelo()
        cn = sqlite3.connect(f"file:{CATALOGO.as_posix()}?mode=ro", uri=True)
        cn.row_factory = sqlite3.Row
        self.tabelas = {r["nome_lower"]: dict(r) for r in cn.execute("select nome, nome_lower, linhas, comentario, departamento from tabelas")}
        self._cols: dict[str, dict[str, dict]] = {}
        for r in cn.execute("select tabela, nome, tipo, tamanho, comentario from colunas"):
            self._cols.setdefault(r["tabela"].lower(), {})[r["nome"].lower()] = dict(r)
        cn.close()

    def coluna(self, tabela: str, nome: str) -> dict:
        return self._cols.get(tabela.lower(), {}).get(str(nome).lower(), {})

    def linhas(self, tabela: str) -> int | None:
        return (self.tabelas.get(tabela.lower()) or {}).get("linhas")


@functools.lru_cache(maxsize=1)
def contexto() -> Contexto:
    return Contexto()
