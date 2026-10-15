"""Sonda quais views/colunas do catálogo SYS o usuário de leitura enxerga."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))
from extractor.db import conectar, select

cn = conectar()
for obj in ["SYSTAB", "SYSTABLE", "SYSTABCOL", "SYSCOLUMN", "SYSCOLUMNS", "SYSIDX", "SYSIDXCOL",
            "SYSFKEY", "SYSFOREIGNKEY", "SYSFOREIGNKEYS", "SYSDOMAIN", "SYSREMARK", "SYSUSER", "SYSPROCEDURE", "SYSVIEW"]:
    try:
        r = select(cn, f"SELECT TOP 1 * FROM SYS.{obj}")
        print(f"OK  SYS.{obj}: {list(r[0].keys()) if r else '(vazia)'}")
    except Exception as e:
        print(f"ERR SYS.{obj}: {str(e)[-90:]}")
