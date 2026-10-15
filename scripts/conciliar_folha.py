"""Concilia a Folha com os totais que a própria Domínio guarda (somente agregados; nenhum dado de empregado é exibido).

  1. fobasesserv.proventos  == Σ fomovtoserv.valor_cal dos eventos P  com aparece_recibo = 'S'
  2. fobasesserv.descontos  == Σ fomovtoserv.valor_cal dos eventos D  com aparece_recibo = 'S'
  3. foliquidosfilepr.liquido == proventos − descontos  (por empregado e cálculo)
Uso: python scripts/conciliar_folha.py [empresa ...]      (padrão: 5 empresas de portes diferentes)
"""
import pathlib, sys
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from extractor.db import conectar, select
cn = conectar()
args = [int(a) for a in sys.argv[1:]]
if not args:
    r = select(cn, "SELECT codi_emp, COUNT(*) AS n FROM bethadba.fobasesserv GROUP BY codi_emp HAVING COUNT(*) >= 200 ORDER BY n")
    args = {r[0]["codi_emp"], r[len(r) // 4]["codi_emp"], r[len(r) // 2]["codi_emp"], r[len(r) * 3 // 4]["codi_emp"], r[-1]["codi_emp"]}
    # empresas SEM nenhum evento próprio (usam só os padrões): o caso que a 1ª versão do teste não cobria
    sem = select(cn, "SELECT TOP 4 b.codi_emp, COUNT(*) AS n FROM bethadba.fobasesserv b WHERE NOT EXISTS (SELECT 1 FROM bethadba.foeventos e WHERE e.codi_emp = b.codi_emp) "
                     "GROUP BY b.codi_emp HAVING COUNT(*) >= 100 ORDER BY n DESC")
    args = sorted(args | {s["codi_emp"] for s in sem})
    print("empresas sem eventos próprios incluídas:", [s["codi_emp"] for s in sem])

# REGRA (validada): o evento é resolvido na ordem cadastro da própria empresa (foeventos) -> eventos padrão (foeventosdef);
# ele ENTRA nos totais se aparece_recibo = 'S' OU se não tem cadastro nenhum (default 'S').
# (309 das 310 empresas com movimento sem evento próprio usam só os padrões.)
MOV = """(SELECT v.codi_emp, v.i_empregados, v.data, v.tipo_proces, v.i_servicos, v.rateio, v.I_CALCULOS,
          SUM(CASE WHEN v.prov_desc = 'P' AND COALESCE(e.aparece_recibo, d.aparece_recibo, 'S') = 'S' THEN v.valor_cal ELSE 0 END) AS p,
          SUM(CASE WHEN v.prov_desc = 'D' AND COALESCE(e.aparece_recibo, d.aparece_recibo, 'S') = 'S' THEN v.valor_cal ELSE 0 END) AS d
     FROM bethadba.fomovtoserv v
     LEFT JOIN bethadba.foeventos e ON e.codi_emp = v.codi_emp AND e.i_eventos = v.i_eventos
     LEFT JOIN bethadba.foeventosdef d ON d.i_eventos = v.i_eventos
    WHERE v.codi_emp = {emp}
    GROUP BY v.codi_emp, v.i_empregados, v.data, v.tipo_proces, v.i_servicos, v.rateio, v.I_CALCULOS)"""
JOIN = "m.codi_emp = b.codi_emp AND m.i_empregados = b.i_empregados AND m.data = b.competencia AND m.tipo_proces = b.tipo_process AND m.i_servicos = b.i_servicos AND m.rateio = b.rateio AND m.I_CALCULOS = b.I_CALCULOS"
tot = {"linhas": 0, "prov": 0, "desc": 0}
print(f"{'empresa':<9}{'linhas':>8}{'proventos ok':>14}{'descontos ok':>14}   líquido (empregado×cálculo): iguais/total")
for emp in args:
    r = select(cn, f"""SELECT COUNT(*) AS n, SUM(CASE WHEN ABS(b.proventos - COALESCE(m.p,0)) < 0.005 THEN 1 ELSE 0 END) AS p_ok,
                              SUM(CASE WHEN ABS(b.descontos - COALESCE(m.d,0)) < 0.005 THEN 1 ELSE 0 END) AS d_ok
                         FROM bethadba.fobasesserv b LEFT JOIN {MOV.format(emp=emp)} m ON {JOIN} WHERE b.codi_emp = {emp}""")[0]
    liq = select(cn, f"""
        SELECT COUNT(*) AS n, SUM(CASE WHEN ABS(l.liquido - (x.p - x.d)) < 0.005 THEN 1 ELSE 0 END) AS ok
          FROM (SELECT codi_emp, i_empregados, i_calculos, SUM(liquido) AS liquido FROM bethadba.foliquidosfilepr WHERE codi_emp = {emp}
                 GROUP BY codi_emp, i_empregados, i_calculos) l
          JOIN (SELECT b.codi_emp, b.i_empregados, b.I_CALCULOS AS i_calculos, SUM(b.proventos) AS p, SUM(b.descontos) AS d
                  FROM bethadba.fobasesserv b WHERE b.codi_emp = {emp} GROUP BY b.codi_emp, b.i_empregados, b.I_CALCULOS) x
            ON x.codi_emp = l.codi_emp AND x.i_empregados = l.i_empregados AND x.i_calculos = l.i_calculos""")[0]
    tot["linhas"] += r["n"]; tot["prov"] += r["p_ok"]; tot["desc"] += r["d_ok"]
    print(f"{emp:<9}{r['n']:>8}{r['p_ok']:>11}/{r['n']:<4}{r['d_ok']:>10}/{r['n']:<4}   {liq['ok']}/{liq['n']}")
print(f"\nTOTAL: {tot['linhas']} linhas de base | proventos iguais {tot['prov']} ({100*tot['prov']/max(tot['linhas'],1):.1f}%) | descontos iguais {tot['desc']} ({100*tot['desc']/max(tot['linhas'],1):.1f}%)")
