import sqlite3, pathlib
db = sqlite3.connect(pathlib.Path(__file__).resolve().parents[1] / "data/catalog/dominio_catalog.db")
q = lambda s: db.execute(s).fetchall()
print("tabelas/views:", q("select count(*) from tabelas")[0][0], "| na lista do gerador:", q("select count(*) from tabelas where na_lista_gerador=1")[0][0],
      "| legíveis:", q("select count(*) from tabelas where legivel=1")[0][0],
      "| gerador+legível:", q("select count(*) from tabelas where na_lista_gerador=1 and legivel=1")[0][0])
print("colunas:", q("select count(*) from colunas")[0][0], "| FKs:", q("select count(*) from fks")[0][0])
print("tabelas sem colunas:", q("select count(*) from tabelas t where not exists (select 1 from colunas c where c.table_id=t.table_id)")[0][0])
print("tabelas sem PK (base):", q("select count(*) from tabelas t where tipo='BASE' and not exists (select 1 from colunas c where c.table_id=t.table_id and c.pk=1)")[0][0])
print("FKs com tabela não encontrada:", q("select count(*) from fks f where not exists(select 1 from tabelas t where t.nome_lower=lower(f.filha)) or not exists(select 1 from tabelas t where t.nome_lower=lower(f.pai))")[0][0])
print("com comentario: tabelas", q("select count(*) from tabelas where comentario is not null")[0][0], "| colunas", q("select count(*) from colunas where comentario is not null")[0][0])
print("\nTipos de objeto:", q("select tipo,count(*) from tabelas group by tipo"))
print("\nDepartamento (gerador): tabelas / colunas / linhas")
for r in q("""select t.departamento, count(distinct t.table_id), count(c.ordem), sum(distinct 0)+ (select sum(linhas) from tabelas x where x.departamento=t.departamento and x.na_lista_gerador=1)
              from tabelas t left join colunas c on c.table_id=t.table_id where t.na_lista_gerador=1 group by 1 order by 2 desc"""):
    print(f"  {r[0]:<26}{r[1]:>6}{r[2]:>9}{(r[3] or 0):>14,}")
print("\nTop 10 por colunas:", q("select tabela,count(*) n from colunas group by tabela order by n desc limit 10"))
print("Tipos de coluna:", q("select tipo,count(*) from colunas group by tipo order by 2 desc limit 12"))
