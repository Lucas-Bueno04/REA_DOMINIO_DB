# Módulo `geral_atendimento`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `geatendimento_bancos_iceberg_consultar` | consultar | geatendimento_bancos_iceberg | — | ✔ |
| `geatendimento_bancos_iceberg_obter` | obter | geatendimento_bancos_iceberg | codigo_da_instituicao_financeira | ✔ |
| `geatendimento_bloco_informacoes_consultar` | consultar | geatendimento_bloco_informacoes | — | ✔ |
| `geatendimento_bloco_informacoes_obter` | obter | geatendimento_bloco_informacoes | id_bloco_informacoes | ✔ |
| `geatendimento_codigo_empresa_consultar` | consultar | geatendimento_codigo_empresa | — | ✔ |
| `geatendimento_controle_requisicoes_consultar` | consultar | geatendimento_controle_requisicoes | — | ✔ |
| `geatendimento_controle_requisicoes_obter` | obter | geatendimento_controle_requisicoes | sequencial_unico | ✔ |
| `geatendimento_dados_escritorio_consultar` | consultar | geatendimento_dados_escritorio | — | ✔ |
| `geatendimento_dados_escritorio_obter` | obter | geatendimento_dados_escritorio | codigo_do_cliente_do_sgd | ✔ |
| `geatendimento_dados_escritorio_historico_consultar` | consultar | geatendimento_dados_escritorio_historico | — | ✔ |
| `geatendimento_dados_escritorio_historico_obter` | obter | geatendimento_dados_escritorio_historico | sequencial | ✔ |
| `geatendimento_digitalbank_catalogo_consultar` | consultar | geatendimento_digitalbank_catalogo | empresa | ✔ |
| `geatendimento_digitalbank_catalogo_obter` | obter | geatendimento_digitalbank_catalogo | empresa, codi | ✔ |
| `geatendimento_digitalbank_catalogo_totais` | totais | geatendimento_digitalbank_catalogo | empresa | ✔ |
| `geatendimento_escritorio_consultar` | consultar | geatendimento_escritorio | — | ✔ |
| `geatendimento_escritorio_obter` | obter | geatendimento_escritorio | coluna_depreciada_nao_representa_o_codig | ✔ |
| `geatendimento_log_catalogo_consultar` | consultar | geatendimento_log_catalogo | — | ✔ |
| `geatendimento_log_catalogo_obter` | obter | geatendimento_log_catalogo | campo_auto_numeraaao_identificaaao_do_re | ✔ |
| `geatendimento_mimetype_consultar` | consultar | geatendimento_mimetype | — | ✔ |
| `geatendimento_mimetype_obter` | obter | geatendimento_mimetype | chave_primaria | ✔ |
| `geatendimento_onvio_empresas_ignoradas_consultar` | consultar | geatendimento_onvio_empresas_ignoradas | empresa | ✔ |
| `geatendimento_onvio_empresas_ignoradas_obter` | obter | geatendimento_onvio_empresas_ignoradas | empresa, sequencial_autoincremento | ✔ |
| `geatendimento_parar_servico_consultar` | consultar | geatendimento_parar_servico | — | ✔ |
| `geatendimento_parar_servico_obter` | obter | geatendimento_parar_servico | c_1_parar_serviao_2_iniciar_serviao_3_pa | ✔ |
| `geatendimento_plano_contas_contabilidade_consultar` | consultar | geatendimento_plano_contas_contabilidade | empresa | ✔ |
| `geatendimento_plano_contas_contabilidade_obter` | obter | geatendimento_plano_contas_contabilidade | empresa, codigo | ✔ |
| `geatendimento_sgd_notificacoes_consultar` | consultar | geatendimento_sgd_notificacoes | — | ✔ |
| `geatendimento_sgd_notificacoes_obter` | obter | geatendimento_sgd_notificacoes | codigo_auto_numeracao | ✔ |
| `geatendimento_sgd_notificacoes_usuarios_consultar` | consultar | geatendimento_sgd_notificacoes_usuarios | — | ✔ |
| `geatendimento_sgd_notificacoes_usuarios_obter` | obter | geatendimento_sgd_notificacoes_usuarios | codigo_auto_numeracao | ✔ |
| `geatendimento_sincronizar_dados_consultar` | consultar | geatendimento_sincronizar_dados | empresa | ✔ |
| `geatendimento_sincronizar_dados_obter` | obter | geatendimento_sincronizar_dados | empresa, i_acoes | ✔ |
| `geatendimento_sincronizar_empresas_da_consultar` | consultar | geatendimento_sincronizar_empresas_da | — | ✔ |
| `geatendimento_status_opcoes_barra_dominio_consultar` | consultar | geatendimento_status_opcoes_barra_dominio | — | ✔ |
| `geatendimento_status_opcoes_barra_dominio_obter` | obter | geatendimento_status_opcoes_barra_dominio | codigo_sempre_existira_apenas_uma_linha | ✔ |
| `geatendimento_status_servico_consultar` | consultar | geatendimento_status_servico | — | ✔ |
| `geatendimento_status_servico_obter` | obter | geatendimento_status_servico | pk_sempre_1_para_realizar_o_controle_de | ✔ |
| `geatendimento_telemetria_consultar` | consultar | geatendimento_telemetria | — | ✔ |
| `geatendimento_telemetria_obter` | obter | geatendimento_telemetria | codigo_unico_na_tabela | ✔ |
