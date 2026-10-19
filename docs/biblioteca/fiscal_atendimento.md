# Módulo `fiscal_atendimento`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `efatendimento_nfe_catalogo_consultar` | consultar | efatendimento_nfe_catalogo | empresa | ✔ |
| `efatendimento_nfe_catalogo_obter` | obter | efatendimento_nfe_catalogo | empresa, codigo_do_catalogo | ✔ |
| `efatendimento_nfe_catalogo_totais` | totais | efatendimento_nfe_catalogo | empresa | ✔ |
| `efatendimento_nfe_catalogo_log_consultar` | consultar | efatendimento_nfe_catalogo_log | — | ✔ |
| `efatendimento_nfe_catalogo_log_obter` | obter | efatendimento_nfe_catalogo_log | sequencial_do_log | ✔ |
| `efatendimento_nfe_catalogo_visualizados_consultar` | consultar | efatendimento_nfe_catalogo_visualizados | empresa | ✔ |
| `efatendimento_nfe_catalogo_visualizados_obter` | obter | efatendimento_nfe_catalogo_visualizados | empresa, codigo_da_configuracao_do_usuario, tipo_da_configuracao_1_usuario_2_grupo, codigo_do_catalogo | ✔ |
| `efatendimento_nfe_controle_websocket_consultar` | consultar | efatendimento_nfe_controle_websocket | — | ✔ |
| `efatendimento_nfe_controle_websocket_obter` | obter | efatendimento_nfe_controle_websocket | data_pacote | ✔ |
| `efatendimento_nfe_empresa_consultar` | consultar | efatendimento_nfe_empresa | empresa | ✔ |
| `efatendimento_nfe_xml_consultar` | consultar | efatendimento_nfe_xml | — | ✔ |
| `efatendimento_nfe_xml_obter` | obter | efatendimento_nfe_xml | i_catalogo | ✔ |
| `efatendimento_nfe_xml_v2_consultar` | consultar | efatendimento_nfe_xml_v2 | — | ✔ |
| `efatendimento_nfe_xml_v2_obter` | obter | efatendimento_nfe_xml_v2 | i_catalogo | ✔ |
