"""Tabulação cruzada de duas colunas (COUNT) para validar o significado de códigos. SOMENTE LEITURA.
Uso: python scripts/cruzar.py tabela colA colB   |   python scripts/cruzar.py --tabela geimposto   (lista tabela pequena, <=300 linhas)
"""
import pathlib, re, sqlite3, sys
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from extractor.db import conectar, select
cn = conectar()
lite = sqlite3.connect(RAIZ / "data/catalog/dominio_catalog.db")
def col_ok(t, c):
    return bool(re.fullmatch(r"\w+", t + c)) and lite.execute("select 1 from colunas where tabela=? collate nocase and nome=? collate nocase", (t, c)).fetchone()
if sys.argv[1] == "--tabela":
    t = sys.argv[2]
    n = lite.execute("select linhas from tabelas where nome_lower=lower(?)", (t,)).fetchone()
    assert n and n[0] <= 300, "tabela inexistente ou grande demais"
    for r in select(cn, f"SELECT * FROM bethadba.{t}"):
        print({k: (v.strip() if isinstance(v, str) else v) for k, v in r.items()})
else:
    t, a, b = sys.argv[1:4]
    assert col_ok(t, a) and col_ok(t, b), "coluna inexistente"
    for r in select(cn, f"SELECT {a} AS a, {b} AS b, COUNT(*) AS n FROM bethadba.{t} GROUP BY {a}, {b} ORDER BY n DESC"):
        print(f"{a}={str(r['a']).strip()!r:<6} {b}={str(r['b']).strip()!r:<6} n={r['n']}")
