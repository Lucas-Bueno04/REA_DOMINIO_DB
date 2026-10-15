"""Sonda do Contábil, parte 6: elo Fiscal<->Contábil via efsaidas_lancto (agregados, somente leitura)."""
import pathlib, sys
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from extractor.db import conectar, select
cn = conectar()
EMP = int(sys.argv[1]) if len(sys.argv) > 1 else 1430
def q(titulo, sql):
    print(f"\n== {titulo}")
    for r in select(cn, sql):
        print("  ", {k: (float(v) if hasattr(v, 'as_tuple') else v) for k, v in r.items()})

q("efsaidas_lancto: tipo x origem_lancamento", "SELECT tipo, origem_lancamento, COUNT(*) AS n FROM bethadba.efsaidas_lancto GROUP BY tipo, origem_lancamento ORDER BY n DESC")
q("codi_emp = fili_lan nesta tabela?", "SELECT SUM(CASE WHEN codi_emp = fili_lan THEN 1 ELSE 0 END) AS iguais, SUM(CASE WHEN codi_emp <> fili_lan THEN 1 ELSE 0 END) AS diferentes FROM bethadba.efsaidas_lancto")
q(f"empresa {EMP}: notas de saída contabilizadas — o valor lançado bate com o valor da nota?", f"""
    SELECT COUNT(*) AS notas,
           SUM(CASE WHEN soma_lan = vcon THEN 1 ELSE 0 END) AS soma_igual_vcon,
           SUM(CASE WHEN max_lan = vcon THEN 1 ELSE 0 END) AS maior_lancto_igual_vcon,
           SUM(CASE WHEN soma_deb = vcon THEN 1 ELSE 0 END) AS soma_lado_deb_igual_vcon
      FROM (SELECT s.codi_sai, s.vcon_sai AS vcon, SUM(l.vlor_lan) AS soma_lan, MAX(l.vlor_lan) AS max_lan,
                   SUM(CASE WHEN l.cdeb_lan <> 0 THEN l.vlor_lan ELSE 0 END) AS soma_deb
              FROM bethadba.efsaidas s
              JOIN bethadba.efsaidas_lancto x ON x.codi_emp = s.codi_emp AND x.codi_sai = s.codi_sai
              JOIN bethadba.ctlancto l ON l.codi_emp = x.fili_lan AND l.nume_lan = x.nume_lan
             WHERE s.codi_emp = {EMP} AND s.cancelada_sai = 'N'
             GROUP BY s.codi_sai, s.vcon_sai) t""")
