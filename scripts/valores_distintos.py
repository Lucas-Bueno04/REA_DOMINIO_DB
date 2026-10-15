"""Valores distintos (com contagem) de colunas de código: descobre o significado dos domínios.
SOMENTE LEITURA. Só agrega (COUNT) — não retorna linhas de dados de clientes.
Uso: python scripts/valores_distintos.py tabela.coluna [tabela.coluna ...]   (máx. 30 valores por coluna)
Saída também gravada em data/raw/valores_distintos.json (acumulativo).
"""
import json, pathlib, re, sqlite3, sys
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from extractor.db import conectar, select

lite = sqlite3.connect(RAIZ / "data/catalog/dominio_catalog.db")
cn = conectar()
arq = RAIZ / "data/raw/valores_distintos.json"
acum = json.loads(arq.read_text(encoding="utf-8")) if arq.exists() else {}
for spec in sys.argv[1:]:
    t, c = spec.split(".")
    ok = lite.execute("select 1 from colunas where tabela=? collate nocase and nome=? collate nocase", (t, c)).fetchone()
    if not ok or not re.fullmatch(r"\w+", t + c):
        print(f"{spec}: coluna/tabela inexistente no catálogo"); continue
    rows = select(cn, f"SELECT TOP 30 {c} AS v, COUNT(*) AS n FROM bethadba.{t} GROUP BY {c} ORDER BY n DESC")
    tot = select(cn, f"SELECT COUNT(DISTINCT {c}) AS d FROM bethadba.{t}")[0]["d"]
    vals = [[None if r["v"] is None else str(r["v"]).strip(), r["n"]] for r in rows]
    acum[spec.lower()] = {"distintos": tot, "valores": vals}
    print(f"{spec} ({tot} distintos): " + ", ".join(f"{v!r}={n}" for v, n in vals[:14]) + (" ..." if len(vals) > 14 else ""))
arq.write_text(json.dumps(acum, ensure_ascii=False, indent=1), encoding="utf-8")
