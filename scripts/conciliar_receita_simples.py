"""Conciliação da receita bruta do Simples Nacional: base de cálculo que a Domínio apurou (efsdoimp_simples_nacional, imposto 44, linhas de detalhe)
x receita recomputada = saídas (acumulador IREC=S) + serviços (IREC=S) + CF-e (acumulador IREC=S) - devoluções (entradas, acumulador IDEV=S).
Só agregados. Uso: python scripts/conciliar_receita_simples.py [n_amostra] [seed]"""
import pathlib, random, sys
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from extractor.db import conectar, select
B = "bethadba."
N = int(sys.argv[1]) if len(sys.argv) > 1 else 40
random.seed(int(sys.argv[2]) if len(sys.argv) > 2 else 7)
def r(sql): return select(conectar(), sql, timeout=300)
f = lambda x: float(x or 0)
def vig(col_dt): return f"a.vigencia_acu=(SELECT MAX(v.vigencia_acu) FROM {B}efacumulador_vigencia v WHERE v.codi_emp=n.codi_emp AND v.codi_acu=n.codi_acu AND v.vigencia_acu<={col_dt})"
pares = r(f"SELECT codi_emp, data_sim FROM {B}efsdoimp_simples_nacional WHERE codi_imp=44 AND anexo>0 AND pdic_sim=6 AND data_sim>='2023-01-01' GROUP BY codi_emp, data_sim HAVING SUM(basen)>0")
amostra = random.sample(pares, min(N, len(pares)))
print(f"{len(pares)} pares empresa/competência com base > 0; amostra de {len(amostra)}")
ok = fino = 0; difs = []
for p in amostra:
    E, d = p["codi_emp"], p["data_sim"].isoformat(); fim = f"DATEADD(month,1,'{d}')"
    base = f(r(f"SELECT SUM(basen) b FROM {B}efsdoimp_simples_nacional WHERE codi_emp={E} AND codi_imp=44 AND data_sim='{d}' AND anexo>0")[0]["b"])
    sai = f(r(f"SELECT SUM(CASE WHEN a.irec_acu='S' THEN n.vcon_sai ELSE 0 END) v FROM {B}efsaidas n LEFT JOIN {B}efacumulador_vigencia a ON a.codi_emp=n.codi_emp AND a.codi_acu=n.codi_acu AND {vig('n.dsai_sai')} WHERE n.codi_emp={E} AND n.cancelada_sai='N' AND n.dsai_sai>='{d}' AND n.dsai_sai<{fim}")[0]["v"])
    ser = f(r(f"SELECT SUM(CASE WHEN a.irec_acu='S' THEN n.vcon_ser ELSE 0 END) v FROM {B}efservicos n LEFT JOIN {B}efacumulador_vigencia a ON a.codi_emp=n.codi_emp AND a.codi_acu=n.codi_acu AND {vig('n.dser_ser')} WHERE n.codi_emp={E} AND n.cancelada_ser='N' AND n.dser_ser>='{d}' AND n.dser_ser<{fim}")[0]["v"])
    cfe = f(r(f"SELECT SUM(CASE WHEN a.irec_acu='S' THEN i.valor_total ELSE 0 END) v FROM {B}efcupom_fiscal_eletronico_impostos i JOIN {B}efcupom_fiscal_eletronico h ON h.codi_emp=i.codi_emp AND h.i_cfe=i.i_cfe LEFT JOIN {B}efacumulador_vigencia a ON a.codi_emp=i.codi_emp AND a.codi_acu=i.codi_acu AND a.vigencia_acu=(SELECT MAX(v.vigencia_acu) FROM {B}efacumulador_vigencia v WHERE v.codi_emp=i.codi_emp AND v.codi_acu=i.codi_acu AND v.vigencia_acu<=h.data_cfe) WHERE i.codi_emp={E} AND h.situacao=0 AND h.data_cfe>='{d}' AND h.data_cfe<{fim}")[0]["v"])
    dev = f(r(f"SELECT SUM(CASE WHEN a.idev_acu='S' THEN n.vcon_ent ELSE 0 END) v FROM {B}efentradas n LEFT JOIN {B}efacumulador_vigencia a ON a.codi_emp=n.codi_emp AND a.codi_acu=n.codi_acu AND {vig('n.dent_ent')} WHERE n.codi_emp={E} AND n.dent_ent>='{d}' AND n.dent_ent<{fim}")[0]["v"])
    calc = sai + ser + cfe - dev
    dif = round(calc - base, 2)
    ok += abs(dif) < 0.01; fino += abs(dif) < 1.0; difs.append((abs(dif), E, d, base, calc, dif, sai, ser, cfe, dev))
print(f"exato (< R$ 0,01): {ok}/{len(amostra)} | dentro de R$ 1,00: {fino}/{len(amostra)}")
for x in sorted(difs, reverse=True)[:8]:
    if x[0] >= 0.01:
        print(f"  emp {x[1]} {x[2]} base={x[3]:,.2f} calc={x[4]:,.2f} dif={x[5]:,.2f} (saídas {x[6]:,.2f} serviços {x[7]:,.2f} cfe {x[8]:,.2f} dev {x[9]:,.2f})")
