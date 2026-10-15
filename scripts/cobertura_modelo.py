"""Cobertura do modelo de entidades frente às tabelas legíveis do catálogo (sem acessar o banco)."""
import collections, pathlib, sqlite3, yaml
RAIZ = pathlib.Path(__file__).resolve().parents[1]
d = sqlite3.connect(RAIZ / "data/catalog/dominio_catalog.db")
usadas, por_modulo = {}, collections.defaultdict(set)
cons = collections.Counter()
for arq in sorted((RAIZ / "src/model/modulos").glob("*.yaml")):
    y = yaml.safe_load(arq.read_text(encoding="utf-8"))
    for n, e in y["entidades"].items():
        usadas[e["tabela"].lower()] = y["modulo"]
        por_modulo[y["modulo"]].add(e["tabela"].lower())
        for v in e.get("vinculos", {}).values():
            usadas.setdefault(v["tabela"].lower(), y["modulo"] + " (só vínculo)")
    cons[y["modulo"]] = len(y["entidades"])
ent_total = sum(cons.values())
leg = d.execute("select nome_lower, departamento, linhas from tabelas where tipo='BASE' and legivel=1 and na_lista_gerador=1").fetchall()
tot_t, tot_l = len(leg), sum(l or 0 for _, _, l in leg)
mod_t = [(n, dep, l or 0) for n, dep, l in leg if n in usadas]
print(f"Entidades: {ent_total}  ({', '.join(f'{m}={c}' for m, c in cons.items())})")
print(f"Tabelas legíveis (fontes do gerador): {tot_t:,}  |  linhas: {tot_l:,}".replace(",", "."))
print(f"Tabelas tocadas pelo modelo: {len(mod_t)} ({100*len(mod_t)/tot_t:.1f}%)  |  linhas: {sum(x[2] for x in mod_t):,} ({100*sum(x[2] for x in mod_t)/tot_l:.1f}%)".replace(",", "."))
print("\nPor departamento: tabelas modeladas / total  |  % das linhas")
agg = collections.defaultdict(lambda: [0, 0, 0, 0])
for n, dep, l in leg:
    a = agg[dep]; a[1] += 1; a[3] += l or 0
    if n in usadas:
        a[0] += 1; a[2] += l or 0
for dep, (m, t, ml, tl) in sorted(agg.items(), key=lambda x: -x[1][1]):
    print(f"  {dep:<26}{m:>5} / {t:<6}{100*m/t:>5.1f}%   |  {100*ml/max(tl,1):>5.1f}% das linhas")
print("\nMaiores tabelas ainda NÃO modeladas (top 15 por linhas):")
for n, dep, l in sorted([x for x in leg if x[0] not in usadas], key=lambda x: -x[2])[:15]:
    c = d.execute("select comentario from tabelas where nome_lower=?", (n,)).fetchone()[0]
    print(f"  {n:<44}{l:>12,}  {dep:<12}{(c or '')[:50]}".replace(",", "."))
