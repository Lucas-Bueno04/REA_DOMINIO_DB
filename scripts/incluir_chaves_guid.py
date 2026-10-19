"""Inclui, nas entidades dos módulos "Gerado em lote", as colunas uniqueidentifier (GUID) que são PK ou FK e que o primeiro lote deixou de fora.
Idempotente. Uso: python scripts/incluir_chaves_guid.py"""
import pathlib, sqlite3, sys
import yaml
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from plataforma import dados
d = sqlite3.connect(RAIZ / "data/catalog/dominio_catalog.db")
fk = set()
for f, cf, p, cp in d.execute("select lower(filha), colunas_filha, lower(pai), colunas_pai from fks"):
    fk |= {(f, c.strip().lower()) for c in cf.split(",")} | {(p, c.strip().lower()) for c in cp.split(",")}
n = 0
for arq in sorted((RAIZ / "src/model/modulos").glob("*.yaml")):
    txt = arq.read_text(encoding="utf-8")
    if "Gerado em lote" not in txt[:200]:
        continue
    cab = txt.split("\nmodulo:", 1)[0]; y = yaml.safe_load(txt); mud = False
    for e in y["entidades"].values():
        t = e["tabela"].lower()
        expostas = {(v["coluna"] if isinstance(v, dict) else v).lower() for v in e["colunas"].values()}
        for nome, pk in d.execute("select nome, pk from colunas where tabela=? collate nocase and tipo='uniqueidentifier'", (e["tabela"],)):
            if nome.lower() in expostas or not (pk or (t, nome.lower()) in fk):
                continue
            api = dados._slug(nome, 40)
            while api in e["colunas"]:
                api += "_g"
            e["colunas"][api] = nome
            e.setdefault("filtros", {})[api] = {"coluna": nome, "ops": ["eq", "in"]}
            mud = True; n += 1
    if mud:
        arq.write_text(cab + "\n" + yaml.safe_dump(y, allow_unicode=True, sort_keys=False, width=160, default_flow_style=None), encoding="utf-8")
print(n, "colunas GUID de chave incluídas")
