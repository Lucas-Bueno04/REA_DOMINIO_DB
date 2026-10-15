"""Testa o balancete contra invariantes contábeis, em empresas de portes diferentes (somente leitura).

Invariantes verificadas:
  1. Σ débitos == Σ créditos no período (partida dobrada);
  2. Σ saldo anterior == 0 e Σ saldo final == 0 (todas as contas juntas);
  3. Σ débitos do balancete == SUM(vlor_lan) direto de ctlancto (consulta independente, outro caminho de acesso);
  4. contas sem cadastro no plano (órfãs) e lançamentos em contas sintéticas são contados e reportados.
Uso: python scripts/testar_balancete.py [empresa ...]      (padrão: pequena, mediana, grande e uma com plano alheio)
"""
import datetime, pathlib, sys, time
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from extractor.db import conectar, select
from server.sqlbuilder import montar_balancete

cn = conectar()
args = [int(a) for a in sys.argv[1:]]
if not args:
    todas = select(cn, "SELECT codi_emp, COUNT(*) AS n FROM bethadba.ctlancto GROUP BY codi_emp HAVING COUNT(*) >= 300 ORDER BY n")
    alheio = select(cn, "SELECT TOP 3 codi_emp, COUNT(*) AS n FROM bethadba.ctlancto WHERE codi_emp <> codi_emp_plano GROUP BY codi_emp ORDER BY n DESC")
    args = [todas[0]["codi_emp"], todas[len(todas) // 2]["codi_emp"], todas[-1]["codi_emp"], todas[len(todas) * 3 // 4]["codi_emp"]] + [a["codi_emp"] for a in alheio]
def periodo_ativo(emp):
    """Ano de maior movimento da empresa (ignora datas absurdas) — evita testar um período vazio."""
    r = select(cn, "SELECT TOP 1 YEAR(data_lan) AS ano, COUNT(*) AS n FROM bethadba.ctlancto WHERE codi_emp = ? AND data_lan BETWEEN '2000-01-01' AND '2100-01-01' "
                   "GROUP BY YEAR(data_lan) ORDER BY n DESC", (emp,))
    return (datetime.date(r[0]["ano"], 1, 1), datetime.date(r[0]["ano"], 12, 31), r[0]["n"]) if r else (None, None, 0)

falhas = 0
for emp in args:
    ini, fim, n_lan = periodo_ativo(emp)
    if ini is None:
        print(f"-- empresa {emp}: sem lançamentos, ignorada"); continue
    t0 = time.time()
    sql, par = montar_balancete(emp, ini, fim)
    rows = select(cn, sql, tuple(par))
    dt = time.time() - t0
    f = lambda v: float(v or 0)
    deb = sum(f(r["debitos"]) for r in rows)
    cre = sum(f(r["creditos"]) for r in rows)
    sa = sum(f(r["saldo_anterior"]) for r in rows)
    sf = sum(f(r["saldo_anterior"]) + f(r["debitos"]) - f(r["creditos"]) for r in rows)
    ind = select(cn, "SELECT COALESCE(SUM(CASE WHEN cdeb_lan <> 0 THEN vlor_lan ELSE 0 END),0) AS d, COALESCE(SUM(CASE WHEN ccre_lan <> 0 THEN vlor_lan ELSE 0 END),0) AS c "
                     "FROM bethadba.ctlancto WHERE codi_emp = ? AND data_lan BETWEEN ? AND ?", (emp, ini, fim))[0]
    orfas = [r for r in rows if r["classificacao"] is None]
    sint = [r for r in rows if r["tipo"] == "S"]
    planos = sorted({r["plano_empresa"] for r in rows})
    ok = abs(deb - cre) < 0.005 and abs(sa) < 0.005 and abs(sf) < 0.005 and abs(deb - f(ind["d"])) < 0.005 and abs(cre - f(ind["c"])) < 0.005
    falhas += not ok
    print(f"{'OK  ' if ok else 'ERRO'} empresa {emp:<5} ano {ini.year} ({n_lan:,} lançamentos) {len(rows):>5} contas  {dt:5.1f}s  plano={planos}\n"
          f"       débitos={deb:>18,.2f} créditos={cre:>18,.2f} | independente: D={f(ind['d']):,.2f} C={f(ind['c']):,.2f}\n"
          f"       Σ saldo anterior={sa:,.2f}  Σ saldo final={sf:,.2f}  | contas órfãs={len(orfas)}  com lançamento em sintética={len(sint)}")
print(f"\n{len(args)} empresas, {falhas} falhas")
sys.exit(1 if falhas else 0)
