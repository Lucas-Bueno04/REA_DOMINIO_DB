"""Lista tabelas do catálogo por prefixo/subcluster/padrão.  Uso: python scripts/listar_tabelas.py PREFIXO [--nucleo] [--like padrao] [--max N]"""
import pathlib, sqlite3, sys
d = sqlite3.connect(pathlib.Path(__file__).resolve().parents[1] / "data/catalog/dominio_catalog.db")
a = sys.argv[1:]
pref = a[0].upper()
mx = int(a[a.index("--max") + 1]) if "--max" in a else 40
like = a[a.index("--like") + 1].lower() if "--like" in a else None
sql = "select nome, linhas, comentario from tabelas where tipo='BASE' and legivel=1 and prefixo=?"
par = [pref]
if "--nucleo" in a:
    sql += " and subcluster='NUCLEO'"
if like:
    sql += " and (nome_lower like ? or lower(comentario) like ?)"; par += [f"%{like}%"] * 2
sql += " order by linhas desc limit ?"
for n, l, c in d.execute(sql, par + [mx]):
    print(f"{n:<34}{l:>12,}  {(c or '-')[:72]}")
