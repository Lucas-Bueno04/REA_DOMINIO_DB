# Módulo `pessoal_empregados`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `foempregados_alteracao_cadastral_consultar` | consultar | foempregados_alteracao_cadastral | empresa | ✔ |
| `foempregados_alteracao_cadastral_obter` | obter | foempregados_alteracao_cadastral | empresa, codigo_do_empregado, data_da_alteracao | ✔ |
| `foempregados_alteracao_cadastral_envios_esocial_consultar` | consultar | foempregados_alteracao_cadastral_envios_esocial | empresa | ✔ |
| `foempregados_alteracao_cadastral_envios_esocial_obter` | obter | foempregados_alteracao_cadastral_envios_esocial | empresa, codigo_do_empregado, data_da_alteracao, codigo_da_empresa_referente_a_foesocial, codigo_do_evento_referente_a_foesocial_d | ✔ |
| `foempregados_alteracao_contratual_envios_esocial_consultar` | consultar | foempregados_alteracao_contratual_envios_esocial | empresa | ✔ |
| `foempregados_alteracao_contratual_envios_esocial_obter` | obter | foempregados_alteracao_contratual_envios_esocial | empresa, codigo_do_empregado, data_da_alteracao, codigo_da_empresa_referente_a_foesocial, codigo_do_evento_referente_a_foesocial_d | ✔ |
| `foempregados_alteracao_outros_campos_consultar` | consultar | foempregados_alteracao_outros_campos | empresa | ✔ |
| `foempregados_alteracao_outros_campos_obter` | obter | foempregados_alteracao_outros_campos | empresa, codigo_do_empregado, data_da_alteracao | ✔ |
| `foempregados_alteracao_outros_campos_totais` | totais | foempregados_alteracao_outros_campos | empresa | ✔ |
| `foempregados_atestados_ocupacionais_consultar` | consultar | foempregados_atestados_ocupacionais | empresa | ✔ |
| `foempregados_atestados_ocupacionais_obter` | obter | foempregados_atestados_ocupacionais | empresa, codigo_do_empregado, codigo_do_atestado_ocupacional | ✔ |
| `foempregados_atestados_ocupacionais_exames_consultar` | consultar | foempregados_atestados_ocupacionais_exames | empresa | ✔ |
| `foempregados_atestados_ocupacionais_exames_obter` | obter | foempregados_atestados_ocupacionais_exames | empresa, codigo_do_empregado, codigo_do_atestado_ocupacional, codigo_do_exame | ✔ |
| `foempregados_atestados_ocupacionais_resultado_mon_2b0a_consultar` | consultar | foempregados_atestados_ocupacionais_resultado_monitoracao_biologica | empresa | ✔ |
| `foempregados_atestados_ocupacionais_resultado_monitor_2b0a_obter` | obter | foempregados_atestados_ocupacionais_resultado_monitoracao_biologica | empresa, codigo_do_empregado, codigo_sequencial_do_atestado_ocupaciona, codigo_sequencial_do_resultado_da_monito | ✔ |
| `foempregados_certidao_civil_consultar` | consultar | foempregados_certidao_civil | empresa | ✔ |
| `foempregados_certidao_civil_obter` | obter | foempregados_certidao_civil | empresa, codigo_do_empregado, tipo_da_certidao_1_certidao_de_nasciment, data_de_emissao_da_certidao | ✔ |
| `foempregados_chave_pix_consultar` | consultar | foempregados_chave_pix | empresa | ✔ |
| `foempregados_chave_pix_obter` | obter | foempregados_chave_pix | empresa, empregado, sequencial | ✔ |
| `foempregados_chave_pix_alternativa_consultar` | consultar | foempregados_chave_pix_alternativa | empresa | ✔ |
| `foempregados_chave_pix_alternativa_obter` | obter | foempregados_chave_pix_alternativa | empresa, empregado, sequencial | ✔ |
| `foempregados_conselhos_regionais_consultar` | consultar | foempregados_conselhos_regionais | empresa | ✔ |
| `foempregados_conselhos_regionais_obter` | obter | foempregados_conselhos_regionais | empresa, codigo_do_empregado, codigo_do_conselho_regional | ✔ |
| `foempregados_conselhos_regionais_alteracao_consultar` | consultar | foempregados_conselhos_regionais_alteracao | empresa | ✔ |
| `foempregados_conselhos_regionais_alteracao_obter` | obter | foempregados_conselhos_regionais_alteracao | empresa, codigo_do_empregado, codigo_do_conselho_regional, campo_alterado, data_da_alteracao | ✔ |
| `foempregados_dados_eventos_esocial_consultar` | consultar | foempregados_dados_eventos_esocial | empresa | ✔ |
| `foempregados_dados_eventos_esocial_obter` | obter | foempregados_dados_eventos_esocial | empresa, codigo_do_empregado, codigo_do_registro_de_envio | ✔ |
| `foempregados_envios_esocial_consultar` | consultar | foempregados_envios_esocial | empresa | ✔ |
| `foempregados_envios_esocial_obter` | obter | foempregados_envios_esocial | empresa, codigo_do_empregado, codigo_da_empresa_referente_a_foesocial, codigo_do_evento_referente_a_foesocial_d | ✔ |
| `foempregados_esocial_domestico_consultar` | consultar | foempregados_esocial_domestico | empresa | ✔ |
| `foempregados_esocial_domestico_obter` | obter | foempregados_esocial_domestico | empresa, codigo_do_empregado | ✔ |
| `foempregados_estabilidade_consultar` | consultar | foempregados_estabilidade | empresa | ✔ |
| `foempregados_estabilidade_obter` | obter | foempregados_estabilidade | empresa, codigo_do_empregado, codigo_do_tipo_de_estabilidade, codigo_sequencial | ✔ |
| `foempregados_estabilidade_totais` | totais | foempregados_estabilidade | empresa | ✔ |
| `foempregados_exames_toxicologicos_consultar` | consultar | foempregados_exames_toxicologicos | empresa | ✔ |
| `foempregados_exames_toxicologicos_obter` | obter | foempregados_exames_toxicologicos | empresa, codigo_do_empregado, tipo_do_exame_1_admissional_2_demissiona, sequencial_para_exames_periodicos | ✔ |
| `foempregados_plano_saude_consultar` | consultar | foempregados_plano_saude | empresa | ✔ |
| `foempregados_plano_saude_obter` | obter | foempregados_plano_saude | empresa, codigo_do_empregado, codigo_da_operadora_de_plano_de_saude, data_inicio_periodo | ✔ |
| `foempregados_transf_consultar` | consultar | foempregados_transf | empresa | ✔ |
| `foempregados_transf_obter` | obter | foempregados_transf | empresa, codigo_do_empregado, codigo_da_empresa_de_origem, codigo_do_empregado_de_origem | ✔ |
| `foempregados_vale_alimentacao_consultar` | consultar | foempregados_vale_alimentacao | empresa | ✔ |
| `foempregados_vale_alimentacao_obter` | obter | foempregados_vale_alimentacao | empresa, codigo_do_empregado, codigo_do_vale_alimentacao | ✔ |
| `foempregados_vale_alimentacao_totais` | totais | foempregados_vale_alimentacao | empresa | ✔ |
| `foempregados_vale_alimentacao_desconto_consultar` | consultar | foempregados_vale_alimentacao_desconto | empresa | ✔ |
| `foempregados_vale_alimentacao_desconto_obter` | obter | foempregados_vale_alimentacao_desconto | empresa, codigo_do_empregado, competencia, tipo_de_processo, tipo_de_lancamento, codigo_da_rubrica_de_desconto, sequencial | ✔ |
| `foempregados_vale_alimentacao_desconto_totais` | totais | foempregados_vale_alimentacao_desconto | empresa | ✔ |
| `foempregados_vinc_consultar` | consultar | foempregados_vinc | empresa | ✔ |
| `foempregados_vinc_obter` | obter | foempregados_vinc | empresa, codigo_empregado, codi_emp_vinc, i_empregados_vinc | ✔ |
