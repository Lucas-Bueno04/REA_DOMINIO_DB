import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))
from extractor.db import conectar, select

cn = conectar()
print("RELATORIOS por sistema/tipo/ativado:")
for r in select(cn, "SELECT i_sistema, tipo, ativado, COUNT(*) AS n FROM bethadba.RELATORIOS GROUP BY i_sistema, tipo, ativado ORDER BY 1,2,3"):
    print("  ", r)

print("\n--- amostra DEFSELECT.defsql (3) ---")
for r in select(cn, "SELECT TOP 3 i_relatorio, i_sql, LEFT(defsql, 700) AS d FROM bethadba.DEFSELECT WHERE defsql IS NOT NULL ORDER BY i_relatorio"):
    print(r["i_relatorio"], r["i_sql"], repr(r["d"]), "\n")

print("--- OBJETOS_RELS: quantos contêm 'retrieve=' / 'PBSELECT' / 'JOIN' ---")
for pad in ["retrieve=", "PBSELECT", "JOIN (", "select ", "table(column"]:
    n = select(cn, f"SELECT COUNT(*) AS n FROM bethadba.OBJETOS_RELS WHERE LOCATE(definicao, '{pad}') > 0")[0]["n"]
    print(f"  {pad!r}: {n}")

print("\n--- amostra OBJETOS_RELS com PBSELECT ---")
for r in select(cn, "SELECT TOP 2 i_relatorio, i_objeto, LENGTH(definicao) AS len, SUBSTR(definicao, LOCATE(definicao,'retrieve='), 900) AS d FROM bethadba.OBJETOS_RELS WHERE LOCATE(definicao,'retrieve=') > 0 ORDER BY LENGTH(definicao) DESC"):
    print(r["i_relatorio"], r["i_objeto"], r["len"], repr(r["d"]), "\n")
