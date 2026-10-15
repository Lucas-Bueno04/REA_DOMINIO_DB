"""Perfil de qualidade das colunas expostas no modelo (somente agregados — nenhuma linha de dados é lida).

Para cada coluna de cada entidade: linhas, não nulos, em branco (texto), zeros (numérico), datas-sentinela
(1900-01-01), mínimo e máximo. Grava na tabela `perfil_colunas` do catálogo SQLite.
Uso: python src/extractor/perfil_colunas.py [modulo ...]      (padrão: fiscal)
Uma consulta por tabela, sequencial, leitura sem bloqueio.
"""
import pathlib
import sqlite3
import sys
import time

import yaml

RAIZ = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "src"))
from extractor.db import conectar, select  # noqa: E402

DB = RAIZ / "data" / "catalog" / "dominio_catalog.db"
MODULOS = RAIZ / "src" / "model" / "modulos"


def colunas_reais(e) -> list[str]:
    cs = [(v["coluna"] if isinstance(v, dict) else v) for v in e["colunas"].values()]
    # colunas de vínculo pertencem a outra tabela: são perfiladas na entidade dona dessa tabela
    return list(dict.fromkeys(c.lower() for c in cs))


def colunas_sensiveis(e) -> set[str]:
    """Colunas marcadas `sensivel` no modelo: para elas NÃO se guarda mínimo/máximo (seriam valores individuais, ex.: o maior salário)."""
    return {v["coluna"].lower() for v in e["colunas"].values() if isinstance(v, dict) and v.get("sensivel")}


def main(mods: list[str]) -> None:
    lite = sqlite3.connect(DB)
    lite.execute("""CREATE TABLE IF NOT EXISTS perfil_colunas(tabela TEXT, coluna TEXT, tipo TEXT, linhas INTEGER, nao_nulos INTEGER,
                    em_branco INTEGER, zeros INTEGER, sentinela INTEGER, minimo TEXT, maximo TEXT, gerado_em TEXT,
                    PRIMARY KEY(tabela, coluna))""")
    tipos = {(t, c): tp for t, c, tp in lite.execute("select lower(tabela), lower(nome), tipo from colunas")}
    cn = conectar()
    feitas = set()
    for m in mods:
        d = yaml.safe_load((MODULOS / f"{m}.yaml").read_text(encoding="utf-8"))
        for nome, e in d["entidades"].items():
            t = e["tabela"].lower()
            if t in feitas:
                continue
            feitas.add(t)
            cols = [c for c in colunas_reais(e) if (t, c) in tipos]
            sens = colunas_sensiveis(e)
            sel = ["COUNT(*) AS linhas"]
            for i, c in enumerate(cols):
                tp = tipos[(t, c)]
                sel.append(f"COUNT({c}) AS nn{i}")
                if tp in ("char", "varchar", "long varchar"):
                    sel.append(f"SUM(CASE WHEN TRIM({c}) = '' THEN 1 ELSE 0 END) AS br{i}")
                elif tp in ("date", "timestamp"):
                    sel.append(f"SUM(CASE WHEN CAST({c} AS DATE) = '1900-01-01' THEN 1 ELSE 0 END) AS se{i}")
                    if c not in sens:
                        sel.append(f"MIN(CASE WHEN CAST({c} AS DATE) > '1900-01-01' THEN {c} END) AS mn{i}")
                        sel.append(f"MAX({c}) AS mx{i}")
                elif tp in ("integer", "smallint", "tinyint", "numeric", "decimal", "double", "bigint", "float", "real"):
                    sel.append(f"SUM(CASE WHEN {c} = 0 THEN 1 ELSE 0 END) AS ze{i}")
                    if c not in sens:
                        sel.append(f"MIN({c}) AS mn{i}")
                        sel.append(f"MAX({c}) AS mx{i}")
            t0 = time.time()
            r = select(cn, f"SELECT {', '.join(sel)} FROM bethadba.{t}")[0]
            agora = time.strftime("%Y-%m-%d %H:%M:%S")
            for i, c in enumerate(cols):
                g = lambda k: r.get(f"{k}{i}")
                lite.execute("INSERT OR REPLACE INTO perfil_colunas VALUES(?,?,?,?,?,?,?,?,?,?,?)",
                             (t, c, tipos[(t, c)], r["linhas"], g("nn"), g("br"), g("ze"), g("se"),
                              None if g("mn") is None else str(g("mn")), None if g("mx") is None else str(g("mx")), agora))
            lite.commit()
            print(f"{t:<24}{r['linhas']:>10,} linhas  {len(cols):>3} colunas  {time.time()-t0:5.1f}s", flush=True)


if __name__ == "__main__":
    main(sys.argv[1:] or ["fiscal"])
