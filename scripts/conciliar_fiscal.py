"""Concilia o modelo com a apuração da própria Domínio (efsdoimp) — valida o SIGNIFICADO das colunas.

Para uma empresa e competências mensais já apuradas, compara:
  saídas   : efsdoimp.vcos_sim (valor contábil de saídas)  x  SUM(efsaidas.vcon_sai)  por mês de dsai_sai
  entradas : efsdoimp.vcoe_sim                              x  SUM(efentradas.vcon_ent) por mês de dent_ent
  serviços : efsdoimp.vcov_sim                              x  SUM(efservicos.vcon_ser) por mês de dser_ser
com variações de filtro (todas / não canceladas / situação 0 / ambas) para descobrir qual regra a Domínio usa.
SOMENTE LEITURA, só agregados.   Uso: python scripts/conciliar_fiscal.py EMPRESA [imposto=1] [meses=6]
"""
import pathlib, sys
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from extractor.db import conectar, select

emp = int(sys.argv[1]); imp = int(sys.argv[2]) if len(sys.argv) > 2 else 1; n = int(sys.argv[3]) if len(sys.argv) > 3 else 6
cn = conectar()
apur = select(cn, "SELECT TOP ? data_sim, vcoe_sim, vcos_sim, vcov_sim FROM bethadba.efsdoimp WHERE codi_emp=? AND codi_imp=? AND pdic_sim=6 "
                  "AND (vcos_sim<>0 OR vcoe_sim<>0 OR vcov_sim<>0) ORDER BY data_sim DESC".replace("TOP ?", f"TOP {n}"), (emp, imp))
if not apur:
    print("sem apuração mensal para essa empresa/imposto"); sys.exit()

def soma(tab, col_val, col_dt, ini, fim, extra=""):
    return select(cn, f"SELECT COALESCE(SUM({col_val}),0) AS s, COUNT(*) AS n FROM bethadba.{tab} WHERE codi_emp=? AND {col_dt}>=? AND {col_dt}<? {extra}", (emp, ini, fim))[0]

def prox(d):
    return d.replace(year=d.year + 1, month=1, day=1) if d.month == 12 else d.replace(month=d.month + 1, day=1)

grupos = [("saídas", "vcos_sim", "efsaidas", "vcon_sai", "dsai_sai", {"todas": "", "cancelada='N'": "AND cancelada_sai='N'", "situacao=0": "AND situacao_sai=0", "ambas": "AND cancelada_sai='N' AND situacao_sai=0"}),
          ("entradas", "vcoe_sim", "efentradas", "vcon_ent", "dent_ent", {"todas": "", "situacao=0": "AND situacao_ent=0"}),
          ("serviços", "vcov_sim", "efservicos", "vcon_ser", "dser_ser", {"todas": "", "cancelada='N'": "AND cancelada_ser='N'", "situacao=0": "AND situacao_ser=0", "ambas": "AND cancelada_ser='N' AND situacao_ser=0"})]
placar = {}
# Hipótese: a apuração por imposto soma o valor contábil do IMPOSTO (efimp*.vcon_*), não o da nota.
IMP = {"efsaidas": ("efimpsai", "vcon_isa", "codi_sai"), "efentradas": ("efimpent", "vcon_ien", "codi_ent"),
       "efservicos": ("efimpser", "vcon_ise", "codi_ser")}
COMP = {"efentradas": "compte_ent"}   # coluna de competência alternativa à data de movimento

def soma_imp(tab, col_dt, ini, fim):
    ti, cv, k = IMP[tab]
    return float(select(cn, f"SELECT COALESCE(SUM(i.{cv}),0) AS s FROM bethadba.{ti} i JOIN bethadba.{tab} n ON n.codi_emp=i.codi_emp AND n.{k}=i.{k} "
                            f"WHERE i.codi_emp=? AND i.codi_imp=? AND n.{col_dt}>=? AND n.{col_dt}<?", (emp, imp, ini, fim))[0]["s"])

for r in apur:
    ini = r["data_sim"]; fim = prox(ini)
    print(f"\ncompetência {ini}:")
    for nome, cap, tab, cv, cd, variantes in grupos:
        alvo = float(r[cap] or 0)
        if alvo == 0:
            continue
        linha = []
        for vn, extra in variantes.items():
            s = float(soma(tab, cv, cd, ini, fim, extra)["s"])
            ok = abs(s - alvo) < 0.01
            placar.setdefault((nome, vn), [0, 0]); placar[(nome, vn)][1] += 1; placar[(nome, vn)][0] += ok
            linha.append(f"{vn}={s:,.2f}{' ✔' if ok else ''}")
        for vn, s in (("via_imposto", soma_imp(tab, cd, ini, fim)),) + ((("via_imposto+compet", soma_imp(tab, COMP[tab], ini, fim)),) if tab in COMP else ()):
            ok = abs(s - alvo) < 0.01
            placar.setdefault((nome, vn), [0, 0]); placar[(nome, vn)][1] += 1; placar[(nome, vn)][0] += ok
            linha.append(f"{vn}={s:,.2f}{' ✔' if ok else ''}")
        print(f"  {nome:<9} apuração={alvo:>16,.2f} | " + " | ".join(linha))
print("\nPLACAR (competências em que a soma bate exatamente com a apuração):")
for (nome, vn), (ok, tot) in placar.items():
    print(f"  {nome:<9} {vn:<16} {ok}/{tot}")
