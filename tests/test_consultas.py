"""Funções de consulta nomeadas (server/consultas.py) contra o banco real. Dependem de dados reais: ver STATUS.md (empresas de teste)."""
import pytest

from server import consultas
from server.motor import ErroUso, Motor


@pytest.fixture(scope="module")
def motor():
    return Motor(auditar=False)


def test_catalogo_de_funcoes():
    assert "receita_bruta_simples" in consultas.FUNCOES
    f = consultas.FUNCOES["receita_bruta_simples"]
    assert f["descricao"] and set(f["parametros"]) == {"empresa", "competencia"}


def test_receita_simples_confere_sem_devolucao(motor):
    r = consultas.receita_bruta_simples(motor, 679, "2026-09")
    assert r["situacao"] == "confere" and r["diferenca"] == 0
    assert r["recalculado"]["receita_bruta"] == r["apurado_pela_dominio"]["base_calculo"] == 54683.68


def test_receita_simples_confere_com_devolucao(motor):
    r = consultas.receita_bruta_simples(motor, 644, "2026-09")
    assert r["situacao"] == "confere"
    assert r["recalculado"]["devolucoes_de_venda"]["valor"] == 10355.94 == r["apurado_pela_dominio"]["devolucao_venda"]
    assert r["recalculado"]["receita_bruta"] == 38494.69


def test_receita_simples_divergencia_documentada(motor):
    r = consultas.receita_bruta_simples(motor, 1110, "2025-10")
    assert r["situacao"] == "diverge" and abs(r["diferenca"] - 87948.65) < 0.01 and r["aviso"]


def test_receita_simples_sem_apuracao(motor):
    r = consultas.receita_bruta_simples(motor, 1, "2015-01")
    assert r["situacao"] == "sem_apuracao" and r["apurado_pela_dominio"] is None


def test_competencia_invalida(motor):
    with pytest.raises(ErroUso):
        consultas.receita_bruta_simples(motor, 679, "setembro")
    with pytest.raises(ErroUso):
        consultas.executar(motor, "nao_existe")


def _empresa(motor, rfed, filtro_existe):
    return motor._sql("SELECT TOP 1 p.codi_emp AS e FROM bethadba.efparametro_vigencia p WHERE p.rfed_par = ? AND p.vigencia_par = "
                      "(SELECT MAX(x.vigencia_par) FROM bethadba.efparametro_vigencia x WHERE x.codi_emp = p.codi_emp) AND EXISTS (" + filtro_existe + ") ORDER BY p.codi_emp", (rfed,))[0]["e"]


def test_perfil_fiscal_simples(motor):
    emp = _empresa(motor, 4, "SELECT 1 FROM bethadba.efsdoimp_simples_nacional s WHERE s.codi_emp = p.codi_emp AND s.codi_imp = 44 AND s.basen > 0 AND s.data_sim >= '2026-01-01'")
    r = consultas.perfil_fiscal(motor, emp, "2026-09-30")
    assert r["regime_federal"]["codigo"] == 4 and r["regime_federal"]["significado"] == "Simples Nacional"
    assert r["regime_federal"]["confianca_da_legenda"].startswith("alta")
    assert r["evidencias_12_meses"]["apuracao_simples_nacional"]["competencias"] >= 6
    assert any(i["codigo"] == 44 for i in r["impostos_ativos"])


def test_perfil_fiscal_variante_do_simples(motor):
    r = consultas.perfil_fiscal(motor, 679, "2026-09-30")          # empresa 679: regime 2 e apura o Simples todo mês
    assert r["regime_federal"]["codigo"] == 2 and r["evidencias_12_meses"]["apuracao_simples_nacional"]["competencias"] >= 6


