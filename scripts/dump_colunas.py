"""Despeja colunas (nome, tipo, tamanho, PK, nulo, comentário) de tabelas -> docs/colunas/<tabela>.md
Uso: python scripts/dump_colunas.py tabela1 tabela2 ...
"""
import pathlib, sqlite3, sys
RAIZ = pathlib.Path(__file__).resolve().parents[1]
d = sqlite3.connect(RAIZ / "data/catalog/dominio_catalog.db")
out = RAIZ / "docs" / "colunas"
out.mkdir(parents=True, exist_ok=True)
for t in sys.argv[1:]:
    info = d.execute("select nome, comentario, linhas from tabelas where nome_lower=lower(?)", (t,)).fetchone()
    if not info:
        print("não encontrada:", t); continue
    rows = d.execute("select nome, tipo, tamanho, pk, aceita_nulo, comentario from colunas where tabela=? collate nocase order by ordem", (info[0],)).fetchall()
    L = [f"# {info[0]} — {info[1] or ''}", f"{info[2]:,} linhas".replace(",", "."), "",
         "| Coluna | Tipo | PK | Nulo | Comentário |", "|---|---|---|---|---|"]
    for n, tp, tam, pk, nul, c in rows:
        L.append(f"| {n} | {tp}({tam}) | {'PK' if pk else ''} | {'S' if nul else ''} | {(c or '').replace('|','/')} |")
    (out / f"{info[0].lower()}.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"{info[0]}: {len(rows)} colunas")
