"""Descoberta da biblioteca: importa cada pacote de módulo (src/biblioteca/<modulo>/<tabela>.py) e as ferramentas de casos de uso e monta o índice."""
from __future__ import annotations

import collections
import functools
import importlib
import pathlib
import pkgutil

from biblioteca.base import Ferramenta

AQUI = pathlib.Path(__file__).resolve().parent


class Biblioteca:
    def __init__(self):
        self.ferramentas: dict[str, Ferramenta] = {}
        self.por_tabela: dict[str, list[Ferramenta]] = collections.defaultdict(list)
        self.por_modulo: dict[str, list[Ferramenta]] = collections.defaultdict(list)
        self.arquivos: dict[str, str] = {}          # tabela -> módulo.arquivo
        self.erros: list[str] = []

    def adicionar(self, f: Ferramenta, origem: str):
        if f.nome in self.ferramentas:
            self.erros.append(f"nome duplicado: {f.nome} ({origem})")
            return
        self.ferramentas[f.nome] = f
        for t in f.tabelas:
            self.por_tabela[t].append(f)
        self.por_modulo[f.modulo].append(f)


@functools.lru_cache(maxsize=1)
def carregar() -> Biblioteca:
    b = Biblioteca()
    for pk in sorted(p for p in pkgutil.iter_modules([str(AQUI)]) if p.ispkg):
        pkg = importlib.import_module(f"biblioteca.{pk.name}")
        for m in pkgutil.iter_modules(pkg.__path__):
            nome = f"biblioteca.{pk.name}.{m.name}"
            try:
                mod = importlib.import_module(nome)
            except Exception as ex:
                b.erros.append(f"{nome}: {type(ex).__name__}: {str(ex)[:150]}")
                continue
            for f in getattr(mod, "TOOLS", []):
                if not f.modulo:
                    f.modulo = pk.name
                b.adicionar(f, nome)
            if hasattr(mod, "TABELA"):
                b.arquivos[mod.TABELA.lower()] = nome
    return b
