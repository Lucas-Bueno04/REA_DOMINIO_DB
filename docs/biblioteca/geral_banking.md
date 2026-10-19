# Módulo `geral_banking`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `gebanking_acoes_empregados_consultar` | consultar | gebanking_acoes_empregados | empresa | ✔ |
| `gebanking_acoes_empregados_obter` | obter | gebanking_acoes_empregados | empresa, codigo_sequencial_do_registro | ✔ |
| `gebanking_dados_fintech_consultar` | consultar | gebanking_dados_fintech | empresa | ✔ |
| `gebanking_dados_fintech_obter` | obter | gebanking_dados_fintech | empresa, guid_do_escritorio | ✔ |
| `gebanking_feature_flag_consultar` | consultar | gebanking_feature_flag | — | ✔ |
| `gebanking_feature_flag_obter` | obter | gebanking_feature_flag | nome_da_feature_flag | ✔ |
| `gebanking_log_temporario_consultar` | consultar | gebanking_log_temporario | empresa | ✔ |
| `gebanking_log_temporario_obter` | obter | gebanking_log_temporario | empresa, sequencial_auto_incremental | ✔ |
