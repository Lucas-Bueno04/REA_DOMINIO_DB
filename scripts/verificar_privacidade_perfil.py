"""Garante que o perfil de colunas não guarda mínimo/máximo de colunas marcadas `sensivel` nos modelos YAML."""
import pathlib, sqlite3, sys, yaml
RAIZ = pathlib.Path(__file__).resolve().parents[1]
d = sqlite3.connect(RAIZ / "data/catalog/dominio_catalog.db")
viol, total = [], 0
for arq in sorted((RAIZ / "src/model/modulos").glob("*.yaml")):
    y = yaml.safe_load(arq.read_text(encoding="utf-8"))
    for nome, e in y["entidades"].items():
        for api, v in e["colunas"].items():
            if isinstance(v, dict) and v.get("sensivel"):
                total += 1
                r = d.execute("select minimo, maximo from perfil_colunas where tabela=? and coluna=?", (e["tabela"].lower(), v["coluna"].lower())).fetchone()
                if r and (r[0] is not None or r[1] is not None):
                    viol.append(f"{nome}.{api} ({e['tabela']}.{v['coluna']}): min={r[0]!r} max={r[1]!r}")
print(f"{total} colunas sensíveis nos modelos; {len(viol)} com mínimo/máximo guardado")
for x in viol:
    print("  VIOLAÇÃO:", x)
sys.exit(1 if viol else 0)
