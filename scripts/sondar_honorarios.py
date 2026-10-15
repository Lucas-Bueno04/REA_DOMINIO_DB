"""Sonda de Honorários, parte 3 (somente agregados): identidade do líquido e saldo por parcela."""
import pathlib, sys
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from extractor.db import conectar, select
cn = conectar()
def q(titulo, sql, params=()):
    print(f"\n== {titulo}")
    for r in select(cn, sql, params):
        print("  ", {k: (float(v) if hasattr(v, 'as_tuple') else (v.strip() if isinstance(v, str) else v)) for k, v in r.items()})

q("identidade geral: valor = valor_recebido − juros − multa + desconto", """
    SELECT COUNT(*) AS recebimentos, SUM(CASE WHEN ABS(valor - (valor_recebido - COALESCE(valor_juros,0) - COALESCE(valor_multa,0) + COALESCE(valor_desconto,0))) < 0.005 THEN 1 ELSE 0 END) AS identidade_ok
      FROM bethadba.hrrecebimento""")
q("identidade nos itens: valor = recebido − juros − multa + desconto", """
    SELECT COUNT(*) AS itens, SUM(CASE WHEN ABS(valor - (valor_recebido - COALESCE(valor_juros,0) - COALESCE(valor_multa,0) + COALESCE(valor_desconto,0))) < 0.005 THEN 1 ELSE 0 END) AS identidade_ok
      FROM bethadba.hrrecebimento_item""")
for rotulo, expr in [("pelo valor LÍQUIDO + desconto + quitado + refaturado + reparcelado",
                      "r.valor + COALESCE(r.valor_desconto,0) + COALESCE(r.valor_quitado,0) + COALESCE(r.valor_refaturado,0) + COALESCE(r.valor_reparcelado,0)"),
                     ("pelo valor LÍQUIDO apenas", "r.valor")]:
    q(f"saldo por parcela = Σ itens faturados − Σ baixas ({rotulo})", f"""
        SELECT situacao, COUNT(*) AS parcelas FROM (
        SELECT CASE WHEN saldo < -0.005 THEN 'baixado a mais' WHEN saldo < 0.005 THEN 'quitada' ELSE 'em aberto' END AS situacao
          FROM (SELECT COALESCE((SELECT SUM(i.valor) FROM bethadba.hrfaturamento_parcela_item i WHERE i.codi_emp = p.codi_emp AND i.i_faturamento = p.i_faturamento AND i.i_parcela = p.i_parcela),0)
                     - COALESCE((SELECT SUM({expr}) FROM bethadba.hrrecebimento r WHERE r.codi_emp = p.codi_emp AND r.i_faturamento = p.i_faturamento AND r.i_parcela = p.i_parcela),0) AS saldo
                  FROM bethadba.hrfaturamento_parcela p) t) u GROUP BY situacao""")
