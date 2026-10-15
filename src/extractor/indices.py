"""Extrai os índices (únicos e não únicos) das tabelas do owner bethadba para o catálogo.
Servem para: (1) identificar chave única nas tabelas sem PK; (2) orientar filtros/ordenação
eficientes na camada de consulta (colunas indexadas).

Uso: python src/extractor/indices.py
"""
import pathlib
import sqlite3
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from extractor.db import conectar, select  # noqa: E402

DB = pathlib.Path(__file__).resolve().parents[2] / "data" / "catalog" / "dominio_catalog.db"


def main() -> None:
    cn = conectar()
    rows = select(cn, """
        SELECT t.table_name AS tabela, i.index_name AS indice, i.index_category AS categoria,
               i."unique" AS unico, ic.sequence AS seq, c.column_name AS coluna
          FROM SYS.SYSIDX i
          JOIN SYS.SYSIDXCOL ic ON ic.table_id = i.table_id AND ic.index_id = i.index_id
          JOIN SYS.SYSTABCOL c ON c.table_id = ic.table_id AND c.column_id = ic.column_id
          JOIN SYS.SYSTAB t ON t.table_id = i.table_id
          JOIN SYS.SYSUSER u ON u.user_id = t.creator
         WHERE u.user_name = 'bethadba'
         ORDER BY t.table_name, i.index_id, ic.sequence""")
    lite = sqlite3.connect(DB)
    lite.executescript("""
        DROP TABLE IF EXISTS indices;
        CREATE TABLE indices(tabela TEXT, indice TEXT, categoria INTEGER, unico INTEGER, colunas TEXT,
                             PRIMARY KEY(tabela, indice));""")
    agg: dict = {}
    for r in rows:
        k = (r["tabela"], r["indice"])
        a = agg.setdefault(k, {"cat": r["categoria"], "uni": r["unico"], "cols": []})
        a["cols"].append(r["coluna"])
    lite.executemany("INSERT INTO indices VALUES(?,?,?,?,?)",
                     [(t, i, v["cat"], int(v["uni"] in (1, 2, "1", "2", "Y")), ",".join(v["cols"])) for (t, i), v in agg.items()])
    lite.commit()
    n = lite.execute("select count(*), sum(unico) from indices").fetchone()
    print(f"{n[0]} índices ({n[1]} únicos)")
    cats = lite.execute("select categoria, unico, count(*) from indices group by 1,2").fetchall()
    print("categoria/único:", cats)


if __name__ == "__main__":
    main()