def test_perfil_fiscal_presumido_tem_evidencia_de_irpj(motor):
    emp = _empresa(motor, 5, "SELECT 1 FROM bethadba.efsdoimp i JOIN bethadba.geimposto g ON g.codi_emp = i.codi_emp AND g.codi_imp = i.codi_imp WHERE i.codi_emp = p.codi_emp AND g.nome_imp LIKE '%IRPJ%' AND i.data_sim >= '2026-01-01'")
    r = consultas.perfil_fiscal(motor, emp, "2026-09-30")
    assert r["regime_federal"]["codigo"] == 5 and r["evidencias_12_meses"]["apuracao_irpj"]["linhas"] > 0


def test_perfil_fiscal_sem_parametros(motor):
    with pytest.raises(ErroUso):
        consultas.perfil_fiscal(motor, 679, "1900-01-01")


def test_esocial_competencia_fechada_apos_reabertura(motor):
    # empresa 614: junho/2026 foi fechada (S-1299), reaberta (S-1298) e fechada de novo — vale o último evento
    r = consultas.situacao_esocial(motor, 614, "2026-06")
    assert r["fechamento_da_folha"]["estado"] == "fechada" and r["fechamento_da_folha"]["ultimo_evento"] == "S-1299"
    assert r["fechamento_da_folha"]["recibo"]
    assert {e["evento"] for e in r["eventos_da_competencia"]} <= {"S-1200 Remuneração", "S-1210 Pagamentos"}


def test_esocial_sem_fechamento(motor):
    r = consultas.situacao_esocial(motor, 614, "2030-01")
    assert r["fechamento_da_folha"]["estado"] == "sem_fechamento" and r["avisos"]


def test_esocial_competencia_invalida(motor):
    with pytest.raises(ErroUso):
        consultas.situacao_esocial(motor, 614, "junho")


def test_memoria_calculo_folha(motor):
    linha = motor._sql("SELECT TOP 1 s.i_empregados AS emp, s.competencia AS comp FROM bethadba.fobasesserv s WHERE s.codi_emp = 354 AND s.tipo_process = 11 AND s.competencia >= '2026-01-01' "
                       "AND EXISTS (SELECT 1 FROM bethadba.focalculosbases b WHERE b.i_calculos = s.i_calculos AND b.valor <> 0) ORDER BY s.i_empregados", ())[0]
    r = consultas.memoria_calculo_folha(motor, 354, linha["emp"], linha["comp"].isoformat()[:7], tipo_folha=11)
    assert r["calculos"] and r["calculos"][0]["tipo_folha"]["codigo"] == 11
    bases = r["calculos"][0]["bases"]
    assert bases and all({"base", "valor_da_base", "taxa", "valor"} <= set(b) for b in bases)
    assert any("INSS" in b["base"] or "FGTS" in b["base"] for b in bases)


def test_memoria_calculo_folha_inexistente(motor):
    with pytest.raises(ErroUso):
        consultas.memoria_calculo_folha(motor, 354, 999999, "2026-08")


def test_guias_do_mes_paga_com_pagamento_registrado(motor):
    linha = motor._sql("SELECT TOP 1 r.codi_emp AS e, r.data_sim AS d FROM bethadba.efsdoimp_por_recolhimento r WHERE r.data_sim >= '2022-01-01' AND r.data_sim < '2023-01-01' "
                       "AND r.saldo_recolher > 0 AND r.valor_pago >= r.saldo_recolher ORDER BY r.codi_emp", ())[0]
    r = consultas.guias_do_mes(motor, linha["e"], linha["d"].isoformat()[:7])
    assert any(g["situacao"] == "paga" for g in r["guias"]) and r["totais"]["saldo_a_recolher"] > 0
    assert "avisos" not in r or not any("2024" in a for a in r["avisos"])


def test_guias_do_mes_recente_avisa_que_pagamento_nao_e_confiavel(motor):
    linha = motor._sql("SELECT TOP 1 r.codi_emp AS e, r.data_sim AS d FROM bethadba.efsdoimp_por_recolhimento r WHERE r.data_sim >= '2026-01-01' AND r.saldo_recolher > 0 ORDER BY r.codi_emp", ())[0]
    r = consultas.guias_do_mes(motor, linha["e"], linha["d"].isoformat()[:7])
    assert r["guias"] and any("2024" in a for a in r["avisos"])
    assert all(g["situacao"] != "paga" or g["valor_pago"] > 0 for g in r["guias"])


