"""Concilia notas fiscais com os lançamentos que as contabilizaram: a soma lançada bate com o valor contábil da nota?
(agregados, somente leitura).   Uso: python scripts/conciliar_contabilizacao.py EMPRESA_SAIDA EMPRESA_ENTRADA EMPRESA_SERVICO"""
import pathlib, sys
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from extractor.db import conectar, select
cn = conectar()
emp_s, emp_e, emp_v = (int(x) for x in sys.argv[1:4])
CASOS = [("saídas", "efsaidas", "codi_sai", "vcon_sai", "efsaidas_lancto", emp_s, "AND n.cancelada_sai = 'N'"),
         ("entradas", "efentradas", "codi_ent", "vcon_ent", "efentradas_lancto", emp_e, ""),
         ("serviços", "efservicos", "codi_ser", "vcon_ser", "efservicos_lancto", emp_v, "AND n.cancelada_ser = 'N'")]
for nome, tn, k, vc, tl, emp, extra in CASOS:
    r = select(cn, f"""
        SELECT COUNT(*) AS notas,
               SUM(CASE WHEN soma = vcon THEN 1 ELSE 0 END) AS soma_igual,
               SUM(CASE WHEN mx = vcon THEN 1 ELSE 0 END) AS maior_igual,
               SUM(CASE WHEN soma > vcon THEN 1 ELSE 0 END) AS soma_maior,
               SUM(CASE WHEN soma < vcon THEN 1 ELSE 0 END) AS soma_menor
          FROM (SELECT n.{k}, n.{vc} AS vcon, SUM(l.vlor_lan) AS soma, MAX(l.vlor_lan) AS mx
                  FROM bethadba.{tn} n
                  JOIN bethadba.{tl} x ON x.codi_emp = n.codi_emp AND x.{k} = n.{k}
                  JOIN bethadba.ctlancto l ON l.codi_emp = x.fili_lan AND l.nume_lan = x.nume_lan
                 WHERE n.codi_emp = {emp} {extra}
                 GROUP BY n.{k}, n.{vc}) t""")[0]
    n = r["notas"] or 0
    pc = lambda v: f"{100*(v or 0)/n:.1f}%" if n else "-"
    print(f"{nome:<9} empresa {emp:<5} notas contabilizadas={n:<6} soma==vcon: {r['soma_igual']} ({pc(r['soma_igual'])}) | "
          f"maior lançamento==vcon: {pc(r['maior_igual'])} | soma>vcon: {pc(r['soma_maior'])} | soma<vcon: {pc(r['soma_menor'])}")
