"""Calibra as regras de inferência usando as FKs declaradas como verdade-terreno.

Aplica `inferir()` sem olhar as FKs e mede:
  precisão (limite inferior) = pares inferidos que existem como FK declarada / pares inferidos
  cobertura                  = FKs declaradas reencontradas / FKs declaradas
Os "falsos positivos" podem incluir relações reais que só não foram declaradas, então a precisão é conservadora.
"""
import collections, itertools, pathlib, sqlite3, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))
from model.relacoes import inferir

d = sqlite3.connect(pathlib.Path(__file__).resolve().parents[1] / "data/catalog/dominio_catalog.db")
cols = collections.defaultdict(dict)
for t, c, tp, pk in d.execute("select lower(tabela), lower(nome), tipo, pk from colunas"):
    cols[t][c] = (tp, pk)
chave = {t: {c for c, (_, p) in cs.items() if p} for t, cs in cols.items() if any(p for _, p in cs.values())}
for t, c in d.execute("select lower(tabela), lower(colunas) from indices where unico=1 order by length(colunas)"):
    chave.setdefault(t, set(c.split(",")))
decl = {(f.lower(), p.lower()) for f, p in d.execute("select filha, pai from fks")}
print(f"FKs declaradas (pares filha->pai): {len(decl)}\n")
print(f"{'modo':<8}{'max':>5}{'inferidas':>11}{'acertos':>9}{'precisão':>10}{'cobertura':>11}{'  F1':>6}")
for modo, mx in itertools.product(["", "U", "P", "UP"], [25, 60, 1000]):
    pred = {(f, p) for f, p, _ in inferir(cols, chave, modo, mx)}
    hit = len(pred & decl)
    prec = hit / len(pred) if pred else 0
    cov = hit / len(decl)
    f1 = 2 * prec * cov / (prec + cov) if prec + cov else 0
    print(f"{modo or '-':<8}{mx:>5}{len(pred):>11}{hit:>9}{prec:>10.1%}{cov:>11.1%}{f1:>6.2f}")