def test_perfil_empresa_completo(motor):
    r = consultas.perfil_empresa(motor, 614, "2026-09-30")
    assert r["cadastro"]["nome"] and r["cadastro"]["tipo_documento"] in ("CNPJ", "CPF")
    assert r["fiscal"]["regime_federal"]["codigo"] is not None
    assert r["contabilidade"]["mascara_plano_contas"] and r["folha"]["competencia_atual"]
    assert r["esocial"]["ultimo_evento_de_fechamento"] in ("S-1298", "S-1299")


def test_perfil_empresa_inexistente(motor):
    with pytest.raises(ErroUso):
        consultas.perfil_empresa(motor, 99999999)


def test_informativos_da_empresa_dctf_com_recibo(motor):
    linha = motor._sql("SELECT TOP 1 h.codi_emp AS e, h.competencia AS c FROM bethadba.efoutrosdados h WHERE h.i_informativos = 36 AND h.competencia >= '2022-01-01' AND EXISTS "
                       "(SELECT 1 FROM bethadba.efoutrosdados_dados d WHERE d.codi_emp = h.codi_emp AND d.competencia = h.competencia AND d.i_informativos = 36 AND d.campo = 'numero_recibo' AND LENGTH(TRIM(d.valor)) > 0) "
                       "ORDER BY h.codi_emp", ())[0]
    r = consultas.informativos_da_empresa(motor, linha["e"], linha["c"].isoformat()[:7], informativo=36)
    assert r["total"] >= 1 and r["informativos"][0]["informativo"]["nome"] == "DCTF" and r["informativos"][0]["numero_recibo"]


def test_informativos_periodo_invertido_e_vazio(motor):
    with pytest.raises(ErroUso):
        consultas.informativos_da_empresa(motor, 614, "2026-09", "2026-01")
    assert consultas.informativos_da_empresa(motor, 614, "1990-01")["total"] == 0


def test_apuracao_lalur_confere(motor):
    linha = motor._sql("SELECT TOP 1 c.codi_emp AS e, c.competencia AS comp FROM bethadba.lrcalculo c JOIN bethadba.lrcalculo_irpj_real i ON i.codi_emp = c.codi_emp AND i.i_calculo = c.i_calculo "
                       "WHERE i.valor_irpj_devido > 0 AND i.valor_adicional > 0 ORDER BY c.competencia DESC", ())[0]
    r = consultas.apuracao_lalur(motor, linha["e"], linha["comp"].isoformat()[:7])
    assert r["irpj"] and r["csll"] and r["conferencia"]
    assert any("adicional" in c["verificacao"] for c in r["conferencia"])
    assert r["tudo_confere"], [c for c in r["conferencia"] if not c["confere"]]


def test_apuracao_lalur_empresa_sem_calculo(motor):
    with pytest.raises(ErroUso):
        consultas.apuracao_lalur(motor, 679, "2026-09")      # Simples: não tem cálculo de lucro real


def test_situacao_das_declarada_e_emitida(motor):
    linha = motor._sql("SELECT TOP 1 e.codi_emp AS e, e.competencia AS c FROM bethadba.efdas_api_envio_arquivos e WHERE e.tipo_envio = 2 AND e.situacao = 1 AND LENGTH(TRIM(COALESCE(e.numero_das, ''))) > 0 "
                       "AND EXISTS (SELECT 1 FROM bethadba.efdas_api_envio_arquivos d WHERE d.codi_emp = e.codi_emp AND d.competencia = e.competencia AND d.tipo_envio = 1 AND d.situacao = 1) "
                       "AND EXISTS (SELECT 1 FROM bethadba.efsdoimp_simples_nacional s WHERE s.codi_emp = e.codi_emp AND s.data_sim = e.competencia AND s.codi_imp = 44) ORDER BY e.competencia DESC, e.codi_emp", ())[0]
    r = consultas.situacao_das(motor, linha["e"], linha["c"].isoformat()[:7])
    assert r["estado"] == "declarada_e_das_emitido" and len(r["guia_das"]["numero"]) == 17 and r["declaracao"]["transmissoes_com_sucesso"] >= 1


