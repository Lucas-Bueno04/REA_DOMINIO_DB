# Módulo `geral_outros`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `geacoes_suporte_configuracoes_consultar` | consultar | geacoes_suporte_configuracoes | — | ✔ |
| `geacoes_suporte_configuracoes_obter` | obter | geacoes_suporte_configuracoes | codigo_unico | ✔ |
| `geacoes_suporte_configuracoes_totais` | totais | geacoes_suporte_configuracoes | — | ✔ |
| `geatendimento_contas_iceberg_consultar` | consultar | geatendimento_contas_iceberg | empresa | ✔ |
| `geatendimento_contas_iceberg_obter` | obter | geatendimento_contas_iceberg | empresa, codigo_de_identificacao_do_banco | ✔ |
| `geatendimento_publicar_documentos_consultar` | consultar | geatendimento_publicar_documentos | — | ✔ |
| `geatendimento_publicar_documentos_obter` | obter | geatendimento_publicar_documentos | i_documento | ✔ |
| `geatendimento_publicar_documentos_totais` | totais | geatendimento_publicar_documentos | — | ✔ |
| `geatendimentocolunas_tipos_consultar` | consultar | geatendimentocolunas_tipos | — | ✔ |
| `geatendimentocolunas_tipos_obter` | obter | geatendimentocolunas_tipos | codigo | ✔ |
| `geatendimentolog_frp_consultar` | consultar | geatendimentolog_frp | — | ✔ |
| `geatendimentolog_frp_obter` | obter | geatendimentolog_frp | codigo | ✔ |
| `geatendimentolog_frp_totais` | totais | geatendimentolog_frp | — | ✔ |
| `geatvsecundaria_vigencia_consultar` | consultar | geatvsecundaria_vigencia | empresa | ✔ |
| `geatvsecundaria_vigencia_obter` | obter | geatvsecundaria_vigencia | empresa, codigo_cnae, data_da_vigencia | ✔ |
| `gebuscanfe_controle_acesso_consultar` | consultar | gebuscanfe_controle_acesso | — | ✔ |
| `gebuscanfe_controle_acesso_obter` | obter | gebuscanfe_controle_acesso | data_da_ultima_tentativa_ou_conclusao_de | ✔ |
| `gecampo_cabecalho_auditor_consultar` | consultar | gecampo_cabecalho_auditor | — | ✔ |
| `gecampo_cabecalho_auditor_obter` | obter | gecampo_cabecalho_auditor | codigo_do_campo | ✔ |
| `gecheckpoint_comparativo_regime_tributacao_consultar` | consultar | gecheckpoint_comparativo_regime_tributacao | empresa | ✔ |
| `gecheckpoint_comparativo_regime_tributacao_obter` | obter | gecheckpoint_comparativo_regime_tributacao | empresa, ano_calendario, mes | ✔ |
| `gecheckpoint_comparativo_regime_tributacao_totais` | totais | gecheckpoint_comparativo_regime_tributacao | empresa | ✔ |
| `gecheckpoint_comparativo_regime_tributacao_saldo_consultar` | consultar | gecheckpoint_comparativo_regime_tributacao_saldo | empresa | ✔ |
| `gecheckpoint_comparativo_regime_tributacao_saldo_obter` | obter | gecheckpoint_comparativo_regime_tributacao_saldo | empresa, coluna | ✔ |
| `gecheckpoint_comparativo_regime_tributacao_saldo_totais` | totais | gecheckpoint_comparativo_regime_tributacao_saldo | empresa | ✔ |
| `gecheckpoint_incentivos_fiscais_cnae_consultar` | consultar | gecheckpoint_incentivos_fiscais_cnae | — | ✔ |
| `gecheckpoint_incentivos_fiscais_cnae_obter` | obter | gecheckpoint_incentivos_fiscais_cnae | cnae22, campo_site | ✔ |
| `gecnae_classificacao_tributaria_consultar` | consultar | gecnae_classificacao_tributaria | — | ✔ |
| `gecnae_classificacao_tributaria_obter` | obter | gecnae_classificacao_tributaria | i_cnae20 | ✔ |
| `gecnae_previdencia_social_consultar` | consultar | gecnae_previdencia_social | — | ✔ |
| `gecnae_previdencia_social_obter` | obter | gecnae_previdencia_social | codigo_cnae | ✔ |
| `gecomunicador_web_parada_processo_consultar` | consultar | gecomunicador_web_parada_processo | — | ✔ |
| `gecomunicador_web_parada_processo_obter` | obter | gecomunicador_web_parada_processo | codigo | ✔ |
| `gecomunicador_web_parada_processo_totais` | totais | gecomunicador_web_parada_processo | — | ✔ |
| `gecomunicador_web_processo_consultar` | consultar | gecomunicador_web_processo | — | ✔ |
| `gecomunicador_web_processo_obter` | obter | gecomunicador_web_processo | codigo | ✔ |
| `geconfiguracao_envio_email_consultar` | consultar | geconfiguracao_envio_email | — | ✔ |
| `geconfiguracao_envio_email_obter` | obter | geconfiguracao_envio_email | codigo_para_controle_de_linha_unica | ✔ |
| `geconfiguracao_envio_email_parametros_usuarios_consultar` | consultar | geconfiguracao_envio_email_parametros_usuarios | — | ✔ |
| `geconfiguracao_envio_email_parametros_usuarios_obter` | obter | geconfiguracao_envio_email_parametros_usuarios | codigo_do_usuario, tipo_usuario | ✔ |
| `gecontador_envios_esocial_consultar` | consultar | gecontador_envios_esocial | — | ✔ |
| `gecontador_envios_esocial_obter` | obter | gecontador_envios_esocial | codi_con, codi_emp_dados_eventos, i_dados_eventos | ✔ |
| `gecsperguntas_solucoes_consultar` | consultar | gecsperguntas_solucoes | — | ✔ |
| `gecsperguntas_solucoes_obter` | obter | gecsperguntas_solucoes | id | ✔ |
| `gecsperguntas_solucoes_totais` | totais | gecsperguntas_solucoes | — | ✔ |
| `gecsultima_verificacao_consultar` | consultar | gecsultima_verificacao | — | ✔ |
| `gecsultima_verificacao_obter` | obter | gecsultima_verificacao | ultima_verificacao | ✔ |
| `gecsversao_tabelas_consultar` | consultar | gecsversao_tabelas | — | ✔ |
| `gecsversao_tabelas_obter` | obter | gecsversao_tabelas | id | ✔ |
| `gedados_auditor_consultar` | consultar | gedados_auditor | — | ✔ |
| `gedados_auditor_obter` | obter | gedados_auditor | chave_primaria | ✔ |
| `gedados_reforma_tributaria_consultar` | consultar | gedados_reforma_tributaria | — | ✔ |
| `gedados_reforma_tributaria_obter` | obter | gedados_reforma_tributaria | chave_primaria | ✔ |
| `gedctf_web_pagamento_consultar` | consultar | gedctf_web_pagamento | empresa | ✔ |
| `gedctf_web_pagamento_obter` | obter | gedctf_web_pagamento | empresa, competencia, tipo_de_guia_1_mensal_2_13o_salario_3_tr, sequencial_do_pagamento, sequencial | ✔ |
| `gedctf_web_pagamento_totais` | totais | gedctf_web_pagamento | empresa | ✔ |
| `gedctf_web_pagamento_lancto_consultar` | consultar | gedctf_web_pagamento_lancto | empresa | ✔ |
| `gedctf_web_pagamento_lancto_obter` | obter | gedctf_web_pagamento_lancto | empresa, numero_lancamento, empresa_do_pagamento, competencia, tipo_de_guia_1_mensal_2_13o_salario_3_tr, sequencial_do_pagamento, sequencial | ✔ |
| `gedctf_web_pagamento_lancto_totais` | totais | gedctf_web_pagamento_lancto | empresa | ✔ |
| `gediagnostico_performance_ct_consultar` | consultar | gediagnostico_performance_ct | empresa | ✔ |
| `gediagnostico_performance_ct_obter` | obter | gediagnostico_performance_ct | empresa, identificador_unico_do_registro | ✔ |
| `gediagnostico_performance_ct_totais` | totais | gediagnostico_performance_ct | empresa | ✔ |
| `gediagnostico_processamento_consultar` | consultar | gediagnostico_processamento | empresa | ✔ |
| `gediagnostico_processamento_obter` | obter | gediagnostico_processamento | empresa, competencia_data, funcionalidade_apuracao_folhapagamento | ✔ |
| `geempresas_moduloweb_consultar` | consultar | geempresas_moduloweb | empresa | ✔ |
| `geestacoes_moduloweb_consultar` | consultar | geestacoes_moduloweb | — | ✔ |
| `geestacoes_moduloweb_obter` | obter | geestacoes_moduloweb | i_confusuario, tipo, macadress | ✔ |
| `gefarois_atendimento_consultar` | consultar | gefarois_atendimento | — | ✔ |
| `gefarois_atendimento_obter` | obter | gefarois_atendimento | coluna_depreciada_nao_representa_o_codig | ✔ |
| `gefarol_ss_usuario_atendimento_consultar` | consultar | gefarol_ss_usuario_atendimento | — | ✔ |
| `gefarol_ss_usuario_atendimento_obter` | obter | gefarol_ss_usuario_atendimento | codigo_usuario | ✔ |
| `gefarol_ss_usuario_atendimento_onvio_consultar` | consultar | gefarol_ss_usuario_atendimento_onvio | — | ✔ |
| `gefarol_ss_usuario_atendimento_onvio_obter` | obter | gefarol_ss_usuario_atendimento_onvio | codigo_guid_do_usuario_no_onvio | ✔ |
| `geferiados_febraban_consultar` | consultar | geferiados_febraban | — | ✔ |
| `geferiados_febraban_obter` | obter | geferiados_febraban | codigo_sequencial_auto_incremental | ✔ |
| `gegerencia_versoes_consultar` | consultar | gegerencia_versoes | — | ✔ |
| `gegerencia_versoes_obter` | obter | gegerencia_versoes | sequencial | ✔ |
| `gegestta_atividade_consultar` | consultar | gegestta_atividade | — | ✔ |
| `gegestta_atividade_obter` | obter | gegestta_atividade | codigo | ✔ |
| `gegestta_atividade_totais` | totais | gegestta_atividade | — | ✔ |
| `geibge_tipo_obras_servicos_consultar` | consultar | geibge_tipo_obras_servicos | — | ✔ |
| `geibge_tipo_obras_servicos_obter` | obter | geibge_tipo_obras_servicos | codigo | ✔ |
| `geindice_diario_consultar` | consultar | geindice_diario | — | ✔ |
| `geindice_diario_obter` | obter | geindice_diario | codigo_do_indice, data | ✔ |
| `geindice_diario_totais` | totais | geindice_diario | — | ✔ |
| `geindice_medio_consultar` | consultar | geindice_medio | — | ✔ |
| `geindice_medio_obter` | obter | geindice_medio | codigo_do_indice, data | ✔ |
| `geindice_medio_totais` | totais | geindice_medio | — | ✔ |
| `geinformacoes_modulos_consultar` | consultar | geinformacoes_modulos | — | ✔ |
| `geinformacoes_modulos_obter` | obter | geinformacoes_modulos | i_modulo | ✔ |
| `geinformacoes_sgd_modulo_bloqueado_consultar` | consultar | geinformacoes_sgd_modulo_bloqueado | — | ✔ |
| `geinformacoes_sgd_modulo_bloqueado_obter` | obter | geinformacoes_sgd_modulo_bloqueado | sequencial | ✔ |
| `genotificacoes_usuario_atendimento_consultar` | consultar | genotificacoes_usuario_atendimento | — | ✔ |
| `genotificacoes_usuario_atendimento_obter` | obter | genotificacoes_usuario_atendimento | sequencial | ✔ |
| `geonvio_dados_sessao_company_consultar` | consultar | geonvio_dados_sessao_company | — | ✔ |
| `geonvio_dados_sessao_company_obter` | obter | geonvio_dados_sessao_company | chave | ✔ |
| `gepastas_moduloweb_consultar` | consultar | gepastas_moduloweb | — | ✔ |
| `gepastas_moduloweb_obter` | obter | gepastas_moduloweb | modulo, departamento, janela, pasta | ✔ |
| `geperfil_empresa_consultar` | consultar | geperfil_empresa | — | ✔ |
| `geperfil_empresa_obter` | obter | geperfil_empresa | sequencial | ✔ |
| `geperfil_empresa_modulo_consultar` | consultar | geperfil_empresa_modulo | empresa | ✔ |
| `geperfil_empresa_modulo_obter` | obter | geperfil_empresa_modulo | empresa, sequencial_do_perfil, sequencial_do_modulo | ✔ |
| `gepermissoes_usuario_atendimento_consultar` | consultar | gepermissoes_usuario_atendimento | — | ✔ |
| `gepermissoes_usuario_atendimento_obter` | obter | gepermissoes_usuario_atendimento | codigo_usuario, usuario | ✔ |
| `geprocessando_digial_bank_consultar` | consultar | geprocessando_digial_bank | — | ✔ |
| `geprocessando_digial_bank_obter` | obter | geprocessando_digial_bank | usuario | ✔ |
| `geprperguntas_respostas_consultar` | consultar | geprperguntas_respostas | — | ✔ |
| `geprperguntas_respostas_obter` | obter | geprperguntas_respostas | id | ✔ |
| `geprultima_verificacao_consultar` | consultar | geprultima_verificacao | — | ✔ |
| `geprultima_verificacao_obter` | obter | geprultima_verificacao | ultima_verificacao | ✔ |
| `geprversao_tabelas_consultar` | consultar | geprversao_tabelas | — | ✔ |
| `geprversao_tabelas_obter` | obter | geprversao_tabelas | id | ✔ |
| `gequadrosocietario_socios_representante_legal_consultar` | consultar | gequadrosocietario_socios_representante_legal | empresa | ✔ |
| `gequadrosocietario_socios_representante_legal_obter` | obter | gequadrosocietario_socios_representante_legal | empresa, data, socio, tipo_s_socio_a_administrador_r_represent, sequencial | ✔ |
| `gerarotinas_processos_consultar` | consultar | gerarotinas_processos | — | ✔ |
| `gerarotinas_processos_obter` | obter | gerarotinas_processos | codigo_da_rotina, codigo_do_sistema, i_processos | ✔ |
| `geselecao_empresas_contabil_consultar` | consultar | geselecao_empresas_contabil | — | ✔ |
| `geselecao_empresas_contabil_obter` | obter | geselecao_empresas_contabil | identificador_do_filtro, identificador_do_modulo_0_nao_filtra_por | ✔ |
| `geselecao_filtro_consultar` | consultar | geselecao_filtro | — | ✔ |
| `geselecao_filtro_obter` | obter | geselecao_filtro | sequencial_da_selecao, sequencial_do_tipo_de_selecao, sequencial_da_opcao_selecionar | ✔ |
| `gesieg_dados_sessao_company_consultar` | consultar | gesieg_dados_sessao_company | — | ✔ |
| `gesieg_dados_sessao_company_obter` | obter | gesieg_dados_sessao_company | chave | ✔ |
| `getabela_grupo_tributo_consultar` | consultar | getabela_grupo_tributo | — | ✔ |
| `getabela_grupo_tributo_obter` | obter | getabela_grupo_tributo | codigo_do_grupo_de_tributo | ✔ |
| `getabela_relacionamento_cnae_atividade_inss_consultar` | consultar | getabela_relacionamento_cnae_atividade_inss | — | ✔ |
| `getabela_relacionamento_cnae_atividade_inss_obter` | obter | getabela_relacionamento_cnae_atividade_inss | codigo_cnae, codigo_de_atividade_inss | ✔ |
| `getabelas_exclusao_empresa_consultar` | consultar | getabelas_exclusao_empresa | — | ✔ |
| `getipo_arquivo_auditor_consultar` | consultar | getipo_arquivo_auditor | — | ✔ |
| `getipo_arquivo_auditor_obter` | obter | getipo_arquivo_auditor | chave_primaria | ✔ |
| `getipo_selecao_consultar` | consultar | getipo_selecao | — | ✔ |
| `getipo_selecao_obter` | obter | getipo_selecao | sequencial_do_tipo_de_selecao | ✔ |
| `getipo_selecao_selecionar_consultar` | consultar | getipo_selecao_selecionar | — | ✔ |
| `getipo_selecao_selecionar_obter` | obter | getipo_selecao_selecionar | sequencial_do_tipo_de_selecao, sequencial_da_opcao_selecionar | ✔ |
| `gever_executado_consultar` | consultar | gever_executado | — | ✔ |
| `gever_executado_obter` | obter | gever_executado | codigo | ✔ |
| `geverificacao_exclusao_notas_contabil_consultar` | consultar | geverificacao_exclusao_notas_contabil | — | ✔ |
| `geverificacao_exclusao_notas_contabil_obter` | obter | geverificacao_exclusao_notas_contabil | codigo_sequencial_das_configuracoes | ✔ |
| `geversao_agente_consultar` | consultar | geversao_agente | — | ✔ |
| `geversao_agente_obter` | obter | geversao_agente | codigo | ✔ |
| `gexcount_log_comunicacao_consultar` | consultar | gexcount_log_comunicacao | empresa | ✔ |
| `gexcount_log_comunicacao_obter` | obter | gexcount_log_comunicacao | empresa, codigo_sequencial_de_erros | ✔ |
| `usconfusuario_configurado_consultar` | consultar | usconfusuario_configurado | — | ✔ |
| `usconfusuario_configurado_obter` | obter | usconfusuario_configurado | codigo, tipo, codigo_do_modulo | ✔ |
| `usconfusuario_expediente_consultar` | consultar | usconfusuario_expediente | — | ✔ |
| `usconfusuario_expediente_obter` | obter | usconfusuario_expediente | codi_tipo_usuario, codi_usuario, codi_exigencia | ✔ |
| `usconfusuario_preferencias_consultar` | consultar | usconfusuario_preferencias | — | ✔ |
| `usconfusuario_preferencias_obter` | obter | usconfusuario_preferencias | codigo_do_tipo_de_usuario, codigo_do_usuario | ✔ |
