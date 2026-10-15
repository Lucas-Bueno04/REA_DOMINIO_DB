"""Resumo do código do projeto (por análise sintática): arquivos e funções por pasta e as funções principais de cada módulo-chave."""
import collections, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))
from model.gerar_visual import inventario_codigo

inv = inventario_codigo()
por_pasta = collections.defaultdict(lambda: [0, 0, 0, 0])
for a in inv:
    p = por_pasta[a["pasta"]]
    p[0] += 1
    for i in a["itens"]:
        p[{"função": 1, "classe": 2, "método": 3}[i["tipo"]]] += 1
print(f"{'pasta':<16}{'arquivos':>9}{'funções':>9}{'classes':>9}{'métodos':>9}")
for k, (a, f, c, m) in por_pasta.items():
    print(f"{k:<16}{a:>9}{f:>9}{c:>9}{m:>9}")
print(f"{'TOTAL':<16}{sum(v[0] for v in por_pasta.values()):>9}{sum(v[1] for v in por_pasta.values()):>9}{sum(v[2] for v in por_pasta.values()):>9}{sum(v[3] for v in por_pasta.values()):>9}")
for chave in ("src/extractor", "src/model", "src/server"):
    print(f"\n== {chave}")
    for a in inv:
        if a["pasta"] == chave:
            nomes = [i["nome"] for i in a["itens"] if not i["nome"].startswith("_") and "." not in i["nome"]][:7]
            print(f"  {a['arquivo']:<22}{a['descricao'][:90]}\n      {', '.join(nomes)}")