def test_situacao_das_antes_da_integracao_avisa(motor):
    r = consultas.situacao_das(motor, 679, "2023-05")
    assert r["total_de_envios"] == 0 and any("2024-04" in a for a in r["avisos"])


def test_situacao_das_sem_movimento_nao_alarma(motor):
    linha = motor._sql("SELECT TOP 1 e.codi_emp AS e, e.competencia AS c FROM bethadba.efdas_api_envio_arquivos e WHERE e.tipo_envio = 1 AND e.situacao = 1 "
                       "AND EXISTS (SELECT 1 FROM bethadba.efsdoimp_simples_nacional s WHERE s.codi_emp = e.codi_emp AND s.data_sim = e.competencia AND s.codi_imp = 44 AND s.anexo = 0) "
                       "AND NOT EXISTS (SELECT 1 FROM bethadba.efsdoimp_simples_nacional s WHERE s.codi_emp = e.codi_emp AND s.data_sim = e.competencia AND s.codi_imp = 44 AND s.anexo > 0) "
                       "AND NOT EXISTS (SELECT 1 FROM bethadba.efdas_api_envio_arquivos d WHERE d.codi_emp = e.codi_emp AND d.competencia = e.competencia AND d.tipo_envio = 2 AND LENGTH(TRIM(COALESCE(d.numero_das, ''))) > 0) "
                       "ORDER BY e.competencia DESC", ())[0]
    r = consultas.situacao_das(motor, linha["e"], linha["c"].isoformat()[:7])
    assert r["estado"] == "declarada_sem_das" and r["apuracao_simples"]["sem_movimento"]
    assert not any(a.startswith("ATENÇÃO") for a in r.get("avisos", []))


def test_receita_bruta_mensal_bate_com_a_funcao_do_simples(motor):
    serie = consultas.receita_bruta_mensal(motor, 679, "2026-01", "2026-09")
    assert [x["mes"] for x in serie["meses"]][0] == "2026-01" and len(serie["meses"]) == 9
    set_ = next(x for x in serie["meses"] if x["mes"] == "2026-09")
    assert set_["receita_bruta"] == 54683.68 and set_["diferenca_para_simples"] == 0
    assert abs(sum(x["receita_bruta"] for x in serie["meses"]) - serie["total_receita_bruta"]) < 0.02


def test_receita_bruta_mensal_limites(motor):
    with pytest.raises(ErroUso):
        consultas.receita_bruta_mensal(motor, 679, "2026-09", "2026-01")
    with pytest.raises(ErroUso):
        consultas.receita_bruta_mensal(motor, 679, "2020-01", "2026-09")


def test_situacao_reinf_fechada(motor):
    linha = motor._sql("SELECT TOP 1 e.codi_emp AS e, e.competencia AS c FROM bethadba.efd_reinf_envio_arquivos e WHERE e.i_evento = 2099 AND e.situacao = 1 AND COALESCE(e.evento_excluido, 'N') <> 'S' "
                       "AND LENGTH(TRIM(COALESCE(e.numero_recibo, ''))) > 0 ORDER BY e.competencia DESC, e.codi_emp", ())[0]
    r = consultas.situacao_reinf(motor, linha["e"], linha["c"].isoformat()[:7])
    assert r["fechamento_serie_2000"]["estado"] in ("fechada", "reaberta") and r["fechamento_serie_2000"]["recibo"]
    assert r["eventos"] and all({"evento", "enviados", "aceitos", "rejeitados"} <= set(e) for e in r["eventos"])


