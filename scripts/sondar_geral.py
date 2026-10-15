"""Sonda do módulo Geral (somente agregados; nenhum dado pessoal de sócio é exibido)."""
import pathlib, sys
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from extractor.db import conectar, select
cn = conectar()
def q(titulo, sql, params=()):
    print(f"\n== {titulo}")
    for r in select(cn, sql, params):
        print("  ", {k: (float(v) if hasattr(v, 'as_tuple') else (v.strip() if isinstance(v, str) else v)) for k, v in r.items()})

q("geempre_vigencia: vigências por empresa", "SELECT n AS vigencias, COUNT(*) AS empresas FROM (SELECT codi_emp, COUNT(*) AS n FROM bethadba.geempre_vigencia GROUP BY codi_emp) t GROUP BY n ORDER BY n")
q("geempre x geempre_vigencia: valores iguais (nome, cnpj, status, regime)?", """
    SELECT COUNT(*) AS empresas, SUM(CASE WHEN e.cgce_emp = v.cgce_emp THEN 1 ELSE 0 END) AS cnpj_igual,
           SUM(CASE WHEN e.stat_emp = v.stat_emp THEN 1 ELSE 0 END) AS status_igual, SUM(CASE WHEN e.nome_emp = v.nome_emp THEN 1 ELSE 0 END) AS nome_igual
      FROM bethadba.geempre e JOIN bethadba.geempre_vigencia v ON v.codi_emp = e.codi_emp""")
q("geempre: situação x uso dos módulos", "SELECT stat_emp, COUNT(*) AS n, SUM(CASE WHEN uefi_emp = 1 THEN 1 ELSE 0 END) AS usa_fiscal, SUM(CASE WHEN ucta_emp = 1 THEN 1 ELSE 0 END) AS usa_contab, SUM(CASE WHEN ufol_emp = 1 THEN 1 ELSE 0 END) AS usa_folha, SUM(CASE WHEN uhon_emp = 1 THEN 1 ELSE 0 END) AS usa_honorarios FROM bethadba.geempre GROUP BY stat_emp ORDER BY n DESC")
q("geempre.tipoi_emp (motivo da inatividade) x situação", "SELECT stat_emp, tipoi_emp, COUNT(*) AS n FROM bethadba.geempre WHERE stat_emp <> 'A' GROUP BY stat_emp, tipoi_emp ORDER BY n DESC")
q("geempre.rfed_emp / simples_emp (enquadramento)", "SELECT rfed_emp, simples_emp, COUNT(*) AS n FROM bethadba.geempre GROUP BY rfed_emp, simples_emp ORDER BY n DESC")
q("geempre.tins_emp / honorario_tipo", "SELECT tins_emp, honorario_tipo, COUNT(*) AS n FROM bethadba.geempre GROUP BY tins_emp, honorario_tipo ORDER BY n DESC")
q("empresas ativas: quantas sem CNPJ válido (14 dígitos)?", "SELECT SUM(CASE WHEN LENGTH(TRIM(cgce_emp)) = 14 THEN 1 ELSE 0 END) AS cnpj_14, SUM(CASE WHEN LENGTH(TRIM(cgce_emp)) = 11 THEN 1 ELSE 0 END) AS cpf_11, SUM(CASE WHEN cgce_emp IS NULL OR TRIM(cgce_emp) = '' THEN 1 ELSE 0 END) AS sem_documento, COUNT(*) AS n FROM bethadba.geempre WHERE stat_emp = 'A'")
q("quadro societário: Σ participação dos SÓCIOS por quadro (tipo S)", """
    SELECT COUNT(*) AS quadros, SUM(CASE WHEN ABS(p - 100) < 0.01 THEN 1 ELSE 0 END) AS soma_100,
           SUM(CASE WHEN p < 99.99 THEN 1 ELSE 0 END) AS abaixo_100, SUM(CASE WHEN p > 100.01 THEN 1 ELSE 0 END) AS acima_100
      FROM (SELECT codi_emp, data, SUM(participacao) AS p FROM bethadba.gequadrosocietario_socios WHERE tipo = 'S' GROUP BY codi_emp, data) t""")
q("quadro societário: Σ quotas dos sócios x quotas do quadro", """
    SELECT COUNT(*) AS quadros, SUM(CASE WHEN ABS(s.q - c.qdade_quota) < 0.01 THEN 1 ELSE 0 END) AS quotas_iguais,
           SUM(CASE WHEN ABS(s.q - c.qdade_quota) >= 0.01 AND s.q < c.qdade_quota THEN 1 ELSE 0 END) AS socios_menor,
           SUM(CASE WHEN ABS(s.q - c.qdade_quota) >= 0.01 AND s.q > c.qdade_quota THEN 1 ELSE 0 END) AS socios_maior
      FROM bethadba.gequadrosocietario c
      JOIN (SELECT codi_emp, data, SUM(qdade_quotas) AS q FROM bethadba.gequadrosocietario_socios WHERE tipo = 'S' GROUP BY codi_emp, data) s
        ON s.codi_emp = c.codi_emp AND s.data = c.data""")
q("quadro societário: quadros por empresa (histórico)", "SELECT n AS quadros_por_empresa, COUNT(*) AS empresas FROM (SELECT codi_emp, COUNT(*) AS n FROM bethadba.gequadrosocietario GROUP BY codi_emp) t GROUP BY n ORDER BY n LIMIT 6" if False else "SELECT TOP 6 n AS quadros_por_empresa, COUNT(*) AS empresas FROM (SELECT codi_emp, COUNT(*) AS n FROM bethadba.gequadrosocietario GROUP BY codi_emp) t GROUP BY n ORDER BY n")
q("quadro societário: tipos de vínculo (S/A/R) e sócios sem cadastro", """
    SELECT s.tipo, COUNT(*) AS n, SUM(CASE WHEN g.i_socio IS NULL THEN 1 ELSE 0 END) AS socio_sem_cadastro
      FROM bethadba.gequadrosocietario_socios s LEFT JOIN bethadba.gesocios g ON g.i_socio = s.i_socio GROUP BY s.tipo""")
q("sócio compartilhado entre empresas", "SELECT COUNT(*) AS socios, SUM(CASE WHEN e > 1 THEN 1 ELSE 0 END) AS em_mais_de_uma_empresa FROM (SELECT i_socio, COUNT(DISTINCT codi_emp) AS e FROM bethadba.gequadrosocietario_socios GROUP BY i_socio) t")
