"""Concilia a base de cálculo do Simples Nacional (efsdoimp_simples_nacional, imposto 44) com a receita das notas de saída, serviços e CF-e.
Só agregados. Uso: python scripts/sondar_receita_simples.py <empresa> [competencias]"""
import pathlib, sys
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from extractor.db import conectar, select
B = "bethadba."
E = int(sys.argv[1]); N = int(sys.argv[2]) if len(sys.argv) > 2 else 12
def rows(sql):
    return select(conectar(), sql, timeout=300)
sim = rows(f"SELECT TOP {N} data_sim, pdic_sim, SUM(basen) basen, SUM(bases) bases, SUM(basee) basee, SUM(valorn) valorn, COUNT(*) linhas FROM {B}efsdoimp_simples_nacional WHERE codi_emp={E} AND codi_imp=44 GROUP BY data_sim, pdic_sim ORDER BY data_sim DESC")
print(f"empresa {E}: {len(sim)} competências")
print(f"{'comp':<11}{'pdic':>5}{'basen':>14}{'bases':>12}{'basee':>12}{'saídas':>14}{'serviços':>14}{'cfe':>14}{'soma':>14}{'dif':>12}")
for r in sim:
    d = r["data_sim"].isoformat(); ini = d; 
    fim = f"DATEADD(month,1,'{d}')"
    s = rows(f"SELECT COALESCE(SUM(vcon_sai),0) v FROM {B}efsaidas WHERE codi_emp={E} AND cancelada_sai='N' AND dsai_sai>='{ini}' AND dsai_sai<{fim}")[0]["v"]
    v = rows(f"SELECT COALESCE(SUM(vcon_ser),0) v FROM {B}efservicos WHERE codi_emp={E} AND cancelada_ser='N' AND dser_ser>='{ini}' AND dser_ser<{fim}")[0]["v"]
    c = rows(f"SELECT COALESCE(SUM(valor_total_cfe),0) v FROM {B}efcupom_fiscal_eletronico WHERE codi_emp={E} AND situacao=0 AND data_cfe>='{ini}' AND data_cfe<{fim}")[0]["v"]
    tot = float(s) + float(v) + float(c)
    base = float(r["basen"] or 0) + float(r["bases"] or 0) + float(r["basee"] or 0)
    print(f"{d:<11}{r['pdic_sim']:>5}{float(r['basen'] or 0):>14,.2f}{float(r['bases'] or 0):>12,.2f}{float(r['basee'] or 0):>12,.2f}{float(s):>14,.2f}{float(v):>14,.2f}{float(c):>14,.2f}{tot:>14,.2f}{base - tot:>12,.2f}")
