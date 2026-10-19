"""Remove dos módulos "Gerado em lote" as colunas que são código do próprio sistema (scripts, fórmulas, cláusulas compiladas, texto >= 1000 caracteres).
Idempotente. Uso: python scripts/limpar_colunas_script.py"""
import pathlib, re, sqlite3
import yaml
RAIZ = pathlib.Path(__file__).resolve().parents[1]
d = sqlite3.connect(RAIZ / "data/catalog/dominio_catalog.db")
SCRIPT = re.compile(r"script|^fil\d$|^frm_|compila|^comando_|clausula|^codi_comp$", re.I)
tam = {(r[0].lower(), r[1].lower()): (r[2], r[3] or 0) for r in d.execute("select tabela, nome, tipo, tamanho from colunas")}
rem = ents = 0
for arq in sorted((RAIZ / "src/model/modulos").glob("*.yaml")):
    txt = arq.read_text(encoding="utf-8")
    if "Gerado em lote" not in txt[:200]:
        continue
    cab = txt.split("\nmodulo:", 1)[0]; y = yaml.safe_load(txt); mud = False
    for e in y["entidades"].values():
        t = e["tabela"].lower(); chave = {c.lower() for c in e["chave"]}
        for api, v in list(e["colunas"].items()):
            col = v["coluna"] if isinstance(v, dict) else v
            tipo, n = tam.get((t, col.lower()), ("", 0))
            if SCRIPT.search(col) and tipo in ("varchar", "char") and n >= 1000 and col.lower() not in chave:
                del e["colunas"][api]; rem += 1; mud = True
                for fn in [k for k, f in e.get("filtros", {}).items() if f["coluna"] == col]:
                    del e["filtros"][fn]
                    if fn in e.get("acesso", {}).get("exige_algum", []):
                        e["acesso"]["exige_algum"].remove(fn)
        if mud:
            ents += 1
    if mud:
        arq.write_text(cab + "\n" + yaml.safe_dump(y, allow_unicode=True, sort_keys=False, width=160, default_flow_style=None), encoding="utf-8")
print(rem, "colunas de código do sistema removidas de", ents, "entidades")
