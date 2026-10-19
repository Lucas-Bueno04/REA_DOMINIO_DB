# Módulo `fiscal_tabela`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `eftabela_ac_codigo_item_ipm_consultar` | consultar | eftabela_ac_codigo_item_ipm | — | ✔ |
| `eftabela_ac_codigo_item_ipm_obter` | obter | eftabela_ac_codigo_item_ipm | sequencial | ✔ |
| `eftabela_al_codigo_item_ipm_consultar` | consultar | eftabela_al_codigo_item_ipm | — | ✔ |
| `eftabela_al_codigo_item_ipm_obter` | obter | eftabela_al_codigo_item_ipm | sequencial | ✔ |
| `eftabela_al_quadro_iii_dac_consultar` | consultar | eftabela_al_quadro_iii_dac | — | ✔ |
| `eftabela_al_quadro_iii_dac_obter` | obter | eftabela_al_quadro_iii_dac | sequencial | ✔ |
| `eftabela_aliquota_efetiva_icms_st_at_consultar` | consultar | eftabela_aliquota_efetiva_icms_st_at | empresa | ✔ |
| `eftabela_aliquota_efetiva_icms_st_at_obter` | obter | eftabela_aliquota_efetiva_icms_st_at | empresa, sequencial_da_tabela | ✔ |
| `eftabela_aliquota_efetiva_icms_st_at_vigencia_consultar` | consultar | eftabela_aliquota_efetiva_icms_st_at_vigencia | empresa | ✔ |
| `eftabela_aliquota_efetiva_icms_st_at_vigencia_obter` | obter | eftabela_aliquota_efetiva_icms_st_at_vigencia | empresa, sequencial_da_tabela, vigencia | ✔ |
| `eftabela_aliquota_efetiva_icms_st_at_vigencia_ata_336b_consultar` | consultar | eftabela_aliquota_efetiva_icms_st_at_vigencia_atacadista | empresa | ✔ |
| `eftabela_aliquota_efetiva_icms_st_at_vigencia_atacadista_obter` | obter | eftabela_aliquota_efetiva_icms_st_at_vigencia_atacadista | empresa, sequencial_da_tabela, vigencia, sequencial | ✔ |
| `eftabela_aliquota_efetiva_icms_st_at_vigencia_pro_4e11_consultar` | consultar | eftabela_aliquota_efetiva_icms_st_at_vigencia_produto_informatica | empresa | ✔ |
| `eftabela_aliquota_efetiva_icms_st_at_vigencia_produto_4e11_obter` | obter | eftabela_aliquota_efetiva_icms_st_at_vigencia_produto_informatica | empresa, sequencial_da_tabela, vigencia, sequencial | ✔ |
| `eftabela_aliquota_efetiva_icms_st_at_vigencia_var_ad62_consultar` | consultar | eftabela_aliquota_efetiva_icms_st_at_vigencia_varejista | empresa | ✔ |
| `eftabela_aliquota_efetiva_icms_st_at_vigencia_varejista_obter` | obter | eftabela_aliquota_efetiva_icms_st_at_vigencia_varejista | empresa, sequencial_da_tabela, vigencia, sequencial | ✔ |
| `eftabela_aliquota_icms_consultar` | consultar | eftabela_aliquota_icms | empresa | ✔ |
| `eftabela_aliquota_icms_obter` | obter | eftabela_aliquota_icms | empresa, sequencial | ✔ |
| `eftabela_aliquota_icms_original_consultar` | consultar | eftabela_aliquota_icms_original | — | ✔ |
| `eftabela_aliquota_icms_original_obter` | obter | eftabela_aliquota_icms_original | sequencial, uf_origem | ✔ |
| `eftabela_aliquota_icms_vigencia_consultar` | consultar | eftabela_aliquota_icms_vigencia | empresa | ✔ |
| `eftabela_aliquota_icms_vigencia_obter` | obter | eftabela_aliquota_icms_vigencia | empresa, sequencial, vigencia | ✔ |
| `eftabela_aliquota_icms_vigencia_aliquota_consultar` | consultar | eftabela_aliquota_icms_vigencia_aliquota | empresa | ✔ |
| `eftabela_aliquota_icms_vigencia_aliquota_obter` | obter | eftabela_aliquota_icms_vigencia_aliquota | empresa, sequencial, vigencia, uf_origem | ✔ |
| `eftabela_am_sub_apuracao_consultar` | consultar | eftabela_am_sub_apuracao | — | ✔ |
| `eftabela_am_sub_apuracao_obter` | obter | eftabela_am_sub_apuracao | sequencial | ✔ |
| `eftabela_am_sub_apuracao_totais` | totais | eftabela_am_sub_apuracao | — | ✔ |
| `eftabela_atividade_economica_consultar` | consultar | eftabela_atividade_economica | — | ✔ |
| `eftabela_atividade_economica_obter` | obter | eftabela_atividade_economica | codigo_da_atividade_economica | ✔ |
| `eftabela_atividade_gestta_processos_consultar` | consultar | eftabela_atividade_gestta_processos | — | ✔ |
| `eftabela_atividade_gestta_processos_obter` | obter | eftabela_atividade_gestta_processos | sequencial | ✔ |
| `eftabela_atividade_gestta_processos_totais` | totais | eftabela_atividade_gestta_processos | — | ✔ |
| `eftabela_atividade_servico_folha_consultar` | consultar | eftabela_atividade_servico_folha | — | ✔ |
| `eftabela_atividade_servico_folha_obter` | obter | eftabela_atividade_servico_folha | codigo_da_atividade | ✔ |
| `eftabela_atividade_servico_folha_vigencia_consultar` | consultar | eftabela_atividade_servico_folha_vigencia | — | ✔ |
| `eftabela_atividade_servico_folha_vigencia_obter` | obter | eftabela_atividade_servico_folha_vigencia | codigo_da_atividade, vigencia | ✔ |
| `eftabela_ba_codigo_item_ipm_consultar` | consultar | eftabela_ba_codigo_item_ipm | — | ✔ |
| `eftabela_ba_codigo_item_ipm_obter` | obter | eftabela_ba_codigo_item_ipm | sequencial | ✔ |
| `eftabela_ba_dmd_consultar` | consultar | eftabela_ba_dmd | — | ✔ |
| `eftabela_ba_dmd_obter` | obter | eftabela_ba_dmd | codigo_do_dmd | ✔ |
| `eftabela_ba_valores_declaratorios_icms_consultar` | consultar | eftabela_ba_valores_declaratorios_icms | — | ✔ |
| `eftabela_ba_valores_declaratorios_icms_obter` | obter | eftabela_ba_valores_declaratorios_icms | codigo_do_ajuste | ✔ |
| `eftabela_cest_consultar` | consultar | eftabela_cest | — | ✔ |
| `eftabela_cest_obter` | obter | eftabela_cest | codigo_cest | ✔ |
| `eftabela_cest_ncm_consultar` | consultar | eftabela_cest_ncm | — | ✔ |
| `eftabela_cest_ncm_obter` | obter | eftabela_cest_ncm | codigo_cest, codigo_ncm | ✔ |
| `eftabela_cfps_consultar` | consultar | eftabela_cfps | — | ✔ |
| `eftabela_cfps_obter` | obter | eftabela_cfps | codigo | ✔ |
| `eftabela_classe_consumo_consultar` | consultar | eftabela_classe_consumo | — | ✔ |
| `eftabela_classe_consumo_obter` | obter | eftabela_classe_consumo | codigo_sequencial | ✔ |
| `eftabela_classe_enquadramento_ipi_consultar` | consultar | eftabela_classe_enquadramento_ipi | — | ✔ |
| `eftabela_classe_enquadramento_ipi_obter` | obter | eftabela_classe_enquadramento_ipi | sequencial | ✔ |
| `eftabela_classificacao_servicos_consultar` | consultar | eftabela_classificacao_servicos | — | ✔ |
| `eftabela_classificacao_servicos_obter` | obter | eftabela_classificacao_servicos | codigo | ✔ |
| `eftabela_classificacao_sped_consultar` | consultar | eftabela_classificacao_sped | — | ✔ |
| `eftabela_classificacao_sped_obter` | obter | eftabela_classificacao_sped | codigo | ✔ |
| `eftabela_classificacao_tributaria_ibs_cbs_consultar` | consultar | eftabela_classificacao_tributaria_ibs_cbs | — | ✔ |
| `eftabela_classificacao_tributaria_ibs_cbs_obter` | obter | eftabela_classificacao_tributaria_ibs_cbs | sequencial_da_tabela, vigencia_da_tabela, classificacao_tributaria | ✔ |
| `eftabela_classificacao_tributaria_is_consultar` | consultar | eftabela_classificacao_tributaria_is | — | ✔ |
| `eftabela_classificacao_tributaria_is_obter` | obter | eftabela_classificacao_tributaria_is | sequencial_tabela_is, vigencia, codigo_classificacao_tributaria_is | ✔ |
| `eftabela_codigo_base_calculo_credito_consultar` | consultar | eftabela_codigo_base_calculo_credito | — | ✔ |
| `eftabela_codigo_base_calculo_credito_obter` | obter | eftabela_codigo_base_calculo_credito | codigo | ✔ |
| `eftabela_codigo_contribuicao_social_apurada_consultar` | consultar | eftabela_codigo_contribuicao_social_apurada | — | ✔ |
| `eftabela_codigo_contribuicao_social_apurada_obter` | obter | eftabela_codigo_contribuicao_social_apurada | codigo | ✔ |
| `eftabela_codigo_tipo_credito_consultar` | consultar | eftabela_codigo_tipo_credito | — | ✔ |
| `eftabela_codigo_tipo_credito_obter` | obter | eftabela_codigo_tipo_credito | codigo | ✔ |
| `eftabela_codigo_tributacao_consultar` | consultar | eftabela_codigo_tributacao | — | ✔ |
| `eftabela_codigo_tributacao_obter` | obter | eftabela_codigo_tributacao | codigo | ✔ |
| `eftabela_credito_presumido_consultar` | consultar | eftabela_credito_presumido | empresa | ✔ |
| `eftabela_credito_presumido_obter` | obter | eftabela_credito_presumido | empresa, vigencia, tabela | ✔ |
| `eftabela_credito_presumido_faixa_consultar` | consultar | eftabela_credito_presumido_faixa | empresa | ✔ |
| `eftabela_credito_presumido_faixa_obter` | obter | eftabela_credito_presumido_faixa | empresa, vigencia, aliquota, tabela, operacao_i_interna_e_interestadual_a_amb | ✔ |
| `eftabela_credito_presumido_faixa_mg_consultar` | consultar | eftabela_credito_presumido_faixa_mg | — | ✔ |
| `eftabela_credito_presumido_faixa_mg_obter` | obter | eftabela_credito_presumido_faixa_mg | vigencia, tabela_1_credito_presumido_importacao_ar, aliquota | ✔ |
| `eftabela_credito_presumido_faixa_original_consultar` | consultar | eftabela_credito_presumido_faixa_original | — | ✔ |
| `eftabela_credito_presumido_faixa_original_obter` | obter | eftabela_credito_presumido_faixa_original | vigencia, tabela, aliquota | ✔ |
| `eftabela_credito_presumido_faixa_pr_consultar` | consultar | eftabela_credito_presumido_faixa_pr | — | ✔ |
| `eftabela_credito_presumido_faixa_pr_obter` | obter | eftabela_credito_presumido_faixa_pr | vigencia, aliquota, tabela_1_feijao_2_textil_3_cafe_4_arroz | ✔ |
| `eftabela_credito_presumido_faixa_rs_consultar` | consultar | eftabela_credito_presumido_faixa_rs | — | ✔ |
| `eftabela_credito_presumido_faixa_rs_obter` | obter | eftabela_credito_presumido_faixa_rs | vigencia, tabela, aliquota | ✔ |
| `eftabela_credito_presumido_mg_consultar` | consultar | eftabela_credito_presumido_mg | — | ✔ |
| `eftabela_credito_presumido_mg_obter` | obter | eftabela_credito_presumido_mg | vigencia, tabela_1_credito_presumido_importacao_ar | ✔ |
| `eftabela_credito_presumido_original_consultar` | consultar | eftabela_credito_presumido_original | — | ✔ |
| `eftabela_credito_presumido_original_obter` | obter | eftabela_credito_presumido_original | vigencia, tabela | ✔ |
| `eftabela_credito_presumido_pr_consultar` | consultar | eftabela_credito_presumido_pr | — | ✔ |
| `eftabela_credito_presumido_pr_obter` | obter | eftabela_credito_presumido_pr | vigencia, tabela_1_feijao_2_textil_3_cafe_4_arroz | ✔ |
| `eftabela_credito_presumido_rs_consultar` | consultar | eftabela_credito_presumido_rs | — | ✔ |
| `eftabela_credito_presumido_rs_obter` | obter | eftabela_credito_presumido_rs | vigencia, tabela | ✔ |
| `eftabela_cst_consultar` | consultar | eftabela_cst | — | ✔ |
| `eftabela_cst_obter` | obter | eftabela_cst | sequencial | ✔ |
| `eftabela_cst_icms_vigencia_consultar` | consultar | eftabela_cst_icms_vigencia | — | ✔ |
| `eftabela_cst_icms_vigencia_obter` | obter | eftabela_cst_icms_vigencia | codigo_cst, vigencia | ✔ |
| `eftabela_cst_ipi_vigencia_consultar` | consultar | eftabela_cst_ipi_vigencia | — | ✔ |
| `eftabela_cst_ipi_vigencia_obter` | obter | eftabela_cst_ipi_vigencia | codigo_cst, vigencia | ✔ |
| `eftabela_cst_simples_nacional_vigencia_consultar` | consultar | eftabela_cst_simples_nacional_vigencia | — | ✔ |
| `eftabela_cst_simples_nacional_vigencia_obter` | obter | eftabela_cst_simples_nacional_vigencia | codigo_cst, vigencia | ✔ |
| `eftabela_cst_vigencia_consultar` | consultar | eftabela_cst_vigencia | — | ✔ |
| `eftabela_cst_vigencia_obter` | obter | eftabela_cst_vigencia | codigo_sequencial | ✔ |
| `eftabela_dacon_tipo_produto_consultar` | consultar | eftabela_dacon_tipo_produto | — | ✔ |
| `eftabela_dacon_tipo_produto_obter` | obter | eftabela_dacon_tipo_produto | sequencial | ✔ |
| `eftabela_dcip_consultar` | consultar | eftabela_dcip | — | ✔ |
| `eftabela_dcip_obter` | obter | eftabela_dcip | codigo_dcip, tipo_1_credito_presumido_2_estorno_de_de | ✔ |
| `eftabela_dere_concursos_consultar` | consultar | eftabela_dere_concursos | — | ✔ |
| `eftabela_dere_concursos_obter` | obter | eftabela_dere_concursos | sequencial | ✔ |
| `eftabela_dere_planos_saude_consultar` | consultar | eftabela_dere_planos_saude | — | ✔ |
| `eftabela_dere_planos_saude_obter` | obter | eftabela_dere_planos_saude | sequencial | ✔ |
| `eftabela_dere_servicos_financeiros_consultar` | consultar | eftabela_dere_servicos_financeiros | — | ✔ |
| `eftabela_dere_servicos_financeiros_obter` | obter | eftabela_dere_servicos_financeiros | sequencial | ✔ |
| `eftabela_dere_uf_consultar` | consultar | eftabela_dere_uf | — | ✔ |
| `eftabela_dere_uf_obter` | obter | eftabela_dere_uf | sequencial | ✔ |
| `eftabela_df_valores_declaratorios_icms_consultar` | consultar | eftabela_df_valores_declaratorios_icms | — | ✔ |
| `eftabela_df_valores_declaratorios_icms_obter` | obter | eftabela_df_valores_declaratorios_icms | sequencial | ✔ |
| `eftabela_dif_formato_papel_consultar` | consultar | eftabela_dif_formato_papel | — | ✔ |
| `eftabela_dif_formato_papel_obter` | obter | eftabela_dif_formato_papel | sequencial | ✔ |
| `eftabela_dif_periodicidade_consultar` | consultar | eftabela_dif_periodicidade | — | ✔ |
| `eftabela_dif_periodicidade_obter` | obter | eftabela_dif_periodicidade | sequencial | ✔ |
| `eftabela_dif_unidade_medida_consultar` | consultar | eftabela_dif_unidade_medida | — | ✔ |
| `eftabela_dif_unidade_medida_obter` | obter | eftabela_dif_unidade_medida | sequencial | ✔ |
| `eftabela_diferencial_aliquota_ma_consultar` | consultar | eftabela_diferencial_aliquota_ma | — | ✔ |
| `eftabela_diferencial_aliquota_ma_obter` | obter | eftabela_diferencial_aliquota_ma | vigencia | ✔ |
| `eftabela_diferencial_aliquota_ma_faixa_consultar` | consultar | eftabela_diferencial_aliquota_ma_faixa | — | ✔ |
| `eftabela_diferencial_aliquota_ma_faixa_obter` | obter | eftabela_diferencial_aliquota_ma_faixa | vigencia, faixa | ✔ |
| `eftabela_dispositivo_credito_presumido_rs_consultar` | consultar | eftabela_dispositivo_credito_presumido_rs | — | ✔ |
| `eftabela_dispositivo_credito_presumido_rs_obter` | obter | eftabela_dispositivo_credito_presumido_rs | codigo_do_dispositivo_do_credito_presumi | ✔ |
| `eftabela_es_codigo_item_ipm_consultar` | consultar | eftabela_es_codigo_item_ipm | — | ✔ |
| `eftabela_es_codigo_item_ipm_obter` | obter | eftabela_es_codigo_item_ipm | sequencial | ✔ |
| `eftabela_es_sub_apuracao_consultar` | consultar | eftabela_es_sub_apuracao | — | ✔ |
| `eftabela_es_sub_apuracao_obter` | obter | eftabela_es_sub_apuracao | sequencial | ✔ |
| `eftabela_es_valores_declaratorios_icms_consultar` | consultar | eftabela_es_valores_declaratorios_icms | — | ✔ |
| `eftabela_es_valores_declaratorios_icms_obter` | obter | eftabela_es_valores_declaratorios_icms | sequencial | ✔ |
| `eftabela_esocial_tipo_servico_consultar` | consultar | eftabela_esocial_tipo_servico | — | ✔ |
| `eftabela_esocial_tipo_servico_obter` | obter | eftabela_esocial_tipo_servico | sequencial_do_tipo_de_servico | ✔ |
| `eftabela_especie_servico_transporte_consultar` | consultar | eftabela_especie_servico_transporte | — | ✔ |
| `eftabela_especie_servico_transporte_obter` | obter | eftabela_especie_servico_transporte | modelo | ✔ |
| `eftabela_exclusoes_7_1_2_consultar` | consultar | eftabela_exclusoes_7_1_2 | — | ✔ |
| `eftabela_exclusoes_7_1_2_obter` | obter | eftabela_exclusoes_7_1_2 | codigo, vigencia | ✔ |
| `eftabela_finalidade_arquivo_consultar` | consultar | eftabela_finalidade_arquivo | — | ✔ |
| `eftabela_finalidade_arquivo_obter` | obter | eftabela_finalidade_arquivo | codigo | ✔ |
| `eftabela_genero_mercadoria_consultar` | consultar | eftabela_genero_mercadoria | — | ✔ |
| `eftabela_genero_mercadoria_obter` | obter | eftabela_genero_mercadoria | codigo | ✔ |
| `eftabela_gnre_avulsa_detalhamento_consultar` | consultar | eftabela_gnre_avulsa_detalhamento | — | ✔ |
| `eftabela_gnre_avulsa_detalhamento_obter` | obter | eftabela_gnre_avulsa_detalhamento | codigo_do_detalhamento_da_receita | ✔ |
| `eftabela_gnre_avulsa_documentos_origem_consultar` | consultar | eftabela_gnre_avulsa_documentos_origem | — | ✔ |
| `eftabela_gnre_avulsa_documentos_origem_obter` | obter | eftabela_gnre_avulsa_documentos_origem | codigo_do_documento_de_origem_da_receita | ✔ |
| `eftabela_gnre_avulsa_produtos_consultar` | consultar | eftabela_gnre_avulsa_produtos | — | ✔ |
| `eftabela_gnre_avulsa_produtos_obter` | obter | eftabela_gnre_avulsa_produtos | codigo_do_produto_da_receitar | ✔ |
| `eftabela_gnre_avulsa_receita_consultar` | consultar | eftabela_gnre_avulsa_receita | — | ✔ |
| `eftabela_gnre_avulsa_receita_obter` | obter | eftabela_gnre_avulsa_receita | codigo_da_receita | ✔ |
| `eftabela_go_dispositivo_credito_consultar` | consultar | eftabela_go_dispositivo_credito | — | ✔ |
| `eftabela_go_dispositivo_credito_obter` | obter | eftabela_go_dispositivo_credito | dispositivo_do_credito | ✔ |
| `eftabela_go_valores_declaratorios_icms_consultar` | consultar | eftabela_go_valores_declaratorios_icms | — | ✔ |
| `eftabela_go_valores_declaratorios_icms_obter` | obter | eftabela_go_valores_declaratorios_icms | sequencial | ✔ |
| `eftabela_grupo_st_estoque_rs_consultar` | consultar | eftabela_grupo_st_estoque_rs | — | ✔ |
| `eftabela_grupo_st_estoque_rs_obter` | obter | eftabela_grupo_st_estoque_rs | codigo | ✔ |
| `eftabela_icms_st_carga_media_consultar` | consultar | eftabela_icms_st_carga_media | empresa | ✔ |
| `eftabela_icms_st_carga_media_obter` | obter | eftabela_icms_st_carga_media | empresa, sequencial, data | ✔ |
| `eftabela_icms_st_carga_media_padrao_consultar` | consultar | eftabela_icms_st_carga_media_padrao | — | ✔ |
| `eftabela_icms_st_carga_media_padrao_obter` | obter | eftabela_icms_st_carga_media_padrao | sequencial_item | ✔ |
| `eftabela_icms_st_carga_media_vigencia_consultar` | consultar | eftabela_icms_st_carga_media_vigencia | empresa | ✔ |
| `eftabela_icms_st_carga_media_vigencia_obter` | obter | eftabela_icms_st_carga_media_vigencia | empresa, sequencial, data, sequencial_item | ✔ |
| `eftabela_ma_codigo_item_ipm_consultar` | consultar | eftabela_ma_codigo_item_ipm | — | ✔ |
| `eftabela_ma_codigo_item_ipm_obter` | obter | eftabela_ma_codigo_item_ipm | sequencial | ✔ |
| `eftabela_marca_grupo_bebida_consultar` | consultar | eftabela_marca_grupo_bebida | — | ✔ |
| `eftabela_marca_grupo_bebida_obter` | obter | eftabela_marca_grupo_bebida | codigo, tabela | ✔ |
| `eftabela_mg_codigo_item_ipm_consultar` | consultar | eftabela_mg_codigo_item_ipm | — | ✔ |
| `eftabela_mg_codigo_item_ipm_obter` | obter | eftabela_mg_codigo_item_ipm | sequencial | ✔ |
| `eftabela_mg_credito_presumido_consultar` | consultar | eftabela_mg_credito_presumido | — | ✔ |
| `eftabela_mg_credito_presumido_obter` | obter | eftabela_mg_credito_presumido | sequencial | ✔ |
| `eftabela_mg_credito_presumido_produto_consultar` | consultar | eftabela_mg_credito_presumido_produto | — | ✔ |
| `eftabela_mg_credito_presumido_produto_obter` | obter | eftabela_mg_credito_presumido_produto | sequencial_do_tipo_de_credito_presumido, sequencial_do_tipo_do_produto | ✔ |
| `eftabela_mg_incentivo_ret_consultar` | consultar | eftabela_mg_incentivo_ret | empresa | ✔ |
| `eftabela_mg_incentivo_ret_obter` | obter | eftabela_mg_incentivo_ret | empresa, vigencia, sequencial_incentivo | ✔ |
| `eftabela_mg_incentivo_ret_faixas_consultar` | consultar | eftabela_mg_incentivo_ret_faixas | empresa | ✔ |
| `eftabela_mg_incentivo_ret_faixas_obter` | obter | eftabela_mg_incentivo_ret_faixas | empresa, vigencia, sequencial_incentivo_faixa, sequencial_incentivo | ✔ |
| `eftabela_mg_sub_apuracao_consultar` | consultar | eftabela_mg_sub_apuracao | — | ✔ |
| `eftabela_mg_sub_apuracao_obter` | obter | eftabela_mg_sub_apuracao | sequencial | ✔ |
| `eftabela_motivo_desoneracao_icms_consultar` | consultar | eftabela_motivo_desoneracao_icms | — | ✔ |
| `eftabela_motivo_desoneracao_icms_obter` | obter | eftabela_motivo_desoneracao_icms | sequencial | ✔ |
| `eftabela_movaju_ajuste_sped_consultar` | consultar | eftabela_movaju_ajuste_sped | — | ✔ |
| `eftabela_movaju_ajuste_sped_obter` | obter | eftabela_movaju_ajuste_sped | codigo | ✔ |
| `eftabela_mt_ajustes_sped_consultar` | consultar | eftabela_mt_ajustes_sped | — | ✔ |
| `eftabela_mt_ajustes_sped_obter` | obter | eftabela_mt_ajustes_sped | sequencial | ✔ |
| `eftabela_mt_gia_meios_producao_consultar` | consultar | eftabela_mt_gia_meios_producao | — | ✔ |
| `eftabela_mt_gia_meios_producao_obter` | obter | eftabela_mt_gia_meios_producao | codigo_dos_meios_de_producao | ✔ |
| `eftabela_natureza_acao_consultar` | consultar | eftabela_natureza_acao | — | ✔ |
| `eftabela_natureza_acao_obter` | obter | eftabela_natureza_acao | origem_ajuste, natureza_da_acao | ✔ |
| `eftabela_natureza_acao_processo_referenciado_consultar` | consultar | eftabela_natureza_acao_processo_referenciado | — | ✔ |
| `eftabela_natureza_acao_processo_referenciado_obter` | obter | eftabela_natureza_acao_processo_referenciado | origem_do_processo, codigo_da_natureza_da_acao | ✔ |
| `eftabela_natureza_receita_consultar` | consultar | eftabela_natureza_receita | — | ✔ |
| `eftabela_natureza_receita_obter` | obter | eftabela_natureza_receita | codigo, cst | ✔ |
| `eftabela_pa_codigo_item_ipm_consultar` | consultar | eftabela_pa_codigo_item_ipm | — | ✔ |
| `eftabela_pa_codigo_item_ipm_obter` | obter | eftabela_pa_codigo_item_ipm | sequencial | ✔ |
| `eftabela_pb_recolhimento_feef_consultar` | consultar | eftabela_pb_recolhimento_feef | — | ✔ |
| `eftabela_pb_recolhimento_feef_obter` | obter | eftabela_pb_recolhimento_feef | sequencial | ✔ |
| `eftabela_pb_valores_declaratorios_icms_consultar` | consultar | eftabela_pb_valores_declaratorios_icms | — | ✔ |
| `eftabela_pb_valores_declaratorios_icms_obter` | obter | eftabela_pb_valores_declaratorios_icms | codigo_do_ajuste | ✔ |
| `eftabela_pe_ajuste_sef_consultar` | consultar | eftabela_pe_ajuste_sef | — | ✔ |
| `eftabela_pe_ajuste_sef_obter` | obter | eftabela_pe_ajuste_sef | codigo_sequencial | ✔ |
| `eftabela_pe_codigo_item_ipm_consultar` | consultar | eftabela_pe_codigo_item_ipm | — | ✔ |
| `eftabela_pe_codigo_item_ipm_obter` | obter | eftabela_pe_codigo_item_ipm | sequencial | ✔ |
| `eftabela_pe_natureza_operacao_consultar` | consultar | eftabela_pe_natureza_operacao | — | ✔ |
| `eftabela_pe_natureza_operacao_obter` | obter | eftabela_pe_natureza_operacao | codigo_sequencial | ✔ |
| `eftabela_percentual_mistura_combustiveis_consultar` | consultar | eftabela_percentual_mistura_combustiveis | empresa | ✔ |
| `eftabela_percentual_mistura_combustiveis_obter` | obter | eftabela_percentual_mistura_combustiveis | empresa, tipo_produto | ✔ |
| `eftabela_percentual_mistura_combustiveis_original_consultar` | consultar | eftabela_percentual_mistura_combustiveis_original | — | ✔ |
| `eftabela_percentual_mistura_combustiveis_original_obter` | obter | eftabela_percentual_mistura_combustiveis_original | tipo_produto | ✔ |
| `eftabela_percentual_mistura_combustiveis_vigencia_consultar` | consultar | eftabela_percentual_mistura_combustiveis_vigencia | empresa | ✔ |
| `eftabela_percentual_mistura_combustiveis_vigencia_obter` | obter | eftabela_percentual_mistura_combustiveis_vigencia | empresa, tipo_produto, vigencia | ✔ |
| `eftabela_percentual_mistura_combustiveis_vigencia_177a_consultar` | consultar | eftabela_percentual_mistura_combustiveis_vigencia_original | — | ✔ |
| `eftabela_piscofins_sped_tabela_consultar` | consultar | eftabela_piscofins_sped_tabela | — | ✔ |
| `eftabela_piscofins_sped_tabela_obter` | obter | eftabela_piscofins_sped_tabela | codigo | ✔ |
| `eftabela_planilha_cfe_consultar` | consultar | eftabela_planilha_cfe | — | ✔ |
| `eftabela_planilha_cfe_obter` | obter | eftabela_planilha_cfe | documento_1_entrada_2_saida | ✔ |
| `eftabela_planilha_stda_consultar` | consultar | eftabela_planilha_stda | — | ✔ |
| `eftabela_planilha_stda_obter` | obter | eftabela_planilha_stda | documento | ✔ |
| `eftabela_pr_codigo_item_ipm_consultar` | consultar | eftabela_pr_codigo_item_ipm | — | ✔ |
| `eftabela_pr_codigo_item_ipm_obter` | obter | eftabela_pr_codigo_item_ipm | sequencial | ✔ |
| `eftabela_pr_valores_declaratorios_icms_consultar` | consultar | eftabela_pr_valores_declaratorios_icms | — | ✔ |
| `eftabela_pr_valores_declaratorios_icms_obter` | obter | eftabela_pr_valores_declaratorios_icms | sequencial | ✔ |
| `eftabela_protege_dispositivo_consultar` | consultar | eftabela_protege_dispositivo | — | ✔ |
| `eftabela_protege_dispositivo_obter` | obter | eftabela_protege_dispositivo | codigo | ✔ |
| `eftabela_receitas_7_1_1_consultar` | consultar | eftabela_receitas_7_1_1 | — | ✔ |
| `eftabela_receitas_7_1_1_obter` | obter | eftabela_receitas_7_1_1 | codigo, vigencia | ✔ |
| `eftabela_receitas_7_1_3_consultar` | consultar | eftabela_receitas_7_1_3 | — | ✔ |
| `eftabela_receitas_7_1_3_obter` | obter | eftabela_receitas_7_1_3 | codigo, vigencia | ✔ |
| `eftabela_receitas_7_1_4_consultar` | consultar | eftabela_receitas_7_1_4 | — | ✔ |
| `eftabela_receitas_7_1_4_obter` | obter | eftabela_receitas_7_1_4 | codigo, vigencia | ✔ |
| `eftabela_recolhimento_sped_fiscal_consultar` | consultar | eftabela_recolhimento_sped_fiscal | — | ✔ |
| `eftabela_recolhimento_sped_fiscal_obter` | obter | eftabela_recolhimento_sped_fiscal | codigo_sequencial | ✔ |
| `eftabela_rj_codigo_item_ipm_consultar` | consultar | eftabela_rj_codigo_item_ipm | — | ✔ |
| `eftabela_rj_codigo_item_ipm_obter` | obter | eftabela_rj_codigo_item_ipm | sequencial | ✔ |
| `eftabela_rj_valores_declaratorios_icms_consultar` | consultar | eftabela_rj_valores_declaratorios_icms | — | ✔ |
| `eftabela_rj_valores_declaratorios_icms_obter` | obter | eftabela_rj_valores_declaratorios_icms | sequencial | ✔ |
| `eftabela_rn_codigo_item_ipm_consultar` | consultar | eftabela_rn_codigo_item_ipm | — | ✔ |
| `eftabela_rn_codigo_item_ipm_obter` | obter | eftabela_rn_codigo_item_ipm | sequencial | ✔ |
| `eftabela_rn_identificador_tarifa_consultar` | consultar | eftabela_rn_identificador_tarifa | — | ✔ |
| `eftabela_rn_identificador_tarifa_obter` | obter | eftabela_rn_identificador_tarifa | identificador | ✔ |
| `eftabela_rn_tributacao_consultar` | consultar | eftabela_rn_tributacao | — | ✔ |
| `eftabela_rn_tributacao_obter` | obter | eftabela_rn_tributacao | codigo_da_tributacao | ✔ |
| `eftabela_ro_ajuste_sped_fiscal_consultar` | consultar | eftabela_ro_ajuste_sped_fiscal | — | ✔ |
| `eftabela_ro_ajuste_sped_fiscal_obter` | obter | eftabela_ro_ajuste_sped_fiscal | sequencial | ✔ |
| `eftabela_rs_codigo_item_ipm_consultar` | consultar | eftabela_rs_codigo_item_ipm | — | ✔ |
| `eftabela_rs_codigo_item_ipm_obter` | obter | eftabela_rs_codigo_item_ipm | sequencial | ✔ |
| `eftabela_rs_credito_presumido_produto_consultar` | consultar | eftabela_rs_credito_presumido_produto | — | ✔ |
| `eftabela_rs_credito_presumido_produto_obter` | obter | eftabela_rs_credito_presumido_produto | codigo_credito_presumido, codigo_tipo_produto | ✔ |
| `eftabela_rs_transferencia_credito_consultar` | consultar | eftabela_rs_transferencia_credito | — | ✔ |
| `eftabela_rs_transferencia_credito_obter` | obter | eftabela_rs_transferencia_credito | codigo_ajuste | ✔ |
| `eftabela_rs_utilizacao_credito_consultar` | consultar | eftabela_rs_utilizacao_credito | — | ✔ |
| `eftabela_rs_utilizacao_credito_obter` | obter | eftabela_rs_utilizacao_credito | sequencial | ✔ |
| `eftabela_rs_valores_declaratorios_icms_consultar` | consultar | eftabela_rs_valores_declaratorios_icms | — | ✔ |
| `eftabela_rs_valores_declaratorios_icms_obter` | obter | eftabela_rs_valores_declaratorios_icms | codigo_do_ajuste | ✔ |
| `eftabela_sc_codigo_item_ipm_consultar` | consultar | eftabela_sc_codigo_item_ipm | — | ✔ |
| `eftabela_sc_codigo_item_ipm_obter` | obter | eftabela_sc_codigo_item_ipm | sequencial | ✔ |
| `eftabela_sc_credito_presumido_consultar` | consultar | eftabela_sc_credito_presumido | — | ✔ |
| `eftabela_sc_credito_presumido_obter` | obter | eftabela_sc_credito_presumido | sequencial | ✔ |
| `eftabela_sc_credito_presumido_produto_consultar` | consultar | eftabela_sc_credito_presumido_produto | — | ✔ |
| `eftabela_sc_credito_presumido_produto_obter` | obter | eftabela_sc_credito_presumido_produto | sequencial_do_tipo_de_credito_presumido, sequencial_do_tipo_do_produto | ✔ |
| `eftabela_sc_valores_declaratorios_icms_consultar` | consultar | eftabela_sc_valores_declaratorios_icms | — | ✔ |
| `eftabela_sc_valores_declaratorios_icms_obter` | obter | eftabela_sc_valores_declaratorios_icms | sequencial | ✔ |
| `eftabela_servicos_consultar` | consultar | eftabela_servicos | — | ✔ |
| `eftabela_servicos_obter` | obter | eftabela_servicos | codigo | ✔ |
| `eftabela_simp_operacao_consultar` | consultar | eftabela_simp_operacao | — | ✔ |
| `eftabela_simp_operacao_obter` | obter | eftabela_simp_operacao | sequencial_da_operacao | ✔ |
| `eftabela_simp_recipiente_glp_consultar` | consultar | eftabela_simp_recipiente_glp | — | ✔ |
| `eftabela_simp_recipiente_glp_obter` | obter | eftabela_simp_recipiente_glp | codigo | ✔ |
| `eftabela_simp_serie_consultar` | consultar | eftabela_simp_serie | — | ✔ |
| `eftabela_simp_serie_obter` | obter | eftabela_simp_serie | serie | ✔ |
| `eftabela_simples_nacional_anexo_consultar` | consultar | eftabela_simples_nacional_anexo | — | ✔ |
| `eftabela_simples_nacional_anexo_obter` | obter | eftabela_simples_nacional_anexo | anexo, vigencia | ✔ |
| `eftabela_simples_nacional_estadual_consultar` | consultar | eftabela_simples_nacional_estadual | — | ✔ |
| `eftabela_simples_nacional_estadual_obter` | obter | eftabela_simples_nacional_estadual | sigla_da_uf, vigencia, anexo, secao, tabela, numero_da_faixa, porte_e_epp_m_me_n_normal_t_todos | ✔ |
| `eftabela_simples_nacional_estadual_totais` | totais | eftabela_simples_nacional_estadual | — | ✔ |
| `eftabela_simples_nacional_federal_consultar` | consultar | eftabela_simples_nacional_federal | — | ✔ |
| `eftabela_simples_nacional_federal_obter` | obter | eftabela_simples_nacional_federal | vigencia, numero_da_faixa, anexo, secao, tabela | ✔ |
| `eftabela_simples_nacional_federal_totais` | totais | eftabela_simples_nacional_federal | — | ✔ |
| `eftabela_simples_nacional_mei_consultar` | consultar | eftabela_simples_nacional_mei | — | ✔ |
| `eftabela_simples_nacional_mei_obter` | obter | eftabela_simples_nacional_mei | vigencia | ✔ |
| `eftabela_simples_nacional_mei_totais` | totais | eftabela_simples_nacional_mei | — | ✔ |
| `eftabela_simples_nacional_municipal_consultar` | consultar | eftabela_simples_nacional_municipal | — | ✔ |
| `eftabela_simples_nacional_municipal_obter` | obter | eftabela_simples_nacional_municipal | codigo_federal_do_municipio, vigencia, numero_da_faixa, anexo, secao, tabela | ✔ |
| `eftabela_simples_nacional_municipal_totais` | totais | eftabela_simples_nacional_municipal | — | ✔ |
| `eftabela_simples_nacional_secao_consultar` | consultar | eftabela_simples_nacional_secao | — | ✔ |
| `eftabela_simples_nacional_secao_obter` | obter | eftabela_simples_nacional_secao | anexo, secao, vigencia | ✔ |
| `eftabela_simples_nacional_tabela_consultar` | consultar | eftabela_simples_nacional_tabela | — | ✔ |
| `eftabela_simples_nacional_tabela_obter` | obter | eftabela_simples_nacional_tabela | anexo, secao, tabela, vigencia | ✔ |
| `eftabela_siscomex_consultar` | consultar | eftabela_siscomex | — | ✔ |
| `eftabela_siscomex_obter` | obter | eftabela_siscomex | sequencial | ✔ |
| `eftabela_situacao_tributaria_consultar` | consultar | eftabela_situacao_tributaria | — | ✔ |
| `eftabela_situacao_tributaria_obter` | obter | eftabela_situacao_tributaria | codigo | ✔ |
| `eftabela_sp_codigo_item_ipm_consultar` | consultar | eftabela_sp_codigo_item_ipm | — | ✔ |
| `eftabela_sp_codigo_item_ipm_obter` | obter | eftabela_sp_codigo_item_ipm | sequencial | ✔ |
| `eftabela_sp_valores_declaratorios_icms_consultar` | consultar | eftabela_sp_valores_declaratorios_icms | — | ✔ |
| `eftabela_sp_valores_declaratorios_icms_obter` | obter | eftabela_sp_valores_declaratorios_icms | sequencial | ✔ |
| `eftabela_sub_apuracoes_prodepe_pe_consultar` | consultar | eftabela_sub_apuracoes_prodepe_pe | — | ✔ |
| `eftabela_sub_apuracoes_prodepe_pe_obter` | obter | eftabela_sub_apuracoes_prodepe_pe | sequencial | ✔ |
| `eftabela_suspensao_impostos_federais_motivo_suspensao_consultar` | consultar | eftabela_suspensao_impostos_federais_motivo_suspensao | — | ✔ |
| `eftabela_suspensao_impostos_federais_motivo_suspensao_obter` | obter | eftabela_suspensao_impostos_federais_motivo_suspensao | sequencial_do_motivo_da_suspencao | ✔ |
| `eftabela_tipo_conhecimento_consultar` | consultar | eftabela_tipo_conhecimento | — | ✔ |
| `eftabela_tipo_conhecimento_obter` | obter | eftabela_tipo_conhecimento | codigo | ✔ |
| `eftabela_tipo_receita_consultar` | consultar | eftabela_tipo_receita | — | ✔ |
| `eftabela_tipo_receita_obter` | obter | eftabela_tipo_receita | codigo_sequencial | ✔ |
| `eftabela_to_codigo_item_ipm_consultar` | consultar | eftabela_to_codigo_item_ipm | — | ✔ |
| `eftabela_to_codigo_item_ipm_obter` | obter | eftabela_to_codigo_item_ipm | sequencial | ✔ |
| `eftabela_veiculo_marca_consultar` | consultar | eftabela_veiculo_marca | — | ✔ |
| `eftabela_veiculo_marca_obter` | obter | eftabela_veiculo_marca | codigo | ✔ |
| `eftabela_vinculo_cclasstrib_vigencia_itens_exceca_2e9b_consultar` | consultar | eftabela_vinculo_cclasstrib_vigencia_itens_excecao_padrao | — | ✔ |
| `eftabela_vinculo_cclasstrib_vigencia_itens_excecao_padrao_obter` | obter | eftabela_vinculo_cclasstrib_vigencia_itens_excecao_padrao | vigencia, sequencial, excecao | ✔ |
| `eftabela_vinculo_cclasstrib_vigencia_itens_padrao_consultar` | consultar | eftabela_vinculo_cclasstrib_vigencia_itens_padrao | — | ✔ |
| `eftabela_vinculo_cclasstrib_vigencia_itens_padrao_obter` | obter | eftabela_vinculo_cclasstrib_vigencia_itens_padrao | vigencia_do_vinculo, sequencial_do_vinculo | ✔ |
| `eftabela_vinculo_cclasstrib_vigencia_padrao_consultar` | consultar | eftabela_vinculo_cclasstrib_vigencia_padrao | — | ✔ |
| `eftabela_vinculo_cclasstrib_vigencia_padrao_obter` | obter | eftabela_vinculo_cclasstrib_vigencia_padrao | vigencia_do_vinculo | ✔ |
| `eftabela_vinculo_credito_pis_cofins_consultar` | consultar | eftabela_vinculo_credito_pis_cofins | — | ✔ |
| `eftabela_vinculo_credito_pis_cofins_obter` | obter | eftabela_vinculo_credito_pis_cofins | vinculo_de_credito | ✔ |
| `eftabela_vinculo_ncm_nbs_cclasstrib_consultar` | consultar | eftabela_vinculo_ncm_nbs_cclasstrib | — | ✔ |
| `eftabela_vinculo_ncm_nbs_cclasstrib_obter` | obter | eftabela_vinculo_ncm_nbs_cclasstrib | sequencial_da_tabela, vigencia_do_vinculo, classificacao_tributaria, sequencial_do_vinculo | ✔ |
