"""Sonda do SPED ECF - Outros Dados (CTSPED_ECF_OD*). Somente agregados; nada de dado de signatário é exibido."""
import pathlib, sys
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from extractor.db import conectar, select
B = "bethadba."
def q(titulo, sql):
    print(f"\n== {titulo}")
    try:
        for r in select(conectar(), sql, timeout=120):
            print("  ", {k: (float(v) if hasattr(v, 'as_tuple') else (v.strip() if isinstance(v, str) else v)) for k, v in r.items()})
    except Exception as e:
        print("   ERRO:", str(e)[:200])

q("cabeçalho OD: empresas, anos, SCP", f"SELECT COUNT(*) linhas, COUNT(DISTINCT codi_emp) empresas, MIN(ano_calendario) de, MAX(ano_calendario) ate, SUM(CASE WHEN i_scp IS NOT NULL THEN 1 ELSE 0 END) com_scp FROM {B}ctsped_ecf_od")
q("OD: forma de tributação", f"SELECT forma_tributacao, periodo_apuracao_irpj_csll, COUNT(*) n FROM {B}ctsped_ecf_od GROUP BY forma_tributacao, periodo_apuracao_irpj_csll ORDER BY n DESC")
q("OD: retificadora x tipo de escrituração", f"SELECT retificadora, tipo_escrituracao, COUNT(*) n FROM {B}ctsped_ecf_od GROUP BY retificadora, tipo_escrituracao ORDER BY n DESC")
q("OD: qualificação PJ / situação especial", f"SELECT qualificacao_pessoa_juridica q, indicador_situacao_especial e, COUNT(*) n FROM {B}ctsped_ecf_od GROUP BY qualificacao_pessoa_juridica, indicador_situacao_especial ORDER BY n DESC")
q("OD: critério de reconhecimento de receita", f"SELECT criterio_de_reconhecimento_de_receitas c, COUNT(*) n FROM {B}ctsped_ecf_od GROUP BY criterio_de_reconhecimento_de_receitas")
q("OD: empresa tem várias linhas por ano?", f"SELECT n, COUNT(*) empresas_ano FROM (SELECT codi_emp, YEAR(ano_calendario) a, i_scp, COUNT(*) n FROM {B}ctsped_ecf_od GROUP BY codi_emp, a, i_scp) t GROUP BY n ORDER BY n")
q("tabela de registros: linhas e registros distintos", f"SELECT COUNT(*) linhas, COUNT(DISTINCT registro) registros, COUNT(DISTINCT vigencia) vigencias FROM {B}cttabela_sped_ecf_od_registro")
q("OD_REGISTRO: registros mais frequentes", f"SELECT TOP 15 registro, COUNT(*) n, COUNT(DISTINCT codi_emp) empresas FROM {B}ctsped_ecf_od_registro GROUP BY registro ORDER BY n DESC")
q("OD_REGISTRO: competência e valor", f"SELECT MIN(competencia) de, MAX(competencia) ate, SUM(CASE WHEN valor=0 THEN 1 ELSE 0 END) zero, SUM(CASE WHEN contas IS NOT NULL AND LENGTH(contas)>0 THEN 1 ELSE 0 END) com_contas, COUNT(*) n FROM {B}ctsped_ecf_od_registro")
q("OD_REGISTRO: forma de importação x determinar", f"SELECT forma_importacao, determinar_forma_importar_saldo_conta_contabil d, COUNT(*) n FROM {B}ctsped_ecf_od_registro GROUP BY forma_importacao, d ORDER BY n DESC")
q("OD_REGISTRO: órfãos de cabeçalho e de tabela de registros", f"SELECT SUM(CASE WHEN o.i_outros_dados IS NULL THEN 1 ELSE 0 END) sem_cabecalho, SUM(CASE WHEN t.registro IS NULL THEN 1 ELSE 0 END) sem_tabela_registro, COUNT(*) n FROM {B}ctsped_ecf_od_registro r LEFT JOIN {B}ctsped_ecf_od o ON o.codi_emp=r.codi_emp AND o.i_outros_dados=r.i_outros_dados LEFT JOIN {B}cttabela_sped_ecf_od_registro t ON t.registro=r.registro AND t.codigo=r.codigo AND t.vigencia=r.vigencia WHERE r.codi_emp IN (SELECT TOP 3 codi_emp FROM {B}ctsped_ecf_od ORDER BY i_outros_dados DESC)")
q("OD_REGISTRO_LALUR: registros e histórico", f"SELECT TOP 10 registro, COUNT(*) n, SUM(CASE WHEN LENGTH(TRIM(historico))>0 THEN 1 ELSE 0 END) com_historico FROM {B}ctsped_ecf_od_registro_lalur GROUP BY registro ORDER BY n DESC")
q("OD_MES: registros", f"SELECT TOP 10 registro, COUNT(*) n, MIN(i_mes) m1, MAX(i_mes) m2 FROM {B}ctsped_ecf_od_mes GROUP BY registro ORDER BY n DESC")
q("OD_REGISTRO_CONTA: forma e operação", f"SELECT forma_importacao, operacao, COUNT(*) n FROM {B}ctsped_ecf_od_registro_conta GROUP BY forma_importacao, operacao ORDER BY n DESC")
q("LALUR_CONTA: tipo de saldo", f"SELECT tipo_saldo, COUNT(*) n FROM {B}ctsped_ecf_od_registro_lalur_conta GROUP BY tipo_saldo")
q("LALUR_LANCAMENTO: tipo de saldo e período", f"SELECT tipo_saldo, COUNT(*) n, MIN(data_lancamento) de, MAX(data_lancamento) ate FROM {B}ctsped_ecf_od_registro_lalur_lancamento GROUP BY tipo_saldo")
q("BASE_NEGATIVA_PARTE_B: indicador", f"SELECT indicador_lancamento, COUNT(*) n FROM {B}ctsped_ecf_od_registro_lalur_base_negativa_parte_b GROUP BY indicador_lancamento")
q("signatários: tipo de inscrição e qualificação (sem dados pessoais)", f"SELECT tipo_inscricao, i_qualificacao, COUNT(*) n FROM {B}ctsped_ecf_signatario GROUP BY tipo_inscricao, i_qualificacao ORDER BY n DESC")
q("qualificações", f"SELECT i_qualificacao, codigo, descricao, registro_sped FROM {B}ctsped_signatario_qualificacao ORDER BY i_qualificacao")
