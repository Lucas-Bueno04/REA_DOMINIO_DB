import sqlite3, pathlib, random
d = sqlite3.connect(pathlib.Path(__file__).resolve().parents[1] / "data/catalog/dominio_catalog.db")
q = lambda s: d.execute(s).fetchall()
random.seed(7)

print("== INFERIDAS: amostra aleatória de 25 (filha -> pai [colunas])")
rows = q("""select r.filha, r.pai, group_concat(c.col_pai) from relacoes r join relacao_colunas c on c.relacao_id=r.id
            where r.origens='inferida' group by r.id""")
for r in random.sample(rows, 25):
    print(f"  {r[0]:<42} -> {r[1]:<34} [{r[2]}]")

print("\n== INFERIDAS: pais com mais filhas")
for r in q("select pai, count(*) n from relacoes where origens='inferida' group by pai order by n desc limit 8"):
    print("  ", tuple(r))

print("\n== CHECAGEM DE COERÊNCIA (declaradas x observadas): para FKs declaradas com uso observado,")
print("   a orientação filha/pai observada concorda com a declarada?")
# nas relações 'declarada,observada' a orientação é a da FK (por construção). Teste independente:
# para observadas puras com par (A,B) onde existe FK declarada A->B OU B->A em OUTRAS colunas, checa direção
n_tot = n_ok = 0
fk = {(r[0].lower(), r[1].lower()) for r in q("select filha, pai from fks")}
for f, p in q("select filha, pai from relacoes where origens='observada' and tipo='fk'"):
    f, p = f.lower(), p.lower()
    if (f, p) in fk or (p, f) in fk:
        n_tot += 1
        n_ok += (f, p) in fk
print(f"   {n_ok}/{n_tot} orientadas como a FK declarada entre as mesmas tabelas")

print("\n== OBSERVADAS tipo 'fk' (alta confiança >=0.9): amostra 15")
rows = q("""select r.filha, r.pai, group_concat(c.col_filha||'→'||c.col_pai), r.ocorrencias, r.arquivos
            from relacoes r join relacao_colunas c on c.relacao_id=r.id where r.origens='observada' and r.tipo='fk' and r.confianca>=0.9 group by r.id""")
for r in random.sample(rows, 15):
    print(f"  {r[0]:<34} -> {r[1]:<30} [{r[2][:60]}] usos={r[3]} prog={r[4]}")
print("\n   total observadas fk >=0.9:", len(rows))

print("\n== Exemplos pedidos: ctlancto, efmvspro, fomovtoserv")
for t in ("ctlancto", "efmvspro", "fomovtoserv"):
    print(f" [{t}]")
    for r in q(f"""select case when lower(r.filha)='{t}' then 'pai: '||r.pai else 'filha: '||r.filha end, r.origens, r.tipo, r.confianca,
                          (select group_concat(col_filha||'→'||col_pai) from relacao_colunas c where c.relacao_id=r.id)
                   from relacoes r where (lower(r.filha)='{t}' or lower(r.pai)='{t}') and r.tipo<>'temporaria' order by r.confianca desc, r.ocorrencias desc limit 12"""):
        print("   ", tuple(r))
