"""O que ainda não tem entidade curada: agrupa as tabelas legíveis não modeladas por família (prefixo + subcluster)."""
import collections, pathlib, re, sqlite3, sys, yaml
RAIZ = pathlib.Path(__file__).resolve().parents[1]
d = sqlite3.connect(RAIZ / "data/catalog/dominio_catalog.db")
d.row_factory = sqlite3.Row
usadas = set()
for arq in (RAIZ / "src/model/modulos").glob("*.yaml"):
    y = yaml.safe_load(arq.read_text(encoding="utf-8"))
    for e in y["entidades"].values():
        usadas.add(e["tabela"].lower())
        for v in e.get("vinculos", {}).values():
            usadas.add(v["tabela"].lower())
base = d.execute("select count(*) from tabelas where tipo='BASE'").fetchone()[0]
leg = d.execute("select nome_lower, nome, prefixo, departamento, subcluster, linhas, comentario from tabelas where tipo='BASE' and legivel=1 and na_lista_gerador=1").fetchall()
falta = [r for r in leg if r["nome_lower"] not in usadas]
print(f"base={base} | legíveis (fontes do gerador)={len(leg)} | modeladas={len(leg)-len(falta)} | FALTAM={len(falta)} ({sum(r['linhas'] or 0 for r in falta):,} linhas de {sum(r['linhas'] or 0 for r in leg):,})".replace(",", "."))
fora = d.execute("select count(*) from tabelas where tipo='BASE' and (na_lista_gerador=0 or legivel=0)").fetchone()[0]
temp = d.execute("select count(*) from tabelas where tipo='GBL TEMP'").fetchone()[0]
views = d.execute("select count(*) from tabelas where tipo='VIEW'").fetchone()[0]
print(f"fora das fontes do gerador: base não listada={fora} | temporárias={temp} | views={views}")

fam = collections.defaultdict(lambda: {"n": 0, "linhas": 0, "vazias": 0, "ex": []})
for r in falta:
    n = r["nome"].upper(); pref = r["prefixo"]; sub = r["subcluster"]
    chave = f"{pref}_{sub}" if sub not in ("NUCLEO",) else f"{pref} (núcleo)"
    f = fam[(r["departamento"], chave)]
    f["n"] += 1; f["linhas"] += r["linhas"] or 0; f["vazias"] += 0 if r["linhas"] else 1
    if len(f["ex"]) < 3 and (r["linhas"] or 0) > 0:
        f["ex"].append(r["nome"])
print("\nTop famílias não modeladas por nº de tabelas (departamento | família | tabelas | vazias | linhas):")
for (dep, ch), f in sorted(fam.items(), key=lambda x: -x[1]["n"])[:24]:
    print(f"  {dep:<14}{ch:<30}{f['n']:>5}{f['vazias']:>7}{f['linhas']:>14,}".replace(",", "."))
print("\nMaiores famílias por VOLUME de linhas:")
for (dep, ch), f in sorted(fam.items(), key=lambda x: -x[1]["linhas"])[:14]:
    print(f"  {dep:<14}{ch:<30}{f['n']:>5} tabelas {f['linhas']:>14,} linhas".replace(",", "."))
vazias = [r for r in falta if not r["linhas"]]
pequenas = [r for r in falta if 0 < (r["linhas"] or 0) < 1000]
print(f"\nDas {len(falta)} que faltam: vazias={len(vazias)} | <1.000 linhas={len(pequenas)} | >=1.000 linhas={len(falta)-len(vazias)-len(pequenas)}")
print("\nPor departamento (faltam / total):")
dep = collections.Counter(r["departamento"] for r in falta); tot = collections.Counter(r["departamento"] for r in leg)
for k, v in dep.most_common():
    print(f"  {k:<26}{v:>5} / {tot[k]:<5}")
