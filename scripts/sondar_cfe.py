"""Sonda do CF-e (EFCUPOM_FISCAL_ELETRONICO*): somente agregados, nenhum dado de cliente é exibido."""
import pathlib, sys
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from extractor.db import conectar, select
P = "bethadba.efcupom_fiscal_eletronico"
EMP = sys.argv[1] if len(sys.argv) > 1 else "0"
def q(titulo, sql, params=()):
    sql = sql.replace("{EMP}", EMP)
    print(f"\n== {titulo}")
    try:
        cn = conectar()
        for r in select(cn, sql, params, timeout=120):
            print("  ", {k: (float(v) if hasattr(v, 'as_tuple') else (v.strip() if isinstance(v, str) else v)) for k, v in r.items()})
    except Exception as e:
        print("   ERRO:", str(e)[:200])

q("cabeçalho: situação x cancelamento", f"SELECT situacao, COUNT(*) n, SUM(CASE WHEN extrato_cancelamento IS NOT NULL THEN 1 ELSE 0 END) com_extr_canc, SUM(CASE WHEN TRIM(chave_nfe_cancelamento) <> '' THEN 1 ELSE 0 END) com_chave_canc, SUM(valor_total_cfe) valor FROM {P} GROUP BY situacao ORDER BY n DESC")
q("origem_reg x conferido", f"SELECT origem_reg, conferido, COUNT(*) n FROM {P} GROUP BY origem_reg, conferido ORDER BY n DESC")
q("tipo_titulo", f"SELECT tipo_titulo, COUNT(*) n FROM {P} GROUP BY tipo_titulo ORDER BY n DESC")
q("abrangência", f"SELECT COUNT(DISTINCT codi_emp) empresas, MIN(data_cfe) de, MAX(data_cfe) ate, SUM(CASE WHEN codi_cli IS NULL THEN 1 ELSE 0 END) sem_cliente, SUM(CASE WHEN LENGTH(TRIM(chave_cfe))=44 THEN 1 ELSE 0 END) chave44 FROM {P}")
q("duplicidade de chave_cfe (por empresa)", f"SELECT COUNT(*) chaves_repetidas FROM (SELECT codi_emp, chave_cfe FROM {P} WHERE codi_emp IN ({EMP}) GROUP BY codi_emp, chave_cfe HAVING COUNT(*)>1) t")
q("cabeçalho x estoque_total (valor)", f"SELECT SUM(CASE WHEN ABS(c.valor_total_cfe - t.valor_total) < 0.01 THEN 1 ELSE 0 END) iguais, SUM(CASE WHEN ABS(c.valor_total_cfe - t.valor_total) >= 0.01 THEN 1 ELSE 0 END) diferentes, SUM(CASE WHEN t.i_cfe IS NULL THEN 1 ELSE 0 END) sem_total FROM {P} c LEFT JOIN bethadba.efcupom_fiscal_eletronico_estoque_total t ON t.codi_emp=c.codi_emp AND t.i_cfe=c.i_cfe WHERE c.codi_emp IN ({EMP})")
q("estoque_total x soma dos itens (empresa informada)", f"SELECT COUNT(*) cfes, SUM(CASE WHEN ABS(t.valor_total - i.s) < 0.01 THEN 1 ELSE 0 END) iguais FROM bethadba.efcupom_fiscal_eletronico_estoque_total t JOIN (SELECT codi_emp, i_cfe, SUM(valor_total) s FROM bethadba.efcupom_fiscal_eletronico_estoque WHERE codi_emp IN ({EMP}) GROUP BY codi_emp, i_cfe) i ON i.codi_emp=t.codi_emp AND i.i_cfe=t.i_cfe WHERE t.codi_emp IN ({EMP})")
q("itens: nº de itens por CF-e e órfãos (empresa informada)", f"SELECT COUNT(*) itens, SUM(CASE WHEN c.i_cfe IS NULL THEN 1 ELSE 0 END) orfaos FROM bethadba.efcupom_fiscal_eletronico_estoque e LEFT JOIN {P} c ON c.codi_emp=e.codi_emp AND c.i_cfe=e.i_cfe WHERE e.codi_emp IN ({EMP})")
q("impostos: soma valor_total x cabeçalho por situação (empresa informada)", f"SELECT c.situacao, COUNT(*) cfes, SUM(CASE WHEN ABS(c.valor_total_cfe - i.s) < 0.01 THEN 1 ELSE 0 END) iguais FROM {P} c JOIN (SELECT codi_emp, i_cfe, SUM(valor_total) s FROM bethadba.efcupom_fiscal_eletronico_impostos WHERE codi_emp IN ({EMP}) GROUP BY codi_emp, i_cfe) i ON i.codi_emp=c.codi_emp AND i.i_cfe=c.i_cfe WHERE c.codi_emp IN ({EMP}) GROUP BY c.situacao")
q("detalhamento: imposto x CST (top)", "SELECT TOP 12 codi_imp, COUNT(*) n FROM bethadba.efcupom_fiscal_eletronico_impostos_detalhamento WHERE codi_emp IN ({EMP}) GROUP BY codi_imp ORDER BY n DESC")
q("lançamento contábil: tipo", "SELECT tipo, COUNT(*) n, SUM(CASE WHEN fili_lan = codi_emp THEN 1 ELSE 0 END) mesma_empresa FROM bethadba.efcupom_fiscal_eletronico_lancto WHERE codi_emp IN ({EMP}) GROUP BY tipo ORDER BY n DESC")
q("pis_cofins: CST", "SELECT TOP 10 cst, COUNT(*) n FROM bethadba.efcupom_fiscal_eletronico_pis_cofins WHERE codi_emp IN ({EMP}) GROUP BY cst ORDER BY n DESC")
q("estoque: CST ICMS / dados_piscofins_ok", "SELECT TOP 10 cst_icms, dados_piscofins_ok, COUNT(*) n FROM bethadba.efcupom_fiscal_eletronico_estoque WHERE codi_emp IN ({EMP}) GROUP BY cst_icms, dados_piscofins_ok ORDER BY n DESC")
