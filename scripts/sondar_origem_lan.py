"""Descobre o significado de ctlancto.orig_lan cruzando com as tabelas *_lancto do Fiscal (agregados, somente leitura).
Uso: python scripts/sondar_origem_lan.py ORIG [ORIG ...]"""
import pathlib, sys
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from extractor.db import conectar, select
cn = conectar()
TAB = ["efsaidas_lancto", "efentradas_lancto", "efservicos_lancto", "efsaidaspag_lancto", "efentradaspag_lancto", "efservicospag_lancto",
       "efsdoimp_lancto", "efpagimp_lancto", "EFCUPOM_FISCAL_ELETRONICO_LANCTO", "EFECF_CUPOM_FISCAL_LANCTO"]
for orig in map(int, sys.argv[1:]):
    emp = select(cn, f"SELECT TOP 1 codi_emp, COUNT(*) AS n FROM bethadba.ctlancto WHERE orig_lan = {orig} GROUP BY codi_emp ORDER BY n DESC")
    if not emp:
        print(f"orig {orig}: sem lançamentos"); continue
    e, n = emp[0]["codi_emp"], emp[0]["n"]
    partes = []
    for t in TAB:
        col = "codi_emp" if t.lower() not in ("efsaidaspag_lancto", "efentradaspag_lancto", "efservicospag_lancto", "efsaidas_lancto", "efentradas_lancto", "efservicos_lancto") else "fili_lan"
        try:
            k = select(cn, f"SELECT COUNT(*) AS k FROM bethadba.ctlancto l WHERE l.codi_emp = {e} AND l.orig_lan = {orig} AND EXISTS (SELECT 1 FROM bethadba.{t} x WHERE x.{col} = l.codi_emp AND x.nume_lan = l.nume_lan)")[0]["k"]
        except Exception:
            try:
                k = select(cn, f"SELECT COUNT(*) AS k FROM bethadba.ctlancto l WHERE l.codi_emp = {e} AND l.orig_lan = {orig} AND EXISTS (SELECT 1 FROM bethadba.{t} x WHERE x.codi_emp = l.codi_emp AND x.nume_lan = l.nume_lan)")[0]["k"]
            except Exception as ex:
                k = None
        if k:
            partes.append(f"{t}={k}")
    print(f"orig {orig}: empresa {e} ({n} lançamentos) ligados a -> {', '.join(partes) or 'nenhuma tabela testada'}")
