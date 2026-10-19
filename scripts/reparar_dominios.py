"""Recria, nos módulos "Gerado em lote", os domínios referenciados por colunas mas ausentes (a partir dos comentários do banco, como o gerador faz).
Os recriados nascem `confirmado: parcial`; rode depois `scripts/medir_fatos.py --refazer <modulo>` para confirmá-los contra os dados.
Uso: python scripts/reparar_dominios.py"""
import pathlib, sqlite3, sys
import yaml
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from plataforma import dados
d = sqlite3.connect(RAIZ / "data/catalog/dominio_catalog.db")
n = 0
for arq in sorted((RAIZ / "src/model/modulos").glob("*.yaml")):
    txt = arq.read_text(encoding="utf-8")
    if "Gerado em lote" not in txt[:200]:
        continue
    cab = txt.split("\nmodulo:", 1)[0]; y = yaml.safe_load(txt); doms = y.setdefault("dominios", {}); mud = False
    for e in y["entidades"].values():
        for v in e["colunas"].values():
            if isinstance(v, dict) and v.get("dominio") and v["dominio"] not in doms:
                com = (d.execute("select comentario from colunas where tabela=? collate nocase and nome=? collate nocase", (e["tabela"], v["coluna"])).fetchone() or [""])[0]
                dm = dados.dominio_do_comentario(com)
                if dm:
                    doms[v["dominio"]] = {"confirmado": "parcial", "nota": "Extraído do comentário da coluna; não confirmado contra os dados.", "valores": dm}
                    mud = True; n += 1
    if mud:
        arq.write_text(cab + "\n" + yaml.safe_dump(y, allow_unicode=True, sort_keys=False, width=160, default_flow_style=None), encoding="utf-8")
print(n, "domínios recriados")
