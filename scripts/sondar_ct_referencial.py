"""Sonda dos lançamentos referenciais (CTLANCTO_SPED_ECF_GERAL / REFERENCIAL_SRF / SPED_ECF_IMUNE_ISENTA / SCP) e dos planos referenciais.
Somente agregados. Uso: python scripts/sondar_ct_referencial.py [empresa_ecf] [empresa_srf]"""
import pathlib, sys
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from extractor.db import conectar, select
E1 = sys.argv[1] if len(sys.argv) > 1 else "0"
E2 = sys.argv[2] if len(sys.argv) > 2 else E1
B = "bethadba."
def q(titulo, sql):
    print(f"\n== {titulo}")
    try:
        cn = conectar()
        for r in select(cn, sql.replace("{E1}", E1).replace("{E2}", E2), timeout=120):
            print("  ", {k: (float(v) if hasattr(v, 'as_tuple') else (v.strip() if isinstance(v, str) else v)) for k, v in r.items()})
    except Exception as e:
        print("   ERRO:", str(e)[:200])

if E1 == "0":
    q("empresas com mais linhas em ECF_GERAL", f"SELECT TOP 4 codi_emp, COUNT(*) n FROM {B}ctlancto_sped_ecf_geral GROUP BY codi_emp ORDER BY n DESC")
    q("empresas com mais linhas em REFERENCIAL_SRF", f"SELECT TOP 4 codi_emp, COUNT(*) n FROM {B}ctlancto_referencial_srf GROUP BY codi_emp ORDER BY n DESC")
    q("empresas por tabela", f"SELECT (SELECT COUNT(DISTINCT codi_emp) FROM {B}ctlancto_sped_ecf_geral) ecf, (SELECT COUNT(DISTINCT codi_emp) FROM {B}ctlancto_referencial_srf) srf, (SELECT COUNT(DISTINCT codi_emp) FROM {B}ctlancto_sped_ecf_imune_isenta) imune, (SELECT COUNT(DISTINCT codi_emp) FROM {B}ctlancto_scp) scp")
    q("origem_reg", f"SELECT origem_reg, COUNT(*) n FROM {B}ctlancto_referencial_srf GROUP BY origem_reg ORDER BY n DESC")
    q("planos: validade e tipos", f"SELECT tipo, nivel, COUNT(*) n FROM {B}ctcontas_sped_ecf_geral GROUP BY tipo, nivel ORDER BY tipo, nivel")
    q("plano SRF: utilização x natureza", f"SELECT utilizacao_srf, natureza_srf, COUNT(*) n FROM {B}ctcontas_srf GROUP BY utilizacao_srf, natureza_srf")
    q("plano ECF: natureza x utilização", f"SELECT natureza, utilizacao, COUNT(*) n FROM {B}ctcontas_sped_ecf_geral GROUP BY natureza, utilizacao")
    q("scp: tipo x origem", f"SELECT tipo, origem_reg, COUNT(*) n, COUNT(DISTINCT codi_emp) empresas, COUNT(DISTINCT i_scp) scps FROM {B}ctlancto_scp GROUP BY tipo, origem_reg")
    sys.exit()

for nome, tab, plano, col in [("ECF_GERAL", "ctlancto_sped_ecf_geral", "ctcontas_sped_ecf_geral", "codigo_cta_sped_ecf_geral"),
                              ("SRF", "ctlancto_referencial_srf", "ctcontas_srf", "codigo_cta_srf")]:
    E = "{E1}" if nome == "ECF_GERAL" else "{E2}"
    q(f"{nome}: linhas, lançamentos, sequencial máx., valor zero", f"SELECT COUNT(*) linhas, COUNT(DISTINCT nume_lan) lancamentos, MAX(sequencial) seq_max, MIN(sequencial) seq_min, SUM(CASE WHEN valor = 0 THEN 1 ELSE 0 END) valor_zero, SUM(CASE WHEN conta_debito = 0 THEN 1 ELSE 0 END) deb0, SUM(CASE WHEN conta_credito = 0 THEN 1 ELSE 0 END) cre0 FROM {B}{tab} WHERE codi_emp = {E}")
    q(f"{nome}: contas existem no plano referencial?", f"SELECT SUM(CASE WHEN d.{col} IS NULL AND t.conta_debito <> 0 THEN 1 ELSE 0 END) deb_sem_plano, SUM(CASE WHEN c.{col} IS NULL AND t.conta_credito <> 0 THEN 1 ELSE 0 END) cre_sem_plano, COUNT(*) linhas FROM {B}{tab} t LEFT JOIN {B}{plano} d ON d.{col} = t.conta_debito LEFT JOIN {B}{plano} c ON c.{col} = t.conta_credito WHERE t.codi_emp = {E}")
    q(f"{nome}: órfãos de lançamento e de lote", f"SELECT SUM(CASE WHEN l.nume_lan IS NULL THEN 1 ELSE 0 END) sem_lancto, SUM(CASE WHEN lo.codi_lote IS NULL THEN 1 ELSE 0 END) sem_lote, SUM(CASE WHEN l.codi_lote = t.codi_lote THEN 1 ELSE 0 END) lote_igual FROM {B}{tab} t LEFT JOIN {B}ctlancto l ON l.codi_emp = t.codi_emp AND l.nume_lan = t.nume_lan LEFT JOIN {B}ctlanctolote lo ON lo.codi_emp = t.codi_emp AND lo.codi_lote = t.codi_lote WHERE t.codi_emp = {E}")
    q(f"{nome}: soma valor referencial x vlor_lan do lançamento", f"SELECT COUNT(*) lancamentos, SUM(CASE WHEN ABS(r.s - l.vlor_lan) < 0.01 THEN 1 ELSE 0 END) soma_igual, SUM(CASE WHEN r.s > l.vlor_lan + 0.01 THEN 1 ELSE 0 END) ref_maior, SUM(CASE WHEN r.s < l.vlor_lan - 0.01 THEN 1 ELSE 0 END) ref_menor FROM (SELECT nume_lan, SUM(valor) s FROM {B}{tab} WHERE codi_emp = {E} GROUP BY nume_lan) r JOIN {B}ctlancto l ON l.codi_emp = {E} AND l.nume_lan = r.nume_lan")
    q(f"{nome}: quantos lançamentos do livro têm linha referencial", f"SELECT (SELECT COUNT(*) FROM {B}ctlancto WHERE codi_emp = {E}) lancamentos_livro, (SELECT COUNT(DISTINCT nume_lan) FROM {B}{tab} WHERE codi_emp = {E}) com_referencial")
    q(f"{nome}: mapeamento conta→referencial da empresa", f"SELECT (SELECT COUNT(*) FROM {B}ctcontas WHERE codi_emp = {E}) contas, (SELECT COUNT(DISTINCT codi_cta) FROM {B}{plano}_ref WHERE codi_emp = {E}) contas_mapeadas, (SELECT COUNT(*) FROM {B}{plano}_ref WHERE codi_emp = {E}) pares")
