"""Remove de módulos "Gerado em lote" a(s) entidade(s) de uma tabela, para que passe a ser mantida à mão em um módulo manual.
Uso: python scripts/curar_entidade.py <tabela> [<tabela> ...]
Imprime o módulo gerado de onde saiu. Rode ANTES de adicionar a entidade curada ao módulo manual (nome de entidade é único no modelo)."""
import pathlib, sys
import yaml

MODULOS = pathlib.Path(__file__).resolve().parents[1] / "src" / "model" / "modulos"
alvo = {t.lower() for t in sys.argv[1:]}
for arq in sorted(MODULOS.glob("*.yaml")):
    txt = arq.read_text(encoding="utf-8")
    if "Gerado em lote" not in txt[:200]:
        continue
    cab = txt.split("\nmodulo:", 1)[0]
    y = yaml.safe_load(txt); tirou = []
    for n in [n for n, e in y["entidades"].items() if e["tabela"].lower() in alvo]:
        usados = {c["dominio"] for c in y["entidades"][n]["colunas"].values() if isinstance(c, dict) and c.get("dominio")}
        del y["entidades"][n]; tirou.append(n)
        # só remove domínios que a entidade retirada usava E que nenhuma outra entidade do arquivo usa (nunca por prefixo de nome)
        restantes = {c["dominio"] for e in y["entidades"].values() for c in e["colunas"].values() if isinstance(c, dict) and c.get("dominio")}
        for dn in usados - restantes:
            y.get("dominios", {}).pop(dn, None)
    if tirou:
        arq.write_text(cab + "\n" + yaml.safe_dump(y, allow_unicode=True, sort_keys=False, width=160, default_flow_style=None), encoding="utf-8")
        print(arq.name, "->", tirou)
