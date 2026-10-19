# Módulo `pessoal_esocial`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `foesocial_arquivo_retorno_s_5002_consultar` | consultar | foesocial_arquivo_retorno_s_5002 | empresa | ✔ |
| `foesocial_arquivo_retorno_s_5002_obter` | obter | foesocial_arquivo_retorno_s_5002 | empresa, codigo_do_evento_referente_a_foesocial_d | ✔ |
| `foesocial_arquivo_retorno_s_5002_totais` | totais | foesocial_arquivo_retorno_s_5002 | empresa | ✔ |
| `foesocial_arquivo_retorno_s_5002_categoria_consultar` | consultar | foesocial_arquivo_retorno_s_5002_categoria | empresa | ✔ |
| `foesocial_arquivo_retorno_s_5002_categoria_obter` | obter | foesocial_arquivo_retorno_s_5002_categoria | empresa, codigo_do_evento_referente_a_foesocial_d, codigo_da_categoria, residencial_brasil, fonte | ✔ |
| `foesocial_arquivo_retorno_s_5002_categoria_valor_consultar` | consultar | foesocial_arquivo_retorno_s_5002_categoria_valor | empresa | ✔ |
| `foesocial_arquivo_retorno_s_5002_categoria_valor_obter` | obter | foesocial_arquivo_retorno_s_5002_categoria_valor | empresa, codigo_do_evento_referente_a_foesocial_d, codigo_da_categoria, tipo_do_valor, tipo_do_pagamento, fonte | ✔ |
| `foesocial_arquivo_retorno_s_5002_categoria_valor_totais` | totais | foesocial_arquivo_retorno_s_5002_categoria_valor | empresa | ✔ |
| `foesocial_arquivo_retorno_s_5002_dependente_consultar` | consultar | foesocial_arquivo_retorno_s_5002_dependente | empresa | ✔ |
| `foesocial_arquivo_retorno_s_5002_dependente_obter` | obter | foesocial_arquivo_retorno_s_5002_dependente | empresa, codigo_do_evento_referente_a_foesocial_d, cpf, tipo_do_valor | ✔ |
| `foesocial_arquivo_retorno_s_5002_dependente_totais` | totais | foesocial_arquivo_retorno_s_5002_dependente | empresa | ✔ |
| `foesocial_arquivo_retorno_s_5003_consultar` | consultar | foesocial_arquivo_retorno_s_5003 | empresa | ✔ |
| `foesocial_arquivo_retorno_s_5003_obter` | obter | foesocial_arquivo_retorno_s_5003 | empresa, codigo_do_evento_referente_a_foesocial_d | ✔ |
| `foesocial_arquivo_retorno_s_5003_base_servicos_consultar` | consultar | foesocial_arquivo_retorno_s_5003_base_servicos | empresa | ✔ |
| `foesocial_arquivo_retorno_s_5003_base_servicos_obter` | obter | foesocial_arquivo_retorno_s_5003_base_servicos | empresa, codigo_do_evento_referente_a_foesocial_d, codigo_do_servico_referente_a_foservicos, codigo_da_empresa_do_servico_referente_a | ✔ |
| `foesocial_arquivo_retorno_s_5003_base_servicos_ma_0eb6_consultar` | consultar | foesocial_arquivo_retorno_s_5003_base_servicos_matricula | empresa | ✔ |
| `foesocial_arquivo_retorno_s_5003_base_servicos_matricula_obter` | obter | foesocial_arquivo_retorno_s_5003_base_servicos_matricula | empresa, codigo_do_evento_referente_a_foesocial_d, codigo_do_servico_referente_a_foservicos, matricula, codigo_da_empresa_do_servico_referente_a, sequencial_para_registros_repetidos | ✔ |
| `foesocial_arquivo_retorno_s_5003_base_servicos_ma_eb2a_consultar` | consultar | foesocial_arquivo_retorno_s_5003_base_servicos_matricula_valor | empresa | ✔ |
| `foesocial_arquivo_retorno_s_5003_base_servicos_matric_eb2a_obter` | obter | foesocial_arquivo_retorno_s_5003_base_servicos_matricula_valor | empresa, codigo_do_evento_referente_a_foesocial_d, codigo_do_servico_referente_a_foservicos, matricula, tipo_do_valor, codigo_da_empresa_do_servico_referente_a | ✔ |
| `foesocial_arquivo_retorno_s_5003_base_servicos_matri_eb2a_totais` | totais | foesocial_arquivo_retorno_s_5003_base_servicos_matricula_valor | empresa | ✔ |
| `foesocial_arquivo_retorno_s_5003_matricula_consultar` | consultar | foesocial_arquivo_retorno_s_5003_matricula | empresa | ✔ |
| `foesocial_arquivo_retorno_s_5003_matricula_obter` | obter | foesocial_arquivo_retorno_s_5003_matricula | empresa, codigo_do_evento_referente_a_foesocial_d, matricula | ✔ |
| `foesocial_arquivo_retorno_s_5003_matricula_valor_consultar` | consultar | foesocial_arquivo_retorno_s_5003_matricula_valor | empresa | ✔ |
| `foesocial_arquivo_retorno_s_5003_matricula_valor_obter` | obter | foesocial_arquivo_retorno_s_5003_matricula_valor | empresa, codigo_do_evento_referente_a_foesocial_d, matricula, codigo_da_categoria, tipo_de_deposito_de_fgts | ✔ |
| `foesocial_arquivo_retorno_s_5003_matricula_valor_totais` | totais | foesocial_arquivo_retorno_s_5003_matricula_valor | empresa | ✔ |
| `foesocial_avisos_vencimento_fechamento_periodo_consultar` | consultar | foesocial_avisos_vencimento_fechamento_periodo | empresa | ✔ |
| `foesocial_avisos_vencimento_fechamento_periodo_obter` | obter | foesocial_avisos_vencimento_fechamento_periodo | empresa, competencia, tipo_de_calculo_0_mensal_1_anual | ✔ |
| `foesocial_configuracao_agente_consultar` | consultar | foesocial_configuracao_agente | — | ✔ |
| `foesocial_controle_periodos_consultar` | consultar | foesocial_controle_periodos | empresa | ✔ |
| `foesocial_controle_periodos_obter` | obter | foesocial_controle_periodos | empresa, competencia, tipo_processo_enviar_para_o_esocial | ✔ |
| `foesocial_controle_periodos_dados_eventos_consultar` | consultar | foesocial_controle_periodos_dados_eventos | empresa | ✔ |
| `foesocial_controle_periodos_dados_eventos_obter` | obter | foesocial_controle_periodos_dados_eventos | empresa, competencia, sequencial_de_envio_ao_esocial | ✔ |
| `foesocial_controle_periodos_envios_esocial_consultar` | consultar | foesocial_controle_periodos_envios_esocial | empresa | ✔ |
| `foesocial_controle_periodos_envios_esocial_obter` | obter | foesocial_controle_periodos_envios_esocial | empresa, competencia, tipo_da_folha, codigo_da_empresa_referente_a_foesocial, codigo_do_evento_referente_a_foesocial_d | ✔ |
| `foesocial_controle_versao_consultar` | consultar | foesocial_controle_versao | — | ✔ |
| `foesocial_controle_versao_obter` | obter | foesocial_controle_versao | data_da_ultima_consulta_de_versoes | ✔ |
| `foesocial_dados_eventos_tabelas_relacionadas_consultar` | consultar | foesocial_dados_eventos_tabelas_relacionadas | empresa | ✔ |
| `foesocial_dados_eventos_tabelas_relacionadas_obter` | obter | foesocial_dados_eventos_tabelas_relacionadas | empresa, codigo_do_registro_de_envio, sequencial | ✔ |
| `foesocial_dados_eventos_validados_manualmente_consultar` | consultar | foesocial_dados_eventos_validados_manualmente | empresa | ✔ |
| `foesocial_dados_eventos_validados_manualmente_obter` | obter | foesocial_dados_eventos_validados_manualmente | empresa, codigo_do_dado_evento_da_tabela_foesocia | ✔ |
| `foesocial_erros_validacao_xml_consultar` | consultar | foesocial_erros_validacao_xml | empresa | ✔ |
| `foesocial_erros_validacao_xml_obter` | obter | foesocial_erros_validacao_xml | empresa, sequencial_de_erros_do_registro | ✔ |
| `foesocial_eventos_antecessores_consultar` | consultar | foesocial_eventos_antecessores | — | ✔ |
| `foesocial_eventos_antecessores_obter` | obter | foesocial_eventos_antecessores | codigo_do_evento_do_esocial, codigo_do_evento_do_esocial_antecessor | ✔ |
| `foesocial_fila_eventos_gerar_consultar` | consultar | foesocial_fila_eventos_gerar | empresa | ✔ |
| `foesocial_fila_eventos_gerar_obter` | obter | foesocial_fila_eventos_gerar | empresa, codigo_do_evento_do_esocial, sequencial | ✔ |
| `foesocial_fila_eventos_gerar_rubricas_consultar` | consultar | foesocial_fila_eventos_gerar_rubricas | empresa | ✔ |
| `foesocial_fila_eventos_gerar_rubricas_obter` | obter | foesocial_fila_eventos_gerar_rubricas | empresa, codigo_do_evento_esocial, sequencial, codigo_da_rubrica | ✔ |
| `foesocial_fila_eventos_gerar_selecao_1200_consultar` | consultar | foesocial_fila_eventos_gerar_selecao_1200 | empresa | ✔ |
| `foesocial_fila_eventos_gerar_selecao_1200_obter` | obter | foesocial_fila_eventos_gerar_selecao_1200 | empresa, codigo_do_evento_do_esocial, sequencial, cpf | ✔ |
| `foesocial_importacao_sst_log_consultar` | consultar | foesocial_importacao_sst_log | empresa | ✔ |
| `foesocial_importacao_sst_log_obter` | obter | foesocial_importacao_sst_log | empresa, codigo_sequencial_do_log | ✔ |
| `foesocial_importacoes_consultar` | consultar | foesocial_importacoes | empresa | ✔ |
| `foesocial_importacoes_colaboradores_consultar` | consultar | foesocial_importacoes_colaboradores | empresa | ✔ |
| `foesocial_importacoes_colaboradores_obter` | obter | foesocial_importacoes_colaboradores | empresa, codigo_do_colaborador | ✔ |
| `foesocial_importacoes_colaboradores_log_consultar` | consultar | foesocial_importacoes_colaboradores_log | empresa | ✔ |
| `foesocial_importacoes_colaboradores_log_obter` | obter | foesocial_importacoes_colaboradores_log | empresa, codigo_do_evento_esocial, data_de_criacao_do_evento_esocial_trata, codigo_do_colaborador | ✔ |
| `foesocial_importacoes_log_consultar` | consultar | foesocial_importacoes_log | empresa | ✔ |
| `foesocial_importacoes_log_obter` | obter | foesocial_importacoes_log | empresa, codigo_do_log | ✔ |
| `foesocial_importacoes_mensagens_consultar` | consultar | foesocial_importacoes_mensagens | empresa | ✔ |
| `foesocial_importacoes_mensagens_obter` | obter | foesocial_importacoes_mensagens | empresa, codigo_da_mensagem | ✔ |
| `foesocial_ingestao_carga_consultar` | consultar | foesocial_ingestao_carga | empresa | ✔ |
| `foesocial_ingestao_carga_totais` | totais | foesocial_ingestao_carga | empresa | ✔ |
| `foesocial_ingestao_eventos_consultar` | consultar | foesocial_ingestao_eventos | empresa | ✔ |
| `foesocial_ingestao_eventos_obter` | obter | foesocial_ingestao_eventos | empresa, identificador_unico_do_evento_eventid_uu | ✔ |
| `foesocial_ingestao_eventos_totais` | totais | foesocial_ingestao_eventos | empresa | ✔ |
| `foesocial_log_consultar` | consultar | foesocial_log | empresa | ✔ |
| `foesocial_log_obter` | obter | foesocial_log | empresa, identificador_unico_do_log | ✔ |
| `foesocial_log_thread_execucao_consultar` | consultar | foesocial_log_thread_execucao | — | ✔ |
| `foesocial_log_thread_execucao_obter` | obter | foesocial_log_thread_execucao | identificador_unico_do_log | ✔ |
| `foesocial_log_thread_execucao_linha_consultar` | consultar | foesocial_log_thread_execucao_linha | — | ✔ |
| `foesocial_log_thread_execucao_linha_obter` | obter | foesocial_log_thread_execucao_linha | identificador_unico_do_log_referente_a_f, codigo_sequencial_da_linha | ✔ |
| `foesocial_log_thread_linha_detalhe_consultar` | consultar | foesocial_log_thread_linha_detalhe | — | ✔ |
| `foesocial_log_thread_linha_detalhe_obter` | obter | foesocial_log_thread_linha_detalhe | identificador_unico_do_log_referente_a_f, codigo_sequencial_da_linha_referente_a_f, codigo_sequencial_do_detalhe | ✔ |
| `foesocial_lotes_envios_consultar` | consultar | foesocial_lotes_envios | empresa | ✔ |
| `foesocial_lotes_envios_obter` | obter | foesocial_lotes_envios | empresa, codigo_do_lote, sequencial_de_envio | ✔ |
| `foesocial_lotes_envios_ocorrencias_consultar` | consultar | foesocial_lotes_envios_ocorrencias | empresa | ✔ |
| `foesocial_lotes_envios_ocorrencias_obter` | obter | foesocial_lotes_envios_ocorrencias | empresa, codigo_do_lote, sequencial_de_envio, tipo_de_ocorrencia_1_envio_2_consulta, sequencial_de_ocorrencia | ✔ |
| `foesocial_tabelas_controle_consultar` | consultar | foesocial_tabelas_controle | — | ✔ |
| `foesocial_tabelas_controle_obter` | obter | foesocial_tabelas_controle | nome_da_tabela | ✔ |
