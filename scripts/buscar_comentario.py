"""Busca textos nos comentários de colunas/tabelas do catálogo.  Uso: python scripts/buscar_comentario.py padrao [padrao ...] [--tab prefixo%] [--max N]"""
import pathlib, sqlite3, sys
d = sqlite3.connect(pathlib.Path(__file__).resolve().parents[1] / "data/catalog/dominio_catalog.db")
a = sys.argv[1:]
mx = int(a[a.index("--max") + 1]) if "--max" in a else 25
tab = a[a.index("--tab") + 1] if "--tab" in a else "%"
pads = [x for i, x in enumerate(a) if not x.startswith("--") and (i == 0 or a[i - 1] not in ("--max", "--tab"))]
cond = " and ".join("comentario like ?" for _ in pads)
for t, n, c in d.execute(f"select tabela, nome, comentario from colunas where tabela like ? and {cond} limit ?", [tab] + [f"%{p}%" for p in pads] + [mx]):
    print(f"{t}.{n}: {(c or '')[:230]}")
