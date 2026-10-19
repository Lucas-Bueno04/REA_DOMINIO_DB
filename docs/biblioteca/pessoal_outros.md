# Módulo `pessoal_outros`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `foadvertencia_suspensao_consultar` | consultar | foadvertencia_suspensao | empresa | ✔ |
| `foadvertencia_suspensao_obter` | obter | foadvertencia_suspensao | empresa, codigo_do_empregado, data_da_advertencia_suspensao, sequencial | ✔ |
| `foadvertencia_suspensao_totais` | totais | foadvertencia_suspensao | empresa | ✔ |
| `foafastamentos_tipos_consultar` | consultar | foafastamentos_tipos | — | ✔ |
| `foafastamentos_tipos_obter` | obter | foafastamentos_tipos | codigo_do_afastamento | ✔ |
| `foagente_quimico_consultar` | consultar | foagente_quimico | — | ✔ |
| `foagente_quimico_obter` | obter | foagente_quimico | codigo_do_agente_quimico | ✔ |
| `foagentes_integracao_consultar` | consultar | foagentes_integracao | — | ✔ |
| `foagentes_integracao_obter` | obter | foagentes_integracao | codigo_do_agente_de_integracao | ✔ |
| `foaliquota_acidente_trabalho_cnae_consultar` | consultar | foaliquota_acidente_trabalho_cnae | — | ✔ |
| `foaliquota_acidente_trabalho_cnae_obter` | obter | foaliquota_acidente_trabalho_cnae | vigencia_cnae, codigo_cnae | ✔ |
| `foalteracao_retroativa_valor_rubricas_consultar` | consultar | foalteracao_retroativa_valor_rubricas | empresa | ✔ |
| `foalteracao_retroativa_valor_rubricas_obter` | obter | foalteracao_retroativa_valor_rubricas | empresa, codigo_do_empregado, codigo_do_evento, competencia_da_alteracao | ✔ |
| `foalteracao_retroativa_valor_rubricas_totais` | totais | foalteracao_retroativa_valor_rubricas | empresa | ✔ |
| `foalteracao_salarial_complementos_consultar` | consultar | foalteracao_salarial_complementos | empresa | ✔ |
| `foalteracao_salarial_complementos_obter` | obter | foalteracao_salarial_complementos | empresa, codigo_do_empregado, competencia_da_alteracao_salarial, tipo_da_alteracao_salarial_1_normal_2_va, origem_do_complemento_1_lancamento_de_ev, codigo_do_complemento_de_calculo | ✔ |
| `foambientes_trabalho_consultar` | consultar | foambientes_trabalho | empresa | ✔ |
| `foambientes_trabalho_obter` | obter | foambientes_trabalho | empresa, codigo_do_ambiente_de_trabalho | ✔ |
| `foambientes_trabalho_alteracao_consultar` | consultar | foambientes_trabalho_alteracao | empresa | ✔ |
| `foambientes_trabalho_alteracao_obter` | obter | foambientes_trabalho_alteracao | empresa, codigo_do_ambiente_de_trabalho, vigencia | ✔ |
| `foantecipacao_salarial_rais_consultar` | consultar | foantecipacao_salarial_rais | empresa | ✔ |
| `foantecipacao_salarial_rais_obter` | obter | foantecipacao_salarial_rais | empresa, codigo_do_empregado, competencia_do_calculo, tipo_do_calculo, rateio, codigo_do_calculo | ✔ |
| `foantecipacao_salarial_rais_totais` | totais | foantecipacao_salarial_rais | empresa | ✔ |
| `foavisos_vencimento_afastamentos_consultar` | consultar | foavisos_vencimento_afastamentos | — | ✔ |
| `foavisos_vencimento_afastamentos_obter` | obter | foavisos_vencimento_afastamentos | codigo_do_aviso_de_vencimento, tipo_do_afastamento_referente_a_foafasta | ✔ |
| `foavisos_vencimento_afastamentos_totais` | totais | foavisos_vencimento_afastamentos | — | ✔ |
| `foavisos_vencimentos_parametros_consultar` | consultar | foavisos_vencimentos_parametros | — | ✔ |
| `foavisos_vencimentos_parametros_obter` | obter | foavisos_vencimentos_parametros | codigo_do_parametro | ✔ |
| `foavisosconf_fechamento_periodo_consultar` | consultar | foavisosconf_fechamento_periodo | — | ✔ |
| `foavisosconf_fechamento_periodo_obter` | obter | foavisosconf_fechamento_periodo | codigo_do_aviso_de_vencimento, tipo_de_calculo_0_folha_mensal_1_folha_a | ✔ |
| `foavisosconf_fechamento_periodo_totais` | totais | foavisosconf_fechamento_periodo | — | ✔ |
| `fobanking_controle_pessoa_consultar` | consultar | fobanking_controle_pessoa | empresa | ✔ |
| `fobanking_controle_pessoa_obter` | obter | fobanking_controle_pessoa | empresa, codigo_sequencial, codigo_do_empregado | ✔ |
| `fobanking_controle_vinculo_empregaticio_consultar` | consultar | fobanking_controle_vinculo_empregaticio | empresa | ✔ |
| `fobanking_controle_vinculo_empregaticio_obter` | obter | fobanking_controle_vinculo_empregaticio | empresa, codigo_sequencial, codigo_do_empregado | ✔ |
| `focadbases_backup_consultar` | consultar | focadbases_backup | — | ✔ |
| `focadbases_backup_obter` | obter | focadbases_backup | i_cadbases | ✔ |
| `focalcinss_movto_consultar` | consultar | focalcinss_movto | empresa | ✔ |
| `focalcinss_movto_obter` | obter | focalcinss_movto | empresa, identificador_unico | ✔ |
| `focalcinss_movto_totais` | totais | focalcinss_movto | empresa | ✔ |
| `focalcirrf_empregados_consultar` | consultar | focalcirrf_empregados | empresa | ✔ |
| `focalcirrf_empregados_obter` | obter | focalcirrf_empregados | empresa, periodo_inicio, codigo_de_recolhimento, codigo_da_empresa_do_empregado, codigo_do_empregado, tipo_de_guia_1_empregados_e_contribuinte | ✔ |
| `focalcirrf_empregados_totais` | totais | focalcirrf_empregados | empresa | ✔ |
| `focalcmedias_mem_consultar` | consultar | focalcmedias_mem | empresa | ✔ |
| `focalcmedias_mem_obter` | obter | focalcmedias_mem | empresa, codigo | ✔ |
| `focalcmedias_mem_totais` | totais | focalcmedias_mem | empresa | ✔ |
| `focalcmedias_mem_oper_consultar` | consultar | focalcmedias_mem_oper | empresa | ✔ |
| `focalcmedias_mem_oper_obter` | obter | focalcmedias_mem_oper | empresa, operacao, codigo_da_memoria_de_calculo | ✔ |
| `focalcmedias_mem_oper_totais` | totais | focalcmedias_mem_oper | empresa | ✔ |
| `focargos_alteracao_consultar` | consultar | focargos_alteracao | empresa | ✔ |
| `focargos_alteracao_obter` | obter | focargos_alteracao | empresa, codigo_do_cargo, vigencia_da_alteracao | ✔ |
| `focargos_alteracao_envios_esocial_consultar` | consultar | focargos_alteracao_envios_esocial | empresa | ✔ |
| `focargos_alteracao_envios_esocial_obter` | obter | focargos_alteracao_envios_esocial | empresa, codigo_do_cargo_referente_a_focargos_alt, vigencia, codigo_da_empresa_referente_a_foesocial, codigo_do_evento_referente_a_foesocial_d | ✔ |
| `focategoria_agente_publico_consultar` | consultar | focategoria_agente_publico | — | ✔ |
| `focategoria_agente_publico_obter` | obter | focategoria_agente_publico | codigo_da_categoria_para_agente_publico | ✔ |
| `focategoria_celetista_cedido_consultar` | consultar | focategoria_celetista_cedido | — | ✔ |
| `focategoria_celetista_cedido_obter` | obter | focategoria_celetista_cedido | codigo_da_categoria_para_celetista_cedid | ✔ |
| `focategoria_origem_dirigente_sindical_consultar` | consultar | focategoria_origem_dirigente_sindical | — | ✔ |
| `focategoria_origem_dirigente_sindical_obter` | obter | focategoria_origem_dirigente_sindical | codigo_da_categoria_da_origem_do_dirigen | ✔ |
| `foccustos_exposicao_fatores_risco_i_consultar` | consultar | foccustos_exposicao_fatores_risco_i | empresa | ✔ |
| `foccustos_exposicao_fatores_risco_i_obter` | obter | foccustos_exposicao_fatores_risco_i | empresa, codigo_do_centro_de_custos, codigo_sequencial | ✔ |
| `foclassificacoes_eventos_consultar` | consultar | foclassificacoes_eventos | — | ✔ |
| `foclassificacoes_eventos_obter` | obter | foclassificacoes_eventos | codigo_da_classificacao | ✔ |
| `focodigo_esocial_domestico_consultar` | consultar | focodigo_esocial_domestico | — | ✔ |
| `focodigo_esocial_domestico_obter` | obter | focodigo_esocial_domestico | codigo_esocial_domestico, tipo_1_vencimentos_2_desconto_3_informat | ✔ |
| `focodigos_gps_consultar` | consultar | focodigos_gps | — | ✔ |
| `focodigos_gps_obter` | obter | focodigos_gps | codigo_gps | ✔ |
| `focodigos_terceiros_consultar` | consultar | focodigos_terceiros | — | ✔ |
| `focodigos_terceiros_obter` | obter | focodigos_terceiros | codigo, sequencia_de_registros | ✔ |
| `foconfiguracoes_etiquetas_ctps_consultar` | consultar | foconfiguracoes_etiquetas_ctps | — | ✔ |
| `foconfiguracoes_etiquetas_ctps_obter` | obter | foconfiguracoes_etiquetas_ctps | codigo_da_configuracao | ✔ |
| `foconfiguracoes_etiquetas_ctps_totais` | totais | foconfiguracoes_etiquetas_ctps | — | ✔ |
| `focontribuicao_sindical_consultar` | consultar | focontribuicao_sindical | empresa | ✔ |
| `focontribuicao_sindical_obter` | obter | focontribuicao_sindical | empresa, codigo_da_contribuicao_sindical | ✔ |
| `focontribuicao_sindical_totais` | totais | focontribuicao_sindical | empresa | ✔ |
| `focontribuicao_sindical_sindicatos_consultar` | consultar | focontribuicao_sindical_sindicatos | — | ✔ |
| `focontribuicao_sindical_sindicatos_obter` | obter | focontribuicao_sindical_sindicatos | codigo_do_sindicato, codigo_da_contribuicao_sindical | ✔ |
| `focontribuicao_sindical_sindicatos_totais` | totais | focontribuicao_sindical_sindicatos | — | ✔ |
| `focontribuicao_sindical_sindicatos_p_consultar` | consultar | focontribuicao_sindical_sindicatos_p | — | ✔ |
| `focontribuicao_sindical_sindicatos_p_obter` | obter | focontribuicao_sindical_sindicatos_p | codigo_do_sindicato_patronal, codigo_da_contribuicao_sindical | ✔ |
| `focontribuicao_sindical_sindicatos_p_totais` | totais | focontribuicao_sindical_sindicatos_p | — | ✔ |
| `focontrrpa_outros_valores_consultar` | consultar | focontrrpa_outros_valores | empresa | ✔ |
| `focontrrpa_outros_valores_obter` | obter | focontrrpa_outros_valores | empresa, codigo_do_empregado, numero_do_rpa, sequencial | ✔ |
| `focontrrpa_outros_valores_totais` | totais | focontrrpa_outros_valores | empresa | ✔ |
| `foconvenios_terceiros_consultar` | consultar | foconvenios_terceiros | — | ✔ |
| `foconvenios_terceiros_obter` | obter | foconvenios_terceiros | codigo_do_convenio | ✔ |
| `foconvocacao_trabalho_intermitente_consultar` | consultar | foconvocacao_trabalho_intermitente | empresa | ✔ |
| `foconvocacao_trabalho_intermitente_obter` | obter | foconvocacao_trabalho_intermitente | empresa, codigo_do_empregado, codigo_da_convocacao | ✔ |
| `foconvocacao_trabalho_intermitente_envios_esocial_consultar` | consultar | foconvocacao_trabalho_intermitente_envios_esocial | empresa | ✔ |
| `foconvocacao_trabalho_intermitente_envios_esocial_obter` | obter | foconvocacao_trabalho_intermitente_envios_esocial | empresa, codigo_do_empregado, codigo_da_convocacao, codigo_da_empresa_referente_a_foesocial, codigo_do_evento_referente_a_foesocial_d | ✔ |
| `focoordenador_estagio_consultar` | consultar | focoordenador_estagio | — | ✔ |
| `focoordenador_estagio_obter` | obter | focoordenador_estagio | codigo_do_coordenador_de_estagio, tipo_1_coordenador_2_supervisor | ✔ |
| `fodepto_alteracao_consultar` | consultar | fodepto_alteracao | empresa | ✔ |
| `fodepto_alteracao_obter` | obter | fodepto_alteracao | empresa, codigo_do_departamento, campo_alterado_1_nome, data_da_alteracao | ✔ |
| `fodiferenca_alteracao_retroativa_piso_salarial_consultar` | consultar | fodiferenca_alteracao_retroativa_piso_salarial | — | ✔ |
| `fodiferenca_alteracao_retroativa_piso_salarial_obter` | obter | fodiferenca_alteracao_retroativa_piso_salarial | codigo_do_sindicato, codigo_do_piso_salarial, competencia_da_alteracao | ✔ |
| `fodiferenca_salario_consultar` | consultar | fodiferenca_salario | empresa | ✔ |
| `fodiferenca_salario_totais` | totais | fodiferenca_salario | empresa | ✔ |
| `fodirf_descricoes_outros_consultar` | consultar | fodirf_descricoes_outros | empresa | ✔ |
| `fodirf_descricoes_outros_obter` | obter | fodirf_descricoes_outros | empresa, ano_base, codigo_do_empregado | ✔ |
| `fodirf_descricoes_outros_eventos_consultar` | consultar | fodirf_descricoes_outros_eventos | empresa | ✔ |
| `fodirf_descricoes_outros_eventos_obter` | obter | fodirf_descricoes_outros_eventos | empresa, ano_base, codigo_do_empregado, codigo_do_evento | ✔ |
| `fodirf_outros_dados_consultar` | consultar | fodirf_outros_dados | empresa | ✔ |
| `fodirf_outros_dados_obter` | obter | fodirf_outros_dados | empresa, ano_base | ✔ |
| `fodirf_outros_dados_totais` | totais | fodirf_outros_dados | empresa | ✔ |
| `fodominio_beneficios_controle_identificador_empregado_consultar` | consultar | fodominio_beneficios_controle_identificador_empregado | empresa | ✔ |
| `fodominio_beneficios_controle_identificador_empregado_obter` | obter | fodominio_beneficios_controle_identificador_empregado | empresa, sequencial_do_controle | ✔ |
| `foempreg_campolivres_consultar` | consultar | foempreg_campolivres | empresa | ✔ |
| `foempreg_campolivres_obter` | obter | foempreg_campolivres | empresa, codigo_empregado, numero_campo | ✔ |
| `foempreg_contrsind_consultar` | consultar | foempreg_contrsind | empresa | ✔ |
| `foempreg_contrsind_obter` | obter | foempreg_contrsind | empresa, codigo_empregado, competencia | ✔ |
| `foencargo_simples_domestico_consultar` | consultar | foencargo_simples_domestico | empresa | ✔ |
| `foencargo_simples_domestico_obter` | obter | foencargo_simples_domestico | empresa, competencia_do_calculo, tipo_de_calculo, codigo_da_filial, sequencial | ✔ |
| `foencargo_simples_domestico_totais` | totais | foencargo_simples_domestico | empresa | ✔ |
| `foencargo_simples_domestico_empregados_consultar` | consultar | foencargo_simples_domestico_empregados | empresa | ✔ |
| `foencargo_simples_domestico_empregados_obter` | obter | foencargo_simples_domestico_empregados | empresa, competencia_do_calculo, tipo_de_calculo, codigo_da_filial, codigo_do_empregado, sequencial | ✔ |
| `foencargo_simples_domestico_empregados_totais` | totais | foencargo_simples_domestico_empregados | empresa | ✔ |
| `foencargo_simples_domestico_rescisorio_consultar` | consultar | foencargo_simples_domestico_rescisorio | empresa | ✔ |
| `foencargo_simples_domestico_rescisorio_obter` | obter | foencargo_simples_domestico_rescisorio | empresa, codigo_do_empregado, tipo_da_rescisao, sequencial, codigo_do_calculo_da_rescisao | ✔ |
| `foencargo_simples_domestico_rescisorio_totais` | totais | foencargo_simples_domestico_rescisorio | empresa | ✔ |
| `foencargos_emprestimo_credito_trabalhador_consultar` | consultar | foencargos_emprestimo_credito_trabalhador | empresa | ✔ |
| `foencargos_emprestimo_credito_trabalhador_obter` | obter | foencargos_emprestimo_credito_trabalhador | empresa, competencia, tipo_calculo_folha, sequencial_da_filial | ✔ |
| `foencargos_emprestimo_credito_trabalhador_totais` | totais | foencargos_emprestimo_credito_trabalhador | empresa | ✔ |
| `foencargos_emprestimo_credito_trabalhador_rescisao_consultar` | consultar | foencargos_emprestimo_credito_trabalhador_rescisao | empresa | ✔ |
| `foencargos_emprestimo_credito_trabalhador_rescisao_obter` | obter | foencargos_emprestimo_credito_trabalhador_rescisao | empresa, empregado, competencia, tipo_calculo_folha, sequencial_da_filial | ✔ |
| `foencargos_emprestimo_credito_trabalhador_rescisao_totais` | totais | foencargos_emprestimo_credito_trabalhador_rescisao | empresa | ✔ |
| `foencargos_pensao_alimenticia_consultar` | consultar | foencargos_pensao_alimenticia | empresa | ✔ |
| `foencargos_pensao_alimenticia_obter` | obter | foencargos_pensao_alimenticia | empresa, competencia, tipo_de_processo, data_de_pagamento, encargo_referente_a_rescisao_0_nao_1_sim | ✔ |
| `foencargos_pensao_alimenticia_totais` | totais | foencargos_pensao_alimenticia | empresa | ✔ |
| `foequipamentos_protecao_individual_consultar` | consultar | foequipamentos_protecao_individual | empresa | ✔ |
| `foequipamentos_protecao_individual_obter` | obter | foequipamentos_protecao_individual | empresa, codigo_do_epi | ✔ |
| `foestabilidade_tipos_consultar` | consultar | foestabilidade_tipos | — | ✔ |
| `foestabilidade_tipos_obter` | obter | foestabilidade_tipos | codigo_do_tipo_de_estabilidade | ✔ |
| `fofaltas_lancamentos_consultar` | consultar | fofaltas_lancamentos | empresa | ✔ |
| `fofaltas_lancamentos_obter` | obter | fofaltas_lancamentos | empresa, empregado, competencia, tipo_de_calculo, evento, sequencial_de_faltas_do_empregado, tipo_do_lancamento_1_mensal_2_fixo, sequencial | ✔ |
| `fofatores_risco_consultar` | consultar | fofatores_risco | — | ✔ |
| `fofatores_risco_obter` | obter | fofatores_risco | codigo_do_fator_de_risco | ✔ |
| `fofgtsdigital_competencia_consultar` | consultar | fofgtsdigital_competencia | empresa | ✔ |
| `fofgtsdigital_competencia_obter` | obter | fofgtsdigital_competencia | empresa, identificador_do_registro_de_competencia | ✔ |
| `fofgtsdigital_competencia_totais` | totais | fofgtsdigital_competencia | empresa | ✔ |
| `fofgtsdigital_consulta_consultar` | consultar | fofgtsdigital_consulta | empresa | ✔ |
| `fofgtsdigital_consulta_obter` | obter | fofgtsdigital_consulta | empresa, codigo_da_execucao_da_consulta | ✔ |
| `fofgtsdigital_ocorrencia_consultar` | consultar | fofgtsdigital_ocorrencia | empresa | ✔ |
| `fofgtsdigital_ocorrencia_obter` | obter | fofgtsdigital_ocorrencia | empresa, identificador_da_ocorrencia | ✔ |
| `fofilhos_alteracao_consultar` | consultar | fofilhos_alteracao | empresa | ✔ |
| `fofilhos_alteracao_obter` | obter | fofilhos_alteracao | empresa, codigo_do_empregado, codigo_do_dependente, data_da_alteracao | ✔ |
| `fofilhos_plano_saude_consultar` | consultar | fofilhos_plano_saude | empresa | ✔ |
| `fofilhos_plano_saude_obter` | obter | fofilhos_plano_saude | empresa, codigo_do_empregado, codigo_do_dependente, codigo_da_operadora_de_plano_de_saude, data_inicio_periodo | ✔ |
| `fofiliais_fap_consultar` | consultar | fofiliais_fap | empresa | ✔ |
| `fofiliais_fap_obter` | obter | fofiliais_fap | empresa, codigo_da_filial, vigencia | ✔ |
| `fofiliais_historico_consultar` | consultar | fofiliais_historico | empresa | ✔ |
| `fofiliais_historico_obter` | obter | fofiliais_historico | empresa, codigo_da_filial, data_da_troca, campo | ✔ |
| `fofiliais_sindicatos_patronais_consultar` | consultar | fofiliais_sindicatos_patronais | empresa | ✔ |
| `fofiliais_sindicatos_patronais_obter` | obter | fofiliais_sindicatos_patronais | empresa, codigo_da_filial, codigo_do_sindicato_patronal | ✔ |
| `fofiliais_sindicatos_patronais_totais` | totais | fofiliais_sindicatos_patronais | empresa | ✔ |
| `foformas_ajuste_parcelamento_consultar` | consultar | foformas_ajuste_parcelamento | — | ✔ |
| `foformas_ajuste_parcelamento_obter` | obter | foformas_ajuste_parcelamento | codigo | ✔ |
| `foformas_ajuste_parcelamento_totais` | totais | foformas_ajuste_parcelamento | — | ✔ |
| `foformas_ajuste_parcelamento_competencias_consultar` | consultar | foformas_ajuste_parcelamento_competencias | — | ✔ |
| `foformas_ajuste_parcelamento_competencias_obter` | obter | foformas_ajuste_parcelamento_competencias | codigo_da_forma_de_ajuste_conforme_parce, numero_da_parcela | ✔ |
| `foformas_ajuste_parcelamento_competencias_totais` | totais | foformas_ajuste_parcelamento_competencias | — | ✔ |
| `fofuncoes_alteracao_consultar` | consultar | fofuncoes_alteracao | empresa | ✔ |
| `fofuncoes_alteracao_obter` | obter | fofuncoes_alteracao | empresa, codigo_da_funcao, vigencia_da_alteracao | ✔ |
| `fofuncoes_alteracao_envios_esocial_consultar` | consultar | fofuncoes_alteracao_envios_esocial | empresa | ✔ |
| `fofuncoes_alteracao_envios_esocial_obter` | obter | fofuncoes_alteracao_envios_esocial | empresa, codigo_da_funcao, vigencia, codigo_da_empresa_referente_a_foesocial, codigo_do_evento_referente_a_foesocial_d | ✔ |
| `foguia_inss_servicos_valores_consultar` | consultar | foguia_inss_servicos_valores | empresa | ✔ |
| `foguia_inss_servicos_valores_obter` | obter | foguia_inss_servicos_valores | empresa, codigo_do_servico, tipo_valor, codigo_da_guia_do_inss | ✔ |
| `foguia_inss_servicos_valores_totais` | totais | foguia_inss_servicos_valores | empresa | ✔ |
| `foguia_iss_consultar` | consultar | foguia_iss | empresa | ✔ |
| `foguia_iss_obter` | obter | foguia_iss | empresa, sequencial_da_guia | ✔ |
| `foguia_iss_totais` | totais | foguia_iss | empresa | ✔ |
| `foguiainss_dados_serv_consultar` | consultar | foguiainss_dados_serv | empresa | ✔ |
| `foguiainss_dados_serv_obter` | obter | foguiainss_dados_serv | empresa, codigo_do_servico, competencia | ✔ |
| `foguiainss_dados_serv_totais` | totais | foguiainss_dados_serv | empresa | ✔ |
| `fohorafolha_backup_consultar` | consultar | fohorafolha_backup | empresa | ✔ |
| `fohorafolha_backup_obter` | obter | fohorafolha_backup | empresa, codigo | ✔ |
| `fohorarios_alteracao_consultar` | consultar | fohorarios_alteracao | empresa | ✔ |
| `fohorarios_alteracao_obter` | obter | fohorarios_alteracao | empresa, codigo_do_horario, vigencia_da_alteracao | ✔ |
| `fohorarios_alteracao_envios_esocial_consultar` | consultar | fohorarios_alteracao_envios_esocial | empresa | ✔ |
| `fohorarios_alteracao_envios_esocial_obter` | obter | fohorarios_alteracao_envios_esocial | empresa, codigo_do_horario, vigencia, codigo_da_empresa_referente_a_foesocial, codigo_do_evento_referente_a_foesocial_d | ✔ |
| `fohorarios_intervalos_consultar` | consultar | fohorarios_intervalos | empresa | ✔ |
| `fohorarios_intervalos_obter` | obter | fohorarios_intervalos | empresa, codigo_do_horario, codigo_do_intervalo | ✔ |
| `fohorasaula_reajustes_consultar` | consultar | fohorasaula_reajustes | empresa | ✔ |
| `fohorasaula_reajustes_obter` | obter | fohorasaula_reajustes | empresa, codigo_das_horas_aula, codigo_das_horas_aula_reajuste | ✔ |
| `fohorasaula_reajustes_totais` | totais | fohorasaula_reajustes | empresa | ✔ |
| `foibge_beneficios_classificacao_rubricas_consultar` | consultar | foibge_beneficios_classificacao_rubricas | empresa | ✔ |
| `foibge_beneficios_classificacao_rubricas_obter` | obter | foibge_beneficios_classificacao_rubricas | empresa, competencia_da_tela_de_outros_dados_ibge, sequencial, c_1_pac_2_pas_3_pia_4_paic | ✔ |
| `foibge_salarios_outras_remuneracoes_natureza_rubricas_consultar` | consultar | foibge_salarios_outras_remuneracoes_natureza_rubricas | empresa | ✔ |
| `foibge_salarios_outras_remuneracoes_natureza_rubricas_obter` | obter | foibge_salarios_outras_remuneracoes_natureza_rubricas | empresa, competencia_da_tela_de_outros_dados_ibge, sequencial, c_1_pac_2_pas_3_pia_4_paic | ✔ |
| `foinformacoes_complementares_eventos_periodicos_e_d46e_consultar` | consultar | foinformacoes_complementares_eventos_periodicos_esocial | empresa | ✔ |
| `foinformacoes_complementares_eventos_periodicos_esocial_obter` | obter | foinformacoes_complementares_eventos_periodicos_esocial | empresa, competencia, tipo_processo_enviar_para_o_esocial | ✔ |
| `foinformacoes_complementares_eventos_periodicos_e_4b8f_consultar` | consultar | foinformacoes_complementares_eventos_periodicos_esocial_envios_esocial | empresa | ✔ |
| `foinformacoes_complementares_eventos_periodicos_esoci_4b8f_obter` | obter | foinformacoes_complementares_eventos_periodicos_esocial_envios_esocial | empresa, competencia, tipo_do_processo, codigo_da_empresa_referente_a_foesocial, codigo_do_evento_referente_a_foesocial_d | ✔ |
| `foinss_empresa_receita_bruta_consultar` | consultar | foinss_empresa_receita_bruta | empresa | ✔ |
| `foinss_empresa_receita_bruta_obter` | obter | foinss_empresa_receita_bruta | empresa, codigo_sequencial | ✔ |
| `foinss_empresa_receita_bruta_totais` | totais | foinss_empresa_receita_bruta | empresa | ✔ |
| `foinss_empresa_receita_bruta_envios_esocial_consultar` | consultar | foinss_empresa_receita_bruta_envios_esocial | — | ✔ |
| `foinss_empresa_receita_bruta_envios_esocial_obter` | obter | foinss_empresa_receita_bruta_envios_esocial | codigo_do_registro_de_inss_da_empresa_so, codigo_da_empresa_referente_a_foesocial, codigo_do_evento_referente_a_foesocial_d | ✔ |
| `foinstituicao_ensino_consultar` | consultar | foinstituicao_ensino | — | ✔ |
| `foinstituicao_ensino_obter` | obter | foinstituicao_ensino | codigo_da_instituicao_de_ensino | ✔ |
| `fojornadas_alteracao_consultar` | consultar | fojornadas_alteracao | empresa | ✔ |
| `fojornadas_alteracao_obter` | obter | fojornadas_alteracao | empresa, codigo_da_jornada, campo_alterado_1_tipo_de_jornada_2_tipo, data_da_alteracao | ✔ |
| `fojornadas_horarios_consultar` | consultar | fojornadas_horarios | empresa | ✔ |
| `fojornadas_horarios_obter` | obter | fojornadas_horarios | empresa, codigo_do_jornada, sequencial | ✔ |
| `folinhas_valores_passagem_consultar` | consultar | folinhas_valores_passagem | — | ✔ |
| `folinhas_valores_passagem_obter` | obter | folinhas_valores_passagem | codigo_da_linha, competencia | ✔ |
| `folinhas_valores_passagem_totais` | totais | folinhas_valores_passagem | — | ✔ |
| `fomediascalc_simulacao_consultar` | consultar | fomediascalc_simulacao | empresa | ✔ |
| `fomediascalc_simulacao_obter` | obter | fomediascalc_simulacao | empresa, empregado, tipo_informado, tipo_calculo, tipo, codigo_do_calculo | ✔ |
| `fomediascalc_simulacao_totais` | totais | fomediascalc_simulacao | empresa | ✔ |
| `fomedidas_protecao_emprego_covid_19_consultar` | consultar | fomedidas_protecao_emprego_covid_19 | empresa | ✔ |
| `fomedidas_protecao_emprego_covid_19_obter` | obter | fomedidas_protecao_emprego_covid_19 | empresa, codigo_do_empregado, data_do_inicio_da_vigencia_da_medida, sequencial_usado_para_quando_houver_uma | ✔ |
| `fomedidas_protecao_emprego_covid_19_totais` | totais | fomedidas_protecao_emprego_covid_19 | empresa | ✔ |
| `fomedidas_protecao_emprego_covid_19_afastamentos_consultar` | consultar | fomedidas_protecao_emprego_covid_19_afastamentos | empresa | ✔ |
| `fomedidas_protecao_emprego_covid_19_afastamentos_obter` | obter | fomedidas_protecao_emprego_covid_19_afastamentos | empresa, codigo_do_empregado, data_do_inicio_da_vigencia_da_medida, data_do_afastamento, sequencial_usado_para_quando_houver_uma | ✔ |
| `fomedidas_protecao_emprego_covid_19_prorrogacao_a_4a6c_consultar` | consultar | fomedidas_protecao_emprego_covid_19_prorrogacao_antecipacao | empresa | ✔ |
| `fomedidas_protecao_emprego_covid_19_prorrogacao_antec_4a6c_obter` | obter | fomedidas_protecao_emprego_covid_19_prorrogacao_antecipacao | empresa, codigo_do_empregado, data_do_inicio_da_vigencia_da_medida, sequencial_da_tabela_pai_chave_primaria, sequencial | ✔ |
| `fomensagem_aviso_consultar` | consultar | fomensagem_aviso | — | ✔ |
| `fomensagem_aviso_obter` | obter | fomensagem_aviso | identificacao_do_aviso, usuario | ✔ |
| `fomodelos_etiquetas_ctps_consultar` | consultar | fomodelos_etiquetas_ctps | — | ✔ |
| `fomodelos_etiquetas_ctps_obter` | obter | fomodelos_etiquetas_ctps | codigo_do_modelo | ✔ |
| `fomonitoracao_biologica_analise_efetuada_consultar` | consultar | fomonitoracao_biologica_analise_efetuada | — | ✔ |
| `fomonitoracao_biologica_analise_efetuada_obter` | obter | fomonitoracao_biologica_analise_efetuada | codigo_da_analise_efetuada | ✔ |
| `fomonitoramento_saude_trabalhador_consultar` | consultar | fomonitoramento_saude_trabalhador | empresa | ✔ |
| `fomonitoramento_saude_trabalhador_obter` | obter | fomonitoramento_saude_trabalhador | empresa, codigo_do_empregado, codigo_sequencial | ✔ |
| `fomonitoramento_saude_trabalhador_envios_esocial_consultar` | consultar | fomonitoramento_saude_trabalhador_envios_esocial | empresa | ✔ |
| `fomonitoramento_saude_trabalhador_envios_esocial_obter` | obter | fomonitoramento_saude_trabalhador_envios_esocial | empresa, codigo_do_empregado, numero_sequencial, codigo_da_empresa_referente_a_foesocial, codigo_do_evento_referente_a_foesocial_d | ✔ |
| `fomonitoramento_saude_trabalhador_exames_consultar` | consultar | fomonitoramento_saude_trabalhador_exames | empresa | ✔ |
| `fomonitoramento_saude_trabalhador_exames_obter` | obter | fomonitoramento_saude_trabalhador_exames | empresa, codigo_do_empregado, codigo_sequencial, codigo_sequencial_do_exame | ✔ |
| `fonatureza_evento_consultar` | consultar | fonatureza_evento | — | ✔ |
| `fonatureza_evento_obter` | obter | fonatureza_evento | codigo_da_natureza | ✔ |
| `fopagamentos_ajuste_parcelamento_consultar` | consultar | fopagamentos_ajuste_parcelamento | — | ✔ |
| `fopagamentos_ajuste_parcelamento_obter` | obter | fopagamentos_ajuste_parcelamento | indice_da_parcela, codigo_do_calculo_da_diferenca | ✔ |
| `fopagto_dados_pagamento_consultar` | consultar | fopagto_dados_pagamento | empresa | ✔ |
| `fopagto_dados_pagamento_obter` | obter | fopagto_dados_pagamento | empresa, sequencial | ✔ |
| `fopagto_dados_pagamento_totais` | totais | fopagto_dados_pagamento | empresa | ✔ |
| `fopagto_publicar_documento_consultar` | consultar | fopagto_publicar_documento | empresa | ✔ |
| `fopagto_publicar_documento_obter` | obter | fopagto_publicar_documento | empresa, sequencial | ✔ |
| `fopagto_publicar_documento_totais` | totais | fopagto_publicar_documento | empresa | ✔ |
| `fopagtoparcial_sindicatos_consultar` | consultar | fopagtoparcial_sindicatos | empresa | ✔ |
| `fopagtoparcial_sindicatos_obter` | obter | fopagtoparcial_sindicatos | empresa, sequencia_de_pagamento, sequencial_de_pagamentos, codigo_do_sindicato | ✔ |
| `fopagtoparcial_sindicatos_totais` | totais | fopagtoparcial_sindicatos | empresa | ✔ |
| `foparametro_thread_consultar` | consultar | foparametro_thread | — | ✔ |
| `foparametro_thread_obter` | obter | foparametro_thread | codigo_do_parametro | ✔ |
| `foportal_empregado_consultar` | consultar | foportal_empregado | — | ✔ |
| `foportal_empregado_obter` | obter | foportal_empregado | codigo_chave | ✔ |
| `foremuneracao_variavel_consultar` | consultar | foremuneracao_variavel | empresa | ✔ |
| `foremuneracao_variavel_obter` | obter | foremuneracao_variavel | empresa, codigo_sequencial_da_remuneracao_variave | ✔ |
| `forequerimento_seguro_desemprego_salarios_consultar` | consultar | forequerimento_seguro_desemprego_salarios | empresa | ✔ |
| `forequerimento_seguro_desemprego_salarios_obter` | obter | forequerimento_seguro_desemprego_salarios | empresa, codigo_do_empregado | ✔ |
| `forequerimento_seguro_desemprego_salarios_totais` | totais | forequerimento_seguro_desemprego_salarios | empresa | ✔ |
| `forescisoesaviso_envios_esocial_consultar` | consultar | forescisoesaviso_envios_esocial | empresa | ✔ |
| `forescisoesaviso_envios_esocial_obter` | obter | forescisoesaviso_envios_esocial | empresa, codigo_do_empregado, codigo_sequencial_do_aviso_referente_a_f, codigo_da_empresa_referente_a_foesocial, codigo_do_evento_referente_a_foesocial_d | ✔ |
| `fosefip_tbtercr_consultar` | consultar | fosefip_tbtercr | — | ✔ |
| `fosefip_tbtercr_obter` | obter | fosefip_tbtercr | fpas, cod_terceiro | ✔ |
| `fosind_diasdesconsiderar_consultar` | consultar | fosind_diasdesconsiderar | — | ✔ |
| `fosind_diasdesconsiderar_obter` | obter | fosind_diasdesconsiderar | codigo_do_sindicato, dia, mes | ✔ |
| `fosituacoes_avo_13_consultar` | consultar | fosituacoes_avo_13 | — | ✔ |
| `fosituacoes_avo_13_obter` | obter | fosituacoes_avo_13 | codigo_do_calculo_do_13o_salario | ✔ |
| `fotabcalcinss_faixas_consultar` | consultar | fotabcalcinss_faixas | — | ✔ |
| `fotabcalcinss_faixas_obter` | obter | fotabcalcinss_faixas | competencia, valor_ate | ✔ |
| `fotabcalcinss_salfam_consultar` | consultar | fotabcalcinss_salfam | — | ✔ |
| `fotabcalcinss_salfam_obter` | obter | fotabcalcinss_salfam | competencia, valor_ate | ✔ |
| `fotabcalcinss_salfam_totais` | totais | fotabcalcinss_salfam | — | ✔ |
| `fotermo_rescisao_rais_consultar` | consultar | fotermo_rescisao_rais | empresa | ✔ |
| `fotermo_rescisao_rais_obter` | obter | fotermo_rescisao_rais | empresa, codigo_do_empregado, competencia_do_calculo, tipo_do_calculo, servico_relacionado_no_calculo, rateio, codigo_do_calculo | ✔ |
| `fotermo_rescisao_rais_totais` | totais | fotermo_rescisao_rais | empresa | ✔ |
| `fotipos_itens_prestacao_servico_consultar` | consultar | fotipos_itens_prestacao_servico | — | ✔ |
| `fotipos_itens_prestacao_servico_obter` | obter | fotipos_itens_prestacao_servico | codigo_do_tipo_de_servico | ✔ |
| `fovale_alimentacao_consultar` | consultar | fovale_alimentacao | empresa | ✔ |
| `fovale_alimentacao_obter` | obter | fovale_alimentacao | empresa, codigo_do_vale_alimentacao | ✔ |
| `fovale_alimentacao_vigencias_consultar` | consultar | fovale_alimentacao_vigencias | empresa | ✔ |
| `fovale_alimentacao_vigencias_obter` | obter | fovale_alimentacao_vigencias | empresa, codigo_do_vale_alimentacao, competencia | ✔ |
| `fovale_alimentacao_vigencias_totais` | totais | fovale_alimentacao_vigencias | empresa | ✔ |
| `fovalores_ajuste_parcelamento_consultar` | consultar | fovalores_ajuste_parcelamento | — | ✔ |
| `fovalores_ajuste_parcelamento_obter` | obter | fovalores_ajuste_parcelamento | codigo_do_evento_de_diferenca, codigo_do_calculo_ajustado, codigo_do_calculo_da_diferenca | ✔ |
| `fovalores_ajuste_parcelamento_totais` | totais | fovalores_ajuste_parcelamento | — | ✔ |
| `fovalores_pagamento_ajuste_parcelamento_consultar` | consultar | fovalores_pagamento_ajuste_parcelamento | — | ✔ |
| `fovalores_pagamento_ajuste_parcelamento_obter` | obter | fovalores_pagamento_ajuste_parcelamento | indice_da_parcela, codigo_do_evento_de_diferenca, codigo_do_calculo_da_diferenca | ✔ |
| `fovalores_pagamento_ajuste_parcelamento_totais` | totais | fovalores_pagamento_ajuste_parcelamento | — | ✔ |
| `fovalores_pagamento_ajuste_parcelamento_esocial_consultar` | consultar | fovalores_pagamento_ajuste_parcelamento_esocial | — | ✔ |
| `fovalores_pagamento_ajuste_parcelamento_esocial_obter` | obter | fovalores_pagamento_ajuste_parcelamento_esocial | codigo_da_parcela, codigo_da_rubrica, codigo_da_empresa_servico, codigo_do_servico, rateio_do_servico, codigo_do_calculo_ajustado, codigo_do_calculo_da_diferenca | ✔ |
| `fovalores_pagamento_ajuste_parcelamento_esocial_totais` | totais | fovalores_pagamento_ajuste_parcelamento_esocial | — | ✔ |
| `fovariavel_planosaude_consultar` | consultar | fovariavel_planosaude | empresa | ✔ |
| `fovariavel_planosaude_obter` | obter | fovariavel_planosaude | empresa, codigo_do_empregado, competencia, tipo_de_calculo, codigo_do_evento, sequencial_de_beneficiario, tipo_do_lancamento_1_mensal_2_fixo, sequencial, sequencial_lancamento | ✔ |
| `fovariavel_planosaude_totais` | totais | fovariavel_planosaude | empresa | ✔ |
| `fovigencia_regime_consultar` | consultar | fovigencia_regime | empresa | ✔ |
| `fovigencia_regime_obter` | obter | fovigencia_regime | empresa, competencia | ✔ |
| `fovigencia_unidade_calculo_consultar` | consultar | fovigencia_unidade_calculo | empresa | ✔ |
| `fovigencia_unidade_calculo_obter` | obter | fovigencia_unidade_calculo | empresa, competencia | ✔ |
