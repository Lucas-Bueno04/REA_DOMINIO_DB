"""Empresas com mais linhas em uma tabela (COUNT agregado, somente leitura).  Uso: python scripts/empresas_com_dados.py tabela [qtde]"""
import pathlib, re, sqlite3, sys
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from extractor.db import conectar, select
t = sys.argv[1]; n = int(sys.argv[2]) if len(sys.argv) > 2 else 5
lite = sqlite3.connect(RAIZ / "data/catalog/dominio_catalog.db")
assert re.fullmatch(r"\w+", t) and lite.execute("select 1 from colunas where tabela=? collate nocase and nome='codi_emp' collate nocase", (t,)).fetchone(), "tabela sem codi_emp"
rows = select(conectar(), f"SELECT codi_emp, COUNT(*) AS n FROM bethadba.{t} GROUP BY codi_emp ORDER BY n DESC")
print(f"{t}: {len(rows)} empresas com dados; topo:", [(r['codi_emp'], r['n']) for r in rows[:n]], "| mediana:", rows[len(rows)//2]['codi_emp'], rows[len(rows)//2]['n'])
