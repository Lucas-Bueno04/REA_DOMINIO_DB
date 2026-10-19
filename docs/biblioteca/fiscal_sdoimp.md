# Módulo `fiscal_sdoimp`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `efsdoimp_aproveitamento_credito_consultar` | consultar | efsdoimp_aproveitamento_credito | empresa | ✔ |
| `efsdoimp_aproveitamento_credito_obter` | obter | efsdoimp_aproveitamento_credito | empresa, imposto, competencia, periodicidade, origem_do_credito_1_interno_2_externo, tipo_1_interno_2_nao_tributado_3_externo, periodo_de_apuracao_do_credito | ✔ |
| `efsdoimp_aproveitamento_credito_totais` | totais | efsdoimp_aproveitamento_credito | empresa | ✔ |
| `efsdoimp_csll_csll_retido_consultar` | consultar | efsdoimp_csll_csll_retido | empresa | ✔ |
| `efsdoimp_csll_csll_retido_obter` | obter | efsdoimp_csll_csll_retido | empresa, imposto, data, periodicidade, natureza, periodo_de_apuracao_da_retencao | ✔ |
| `efsdoimp_csll_csll_retido_totais` | totais | efsdoimp_csll_csll_retido | empresa | ✔ |
| `efsdoimp_es_compete_consultar` | consultar | efsdoimp_es_compete | empresa | ✔ |
| `efsdoimp_es_compete_obter` | obter | efsdoimp_es_compete | empresa, imposto, periodo, periodicidade | ✔ |
| `efsdoimp_es_compete_totais` | totais | efsdoimp_es_compete | empresa | ✔ |
| `efsdoimp_estadual_ac_consultar` | consultar | efsdoimp_estadual_ac | empresa | ✔ |
| `efsdoimp_estadual_ac_obter` | obter | efsdoimp_estadual_ac | empresa, imposto, periodicidade, competencia | ✔ |
| `efsdoimp_estadual_ac_totais` | totais | efsdoimp_estadual_ac | empresa | ✔ |
| `efsdoimp_estadual_al_consultar` | consultar | efsdoimp_estadual_al | empresa | ✔ |
| `efsdoimp_estadual_al_obter` | obter | efsdoimp_estadual_al | empresa, imposto, periodicidade, competencia | ✔ |
| `efsdoimp_estadual_al_totais` | totais | efsdoimp_estadual_al | empresa | ✔ |
| `efsdoimp_estadual_am_consultar` | consultar | efsdoimp_estadual_am | empresa | ✔ |
| `efsdoimp_estadual_am_obter` | obter | efsdoimp_estadual_am | empresa, imposto, competencia, pdic_sim | ✔ |
| `efsdoimp_estadual_am_totais` | totais | efsdoimp_estadual_am | empresa | ✔ |
| `efsdoimp_estadual_ba_consultar` | consultar | efsdoimp_estadual_ba | empresa | ✔ |
| `efsdoimp_estadual_ba_obter` | obter | efsdoimp_estadual_ba | empresa, imposto, competencia, pdic_sim | ✔ |
| `efsdoimp_estadual_ba_totais` | totais | efsdoimp_estadual_ba | empresa | ✔ |
| `efsdoimp_estadual_ce_consultar` | consultar | efsdoimp_estadual_ce | empresa | ✔ |
| `efsdoimp_estadual_ce_obter` | obter | efsdoimp_estadual_ce | empresa, imposto, competencia, pdic_sim | ✔ |
| `efsdoimp_estadual_ce_totais` | totais | efsdoimp_estadual_ce | empresa | ✔ |
| `efsdoimp_estadual_df_consultar` | consultar | efsdoimp_estadual_df | empresa | ✔ |
| `efsdoimp_estadual_df_obter` | obter | efsdoimp_estadual_df | empresa, imposto, competencia, pdic_sim | ✔ |
| `efsdoimp_estadual_df_totais` | totais | efsdoimp_estadual_df | empresa | ✔ |
| `efsdoimp_estadual_es_consultar` | consultar | efsdoimp_estadual_es | empresa | ✔ |
| `efsdoimp_estadual_es_obter` | obter | efsdoimp_estadual_es | empresa, imposto, competencia, pdic_sim | ✔ |
| `efsdoimp_estadual_es_totais` | totais | efsdoimp_estadual_es | empresa | ✔ |
| `efsdoimp_estadual_mg_consultar` | consultar | efsdoimp_estadual_mg | empresa | ✔ |
| `efsdoimp_estadual_mg_obter` | obter | efsdoimp_estadual_mg | empresa, imposto, competencia, pdic_sim | ✔ |
| `efsdoimp_estadual_mg_totais` | totais | efsdoimp_estadual_mg | empresa | ✔ |
| `efsdoimp_estadual_mt_consultar` | consultar | efsdoimp_estadual_mt | empresa | ✔ |
| `efsdoimp_estadual_mt_obter` | obter | efsdoimp_estadual_mt | empresa, imposto, competencia, pdic_sim | ✔ |
| `efsdoimp_estadual_mt_totais` | totais | efsdoimp_estadual_mt | empresa | ✔ |
| `efsdoimp_estadual_pa_consultar` | consultar | efsdoimp_estadual_pa | empresa | ✔ |
| `efsdoimp_estadual_pa_obter` | obter | efsdoimp_estadual_pa | empresa, imposto, competencia, pdic_sim | ✔ |
| `efsdoimp_estadual_pa_totais` | totais | efsdoimp_estadual_pa | empresa | ✔ |
| `efsdoimp_estadual_pe_consultar` | consultar | efsdoimp_estadual_pe | empresa | ✔ |
| `efsdoimp_estadual_pe_obter` | obter | efsdoimp_estadual_pe | empresa, imposto, competencia, pdic_sim | ✔ |
| `efsdoimp_estadual_pe_totais` | totais | efsdoimp_estadual_pe | empresa | ✔ |
| `efsdoimp_estadual_pi_consultar` | consultar | efsdoimp_estadual_pi | empresa | ✔ |
| `efsdoimp_estadual_pi_obter` | obter | efsdoimp_estadual_pi | empresa, imposto, competencia, pdic_sim | ✔ |
| `efsdoimp_estadual_pi_totais` | totais | efsdoimp_estadual_pi | empresa | ✔ |
| `efsdoimp_estadual_pr_consultar` | consultar | efsdoimp_estadual_pr | empresa | ✔ |
| `efsdoimp_estadual_pr_obter` | obter | efsdoimp_estadual_pr | empresa, imposto, competencia, pdic_sim | ✔ |
| `efsdoimp_estadual_pr_totais` | totais | efsdoimp_estadual_pr | empresa | ✔ |
| `efsdoimp_estadual_rj_consultar` | consultar | efsdoimp_estadual_rj | empresa | ✔ |
| `efsdoimp_estadual_rj_obter` | obter | efsdoimp_estadual_rj | empresa, competencia, pdic_sim, imposto | ✔ |
| `efsdoimp_estadual_rj_totais` | totais | efsdoimp_estadual_rj | empresa | ✔ |
| `efsdoimp_estadual_rn_consultar` | consultar | efsdoimp_estadual_rn | empresa | ✔ |
| `efsdoimp_estadual_rn_obter` | obter | efsdoimp_estadual_rn | empresa, imposto, competencia, pdic_sim | ✔ |
| `efsdoimp_estadual_rn_totais` | totais | efsdoimp_estadual_rn | empresa | ✔ |
| `efsdoimp_estadual_ro_consultar` | consultar | efsdoimp_estadual_ro | empresa | ✔ |
| `efsdoimp_estadual_ro_obter` | obter | efsdoimp_estadual_ro | empresa, imposto, competencia, pdic_sim | ✔ |
| `efsdoimp_estadual_ro_totais` | totais | efsdoimp_estadual_ro | empresa | ✔ |
| `efsdoimp_estadual_sc_consultar` | consultar | efsdoimp_estadual_sc | empresa | ✔ |
| `efsdoimp_estadual_sc_obter` | obter | efsdoimp_estadual_sc | empresa, imposto, competencia, pdic_sim | ✔ |
| `efsdoimp_estadual_sc_totais` | totais | efsdoimp_estadual_sc | empresa | ✔ |
| `efsdoimp_estadual_sp_consultar` | consultar | efsdoimp_estadual_sp | empresa | ✔ |
| `efsdoimp_estadual_sp_obter` | obter | efsdoimp_estadual_sp | empresa, imposto, competencia, periodicidade | ✔ |
| `efsdoimp_estadual_sp_totais` | totais | efsdoimp_estadual_sp | empresa | ✔ |
| `efsdoimp_estadual_to_consultar` | consultar | efsdoimp_estadual_to | empresa | ✔ |
| `efsdoimp_estadual_to_obter` | obter | efsdoimp_estadual_to | empresa, imposto, competencia, pdic_sim | ✔ |
| `efsdoimp_estadual_to_totais` | totais | efsdoimp_estadual_to | empresa | ✔ |
| `efsdoimp_inss_rb_por_recolhimento_consultar` | consultar | efsdoimp_inss_rb_por_recolhimento | empresa | ✔ |
| `efsdoimp_inss_rb_por_recolhimento_obter` | obter | efsdoimp_inss_rb_por_recolhimento | empresa, imposto, competencia, pdic_sim, codigo_do_recolhimento, sequencial_scp | ✔ |
| `efsdoimp_inss_rb_por_recolhimento_totais` | totais | efsdoimp_inss_rb_por_recolhimento | empresa | ✔ |
| `efsdoimp_inss_rb_por_recolhimento_cno_consultar` | consultar | efsdoimp_inss_rb_por_recolhimento_cno | empresa | ✔ |
| `efsdoimp_inss_rb_por_recolhimento_cno_obter` | obter | efsdoimp_inss_rb_por_recolhimento_cno | empresa, imposto, competencia, pdic_sim, codigo_do_recolhimento, sequencial_scp, codigo_cno | ✔ |
| `efsdoimp_inss_rb_por_recolhimento_cno_totais` | totais | efsdoimp_inss_rb_por_recolhimento_cno | empresa | ✔ |
| `efsdoimp_inss_rb_por_recolhimento_por_atividade_consultar` | consultar | efsdoimp_inss_rb_por_recolhimento_por_atividade | empresa | ✔ |
| `efsdoimp_inss_rb_por_recolhimento_por_atividade_obter` | obter | efsdoimp_inss_rb_por_recolhimento_por_atividade | empresa, imposto, competencia, pdic_sim, codigo_do_recolhimento, codigo_da_filial, atividade_inss_receita_bruta, sequencial_scp | ✔ |
| `efsdoimp_inss_rb_por_recolhimento_por_atividade_totais` | totais | efsdoimp_inss_rb_por_recolhimento_por_atividade | empresa | ✔ |
| `efsdoimp_inss_rb_por_recolhimento_por_atividade_cno_consultar` | consultar | efsdoimp_inss_rb_por_recolhimento_por_atividade_cno | empresa | ✔ |
| `efsdoimp_inss_rb_por_recolhimento_por_atividade_cno_obter` | obter | efsdoimp_inss_rb_por_recolhimento_por_atividade_cno | empresa, imposto, competencia, pdic_sim, codigo_do_recolhimento, codigo_da_filial, atividade_inss_receita_bruta, sequencial_scp, codigo_cno | ✔ |
| `efsdoimp_inss_rb_por_recolhimento_por_atividade_cno_totais` | totais | efsdoimp_inss_rb_por_recolhimento_por_atividade_cno | empresa | ✔ |
| `efsdoimp_inss_rb_receita_consultar` | consultar | efsdoimp_inss_rb_receita | empresa | ✔ |
| `efsdoimp_inss_rb_receita_obter` | obter | efsdoimp_inss_rb_receita | empresa, imposto, competencia, pdic_sim, codigo_da_filial, sequencial_scp | ✔ |
| `efsdoimp_inss_rb_receita_totais` | totais | efsdoimp_inss_rb_receita | empresa | ✔ |
| `efsdoimp_irpj_irrf_retido_consultar` | consultar | efsdoimp_irpj_irrf_retido | empresa | ✔ |
| `efsdoimp_irpj_irrf_retido_obter` | obter | efsdoimp_irpj_irrf_retido | empresa, imposto, data, periodicidade, natureza, periodo_de_apuracao_da_retencao, tipo_retencao_1_retido_2_propaganda | ✔ |
| `efsdoimp_irpj_irrf_retido_totais` | totais | efsdoimp_irpj_irrf_retido | empresa | ✔ |
| `efsdoimp_lancto_consultar` | consultar | efsdoimp_lancto | empresa | ✔ |
| `efsdoimp_lancto_obter` | obter | efsdoimp_lancto | empresa, numero_do_lancamento, empresa_do_imposto, codigo_do_imposto, competencia_do_imposto, periodicidade_do_imposto | ✔ |
| `efsdoimp_mg_sub_apuracao_consultar` | consultar | efsdoimp_mg_sub_apuracao | empresa | ✔ |
| `efsdoimp_mg_sub_apuracao_obter` | obter | efsdoimp_mg_sub_apuracao | empresa, imposto, competencia, periodicidade, sequencial_sub_apuracao | ✔ |
| `efsdoimp_mg_sub_apuracao_totais` | totais | efsdoimp_mg_sub_apuracao | empresa | ✔ |
| `efsdoimp_mg_sub_apuracao_incentivo_ret_consultar` | consultar | efsdoimp_mg_sub_apuracao_incentivo_ret | empresa | ✔ |
| `efsdoimp_mg_sub_apuracao_incentivo_ret_obter` | obter | efsdoimp_mg_sub_apuracao_incentivo_ret | empresa, imposto, competencia, periodicidade, sequencial_sub_apuracao, sequencial_sub_apuracao_0_apuracao_norma, sequencial_incentivo | ✔ |
| `efsdoimp_mg_sub_apuracao_incentivo_ret_totais` | totais | efsdoimp_mg_sub_apuracao_incentivo_ret | empresa | ✔ |
| `efsdoimp_nao_cumulativos_consultar` | consultar | efsdoimp_nao_cumulativos | empresa | ✔ |
| `efsdoimp_nao_cumulativos_obter` | obter | efsdoimp_nao_cumulativos | empresa, imposto, competencia, periodicidade | ✔ |
| `efsdoimp_nao_cumulativos_totais` | totais | efsdoimp_nao_cumulativos | empresa | ✔ |
| `efsdoimp_parcelas_consultar` | consultar | efsdoimp_parcelas | empresa | ✔ |
| `efsdoimp_parcelas_obter` | obter | efsdoimp_parcelas | empresa, imposto, competencia, pdic_sim, parcela_do_imposto | ✔ |
| `efsdoimp_parcelas_totais` | totais | efsdoimp_parcelas | empresa | ✔ |
| `efsdoimp_pis_cofins_contabilizacao_consultar` | consultar | efsdoimp_pis_cofins_contabilizacao | empresa | ✔ |
| `efsdoimp_pis_cofins_contabilizacao_obter` | obter | efsdoimp_pis_cofins_contabilizacao | empresa, imposto, competencia, pdic_sim, scp, recolhimento, consolidado | ✔ |
| `efsdoimp_pis_cofins_contabilizacao_totais` | totais | efsdoimp_pis_cofins_contabilizacao | empresa | ✔ |
| `efsdoimp_pis_cofins_contabilizacao_detalhamento_c_017f_consultar` | consultar | efsdoimp_pis_cofins_contabilizacao_detalhamento_credito | empresa | ✔ |
| `efsdoimp_pis_cofins_contabilizacao_detalhamento_credito_obter` | obter | efsdoimp_pis_cofins_contabilizacao_detalhamento_credito | empresa, imposto, competencia, pdic_sim, scp, recolhimento, consolidado, codigo_do_credito | ✔ |
| `efsdoimp_pis_cofins_contabilizacao_detalhamento_credito_totais` | totais | efsdoimp_pis_cofins_contabilizacao_detalhamento_credito | empresa | ✔ |
| `efsdoimp_pis_cofins_detalhamento_consultar` | consultar | efsdoimp_pis_cofins_detalhamento | empresa | ✔ |
| `efsdoimp_pis_cofins_detalhamento_obter` | obter | efsdoimp_pis_cofins_detalhamento | empresa, imposto, competencia, periodicidade, sequencial_do_scp, sequencial_do_recolhimento | ✔ |
| `efsdoimp_pis_cofins_detalhamento_totais` | totais | efsdoimp_pis_cofins_detalhamento | empresa | ✔ |
| `efsdoimp_pis_cofins_detalhamento_credito_consultar` | consultar | efsdoimp_pis_cofins_detalhamento_credito | empresa | ✔ |
| `efsdoimp_pis_cofins_detalhamento_credito_obter` | obter | efsdoimp_pis_cofins_detalhamento_credito | empresa, imposto, competencia, periodicidade, codigo_do_credito, periodo_em_que_o_credito_foi_apurado, valor_da_aliquota_do_imposto, aliquota_em_moeda_quando_o_calculo_e_por, sequencial_do_scp, sequencial_do_recolhimento | ✔ |
| `efsdoimp_pis_cofins_detalhamento_credito_totais` | totais | efsdoimp_pis_cofins_detalhamento_credito | empresa | ✔ |
| `efsdoimp_pis_cofins_detalhamento_credito_bases_consultar` | consultar | efsdoimp_pis_cofins_detalhamento_credito_bases | empresa | ✔ |
| `efsdoimp_pis_cofins_detalhamento_credito_bases_obter` | obter | efsdoimp_pis_cofins_detalhamento_credito_bases | empresa, imposto, competencia, periodicidade, codigo_do_credito, periodo_em_que_o_credito_foi_apurado, valor_da_aliquota_do_imposto, aliquota_em_moeda_quando_o_calculo_e_por, natureza_da_base_de_calculo_do_credito, cst_vinculado_ao_credito, sequencial_do_scp, sequencial_do_recolhimento | ✔ |
| `efsdoimp_pis_cofins_detalhamento_credito_bases_totais` | totais | efsdoimp_pis_cofins_detalhamento_credito_bases | empresa | ✔ |
| `efsdoimp_pis_cofins_detalhamento_debito_consultar` | consultar | efsdoimp_pis_cofins_detalhamento_debito | empresa | ✔ |
| `efsdoimp_pis_cofins_detalhamento_debito_obter` | obter | efsdoimp_pis_cofins_detalhamento_debito | empresa, imposto, competencia, periodicidade, codigo_da_contribuicao, valor_da_aliquota_do_imposto, aliquota_em_moeda_quando_o_calculo_e_por, sequencial_do_scp, sequencial_do_recolhimento | ✔ |
| `efsdoimp_pis_cofins_detalhamento_debito_totais` | totais | efsdoimp_pis_cofins_detalhamento_debito | empresa | ✔ |
| `efsdoimp_pis_cofins_detalhamento_debito_devolucao_consultar` | consultar | efsdoimp_pis_cofins_detalhamento_debito_devolucao | empresa | ✔ |
| `efsdoimp_pis_cofins_detalhamento_debito_devolucao_obter` | obter | efsdoimp_pis_cofins_detalhamento_debito_devolucao | empresa, imposto, competencia, periodicidade, codigo_da_contribuicao, valor_da_aliquota_do_imposto, aliquota_em_moeda_quando_o_calculo_e_por, periodo_em_que_o_dedito_foi_apurado, codigo_da_nota_de_entrada, filial, sequencial_do_scp, sequencial_do_recolhimento, codigo_da_nota_de_saida | ✔ |
| `efsdoimp_pis_cofins_detalhamento_debito_devolucao_totais` | totais | efsdoimp_pis_cofins_detalhamento_debito_devolucao | empresa | ✔ |
| `efsdoimp_pis_cofins_detalhamento_debito_devolucao_d118_consultar` | consultar | efsdoimp_pis_cofins_detalhamento_debito_devolucao_aproveitamento | empresa | ✔ |
| `efsdoimp_pis_cofins_detalhamento_debito_devolucao_ap_d118_totais` | totais | efsdoimp_pis_cofins_detalhamento_debito_devolucao_aproveitamento | empresa | ✔ |
| `efsdoimp_pis_cofins_detalhamento_debito_imobiliario_consultar` | consultar | efsdoimp_pis_cofins_detalhamento_debito_imobiliario | empresa | ✔ |
| `efsdoimp_pis_cofins_detalhamento_debito_imobiliario_obter` | obter | efsdoimp_pis_cofins_detalhamento_debito_imobiliario | empresa, codigo_da_filial, codigo_do_empreendimento, codigo_da_unidade, imposto, competencia, pdic_sim, codigo_do_contrato, sequencial_do_scp, sequencial_do_recolhimento | ✔ |
| `efsdoimp_pis_cofins_detalhamento_debito_imobiliario_totais` | totais | efsdoimp_pis_cofins_detalhamento_debito_imobiliario | empresa | ✔ |
| `efsdoimp_pis_cofins_detalhamento_debito_por_filial_consultar` | consultar | efsdoimp_pis_cofins_detalhamento_debito_por_filial | empresa | ✔ |
| `efsdoimp_pis_cofins_detalhamento_debito_por_filial_obter` | obter | efsdoimp_pis_cofins_detalhamento_debito_por_filial | empresa, imposto, competencia, periodicidade, codigo_da_contribuicao, valor_da_aliquota_do_imposto, aliquota_em_moeda_quando_o_calculo_e_por, sequencial_do_scp, sequencial_do_recolhimento, filial | ✔ |
| `efsdoimp_pis_cofins_detalhamento_debito_por_filial_totais` | totais | efsdoimp_pis_cofins_detalhamento_debito_por_filial | empresa | ✔ |
| `efsdoimp_pis_cofins_detalhamento_extemporaneo_ctb_consultar` | consultar | efsdoimp_pis_cofins_detalhamento_extemporaneo_ctb | empresa | ✔ |
| `efsdoimp_pis_cofins_detalhamento_extemporaneo_ctb_obter` | obter | efsdoimp_pis_cofins_detalhamento_extemporaneo_ctb | empresa, imposto, competencia, pdic_sim, codigo_do_credito, valor_da_aliquota_do_imposto, aliquota_em_moeda_quando_o_calculo_e_por, sequencial_do_scp, sequencial_do_recolhimento | ✔ |
| `efsdoimp_pis_cofins_detalhamento_extemporaneo_ctb_totais` | totais | efsdoimp_pis_cofins_detalhamento_extemporaneo_ctb | empresa | ✔ |
| `efsdoimp_pis_cofins_detalhamento_retencao_consultar` | consultar | efsdoimp_pis_cofins_detalhamento_retencao | empresa | ✔ |
| `efsdoimp_pis_cofins_detalhamento_retencao_obter` | obter | efsdoimp_pis_cofins_detalhamento_retencao | empresa, imposto, competencia, periodicidade, natureza_da_retencao, periodo_de_apuracao_da_retencao, sequencial_do_scp, sequencial_do_recolhimento | ✔ |
| `efsdoimp_pis_cofins_detalhamento_retencao_totais` | totais | efsdoimp_pis_cofins_detalhamento_retencao | empresa | ✔ |
| `efsdoimp_pis_cofins_detalhamento_retencao_nao_con_2fce_consultar` | consultar | efsdoimp_pis_cofins_detalhamento_retencao_nao_considerado | empresa | ✔ |
| `efsdoimp_pis_cofins_detalhamento_retencao_nao_considerado_obter` | obter | efsdoimp_pis_cofins_detalhamento_retencao_nao_considerado | empresa, imposto, competencia, periodicidade, natureza_da_retencao, periodo_de_apuracao_da_retencao, sequencial_do_scp, sequencial_do_recolhimento | ✔ |
| `efsdoimp_pis_cofins_detalhamento_retencao_nao_considerado_totais` | totais | efsdoimp_pis_cofins_detalhamento_retencao_nao_considerado | empresa | ✔ |
| `efsdoimp_pis_cofins_importacao_por_nota_consultar` | consultar | efsdoimp_pis_cofins_importacao_por_nota | empresa | ✔ |
| `efsdoimp_pis_cofins_importacao_por_nota_obter` | obter | efsdoimp_pis_cofins_importacao_por_nota | empresa, imposto, competencia, periodicidade, codigo_da_nota, empresa_da_nota | ✔ |
| `efsdoimp_pis_cofins_importacao_por_nota_totais` | totais | efsdoimp_pis_cofins_importacao_por_nota | empresa | ✔ |
| `efsdoimp_pis_cofins_reducao_linear_consultar` | consultar | efsdoimp_pis_cofins_reducao_linear | empresa | ✔ |
| `efsdoimp_pis_cofins_reducao_linear_obter` | obter | efsdoimp_pis_cofins_reducao_linear | empresa, imposto, competencia, periodicidade, sequencial_do_scp, sequencial_do_recolhimento, cst, aliquota_do_imposto, percentual_da_reducao_linear, operacao_a_acrescimo_r_reducao | ✔ |
| `efsdoimp_pis_cofins_reducao_linear_totais` | totais | efsdoimp_pis_cofins_reducao_linear | empresa | ✔ |
| `efsdoimp_pis_cofins_reducao_linear_aproveitamento_3477_consultar` | consultar | efsdoimp_pis_cofins_reducao_linear_aproveitamento_credito | empresa | ✔ |
| `efsdoimp_pis_cofins_reducao_linear_aproveitamento_credito_obter` | obter | efsdoimp_pis_cofins_reducao_linear_aproveitamento_credito | empresa, imposto, competencia, periodicidade, sequencial_do_scp, sequencial_do_recolhimento, cst_06_aliquota_zero_07_isencao | ✔ |
| `efsdoimp_pis_cofins_reducao_linear_aproveitamento_credito_totais` | totais | efsdoimp_pis_cofins_reducao_linear_aproveitamento_credito | empresa | ✔ |
| `efsdoimp_pis_cofins_reducao_linear_filial_consultar` | consultar | efsdoimp_pis_cofins_reducao_linear_filial | empresa | ✔ |
| `efsdoimp_pis_cofins_reducao_linear_filial_obter` | obter | efsdoimp_pis_cofins_reducao_linear_filial | empresa, imposto, competencia, periodicidade, sequencial_do_scp, sequencial_do_recolhimento, codigo_filial, cst, aliquota_do_imposto, percentual_da_reducao_linear, operacao_a_acrescimo_r_reducao | ✔ |
| `efsdoimp_pis_cofins_reducao_linear_filial_totais` | totais | efsdoimp_pis_cofins_reducao_linear_filial | empresa | ✔ |
| `efsdoimp_pis_cofins_reducao_linear_natureza_consultar` | consultar | efsdoimp_pis_cofins_reducao_linear_natureza | empresa | ✔ |
| `efsdoimp_pis_cofins_reducao_linear_natureza_obter` | obter | efsdoimp_pis_cofins_reducao_linear_natureza | empresa, imposto, competencia, periodicidade, sequencial_do_scp, sequencial_do_recolhimento, codigo_filial, cst, natureza, aliquota_do_imposto, percentual_da_reducao_linear, operacao_a_acrescimo_r_reducao, codigo_beneficio_dirbi | ✔ |
| `efsdoimp_pis_cofins_reducao_linear_natureza_totais` | totais | efsdoimp_pis_cofins_reducao_linear_natureza | empresa | ✔ |
| `efsdoimp_pis_cofins_reducao_linear_por_nota_consultar` | consultar | efsdoimp_pis_cofins_reducao_linear_por_nota | empresa | ✔ |
| `efsdoimp_pis_cofins_reducao_linear_por_nota_obter` | obter | efsdoimp_pis_cofins_reducao_linear_por_nota | empresa, imposto, competencia, periodicidade, sequencial_do_scp, sequencial_do_recolhimento, codigo_filial, cst, aliquota_do_imposto, percentual_da_reducao_linear, operacao_a_acrescimo_r_reducao, tipo_do_movimento_tipo_mov_in_s_v_b_cfe, documento, chave_de_acesso | ✔ |
| `efsdoimp_pis_cofins_reducao_linear_por_nota_totais` | totais | efsdoimp_pis_cofins_reducao_linear_por_nota | empresa | ✔ |
| `efsdoimp_por_recolhimento_por_data_consultar` | consultar | efsdoimp_por_recolhimento_por_data | empresa | ✔ |
| `efsdoimp_por_recolhimento_por_data_obter` | obter | efsdoimp_por_recolhimento_por_data | empresa, imposto, pdic_sim, competencia, sequencial_do_recolhimento, periodo_referencia | ✔ |
| `efsdoimp_por_recolhimento_por_data_totais` | totais | efsdoimp_por_recolhimento_por_data | empresa | ✔ |
| `efsdoimp_por_recolhimento_por_fornecedor_consultar` | consultar | efsdoimp_por_recolhimento_por_fornecedor | empresa | ✔ |
| `efsdoimp_por_recolhimento_por_fornecedor_obter` | obter | efsdoimp_por_recolhimento_por_fornecedor | empresa, imposto, competencia, pdic_sim, codigo_do_recolhimento, tipo_da_inscricao_do_fornecedor, inscricao_do_fornecedor | ✔ |
| `efsdoimp_por_recolhimento_por_fornecedor_totais` | totais | efsdoimp_por_recolhimento_por_fornecedor | empresa | ✔ |
| `efsdoimp_por_recolhimento_por_nota_consultar` | consultar | efsdoimp_por_recolhimento_por_nota | empresa | ✔ |
| `efsdoimp_por_recolhimento_por_nota_obter` | obter | efsdoimp_por_recolhimento_por_nota | empresa, imposto, competencia, pdic_sim, codigo_da_nota_de_entrada, sequencial_do_codigo_de_recolhimento | ✔ |
| `efsdoimp_por_recolhimento_por_nota_totais` | totais | efsdoimp_por_recolhimento_por_nota | empresa | ✔ |
| `efsdoimp_por_uf_consultar` | consultar | efsdoimp_por_uf | empresa | ✔ |
| `efsdoimp_por_uf_obter` | obter | efsdoimp_por_uf | empresa, imposto, competencia, pdic_sim, sigla_da_uf | ✔ |
| `efsdoimp_por_uf_totais` | totais | efsdoimp_por_uf | empresa | ✔ |
| `efsdoimp_por_uf_es_consultar` | consultar | efsdoimp_por_uf_es | empresa | ✔ |
| `efsdoimp_por_uf_es_obter` | obter | efsdoimp_por_uf_es | empresa, imposto, competencia, pdic_sim, sigla_da_uf | ✔ |
| `efsdoimp_por_uf_es_totais` | totais | efsdoimp_por_uf_es | empresa | ✔ |
| `efsdoimp_por_uf_mg_consultar` | consultar | efsdoimp_por_uf_mg | empresa | ✔ |
| `efsdoimp_por_uf_mg_obter` | obter | efsdoimp_por_uf_mg | empresa, imposto, competencia, pdic_sim, sigla_da_uf | ✔ |
| `efsdoimp_por_uf_mg_totais` | totais | efsdoimp_por_uf_mg | empresa | ✔ |
| `efsdoimp_por_uf_por_nota_consultar` | consultar | efsdoimp_por_uf_por_nota | empresa | ✔ |
| `efsdoimp_por_uf_por_nota_obter` | obter | efsdoimp_por_uf_por_nota | empresa, imposto, competencia, pdic_sim, sigla_da_uf, codigo_nota, tipo_do_documento | ✔ |
| `efsdoimp_por_uf_por_nota_totais` | totais | efsdoimp_por_uf_por_nota | empresa | ✔ |
| `efsdoimp_por_uf_rj_consultar` | consultar | efsdoimp_por_uf_rj | empresa | ✔ |
| `efsdoimp_por_uf_rj_obter` | obter | efsdoimp_por_uf_rj | empresa, imposto, competencia, pdic_sim, sigla_da_uf | ✔ |
| `efsdoimp_por_uf_rj_totais` | totais | efsdoimp_por_uf_rj | empresa | ✔ |
| `efsdoimp_por_uf_sp_consultar` | consultar | efsdoimp_por_uf_sp | empresa | ✔ |
| `efsdoimp_por_uf_sp_obter` | obter | efsdoimp_por_uf_sp | empresa, imposto, competencia, pdic_sim, sigla_da_uf | ✔ |
| `efsdoimp_por_uf_sp_totais` | totais | efsdoimp_por_uf_sp | empresa | ✔ |
| `efsdoimp_receita_impostos_majoracao_consultar` | consultar | efsdoimp_receita_impostos_majoracao | empresa | ✔ |
| `efsdoimp_receita_impostos_majoracao_obter` | obter | efsdoimp_receita_impostos_majoracao | empresa, imposto, periodo, periodicidade, periodo_origem_base_majorada, aliquota_da_base_de_calculo_csll, aliquota_da_base_de_calculo_irpj | ✔ |
| `efsdoimp_receita_impostos_majoracao_totais` | totais | efsdoimp_receita_impostos_majoracao | empresa | ✔ |
| `efsdoimp_scp_consultar` | consultar | efsdoimp_scp | empresa | ✔ |
| `efsdoimp_scp_obter` | obter | efsdoimp_scp | empresa, imposto, competencia, pdic_sim, sequencial_do_scp | ✔ |
| `efsdoimp_scp_totais` | totais | efsdoimp_scp | empresa | ✔ |
| `efsdoimp_scp_csll_csll_retido_consultar` | consultar | efsdoimp_scp_csll_csll_retido | empresa | ✔ |
| `efsdoimp_scp_csll_csll_retido_obter` | obter | efsdoimp_scp_csll_csll_retido | empresa, imposto, data, periodicidade, scp, natureza, periodo_de_apuracao_da_retencao | ✔ |
| `efsdoimp_scp_csll_csll_retido_totais` | totais | efsdoimp_scp_csll_csll_retido | empresa | ✔ |
| `efsdoimp_simples_nacional_base_negativa_consultar` | consultar | efsdoimp_simples_nacional_base_negativa | empresa | ✔ |
| `efsdoimp_simples_nacional_base_negativa_totais` | totais | efsdoimp_simples_nacional_base_negativa | empresa | ✔ |
| `efsdoimp_simples_nacional_controle_base_negativa__7f31_consultar` | consultar | efsdoimp_simples_nacional_controle_base_negativa_devolucao_secundaria | empresa | ✔ |
| `efsdoimp_simples_nacional_controle_base_negativa_dev_7f31_totais` | totais | efsdoimp_simples_nacional_controle_base_negativa_devolucao_secundaria | empresa | ✔ |
| `efsdoimp_simples_nacional_detalhamento_consultar` | consultar | efsdoimp_simples_nacional_detalhamento | empresa | ✔ |
| `efsdoimp_simples_nacional_prorrogacao_consultar` | consultar | efsdoimp_simples_nacional_prorrogacao | empresa | ✔ |
| `efsdoimp_simples_nacional_prorrogacao_obter` | obter | efsdoimp_simples_nacional_prorrogacao | empresa, imposto, periodo, periodicidade, tipo_prorrogacao_1_federais_2_estaduais, vencimento, prorrogacao_f_federais_e_estaduais_m_mun, filial | ✔ |
| `efsdoimp_simples_nacional_prorrogacao_totais` | totais | efsdoimp_simples_nacional_prorrogacao | empresa | ✔ |
| `efsdoimp_simples_nacional_salao_parceiro_consultar` | consultar | efsdoimp_simples_nacional_salao_parceiro | empresa | ✔ |
| `efsdoimp_simples_nacional_salao_parceiro_totais` | totais | efsdoimp_simples_nacional_salao_parceiro | empresa | ✔ |
| `efsdoimp_subtri_por_uf_ba_consultar` | consultar | efsdoimp_subtri_por_uf_ba | empresa | ✔ |
| `efsdoimp_subtri_por_uf_ba_obter` | obter | efsdoimp_subtri_por_uf_ba | empresa, imposto, competencia, periodicidade, sigla_da_uf, recolhimento | ✔ |
| `efsdoimp_subtri_por_uf_df_consultar` | consultar | efsdoimp_subtri_por_uf_df | empresa | ✔ |
| `efsdoimp_subtri_por_uf_df_obter` | obter | efsdoimp_subtri_por_uf_df | empresa, imposto, competencia, periodicidade, sigla_da_uf, recolhimento | ✔ |
| `efsdoimp_subtri_por_uf_df_totais` | totais | efsdoimp_subtri_por_uf_df | empresa | ✔ |
| `efsdoimp_subtri_por_uf_es_consultar` | consultar | efsdoimp_subtri_por_uf_es | empresa | ✔ |
| `efsdoimp_subtri_por_uf_es_obter` | obter | efsdoimp_subtri_por_uf_es | empresa, imposto, competencia, periodicidade, sigla_da_uf, recolhimento | ✔ |
| `efsdoimp_subtri_por_uf_mg_consultar` | consultar | efsdoimp_subtri_por_uf_mg | empresa | ✔ |
| `efsdoimp_subtri_por_uf_mg_obter` | obter | efsdoimp_subtri_por_uf_mg | empresa, imposto, competencia, pdic_sim, sigla_da_uf, recolhimento | ✔ |
| `efsdoimp_subtri_por_uf_mg_totais` | totais | efsdoimp_subtri_por_uf_mg | empresa | ✔ |
| `efsdoimp_subtri_por_uf_pa_consultar` | consultar | efsdoimp_subtri_por_uf_pa | empresa | ✔ |
| `efsdoimp_subtri_por_uf_pa_obter` | obter | efsdoimp_subtri_por_uf_pa | empresa, imposto, competencia, periodicidade, sigla_da_uf, recolhimento | ✔ |
| `efsdoimp_subtri_por_uf_pi_consultar` | consultar | efsdoimp_subtri_por_uf_pi | empresa | ✔ |
| `efsdoimp_subtri_por_uf_pi_obter` | obter | efsdoimp_subtri_por_uf_pi | empresa, imposto, competencia, periodicidade, sigla_da_uf, recolhimento | ✔ |
| `efsdoimp_subtri_por_uf_pr_consultar` | consultar | efsdoimp_subtri_por_uf_pr | empresa | ✔ |
| `efsdoimp_subtri_por_uf_pr_obter` | obter | efsdoimp_subtri_por_uf_pr | empresa, imposto, competencia, pdic_sim, sigla_da_uf, recolhimento | ✔ |
| `efsdoimp_subtri_por_uf_pr_totais` | totais | efsdoimp_subtri_por_uf_pr | empresa | ✔ |
| `efsdoimp_subtri_por_uf_rj_consultar` | consultar | efsdoimp_subtri_por_uf_rj | empresa | ✔ |
| `efsdoimp_subtri_por_uf_rj_obter` | obter | efsdoimp_subtri_por_uf_rj | empresa, imposto, competencia, periodicidade, sigla_da_uf, recolhimento | ✔ |
| `efsdoimp_subtri_por_uf_rj_totais` | totais | efsdoimp_subtri_por_uf_rj | empresa | ✔ |
| `efsdoimp_subtri_por_uf_rj_compl_rest_icms_st_consultar` | consultar | efsdoimp_subtri_por_uf_rj_compl_rest_icms_st | empresa | ✔ |
| `efsdoimp_subtri_por_uf_rj_compl_rest_icms_st_obter` | obter | efsdoimp_subtri_por_uf_rj_compl_rest_icms_st | empresa, imposto, competencia, periodicidade, sigla_da_uf, recolhimento | ✔ |
| `efsdoimp_subtri_por_uf_rj_compl_rest_icms_st_totais` | totais | efsdoimp_subtri_por_uf_rj_compl_rest_icms_st | empresa | ✔ |
| `efsdoimp_subtri_por_uf_sc_consultar` | consultar | efsdoimp_subtri_por_uf_sc | empresa | ✔ |
| `efsdoimp_subtri_por_uf_sc_obter` | obter | efsdoimp_subtri_por_uf_sc | empresa, imposto, competencia, periodicidade, sigla_da_uf, recolhimento | ✔ |
| `efsdoimp_subtri_por_uf_sc_totais` | totais | efsdoimp_subtri_por_uf_sc | empresa | ✔ |
| `efsdoimp_subtri_por_uf_se_consultar` | consultar | efsdoimp_subtri_por_uf_se | empresa | ✔ |
| `efsdoimp_subtri_por_uf_se_obter` | obter | efsdoimp_subtri_por_uf_se | empresa, imposto, competencia, periodicidade, sigla_da_uf, recolhimento | ✔ |
| `efsdoimp_subtri_por_uf_sp_consultar` | consultar | efsdoimp_subtri_por_uf_sp | empresa | ✔ |
| `efsdoimp_subtri_por_uf_sp_obter` | obter | efsdoimp_subtri_por_uf_sp | empresa, imposto, competencia, periodicidade, sigla_da_uf, recolhimento | ✔ |
| `efsdoimp_subtri_por_uf_sp_totais` | totais | efsdoimp_subtri_por_uf_sp | empresa | ✔ |
| `efsdoimp_subtri_por_uf_to_consultar` | consultar | efsdoimp_subtri_por_uf_to | empresa | ✔ |
| `efsdoimp_subtri_por_uf_to_obter` | obter | efsdoimp_subtri_por_uf_to | empresa, imposto, competencia, periodicidade, sigla_da_uf, recolhimento | ✔ |
| `efsdoimp_subtri_por_uf_to_totais` | totais | efsdoimp_subtri_por_uf_to | empresa | ✔ |
