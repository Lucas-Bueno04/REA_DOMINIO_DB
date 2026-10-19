# Módulo `fiscal_outros`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `atcontrole_tabela_selic_consultar` | consultar | atcontrole_tabela_selic | — | ✔ |
| `atjuros_icms_sp_consultar` | consultar | atjuros_icms_sp | — | ✔ |
| `atjuros_icms_sp_obter` | obter | atjuros_icms_sp | competencia | ✔ |
| `efajuste_piscofins_movimento_produto_consultar` | consultar | efajuste_piscofins_movimento_produto | empresa | ✔ |
| `efajuste_piscofins_movimento_produto_obter` | obter | efajuste_piscofins_movimento_produto | empresa, codigo | ✔ |
| `efajuste_piscofins_movimento_produto_totais` | totais | efajuste_piscofins_movimento_produto | empresa | ✔ |
| `efajuste_piscofins_movimento_produto_detalhamento_consultar` | consultar | efajuste_piscofins_movimento_produto_detalhamento | empresa | ✔ |
| `efajuste_piscofins_movimento_produto_detalhamento_obter` | obter | efajuste_piscofins_movimento_produto_detalhamento | empresa, codigo, sequencial | ✔ |
| `efajuste_piscofins_movimento_produto_detalhamento_totais` | totais | efajuste_piscofins_movimento_produto_detalhamento | empresa | ✔ |
| `efam_codigo_tributacao_produto_consultar` | consultar | efam_codigo_tributacao_produto | — | ✔ |
| `efam_codigo_tributacao_produto_obter` | obter | efam_codigo_tributacao_produto | sequencial, vigencia | ✔ |
| `efam_codigo_tributacao_produto_aliquota_consultar` | consultar | efam_codigo_tributacao_produto_aliquota | — | ✔ |
| `efam_codigo_tributacao_produto_aliquota_obter` | obter | efam_codigo_tributacao_produto_aliquota | sequencial, vigencia, sequencial_do_codigo | ✔ |
| `efam_codigo_tributacao_produto_aliquota_totais` | totais | efam_codigo_tributacao_produto_aliquota | — | ✔ |
| `efapuracao_empreendimento_imobiliario_poc_consultar` | consultar | efapuracao_empreendimento_imobiliario_poc | empresa | ✔ |
| `efapuracao_empreendimento_imobiliario_poc_obter` | obter | efapuracao_empreendimento_imobiliario_poc | empresa, empreendimento, competencia | ✔ |
| `efapuracao_empreendimento_imobiliario_poc_totais` | totais | efapuracao_empreendimento_imobiliario_poc | empresa | ✔ |
| `efbase_legal_to_consultar` | consultar | efbase_legal_to | — | ✔ |
| `efbase_legal_to_obter` | obter | efbase_legal_to | codigo, operacao | ✔ |
| `efclientes_alteracao_consultar` | consultar | efclientes_alteracao | empresa | ✔ |
| `efclientes_alteracao_obter` | obter | efclientes_alteracao | empresa, cliente, data_da_alteracao, campo_alterado_1_razao_social_2_endereco | ✔ |
| `efcnae_fortaleza_consultar` | consultar | efcnae_fortaleza | — | ✔ |
| `efcnae_fortaleza_obter` | obter | efcnae_fortaleza | codigo_cnae_fortaleza | ✔ |
| `efcodigo_recolhimento_am_consultar` | consultar | efcodigo_recolhimento_am | — | ✔ |
| `efcodigo_recolhimento_am_obter` | obter | efcodigo_recolhimento_am | codigo_da_receita | ✔ |
| `efcompensacao_imposto_federal_consultar` | consultar | efcompensacao_imposto_federal | empresa | ✔ |
| `efcompensacao_imposto_federal_obter` | obter | efcompensacao_imposto_federal | empresa, sequencial_da_compensacao | ✔ |
| `efcompensacao_imposto_federal_totais` | totais | efcompensacao_imposto_federal | empresa | ✔ |
| `efcompensacao_imposto_federal_compensacao_consultar` | consultar | efcompensacao_imposto_federal_compensacao | empresa | ✔ |
| `efcompensacao_imposto_federal_compensacao_obter` | obter | efcompensacao_imposto_federal_compensacao | empresa, sequencial_da_compensacao, sequencial | ✔ |
| `efcompensacao_imposto_federal_compensacao_totais` | totais | efcompensacao_imposto_federal_compensacao | empresa | ✔ |
| `efcompensacao_imposto_federal_lancto_consultar` | consultar | efcompensacao_imposto_federal_lancto | empresa | ✔ |
| `efcompensacao_imposto_federal_lancto_obter` | obter | efcompensacao_imposto_federal_lancto | empresa, numero_do_lancamento, empresa_da_compensacao, sequencial_da_compensacao | ✔ |
| `efcomplemento_cfop_cat_17_99_consultar` | consultar | efcomplemento_cfop_cat_17_99 | — | ✔ |
| `efcomplemento_cfop_cat_17_99_obter` | obter | efcomplemento_cfop_cat_17_99 | complemento_cfop_cat_17_99 | ✔ |
| `efconf_int_ctb_cont_prev_consultar` | consultar | efconf_int_ctb_cont_prev | empresa | ✔ |
| `efconf_int_ctb_cont_prev_obter` | obter | efconf_int_ctb_cont_prev | empresa, codigo_da_configuracao | ✔ |
| `efconf_int_ctb_cont_prev_vigencia_consultar` | consultar | efconf_int_ctb_cont_prev_vigencia | empresa | ✔ |
| `efconf_int_ctb_cont_prev_vigencia_obter` | obter | efconf_int_ctb_cont_prev_vigencia | empresa, codigo_da_configuracao, vigencia | ✔ |
| `efconf_int_ctb_cont_prev_vigencia_totais` | totais | efconf_int_ctb_cont_prev_vigencia | empresa | ✔ |
| `efcontrole_emissao_relatorio_consultar` | consultar | efcontrole_emissao_relatorio | empresa | ✔ |
| `efcontrole_emissao_relatorio_obter` | obter | efcontrole_emissao_relatorio | empresa, competencia, descricao_do_relatorio | ✔ |
| `efcupom_fiscal_eletronico_estoque_apuracao_estoque_consultar` | consultar | efcupom_fiscal_eletronico_estoque_apuracao_estoque | empresa | ✔ |
| `efcupom_fiscal_eletronico_estoque_apuracao_estoque_obter` | obter | efcupom_fiscal_eletronico_estoque_apuracao_estoque | empresa, codigo_do_cf_e, sequencial_do_estoque | ✔ |
| `efcupom_fiscal_eletronico_estoque_apuracao_estoque_totais` | totais | efcupom_fiscal_eletronico_estoque_apuracao_estoque | empresa | ✔ |
| `efcupom_fiscal_eletronico_estoque_total_consultar` | consultar | efcupom_fiscal_eletronico_estoque_total | empresa | ✔ |
| `efcupom_fiscal_eletronico_estoque_total_obter` | obter | efcupom_fiscal_eletronico_estoque_total | empresa, codigo_do_cf_e | ✔ |
| `efcupom_fiscal_eletronico_estoque_total_totais` | totais | efcupom_fiscal_eletronico_estoque_total | empresa | ✔ |
| `efcupom_fiscal_eletronico_pagamentos_consultar` | consultar | efcupom_fiscal_eletronico_pagamentos | empresa | ✔ |
| `efcupom_fiscal_eletronico_pagamentos_obter` | obter | efcupom_fiscal_eletronico_pagamentos | empresa, codigo_do_cf_e, numero_da_parcela, numero_do_pagamento | ✔ |
| `efcupom_fiscal_eletronico_pagamentos_totais` | totais | efcupom_fiscal_eletronico_pagamentos | empresa | ✔ |
| `efcupom_fiscal_eletronico_parcelas_consultar` | consultar | efcupom_fiscal_eletronico_parcelas | empresa | ✔ |
| `efcupom_fiscal_eletronico_parcelas_obter` | obter | efcupom_fiscal_eletronico_parcelas | empresa, codigo_do_cf_e, numero_da_parcela | ✔ |
| `efcupom_fiscal_eletronico_parcelas_totais` | totais | efcupom_fiscal_eletronico_parcelas | empresa | ✔ |
| `efd_reinf_retorno_arquivos_r2099_consultar` | consultar | efd_reinf_retorno_arquivos_r2099 | empresa | ✔ |
| `efd_reinf_retorno_arquivos_r2099_obter` | obter | efd_reinf_retorno_arquivos_r2099 | empresa, sequencial_envio, filial | ✔ |
| `efdarf_irrf_consultar` | consultar | efdarf_irrf | empresa | ✔ |
| `efdarf_irrf_obter` | obter | efdarf_irrf | empresa, imposto, competencia, periodicidade, sequencial_da_nota, sequencial_do_recolhimento | ✔ |
| `efdarf_irrf_totais` | totais | efdarf_irrf | empresa | ✔ |
| `efdarj_envio_arquivos_consultar` | consultar | efdarj_envio_arquivos | empresa | ✔ |
| `efdarj_envio_arquivos_obter` | obter | efdarj_envio_arquivos | empresa, codigo_sequencial_de_envio_dos_arquivos | ✔ |
| `efdarj_envio_arquivos_totais` | totais | efdarj_envio_arquivos | empresa | ✔ |
| `efdasn_economico_fiscais_consultar` | consultar | efdasn_economico_fiscais | empresa | ✔ |
| `efdasn_economico_fiscais_obter` | obter | efdasn_economico_fiscais | empresa, competencia, informativo, codigo_da_filial | ✔ |
| `efdasn_economico_fiscais_totais` | totais | efdasn_economico_fiscais | empresa | ✔ |
| `efdasn_mudanca_municipio_consultar` | consultar | efdasn_mudanca_municipio | empresa | ✔ |
| `efdasn_mudanca_municipio_obter` | obter | efdasn_mudanca_municipio | empresa, competencia, informativo, filial | ✔ |
| `efdasn_socios_consultar` | consultar | efdasn_socios | empresa | ✔ |
| `efdasn_socios_obter` | obter | efdasn_socios | empresa, data, socio, tipo_s_socio_a_administrador_r_represent, ano_do_informativo | ✔ |
| `efdasn_socios_totais` | totais | efdasn_socios | empresa | ✔ |
| `efdeducao_pis_cofins_consultar` | consultar | efdeducao_pis_cofins | empresa | ✔ |
| `efdeducao_pis_cofins_obter` | obter | efdeducao_pis_cofins | empresa, i_deducao | ✔ |
| `efdeducao_pis_cofins_totais` | totais | efdeducao_pis_cofins | empresa | ✔ |
| `efdeducao_pis_cofins_lancto_consultar` | consultar | efdeducao_pis_cofins_lancto | empresa | ✔ |
| `efdeducao_pis_cofins_lancto_obter` | obter | efdeducao_pis_cofins_lancto | empresa, codigo_da_deducao, numero_do_lancamento, empresa_do_ajuste_no_calculo_do_pis_cofi | ✔ |
| `efdesenvolve_media_consultar` | consultar | efdesenvolve_media | empresa | ✔ |
| `efdesenvolve_media_obter` | obter | efdesenvolve_media | empresa, sequencial, periodo | ✔ |
| `efdesenvolve_media_totais` | totais | efdesenvolve_media | empresa | ✔ |
| `efdespesa_plano_saude_consultar` | consultar | efdespesa_plano_saude | empresa | ✔ |
| `efdespesa_plano_saude_obter` | obter | efdespesa_plano_saude | empresa, codigo_da_despesa | ✔ |
| `efdespesa_plano_saude_totais` | totais | efdespesa_plano_saude | empresa | ✔ |
| `efdespesa_plano_saude_dependentes_consultar` | consultar | efdespesa_plano_saude_dependentes | empresa | ✔ |
| `efdespesa_plano_saude_dependentes_obter` | obter | efdespesa_plano_saude_dependentes | empresa, codigo_da_despesa, sequencial_dos_dependentes | ✔ |
| `efdespesa_plano_saude_dependentes_totais` | totais | efdespesa_plano_saude_dependentes | empresa | ✔ |
| `efdimob_outros_dados_ficha_intermediacao_consultar` | consultar | efdimob_outros_dados_ficha_intermediacao | empresa | ✔ |
| `efdimob_outros_dados_ficha_intermediacao_obter` | obter | efdimob_outros_dados_ficha_intermediacao | empresa, periodo_referencia, codigo_de_intermediacao | ✔ |
| `efdimob_outros_dados_ficha_intermediacao_totais` | totais | efdimob_outros_dados_ficha_intermediacao | empresa | ✔ |
| `efdimob_outros_dados_ficha_locacao_consultar` | consultar | efdimob_outros_dados_ficha_locacao | empresa | ✔ |
| `efdimob_outros_dados_ficha_locacao_obter` | obter | efdimob_outros_dados_ficha_locacao | empresa, periodo_referencia, codigo_da_locacao | ✔ |
| `efdimob_outros_dados_ficha_locacao_rendimentos_consultar` | consultar | efdimob_outros_dados_ficha_locacao_rendimentos | empresa | ✔ |
| `efdimob_outros_dados_ficha_locacao_rendimentos_obter` | obter | efdimob_outros_dados_ficha_locacao_rendimentos | empresa, periodo_referencia, codigo_da_locacao, codigo_do_rendimento | ✔ |
| `efdimob_outros_dados_ficha_locacao_rendimentos_totais` | totais | efdimob_outros_dados_ficha_locacao_rendimentos | empresa | ✔ |
| `efentradaspag_lancto_consultar` | consultar | efentradaspag_lancto | empresa | ✔ |
| `efentradaspag_lancto_obter` | obter | efentradaspag_lancto | empresa, numero_do_lancamento, empresa_do_pagamento, codigo_da_nota, data_do_pagamento, tipo_entp, numero_da_parcela, numero_do_pagamento_sequencial, grupo_do_lancamento | ✔ |
| `efespecificacao_am_consultar` | consultar | efespecificacao_am | — | ✔ |
| `efespecificacao_am_obter` | obter | efespecificacao_am | codigo | ✔ |
| `effornece_alteracao_consultar` | consultar | effornece_alteracao | empresa | ✔ |
| `effornece_alteracao_obter` | obter | effornece_alteracao | empresa, fornecedor, data_da_alteracao, campo_alterado_1_razao_social_2_endereco | ✔ |
| `effornece_dependentes_consultar` | consultar | effornece_dependentes | empresa | ✔ |
| `effornece_dependentes_obter` | obter | effornece_dependentes | empresa, codigo_do_fornecedor, sequencial | ✔ |
| `effornece_natureza_rendimento_consultar` | consultar | effornece_natureza_rendimento | empresa | ✔ |
| `effornece_natureza_rendimento_obter` | obter | effornece_natureza_rendimento | empresa, codigo_do_fornecedor, sequencial_da_natureza_de_rendimento | ✔ |
| `efgoinformacoes_ipm_consultar` | consultar | efgoinformacoes_ipm | — | ✔ |
| `efgoinformacoes_ipm_obter` | obter | efgoinformacoes_ipm | codigo | ✔ |
| `efimposto_padrao_consultar` | consultar | efimposto_padrao | — | ✔ |
| `efimposto_padrao_obter` | obter | efimposto_padrao | imposto, uf | ✔ |
| `efimposto_padrao_vigencia_consultar` | consultar | efimposto_padrao_vigencia | — | ✔ |
| `efimposto_padrao_vigencia_obter` | obter | efimposto_padrao_vigencia | codigo, uf, vigencia | ✔ |
| `efimposto_padrao_vigencia_totais` | totais | efimposto_padrao_vigencia | — | ✔ |
| `efimposto_padrao_vigencia_recolhimento_consultar` | consultar | efimposto_padrao_vigencia_recolhimento | — | ✔ |
| `efimposto_padrao_vigencia_recolhimento_obter` | obter | efimposto_padrao_vigencia_recolhimento | codigo, uf, vigencia, sequencial | ✔ |
| `efimposto_padrao_vigencia_recolhimento_totais` | totais | efimposto_padrao_vigencia_recolhimento | — | ✔ |
| `efincentivo_municipal_consultar` | consultar | efincentivo_municipal | — | ✔ |
| `efincentivo_municipal_obter` | obter | efincentivo_municipal | codigo_do_municipio, vigencia | ✔ |
| `efincentivo_municipal_totais` | totais | efincentivo_municipal | — | ✔ |
| `efincentivo_municipal_faixa_consultar` | consultar | efincentivo_municipal_faixa | — | ✔ |
| `efincentivo_municipal_faixa_obter` | obter | efincentivo_municipal_faixa | codigo_do_municipio, vigencia, faixa | ✔ |
| `efincentivo_municipal_faixa_totais` | totais | efincentivo_municipal_faixa | — | ✔ |
| `efincentivosmuni_faixas_consultar` | consultar | efincentivosmuni_faixas | — | ✔ |
| `efincentivosmuni_faixas_obter` | obter | efincentivosmuni_faixas | codigo_do_municipio_federal, sigla_do_estado, vigencia, sequencial | ✔ |
| `efincentivosmuni_faixas_totais` | totais | efincentivosmuni_faixas | — | ✔ |
| `efinformacoes_complementares_consultar` | consultar | efinformacoes_complementares | empresa | ✔ |
| `efinformacoes_complementares_obter` | obter | efinformacoes_complementares | empresa, codigo_da_informacao_complementar | ✔ |
| `efinformacoes_inventario_consultar` | consultar | efinformacoes_inventario | empresa | ✔ |
| `efinformacoes_inventario_obter` | obter | efinformacoes_inventario | empresa, competencia | ✔ |
| `eflancamentos_lucros_dividendos_tributaveis_consultar` | consultar | eflancamentos_lucros_dividendos_tributaveis | empresa | ✔ |
| `eflancamentos_lucros_dividendos_tributaveis_obter` | obter | eflancamentos_lucros_dividendos_tributaveis | empresa, codigo_de_lancamentos_de_lucros_e_divide | ✔ |
| `eflancamentos_lucros_dividendos_tributaveis_distr_8061_consultar` | consultar | eflancamentos_lucros_dividendos_tributaveis_distribuicao | empresa | ✔ |
| `eflancamentos_lucros_dividendos_tributaveis_distribuicao_obter` | obter | eflancamentos_lucros_dividendos_tributaveis_distribuicao | empresa, codigo_lancamentos_de_distribuicao_de_lu, sequencial | ✔ |
| `eflancamentos_lucros_dividendos_tributaveis_distribuicao_totais` | totais | eflancamentos_lucros_dividendos_tributaveis_distribuicao | empresa | ✔ |
| `eflocatarios_compradores_consultar` | consultar | eflocatarios_compradores | empresa | ✔ |
| `eflocatarios_compradores_obter` | obter | eflocatarios_compradores | empresa, codigo_do_locatorio_compradores | ✔ |
| `eflucros_dividendos_tributaveis_distribuicao_contas_consultar` | consultar | eflucros_dividendos_tributaveis_distribuicao_contas | empresa | ✔ |
| `eflucros_dividendos_tributaveis_distribuicao_contas_obter` | obter | eflucros_dividendos_tributaveis_distribuicao_contas | empresa, codigo_de_lancamento_de_lucros_e_dividen, sequencial_distribuicao, conta | ✔ |
| `eflucros_dividendos_tributaveis_distribuicao_cont_53c3_consultar` | consultar | eflucros_dividendos_tributaveis_distribuicao_contas_param | empresa | ✔ |
| `eflucros_dividendos_tributaveis_distribuicao_contas_param_obter` | obter | eflucros_dividendos_tributaveis_distribuicao_contas_param | empresa, codigo_de_lancamento_de_lucros_e_dividen, sequencial_distribuicao | ✔ |
| `eflucros_dividendos_tributaveis_distribuicao_contas_param_totais` | totais | eflucros_dividendos_tributaveis_distribuicao_contas_param | empresa | ✔ |
| `efmodelo_especie_consultar` | consultar | efmodelo_especie | — | ✔ |
| `efmodelo_especie_obter` | obter | efmodelo_especie | codigo_do_modelo_da_especie | ✔ |
| `efmovacu_compensacoes_consultar` | consultar | efmovacu_compensacoes | empresa | ✔ |
| `efmovacu_compensacoes_obter` | obter | efmovacu_compensacoes | empresa, codigo | ✔ |
| `efmovacu_compensacoes_totais` | totais | efmovacu_compensacoes | empresa | ✔ |
| `efmovacu_detalhamento_retencoes_consultar` | consultar | efmovacu_detalhamento_retencoes | empresa | ✔ |
| `efmovacu_detalhamento_retencoes_obter` | obter | efmovacu_detalhamento_retencoes | empresa, codigo_do_movimento_de_acumulador | ✔ |
| `efmovacu_detalhamento_retencoes_totais` | totais | efmovacu_detalhamento_retencoes | empresa | ✔ |
| `efmovacu_lancto_consultar` | consultar | efmovacu_lancto | empresa | ✔ |
| `efmovacu_lancto_obter` | obter | efmovacu_lancto | empresa, numero_do_lancamento, empresa_do_movimento, codigo_do_movimento | ✔ |
| `efmunicipio_es_dief_consultar` | consultar | efmunicipio_es_dief | — | ✔ |
| `efmunicipio_es_dief_obter` | obter | efmunicipio_es_dief | codigo_estadual_do_municipio | ✔ |
| `efmvvpro_cbs_iva_consultar` | consultar | efmvvpro_cbs_iva | empresa | ✔ |
| `efmvvpro_cbs_iva_obter` | obter | efmvvpro_cbs_iva | empresa, codigo, sequencial | ✔ |
| `efmvvpro_cbs_iva_totais` | totais | efmvvpro_cbs_iva | empresa | ✔ |
| `efmvvpro_federal_consultar` | consultar | efmvvpro_federal | empresa | ✔ |
| `efmvvpro_federal_obter` | obter | efmvvpro_federal | empresa, codigo_do_servico, numero_sequencial_do_estoque | ✔ |
| `efmvvpro_federal_totais` | totais | efmvvpro_federal | empresa | ✔ |
| `efmvvpro_ibs_iva_consultar` | consultar | efmvvpro_ibs_iva | empresa | ✔ |
| `efmvvpro_ibs_iva_obter` | obter | efmvvpro_ibs_iva | empresa, codigo, sequencial | ✔ |
| `efmvvpro_ibs_iva_totais` | totais | efmvvpro_ibs_iva | empresa | ✔ |
| `efnatureza_rendimentos_consultar` | consultar | efnatureza_rendimentos | — | ✔ |
| `efnatureza_rendimentos_obter` | obter | efnatureza_rendimentos | codigo_do_imposto, codigo_da_natureza_de_rendimento | ✔ |
| `efnatureza_rendimentos_isentos_consultar` | consultar | efnatureza_rendimentos_isentos | — | ✔ |
| `efnatureza_rendimentos_isentos_obter` | obter | efnatureza_rendimentos_isentos | codigo_da_natureza_de_rendimento | ✔ |
| `efonbalance_configuracoes_consultar` | consultar | efonbalance_configuracoes | — | ✔ |
| `efonbalance_configuracoes_obter` | obter | efonbalance_configuracoes | codigo_sequencial_das_configuracoes | ✔ |
| `efonbalance_empresas_consultar` | consultar | efonbalance_empresas | — | ✔ |
| `efonbalance_empresas_obter` | obter | efonbalance_empresas | codigo_sequencial_da_empresa_no_atendim | ✔ |
| `efonbalance_empresas_totais` | totais | efonbalance_empresas | — | ✔ |
| `efonbalance_empresas_historico_consultar` | consultar | efonbalance_empresas_historico | — | ✔ |
| `efonbalance_empresas_historico_obter` | obter | efonbalance_empresas_historico | codigo | ✔ |
| `efonbalance_empresas_historico_totais` | totais | efonbalance_empresas_historico | — | ✔ |
| `efoperadora_plano_saude_consultar` | consultar | efoperadora_plano_saude | empresa | ✔ |
| `efoperadora_plano_saude_obter` | obter | efoperadora_plano_saude | empresa, codigo_da_operadora_de_plano_de_saude | ✔ |
| `efoutras_deducoes_pis_cofins_consultar` | consultar | efoutras_deducoes_pis_cofins | empresa | ✔ |
| `efoutras_deducoes_pis_cofins_obter` | obter | efoutras_deducoes_pis_cofins | empresa, codigo_sequencial | ✔ |
| `efoutras_deducoes_pis_cofins_totais` | totais | efoutras_deducoes_pis_cofins | empresa | ✔ |
| `efoutros_creditos_piscofins_imobilizado_consultar` | consultar | efoutros_creditos_piscofins_imobilizado | empresa | ✔ |
| `efoutros_creditos_piscofins_imobilizado_obter` | obter | efoutros_creditos_piscofins_imobilizado | empresa, codigo | ✔ |
| `efoutros_creditos_piscofins_imobilizado_totais` | totais | efoutros_creditos_piscofins_imobilizado | empresa | ✔ |
| `efoutros_creditos_piscofins_imobilizado_base_piscofins_consultar` | consultar | efoutros_creditos_piscofins_imobilizado_base_piscofins | empresa | ✔ |
| `efoutros_creditos_piscofins_imobilizado_base_piscofins_obter` | obter | efoutros_creditos_piscofins_imobilizado_base_piscofins | empresa, codigo, imposto, tipo_de_credito | ✔ |
| `efoutros_creditos_piscofins_imobilizado_base_piscofins_totais` | totais | efoutros_creditos_piscofins_imobilizado_base_piscofins | empresa | ✔ |
| `efoutros_dados_planejamento_tributario_geral_consultar` | consultar | efoutros_dados_planejamento_tributario_geral | empresa | ✔ |
| `efoutros_dados_planejamento_tributario_geral_obter` | obter | efoutros_dados_planejamento_tributario_geral | empresa, competencia, informativo | ✔ |
| `efoutros_dados_planejamento_tributario_iva_consultar` | consultar | efoutros_dados_planejamento_tributario_iva | empresa | ✔ |
| `efoutros_dados_planejamento_tributario_iva_obter` | obter | efoutros_dados_planejamento_tributario_iva | empresa, competencia, informativo | ✔ |
| `efoutros_dados_planejamento_tributario_iva_totais` | totais | efoutros_dados_planejamento_tributario_iva | empresa | ✔ |
| `efpagimp_dados_pagamento_consultar` | consultar | efpagimp_dados_pagamento | empresa | ✔ |
| `efpagimp_dados_pagamento_obter` | obter | efpagimp_dados_pagamento | empresa, sequencial | ✔ |
| `efpagimp_dados_pagamento_totais` | totais | efpagimp_dados_pagamento | empresa | ✔ |
| `efpagimp_lancto_consultar` | consultar | efpagimp_lancto | empresa | ✔ |
| `efpagimp_lancto_obter` | obter | efpagimp_lancto | empresa, numero, empresa_do_pagamento, imposto, competencia, periodicidade, parcela, numero_da_baixa, grupo_do_lancamento, imposto_parcelado, sequencial_do_parcelamento, sequencial_do_parcelamento_parcela, sequencial_do_parcelamento_parcela_parce | ✔ |
| `efpagimp_publicar_documento_consultar` | consultar | efpagimp_publicar_documento | empresa | ✔ |
| `efpagimp_publicar_documento_obter` | obter | efpagimp_publicar_documento | empresa, sequencial | ✔ |
| `efpagimp_publicar_documento_totais` | totais | efpagimp_publicar_documento | empresa | ✔ |
| `efparcelar_imposto_consultar` | consultar | efparcelar_imposto | empresa | ✔ |
| `efparcelar_imposto_obter` | obter | efparcelar_imposto | empresa, competencia, codigo_do_imposto | ✔ |
| `efparcelar_imposto_totais` | totais | efparcelar_imposto | empresa | ✔ |
| `efperfil_contribuinte_consultar` | consultar | efperfil_contribuinte | empresa | ✔ |
| `efperfil_contribuinte_obter` | obter | efperfil_contribuinte | empresa, sequencial | ✔ |
| `efperiodo_trabalho_consultar` | consultar | efperiodo_trabalho | empresa | ✔ |
| `efperiodo_trabalho_usuario_consultar` | consultar | efperiodo_trabalho_usuario | empresa | ✔ |
| `efperiodo_trabalho_usuario_obter` | obter | efperiodo_trabalho_usuario | empresa, sequencial | ✔ |
| `efposse_produtos_competencia_consultar` | consultar | efposse_produtos_competencia | empresa | ✔ |
| `efposse_produtos_competencia_obter` | obter | efposse_produtos_competencia | empresa, codigo_da_posse | ✔ |
| `efposse_produtos_competencia_produtos_consultar` | consultar | efposse_produtos_competencia_produtos | empresa | ✔ |
| `efposse_produtos_competencia_produtos_obter` | obter | efposse_produtos_competencia_produtos | empresa, codigo_da_posse, produto | ✔ |
| `efposse_produtos_competencia_produtos_posse_consultar` | consultar | efposse_produtos_competencia_produtos_posse | empresa | ✔ |
| `efposse_produtos_competencia_produtos_posse_obter` | obter | efposse_produtos_competencia_produtos_posse | empresa, codigo_da_posse, produto, sequencial | ✔ |
| `efposse_produtos_competencia_produtos_posse_totais` | totais | efposse_produtos_competencia_produtos_posse | empresa | ✔ |
| `efproban_tabela_servico_consultar` | consultar | efproban_tabela_servico | — | ✔ |
| `efproban_tabela_servico_obter` | obter | efproban_tabela_servico | sequencial | ✔ |
| `efprofissional_habilitado_classe_consultar` | consultar | efprofissional_habilitado_classe | — | ✔ |
| `efprofissional_habilitado_classe_obter` | obter | efprofissional_habilitado_classe | codigo | ✔ |
| `efprofissional_habilitado_tabela_consultar` | consultar | efprofissional_habilitado_tabela | — | ✔ |
| `efprofissional_habilitado_tabela_obter` | obter | efprofissional_habilitado_tabela | municipio, classe_do_profissional_habilitado, vigencia | ✔ |
| `efprofissional_habilitado_tabela_faixa_consultar` | consultar | efprofissional_habilitado_tabela_faixa | — | ✔ |
| `efprofissional_habilitado_tabela_faixa_obter` | obter | efprofissional_habilitado_tabela_faixa | municipio, classe_do_profissional_habilitado, vigencia, faixa | ✔ |
| `efprofissional_habilitado_tabela_faixa_totais` | totais | efprofissional_habilitado_tabela_faixa | — | ✔ |
| `efregerando_lanctos_contabeis_consultar` | consultar | efregerando_lanctos_contabeis | empresa | ✔ |
| `efremetente_destinatario_consultar` | consultar | efremetente_destinatario | empresa | ✔ |
| `efremetente_destinatario_obter` | obter | efremetente_destinatario | empresa, sequencial | ✔ |
| `efrsgmb_anexo5_consultar` | consultar | efrsgmb_anexo5 | — | ✔ |
| `efrsgmb_anexo5_obter` | obter | efrsgmb_anexo5 | cfop, competencia | ✔ |
| `efsaidaspag_lancto_consultar` | consultar | efsaidaspag_lancto | empresa | ✔ |
| `efsaidaspag_lancto_obter` | obter | efsaidaspag_lancto | empresa, numero_do_lancamento, empresa_do_pagamento, codigo_da_nota, data_do_pagamento, tipo_1_normal_2_juros_3_multa_4_desconto, numero_da_parcela, numero_do_pagamento_sequencial, grupo_do_lancamento | ✔ |
| `efsaidaspar_pis_cofins_consultar` | consultar | efsaidaspar_pis_cofins | empresa | ✔ |
| `efsaidaspar_pis_cofins_obter` | obter | efsaidaspar_pis_cofins | empresa, codigo_da_saida, numero_da_parcela, sequencial, numero_do_pagamento_sequencial | ✔ |
| `efsaidaspar_pis_cofins_totais` | totais | efsaidaspar_pis_cofins | empresa | ✔ |
| `efsat_cf_e_consultar` | consultar | efsat_cf_e | empresa | ✔ |
| `efsat_cf_e_obter` | obter | efsat_cf_e | empresa, numero | ✔ |
| `efselecao_scp_consultar` | consultar | efselecao_scp | empresa | ✔ |
| `efselecao_scp_obter` | obter | efselecao_scp | empresa, sequencial, usuario | ✔ |
| `efservicospag_lancto_consultar` | consultar | efservicospag_lancto | empresa | ✔ |
| `efservicospag_lancto_obter` | obter | efservicospag_lancto | empresa, numero_do_lancamento, empresa_do_pagamento, codigo_da_nota, data_do_pagamento, tipo_1_normal_2_juros_3_multa_4_desconto, numero_da_parcela, numero_do_pagamento_sequencial, grupo_do_lancamento | ✔ |
| `efservicospar_pis_cofins_consultar` | consultar | efservicospar_pis_cofins | empresa | ✔ |
| `efservicospar_pis_cofins_obter` | obter | efservicospar_pis_cofins | empresa, codigo_do_servico, numero_da_parcela, sequencial, numero_do_pagamento_sequencial | ✔ |
| `efservicospar_pis_cofins_totais` | totais | efservicospar_pis_cofins | empresa | ✔ |
| `efsimples_nacional_folha_anterior_consultar` | consultar | efsimples_nacional_folha_anterior | empresa | ✔ |
| `efsimples_nacional_folha_anterior_obter` | obter | efsimples_nacional_folha_anterior | empresa, periodo | ✔ |
| `efsimples_nacional_folha_anterior_totais` | totais | efsimples_nacional_folha_anterior | empresa | ✔ |
| `efsimples_nacional_informacao_estadual_consultar` | consultar | efsimples_nacional_informacao_estadual | — | ✔ |
| `efsimples_nacional_informacao_estadual_obter` | obter | efsimples_nacional_informacao_estadual | codigo_do_estado, vigencia | ✔ |
| `efsp_produtos_consultar` | consultar | efsp_produtos | — | ✔ |
| `efsp_produtos_obter` | obter | efsp_produtos | codigo_do_produtos, estado | ✔ |
| `efsped_contas_analiticas_consultar` | consultar | efsped_contas_analiticas | empresa | ✔ |
| `efsped_contas_analiticas_obter` | obter | efsped_contas_analiticas | empresa, competencia, registro_1_c170_2_c510_3_d100_4_d500 | ✔ |
| `efsped_fiscal_e311_consultar` | consultar | efsped_fiscal_e311 | — | ✔ |
| `efsped_fiscal_e311_obter` | obter | efsped_fiscal_e311 | cod_aj_apur, uf | ✔ |
| `eftabelamuni_itens_consultar` | consultar | eftabelamuni_itens | — | ✔ |
| `eftabelamuni_itens_obter` | obter | eftabelamuni_itens | codigo_da_tabela_municipal, valor_do_item | ✔ |
