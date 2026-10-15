"""Testa a consulta contas_a_receber (Honorários) — somente leitura.

Verifica, para cada escritório:
  1. contagem por situação == contagem direta (aberta + quitada + inconsistente == total de parcelas);
  2. Σ saldo de todas as parcelas == Σ itens faturados − Σ recebimentos (consulta independente por tabela);
  3. paginação: duas páginas consecutivas não repetem nem pulam parcelas;
  4. tempo.
"""
import pathlib, sys, time
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from extractor.db import conectar, select
from server.sqlbuilder import montar_contas_a_receber
cn = conectar()
falhas = 0
for esc in [r["codi_emp"] for r in select(cn, "SELECT DISTINCT codi_emp FROM bethadba.hrfaturamento ORDER BY codi_emp")]:
    t0 = time.time()
    cont = {}
    for sit in ("aberta", "quitada", "inconsistente"):
        sql, par = montar_contas_a_receber(esc, situacao=sit, contar=True)
        cont[sit] = select(cn, sql, tuple(par))[0]["total"]
    sql, par = montar_contas_a_receber(esc, contar=True)
    total = select(cn, sql, tuple(par))[0]["total"]
    direto = select(cn, "SELECT COUNT(*) AS n FROM bethadba.hrfaturamento_parcela WHERE codi_emp = ?", (esc,))[0]["n"]
    # saldo total: pela consulta (paginando só o necessário não — usa agregação direta) x independente
    ind = select(cn, "SELECT (SELECT COALESCE(SUM(valor),0) FROM bethadba.hrfaturamento_parcela_item WHERE codi_emp = ?) - "
                     "(SELECT COALESCE(SUM(valor),0) FROM bethadba.hrrecebimento WHERE codi_emp = ?) AS saldo", (esc, esc))[0]["saldo"]
    sql, par = montar_contas_a_receber(esc, limite=500)
    todas, off = [], 0
    while True:
        sql, par = montar_contas_a_receber(esc, limite=500, offset=off)
        pg = select(cn, sql, tuple(par))
        todas += pg
        if len(pg) < 500:
            break
        off += 500
    saldo_total = sum(float(r["saldo"]) for r in todas)
    chaves = [(r["faturamento_codigo"], r["parcela"]) for r in todas]
    sem_repeticao = len(chaves) == len(set(chaves))
    ok = (sum(cont.values()) == total == direto == len(todas)) and abs(saldo_total - float(ind)) < 0.01 and sem_repeticao
    falhas += not ok
    print(f"{'OK  ' if ok else 'ERRO'} escritório {esc}: parcelas={direto} (consulta={total}, paginadas={len(todas)}) | "
          f"aberta={cont['aberta']} quitada={cont['quitada']} inconsistente={cont['inconsistente']} | "
          f"Σ saldo={saldo_total:,.2f} x independente={float(ind):,.2f} | sem repetição={sem_repeticao} | {time.time()-t0:.1f}s")
# exemplo de filtro: em aberto com vencimento definido (sem exibir nomes)
sql, par = montar_contas_a_receber(1, situacao="aberta", limite=3)
print("\nexemplo situacao=aberta (colunas):", list(select(cn, sql, tuple(par))[0].keys()) if select(cn, sql, tuple(par)) else "(nenhuma)")
print(f"\n{falhas} falhas")
sys.exit(1 if falhas else 0)
