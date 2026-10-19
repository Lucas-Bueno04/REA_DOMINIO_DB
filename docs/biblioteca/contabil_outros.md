# Módulo `contabil_outros`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `ctatendimento_lancto_catalogo_consultar` | consultar | ctatendimento_lancto_catalogo | empresa | ✔ |
| `ctatendimento_lancto_catalogo_obter` | obter | ctatendimento_lancto_catalogo | empresa, codigo_do_catalogo, codigo_sequencial_do_site | ✔ |
| `ctatendimento_lancto_catalogo_totais` | totais | ctatendimento_lancto_catalogo | empresa | ✔ |
| `ctatendimento_plano_contas_controle_websocket_consultar` | consultar | ctatendimento_plano_contas_controle_websocket | — | ✔ |
| `ctatendimento_plano_contas_controle_websocket_obter` | obter | ctatendimento_plano_contas_controle_websocket | data_do_pacote | ✔ |
| `ctcmv_apuracao_consultar` | consultar | ctcmv_apuracao | empresa | ✔ |
| `ctcmv_apuracao_obter` | obter | ctcmv_apuracao | empresa, codigo | ✔ |
| `ctcmv_apuracao_estoque_consultar` | consultar | ctcmv_apuracao_estoque | empresa | ✔ |
| `ctcmv_apuracao_estoque_obter` | obter | ctcmv_apuracao_estoque | empresa, codigo_apuracao, sequencial | ✔ |
| `ctcmv_apuracao_estoque_totais` | totais | ctcmv_apuracao_estoque | empresa | ✔ |
| `ctcmv_apuracao_lancto_consultar` | consultar | ctcmv_apuracao_lancto | empresa | ✔ |
| `ctcmv_apuracao_lancto_obter` | obter | ctcmv_apuracao_lancto | empresa, codigo_apuracao, empresa_do_lancamento_contabil, numero_do_lancamento_contabil | ✔ |
| `ctcoeficiente_formula_consultar` | consultar | ctcoeficiente_formula | — | ✔ |
| `ctcoeficiente_formula_obter` | obter | ctcoeficiente_formula | coeficiente_de_analise, codigo | ✔ |
| `ctcoeficiente_formula_totais` | totais | ctcoeficiente_formula | — | ✔ |
| `ctcoeficiente_formula_calculo_consultar` | consultar | ctcoeficiente_formula_calculo | — | ✔ |
| `ctcoeficiente_formula_calculo_obter` | obter | ctcoeficiente_formula_calculo | coeficiente, formula, codigo | ✔ |
| `ctcoeficiente_formula_calculo_conta_consultar` | consultar | ctcoeficiente_formula_calculo_conta | empresa | ✔ |
| `ctcoeficiente_formula_calculo_conta_obter` | obter | ctcoeficiente_formula_calculo_conta | empresa, coeficiente, formula, calculo, codigo | ✔ |
| `ctconciliacao_bancaria_consultar` | consultar | ctconciliacao_bancaria | empresa | ✔ |
| `ctconciliacao_bancaria_obter` | obter | ctconciliacao_bancaria | empresa, codigo, sequencial_da_conciliacao | ✔ |
| `ctconciliacao_bancaria_iceberg_consultar` | consultar | ctconciliacao_bancaria_iceberg | empresa | ✔ |
| `ctconciliacao_bancaria_iceberg_obter` | obter | ctconciliacao_bancaria_iceberg | empresa, codigo_da_conciliacao, item_da_conciliacao | ✔ |
| `ctconciliacao_conta_consultar` | consultar | ctconciliacao_conta | empresa | ✔ |
| `ctconciliacao_conta_obter` | obter | ctconciliacao_conta | empresa, conta_contabil | ✔ |
| `ctdere_codtrib_consultar` | consultar | ctdere_codtrib | — | ✔ |
| `ctdere_codtrib_obter` | obter | ctdere_codtrib | identificador_interno_do_codigo_de_tribu | ✔ |
| `ctdescricao_final_consultar` | consultar | ctdescricao_final | empresa | ✔ |
| `ctdescricao_final_obter` | obter | ctdescricao_final | empresa, codigo_do_demonstrativo_1_dre_2_dlpa_3_d | ✔ |
| `ctdirigentes_conselheiros_consultar` | consultar | ctdirigentes_conselheiros | empresa | ✔ |
| `ctdirigentes_conselheiros_obter` | obter | ctdirigentes_conselheiros | empresa, codigo | ✔ |
| `ctdirigentes_conselheiros_config_consultar` | consultar | ctdirigentes_conselheiros_config | empresa | ✔ |
| `ctdirigentes_conselheiros_config_obter` | obter | ctdirigentes_conselheiros_config | empresa, i_dirigente_conselheiro, i_configuracao | ✔ |
| `ctdocumentos_ole_consultar` | consultar | ctdocumentos_ole | — | ✔ |
| `ctdocumentos_ole_obter` | obter | ctdocumentos_ole | codigo | ✔ |
| `ctdocumentos_ole_modelos_consultar` | consultar | ctdocumentos_ole_modelos | — | ✔ |
| `ctdocumentos_ole_modelos_obter` | obter | ctdocumentos_ole_modelos | codigo, tipo | ✔ |
| `ctdocumentos_ole_tipo_consultar` | consultar | ctdocumentos_ole_tipo | — | ✔ |
| `ctdocumentos_ole_tipo_obter` | obter | ctdocumentos_ole_tipo | codigo | ✔ |
| `ctgrupo_ebitda_consultar` | consultar | ctgrupo_ebitda | empresa | ✔ |
| `ctgrupo_ebitda_obter` | obter | ctgrupo_ebitda | empresa, codigo | ✔ |
| `ctgrupo_ebitda_totais` | totais | ctgrupo_ebitda | empresa | ✔ |
| `ctgruposdlpa_valor_consultar` | consultar | ctgruposdlpa_valor | empresa | ✔ |
| `ctgruposdlpa_valor_obter` | obter | ctgruposdlpa_valor | empresa, codigo_da_estrutura_dlpa, sequencial | ✔ |
| `ctgruposdlpa_valor_totais` | totais | ctgruposdlpa_valor | empresa | ✔ |
| `ctgruposdmpl_tipolancto_consultar` | consultar | ctgruposdmpl_tipolancto | empresa | ✔ |
| `ctgruposdmpl_tipolancto_obter` | obter | ctgruposdmpl_tipolancto | empresa, grupo, tipo_de_lancamento | ✔ |
| `ctlanctolote_livro_rural_consultar` | consultar | ctlanctolote_livro_rural | empresa | ✔ |
| `ctlanctolote_livro_rural_obter` | obter | ctlanctolote_livro_rural | empresa, codigo_do_lote | ✔ |
| `ctlanctopadrao_contas_consultar` | consultar | ctlanctopadrao_contas | empresa | ✔ |
| `ctlanctopadrao_contas_obter` | obter | ctlanctopadrao_contas | empresa, lancamento_padrao, sequencial | ✔ |
| `ctlanctopadrao_contas_totais` | totais | ctlanctopadrao_contas | empresa | ✔ |
| `ctlista_bancos_banco_central_consultar` | consultar | ctlista_bancos_banco_central | — | ✔ |
| `ctlista_bancos_banco_central_obter` | obter | ctlista_bancos_banco_central | sequencial_do_banco | ✔ |
| `ctlivro_caixa_produtor_rural_leiaute_consultar` | consultar | ctlivro_caixa_produtor_rural_leiaute | — | ✔ |
| `ctlivro_caixa_produtor_rural_leiaute_obter` | obter | ctlivro_caixa_produtor_rural_leiaute | codigo_do_leiaute | ✔ |
| `ctnatureza_conta_consultar` | consultar | ctnatureza_conta | empresa | ✔ |
| `ctnatureza_conta_obter` | obter | ctnatureza_conta | empresa, filtro_ordem | ✔ |
| `ctnatureza_conta_bc_geral_consultar` | consultar | ctnatureza_conta_bc_geral | — | ✔ |
| `ctnatureza_conta_bc_geral_obter` | obter | ctnatureza_conta_bc_geral | codigo_da_tabela | ✔ |
| `ctocupacao_padrao_carne_leao_consultar` | consultar | ctocupacao_padrao_carne_leao | — | ✔ |
| `ctocupacao_padrao_carne_leao_obter` | obter | ctocupacao_padrao_carne_leao | sequencial | ✔ |
| `ctorigem_lancamento_consultar` | consultar | ctorigem_lancamento | — | ✔ |
| `ctorigem_lancamento_obter` | obter | ctorigem_lancamento | codigo_da_origem | ✔ |
| `ctrelacao_empresas_conglomerado_economico_consultar` | consultar | ctrelacao_empresas_conglomerado_economico | empresa | ✔ |
| `ctrelacao_empresas_conglomerado_economico_obter` | obter | ctrelacao_empresas_conglomerado_economico | empresa, sequencial_conglomerado_economico | ✔ |
| `ctscp_selecionada_consultar` | consultar | ctscp_selecionada | empresa | ✔ |
| `ctselecao_conta_redutora_consultar` | consultar | ctselecao_conta_redutora | empresa | ✔ |
| `ctselecao_conta_redutora_obter` | obter | ctselecao_conta_redutora | empresa, sequencial_da_conta_redutora, codigo_da_conta_contabil | ✔ |
| `ctselecao_scp_consultar` | consultar | ctselecao_scp | empresa | ✔ |
| `ctselecao_scp_obter` | obter | ctselecao_scp | empresa, sequencial, usuario | ✔ |
| `ctselecao_scp_opcao_consultar` | consultar | ctselecao_scp_opcao | empresa | ✔ |
| `ctselecao_scp_opcao_obter` | obter | ctselecao_scp_opcao | empresa, usuario | ✔ |
| `laparmto_anos_consultar` | consultar | laparmto_anos | empresa | ✔ |
| `laparmto_anos_obter` | obter | laparmto_anos | empresa, ano | ✔ |
| `lradicao_conta_consultar` | consultar | lradicao_conta | empresa | ✔ |
| `lradicao_conta_obter` | obter | lradicao_conta | empresa, adicao, sequencial | ✔ |
| `lrbase_negativa_parte_b_consultar` | consultar | lrbase_negativa_parte_b | empresa | ✔ |
| `lrbase_negativa_parte_b_obter` | obter | lrbase_negativa_parte_b | empresa, codigo | ✔ |
| `lrexclusao_conta_consultar` | consultar | lrexclusao_conta | empresa | ✔ |
| `lrexclusao_conta_obter` | obter | lrexclusao_conta | empresa, exclusao, sequencial | ✔ |
| `lrganho_conta_consultar` | consultar | lrganho_conta | empresa | ✔ |
| `lrganho_conta_obter` | obter | lrganho_conta | empresa, ganho, sequencial | ✔ |
| `lrincentivo_fiscal_consultar` | consultar | lrincentivo_fiscal | empresa | ✔ |
| `lrincentivo_fiscal_obter` | obter | lrincentivo_fiscal | empresa, codigo | ✔ |
| `lrintegracao_contabil_lancto_consultar` | consultar | lrintegracao_contabil_lancto | empresa | ✔ |
| `lrintegracao_contabil_lancto_obter` | obter | lrintegracao_contabil_lancto | empresa, sequencial, empresa_do_lancamento_contabil, numero_do_lancamento_contabil | ✔ |
| `lropcao_calculo_consultar` | consultar | lropcao_calculo | empresa | ✔ |
| `lropcao_calculo_obter` | obter | lropcao_calculo | empresa, codigo | ✔ |
| `lroperacao_receita_consultar` | consultar | lroperacao_receita | empresa | ✔ |
| `lroperacao_receita_obter` | obter | lroperacao_receita | empresa, codigo | ✔ |
| `lroperacao_receita_acumulador_consultar` | consultar | lroperacao_receita_acumulador | empresa | ✔ |
| `lroperacao_receita_acumulador_obter` | obter | lroperacao_receita_acumulador | empresa, operacoes_de_receita, sequencial | ✔ |
| `lroperacao_receita_conta_contabil_consultar` | consultar | lroperacao_receita_conta_contabil | empresa | ✔ |
| `lroperacao_receita_conta_contabil_obter` | obter | lroperacao_receita_conta_contabil | empresa, operacoes_de_receita, sequencial | ✔ |
| `lrpagamento_imposto_consultar` | consultar | lrpagamento_imposto | empresa | ✔ |
| `lrpagamento_imposto_obter` | obter | lrpagamento_imposto | empresa, competencia, imposto_c_contribuicao_social_i_irpj, tipo_de_calculo_r_real_e_estimado, sequencial_da_parcela, numero_da_parcela, sequencial, ajuste_anual | ✔ |
| `lrpagamento_imposto_totais` | totais | lrpagamento_imposto | empresa | ✔ |
| `lrpagamento_imposto_lancto_consultar` | consultar | lrpagamento_imposto_lancto | empresa | ✔ |
| `lrpagamento_imposto_lancto_obter` | obter | lrpagamento_imposto_lancto | empresa, competencia, imposto_c_contribuicao_social_i_irpj, tipo_de_calculo_r_real_e_estimado, sequencial_da_parcela, numero_da_parcela, sequencial_do_pagamento, empresa_do_lancamento_contabil, numero_do_lancamento_contabil, ajuste_anual | ✔ |
| `lrparametro_saldo_inicial_base_negativa_consultar` | consultar | lrparametro_saldo_inicial_base_negativa | empresa | ✔ |
| `lrparametro_saldo_inicial_base_negativa_obter` | obter | lrparametro_saldo_inicial_base_negativa | empresa, sequencial | ✔ |
| `lrparametro_saldo_inicial_base_negativa_totais` | totais | lrparametro_saldo_inicial_base_negativa | empresa | ✔ |
| `lrparametro_saldo_inicial_parte_b_consultar` | consultar | lrparametro_saldo_inicial_parte_b | empresa | ✔ |
| `lrparametro_saldo_inicial_parte_b_obter` | obter | lrparametro_saldo_inicial_parte_b | empresa, sequencial | ✔ |
| `lrparametro_saldo_inicial_parte_b_totais` | totais | lrparametro_saldo_inicial_parte_b | empresa | ✔ |
| `lrparametro_vigencia_consultar` | consultar | lrparametro_vigencia | empresa | ✔ |
| `lrparametro_vigencia_obter` | obter | lrparametro_vigencia | empresa, vigencia | ✔ |
| `lrparametro_vigencia_totais` | totais | lrparametro_vigencia | empresa | ✔ |
| `lrparcela_imposto_consultar` | consultar | lrparcela_imposto | empresa | ✔ |
| `lrparcela_imposto_obter` | obter | lrparcela_imposto | empresa, competencia, imposto_c_contribuicao_social_i_irpj, tipo_de_calculo_r_real_e_estimado, sequencial_da_parcela, numero_da_parcela, ajuste_anual | ✔ |
| `lrparcela_imposto_totais` | totais | lrparcela_imposto | empresa | ✔ |
| `lrreceita_bruta_consultar` | consultar | lrreceita_bruta | empresa | ✔ |
| `lrreceita_bruta_obter` | obter | lrreceita_bruta | empresa, codigo | ✔ |
| `lrreceita_bruta_item_consultar` | consultar | lrreceita_bruta_item | empresa | ✔ |
| `lrreceita_bruta_item_obter` | obter | lrreceita_bruta_item | empresa, codigo_receita_bruta, sequencial | ✔ |
| `lrreceita_bruta_item_totais` | totais | lrreceita_bruta_item | empresa | ✔ |
| `pabens_consultar` | consultar | pabens | empresa | ✔ |
| `pabens_obter` | obter | pabens | empresa, codigo | ✔ |
| `pabens_totais` | totais | pabens | empresa | ✔ |
| `pmbaixa_lancto_consultar` | consultar | pmbaixa_lancto | empresa | ✔ |
| `pmbaixa_lancto_obter` | obter | pmbaixa_lancto | empresa, baixa, empresa_do_lancamento_contabil, numero_do_lancamento_contabil | ✔ |
| `pmbem_consultar` | consultar | pmbem | empresa | ✔ |
| `pmbem_obter` | obter | pmbem | empresa, codigo | ✔ |
| `pmbem_totais` | totais | pmbem | empresa | ✔ |
| `pmcomplemento_historico_contabil_consultar` | consultar | pmcomplemento_historico_contabil | empresa | ✔ |
| `pmcomplemento_historico_contabil_obter` | obter | pmcomplemento_historico_contabil | empresa, tipo_1_depreciacao_fiscal_2_depreciacao | ✔ |
| `pmconfiguracao_integracao_consultar` | consultar | pmconfiguracao_integracao | empresa | ✔ |
| `pmconfiguracao_integracao_obter` | obter | pmconfiguracao_integracao | empresa, codigo | ✔ |
| `pmconfiguracao_integracao_conta_consultar` | consultar | pmconfiguracao_integracao_conta | empresa | ✔ |
| `pmconfiguracao_integracao_conta_obter` | obter | pmconfiguracao_integracao_conta | empresa, codigo, centro_de_custo | ✔ |
| `pmconfiguracao_integracao_conta_totais` | totais | pmconfiguracao_integracao_conta | empresa | ✔ |
| `pmconta_patrimonial_consultar` | consultar | pmconta_patrimonial | empresa | ✔ |
| `pmconta_patrimonial_obter` | obter | pmconta_patrimonial | empresa, codigo | ✔ |
| `pmconta_patrimonial_totais` | totais | pmconta_patrimonial | empresa | ✔ |
| `pmconta_patrimonial_taxa_consultar` | consultar | pmconta_patrimonial_taxa | empresa | ✔ |
| `pmconta_patrimonial_taxa_obter` | obter | pmconta_patrimonial_taxa | empresa, conta_patrimonial, sequencial | ✔ |
| `pmgrupo_contabil_consultar` | consultar | pmgrupo_contabil | empresa | ✔ |
| `pmgrupo_contabil_obter` | obter | pmgrupo_contabil | empresa, codigo | ✔ |
| `pminformacao_calculo_credito_icms_consultar` | consultar | pminformacao_calculo_credito_icms | empresa | ✔ |
| `pminformacao_calculo_credito_icms_obter` | obter | pminformacao_calculo_credito_icms | empresa, competencia, mansal_ou_quinzenal_0_mensal_1_primeira | ✔ |
| `pminformacao_calculo_credito_icms_totais` | totais | pminformacao_calculo_credito_icms | empresa | ✔ |
| `pmparametro_vigencia_consultar` | consultar | pmparametro_vigencia | empresa | ✔ |
| `pmparametro_vigencia_obter` | obter | pmparametro_vigencia | empresa, vigencia | ✔ |
| `pmparametro_vigencia_totais` | totais | pmparametro_vigencia | empresa | ✔ |
| `pmtabela_bem_historico_tipo_consultar` | consultar | pmtabela_bem_historico_tipo | — | ✔ |
| `pmtabela_bem_historico_tipo_obter` | obter | pmtabela_bem_historico_tipo | codigo | ✔ |