def test_situacao_reinf_sem_fechamento(motor):
    r = consultas.situacao_reinf(motor, 679, "2030-01")
    assert r["fechamento_serie_2000"]["estado"] == "sem_fechamento" and r["avisos"]


def test_resumo_folha(motor):
    r = consultas.resumo_folha(motor, 354, "2026-08")
    assert r["por_tipo_de_folha"] and r["totais"]["proventos"] > 0
    t11 = next(x for x in r["por_tipo_de_folha"] if x["tipo_folha"]["codigo"] == 11)
    assert t11["empregados"] > 0 and abs(t11["liquido_calculado"] - (t11["proventos"] - t11["descontos"])) < 0.02
    if t11["liquido_gravado"] is not None and t11["bases_sem_liquido"] == 0:
        assert abs(t11["liquido_gravado"] - t11["liquido_calculado"]) < 0.05


def test_resumo_folha_sem_folha(motor):
    with pytest.raises(ErroUso):
        consultas.resumo_folha(motor, 354, "1999-01")


def test_historico_salarial(motor):
    linha = motor._sql("SELECT TOP 1 codi_emp AS e, i_empregados AS x FROM bethadba.foaltesal WHERE tipo_alt_grade = 1 AND competencia >= '2010-01-01' GROUP BY codi_emp, i_empregados HAVING COUNT(*) >= 3 ORDER BY codi_emp", ())[0]
    r = consultas.historico_salarial(motor, linha["e"], linha["x"])
    assert len(r["alteracoes_salariais"]) >= 3 and all("novo_salario" in a for a in r["alteracoes_salariais"])
    assert isinstance(r["problemas_de_continuidade"], list)


def test_historico_salarial_inexistente(motor):
    with pytest.raises(ErroUso):
        consultas.historico_salarial(motor, 354, 99999999)


def test_classificacao_produto(motor):
    linha = motor._sql("SELECT TOP 1 v.codi_emp AS e, TRIM(v.codi_pdi) AS p FROM bethadba.efprodutos_vigencia v WHERE v.vigencia_pdi >= '2020-01-01' AND v.codigo_cst_saida IS NOT NULL ORDER BY v.codi_emp, v.codi_pdi", ())[0]
    r = consultas.classificacao_produto(motor, linha["e"], linha["p"], "2026-09-30")
    assert r["pis_cofins"]["cst_saida"]["codigo"] is not None and "icms" in r and r["vigencias_do_produto"] >= 1


def test_classificacao_produto_inexistente(motor):
    with pytest.raises(ErroUso):
        consultas.classificacao_produto(motor, 354, "produto-que-nao-existe-xyz")


def test_visao_mensal_simples(motor):
    r = consultas.visao_mensal(motor, 679, "2026-09")
    assert r["empresa_nome"] and r["receita_bruta"]["receita_bruta"] == 54683.68
    assert r["das"] is not None and r["receita_vs_simples"]["situacao"] == "confere"
    assert isinstance(r["alertas"], list)


def test_visao_mensal_empresa_com_folha_e_esocial(motor):
    r = consultas.visao_mensal(motor, 614, "2026-06")
    assert r["esocial"]["fechamento"] == "fechada" and r["folha"] is not None


def test_resumo_folha_nao_duplica_por_rateio(motor):
    """Regressão achada na revisão independente: fobasesserv grava o cálculo em 2 linhas (rateio 0 e 1) com os mesmos valores; somar as duas dobrava a folha."""
    r = consultas.resumo_folha(motor, 354, "2026-08")
    mensal = next(x for x in r["por_tipo_de_folha"] if x["tipo_folha"]["codigo"] == 11)
    assert mensal["liquido_calculado"] == mensal["liquido_gravado"] == 67938.0
    assert mensal["bases_sem_liquido"] == 0
