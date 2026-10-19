# Módulo `pessoal_rescisoes`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `forescisoes_envios_esocial_consultar` | consultar | forescisoes_envios_esocial | empresa | ✔ |
| `forescisoes_envios_esocial_obter` | obter | forescisoes_envios_esocial | empresa, codigo_do_empregado, tipo_de_rescisao, codigo_da_empresa_referente_a_foesocial, codigo_do_evento_referente_a_foesocial_d, codigo_do_calculo | ✔ |
| `forescisoes_simulacao_consultar` | consultar | forescisoes_simulacao | empresa | ✔ |
| `forescisoes_simulacao_obter` | obter | forescisoes_simulacao | empresa, empregado, tipo_de_calculo_de_rescisao_1_normal_2_c, codigo_do_calculo | ✔ |
| `forescisoes_simulacao_totais` | totais | forescisoes_simulacao | empresa | ✔ |
| `forescisoes_termo_consultar` | consultar | forescisoes_termo | empresa | ✔ |
| `forescisoes_termo_obter` | obter | forescisoes_termo | empresa, codigo_do_empregado, tipo_de_calculo_de_rescisao_1_normal_2_c, codigo_do_calculo | ✔ |
| `forescisoes_termo_totais` | totais | forescisoes_termo | empresa | ✔ |
| `forescisoes_termo_configuracao_consultar` | consultar | forescisoes_termo_configuracao | empresa | ✔ |
| `forescisoes_termo_configuracao_obter` | obter | forescisoes_termo_configuracao | empresa, modelo_1_trct_portaria_mte_1621_2010_ane | ✔ |
| `forescisoes_termo_configuracao_campos_consultar` | consultar | forescisoes_termo_configuracao_campos | empresa | ✔ |
| `forescisoes_termo_configuracao_campos_obter` | obter | forescisoes_termo_configuracao_campos | empresa, nome_codigo_do_campo, modelo_1_trct_portaria_mte_1621_2010_ane | ✔ |
| `forescisoes_termo_ferias_vencidas_consultar` | consultar | forescisoes_termo_ferias_vencidas | empresa | ✔ |
| `forescisoes_termo_ferias_vencidas_obter` | obter | forescisoes_termo_ferias_vencidas | empresa, codigo_do_empregado, tipo_de_calculo_de_rescisao_1_normal_2_c, codigo_do_periodo_aquisitivo, codigo_do_calculo | ✔ |
| `forescisoes_termo_ferias_vencidas_totais` | totais | forescisoes_termo_ferias_vencidas | empresa | ✔ |
| `forescisoes_termo_ferias_vencidas_simulacao_consultar` | consultar | forescisoes_termo_ferias_vencidas_simulacao | empresa | ✔ |
| `forescisoes_termo_ferias_vencidas_simulacao_obter` | obter | forescisoes_termo_ferias_vencidas_simulacao | empresa, codigo_do_empregado, tipo_da_rescisao, codigo_do_periodo_aquisitivo, codigo_do_calculo | ✔ |
| `forescisoes_termo_ferias_vencidas_simulacao_totais` | totais | forescisoes_termo_ferias_vencidas_simulacao | empresa | ✔ |
| `forescisoes_termo_simulacao_consultar` | consultar | forescisoes_termo_simulacao | empresa | ✔ |
| `forescisoes_termo_simulacao_obter` | obter | forescisoes_termo_simulacao | empresa, codigo_do_empregado, tipo_da_rescisao, codigo_do_calculo | ✔ |
| `forescisoes_termo_simulacao_totais` | totais | forescisoes_termo_simulacao | empresa | ✔ |
