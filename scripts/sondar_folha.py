"""Sonda da Folha, parte 8: por que a regra falha em empresas que usam eventos padrão (somente agregados)."""
import pathlib, sys
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from extractor.db import conectar, select
cn = conectar()
JOIN = "m.codi_emp = b.codi_emp AND m.i_empregados = b.i_empregados AND m.data = b.competencia AND m.tipo_proces = b.tipo_process AND m.i_servicos = b.i_servicos AND m.rateio = b.rateio AND m.I_CALCULOS = b.I_CALCULOS"
for emp in map(int, sys.argv[1:]):
    print(f"\n######## empresa {emp}")
    for rotulo, cond_p, cond_d in [
        ("todos P / todos D (sem filtro)", "1=1", "1=1"),
        ("aparece_recibo='S' (padrão)", "COALESCE(e.aparece_recibo, d.aparece_recibo) = 'S'", "COALESCE(e.aparece_recibo, d.aparece_recibo) = 'S'"),
        ("soma_fic_fin='S' (padrão)", "COALESCE(e.soma_fic_fin, d.soma_fic_fin) = 'S'", "COALESCE(e.soma_fic_fin, d.soma_fic_fin) = 'S'"),
        ("recibo='S' ou evento sem cadastro", "(COALESCE(e.aparece_recibo, d.aparece_recibo) = 'S' OR (e.i_eventos IS NULL AND d.i_eventos IS NULL))", "(COALESCE(e.aparece_recibo, d.aparece_recibo) = 'S' OR (e.i_eventos IS NULL AND d.i_eventos IS NULL))"),
    ]:
        r = select(cn, f"""
            SELECT COUNT(*) AS linhas,
                   SUM(CASE WHEN ABS(b.proventos - COALESCE(m.p,0)) < 0.005 THEN 1 ELSE 0 END) AS prov_ok,
                   SUM(CASE WHEN ABS(b.descontos - COALESCE(m.d,0)) < 0.005 THEN 1 ELSE 0 END) AS desc_ok
              FROM bethadba.fobasesserv b
              LEFT JOIN (SELECT v.codi_emp, v.i_empregados, v.data, v.tipo_proces, v.i_servicos, v.rateio, v.I_CALCULOS,
                                SUM(CASE WHEN v.prov_desc = 'P' AND {cond_p} THEN v.valor_cal ELSE 0 END) AS p,
                                SUM(CASE WHEN v.prov_desc = 'D' AND {cond_d} THEN v.valor_cal ELSE 0 END) AS d
                           FROM bethadba.fomovtoserv v
                           LEFT JOIN bethadba.foeventos e ON e.codi_emp = v.codi_emp AND e.i_eventos = v.i_eventos
                           LEFT JOIN bethadba.foeventosdef d ON d.i_eventos = v.i_eventos
                          WHERE v.codi_emp = {emp} GROUP BY v.codi_emp, v.i_empregados, v.data, v.tipo_proces, v.i_servicos, v.rateio, v.I_CALCULOS) m ON {JOIN}
             WHERE b.codi_emp = {emp}""")[0]
        print(f"  {rotulo:<40} linhas={r['linhas']}  proventos={r['prov_ok']}  descontos={r['desc_ok']}")
    # existência de eventos próprios x padrão e competência dos movimentos
    r = select(cn, f"SELECT MIN(data) AS min_comp, MAX(data) AS max_comp, COUNT(*) AS movimentos FROM bethadba.fomovtoserv WHERE codi_emp = {emp}")[0]
    print(f"  movimentos {r['movimentos']} de {r['min_comp']} a {r['max_comp']}")
    r = select(cn, f"""SELECT SUM(CASE WHEN d.i_eventos IS NULL THEN 1 ELSE 0 END) AS sem_padrao, COUNT(*) AS total
                         FROM bethadba.fomovtoserv v LEFT JOIN bethadba.foeventosdef d ON d.i_eventos = v.i_eventos WHERE v.codi_emp = {emp}""")[0]
    print(f"  movimentos cujo evento NÃO existe nos padrões: {r['sem_padrao']}/{r['total']}")
