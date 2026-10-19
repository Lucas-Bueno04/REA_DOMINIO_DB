"""Sonda do saldo de produtos (EFSDOPRO / EFSDOPRO_DIARIO): identidades de saldo, continuidade entre meses e contra o movimento. Só agregados.
Uso: python scripts/sondar_saldo_produtos.py [empresa]"""
import pathlib, sys
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from extractor.db import conectar, select
B = "bethadba."
def q(titulo, sql):
    print(f"\n== {titulo}")
    try:
        for r in select(conectar(), sql, timeout=180):
            print("  ", {k: (float(v) if hasattr(v, 'as_tuple') else (v.strip() if isinstance(v, str) else v)) for k, v in r.items()})
    except Exception as e:
        print("   ERRO:", str(e)[:250])
E = sys.argv[1] if len(sys.argv) > 1 else None
if not E:
    q("empresas por volume (mediana)", f"SELECT TOP 8 codi_emp, COUNT(*) n, COUNT(DISTINCT codi_pdi) produtos, MIN(data_pro) de, MAX(data_pro) ate FROM {B}efsdopro GROUP BY codi_emp HAVING COUNT(*) BETWEEN 20000 AND 80000 ORDER BY n DESC")
    sys.exit()
q("origem_reg e saldo_valido", f"SELECT origem_reg, saldo_valido, COUNT(*) n FROM {B}efsdopro WHERE codi_emp={E} GROUP BY origem_reg, saldo_valido ORDER BY n DESC")
q("identidade física: sfismes = sfisant + entfis - saifis", f"SELECT COUNT(*) n, SUM(CASE WHEN ABS(sfismes_pro-(sfisant_pro+entfis_pro-saifis_pro))<0.0001 THEN 1 ELSE 0 END) fisica_ok, SUM(CASE WHEN ABS(svalmes_pro-(svalant_pro+entval_pro-saival_pro))<0.01 THEN 1 ELSE 0 END) valor_ok, SUM(CASE WHEN ABS(sfismes_pro-(sfisant_pro+entfis_pro-saifis_pro))<0.0001 AND ABS(svalmes_pro-(svalant_pro+entval_pro-saival_pro))<0.01 THEN 1 ELSE 0 END) ambas_ok FROM {B}efsdopro WHERE codi_emp={E}")
q("continuidade: saldo anterior = saldo do mês anterior (mesmo produto)", f"SELECT COUNT(*) pares, SUM(CASE WHEN ABS(a.sfisant_pro-p.sfismes_pro)<0.0001 THEN 1 ELSE 0 END) fisico_igual, SUM(CASE WHEN ABS(a.svalant_pro-p.svalmes_pro)<0.01 THEN 1 ELSE 0 END) valor_igual FROM {B}efsdopro a JOIN {B}efsdopro p ON p.codi_emp=a.codi_emp AND p.codi_pdi=a.codi_pdi AND p.data_pro=DATEADD(month,-1,a.data_pro) WHERE a.codi_emp={E}")
q("meses com lacuna: produtos com saldo anterior <> 0 sem registro do mês anterior", f"SELECT COUNT(*) n FROM {B}efsdopro a WHERE a.codi_emp={E} AND (a.sfisant_pro<>0 OR a.svalant_pro<>0) AND NOT EXISTS (SELECT 1 FROM {B}efsdopro p WHERE p.codi_emp=a.codi_emp AND p.codi_pdi=a.codi_pdi AND p.data_pro=DATEADD(month,-1,a.data_pro))")
q("entradas do mês x efmvepro (qtde) — soma por mês", f"SELECT COUNT(*) meses_produtos, SUM(CASE WHEN ABS(s.entfis_pro-COALESCE(m.q,0))<0.0001 THEN 1 ELSE 0 END) igual, SUM(CASE WHEN s.entfis_pro>COALESCE(m.q,0)+0.0001 THEN 1 ELSE 0 END) saldo_maior, SUM(CASE WHEN s.entfis_pro<COALESCE(m.q,0)-0.0001 THEN 1 ELSE 0 END) saldo_menor FROM {B}efsdopro s LEFT JOIN (SELECT me.codi_emp, me.codi_pdi, DATEFORMAT(e.dent_ent,'YYYY-MM-01') mes, SUM(me.qtde_mep) q FROM {B}efmvepro me JOIN {B}efentradas e ON e.codi_emp=me.codi_emp AND e.codi_ent=me.codi_ent WHERE me.codi_emp={E} GROUP BY me.codi_emp, me.codi_pdi, mes) m ON m.codi_emp=s.codi_emp AND m.codi_pdi=s.codi_pdi AND m.mes=DATEFORMAT(s.data_pro,'YYYY-MM-01') WHERE s.codi_emp={E}")
q("saídas do mês x efmvspro (qtde) — soma por mês", f"SELECT COUNT(*) meses_produtos, SUM(CASE WHEN ABS(s.saifis_pro-COALESCE(m.q,0))<0.0001 THEN 1 ELSE 0 END) igual, SUM(CASE WHEN s.saifis_pro>COALESCE(m.q,0)+0.0001 THEN 1 ELSE 0 END) saldo_maior, SUM(CASE WHEN s.saifis_pro<COALESCE(m.q,0)-0.0001 THEN 1 ELSE 0 END) saldo_menor FROM {B}efsdopro s LEFT JOIN (SELECT ms.codi_emp, ms.codi_pdi, DATEFORMAT(sa.dsai_sai,'YYYY-MM-01') mes, SUM(ms.qtde_msp) q FROM {B}efmvspro ms JOIN {B}efsaidas sa ON sa.codi_emp=ms.codi_emp AND sa.codi_sai=ms.codi_sai WHERE ms.codi_emp={E} GROUP BY ms.codi_emp, ms.codi_pdi, mes) m ON m.codi_emp=s.codi_emp AND m.codi_pdi=s.codi_pdi AND m.mes=DATEFORMAT(s.data_pro,'YYYY-MM-01') WHERE s.codi_emp={E}")
q("Portaria CAT 17/99: estoque_final x valor_unitario = saldo_final", f"SELECT COUNT(*) n, SUM(CASE WHEN estoque_final IS NOT NULL THEN 1 ELSE 0 END) com_dado, SUM(CASE WHEN estoque_final IS NOT NULL AND ABS(estoque_final*valor_unitario - saldo_final)<0.05 THEN 1 ELSE 0 END) produto_ok FROM {B}efsdopro WHERE codi_emp={E}")
q("diário: saldo final do último dia do mês x saldo do mês (físico)", f"SELECT COUNT(*) n_meses, SUM(CASE WHEN ABS(d.saldo_fisico_final - s.sfismes_pro)<0.0001 THEN 1 ELSE 0 END) fisico_igual FROM (SELECT codi_emp, codi_pdi, data_pro, dia_saldo, saldo_fisico_final, ROW_NUMBER() OVER (PARTITION BY codi_emp, codi_pdi, data_pro ORDER BY dia_saldo DESC) rn FROM {B}efsdopro_diario WHERE codi_emp={E}) d JOIN {B}efsdopro s ON s.codi_emp=d.codi_emp AND s.codi_pdi=d.codi_pdi AND s.data_pro=d.data_pro WHERE d.rn=1")
