# Módulo `geral_backup`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `gebackup_nuvem_agenda_consultar` | consultar | gebackup_nuvem_agenda | — | ✔ |
| `gebackup_nuvem_agenda_obter` | obter | gebackup_nuvem_agenda | chave_primaria_para_linha_unica | ✔ |
| `gebackup_nuvem_backups_consultar` | consultar | gebackup_nuvem_backups | — | ✔ |
| `gebackup_nuvem_backups_obter` | obter | gebackup_nuvem_backups | chave_primaria | ✔ |
| `gebackup_nuvem_backups_totais` | totais | gebackup_nuvem_backups | — | ✔ |
| `gebackup_nuvem_backups_situacoes_consultar` | consultar | gebackup_nuvem_backups_situacoes | — | ✔ |
| `gebackup_nuvem_backups_situacoes_obter` | obter | gebackup_nuvem_backups_situacoes | chave_primaria | ✔ |
| `gebackup_nuvem_cliente_consultar` | consultar | gebackup_nuvem_cliente | — | ✔ |
| `gebackup_nuvem_cliente_obter` | obter | gebackup_nuvem_cliente | codigo_do_cliente_no_sgd | ✔ |
| `gebackup_nuvem_configuracoes_consultar` | consultar | gebackup_nuvem_configuracoes | — | ✔ |
| `gebackup_nuvem_configuracoes_obter` | obter | gebackup_nuvem_configuracoes | chave_primaria_para_linha_unica | ✔ |
| `gebackup_nuvem_configuracoes_totais` | totais | gebackup_nuvem_configuracoes | — | ✔ |
| `gebackup_nuvem_dados_envio_consultar` | consultar | gebackup_nuvem_dados_envio | — | ✔ |
| `gebackup_nuvem_dados_envio_obter` | obter | gebackup_nuvem_dados_envio | sequencial_auto_incremento | ✔ |
| `gebackup_nuvem_dados_envio_totais` | totais | gebackup_nuvem_dados_envio | — | ✔ |
| `gebackup_nuvem_estacao_vinculada_consultar` | consultar | gebackup_nuvem_estacao_vinculada | — | ✔ |
| `gebackup_nuvem_estacao_vinculada_obter` | obter | gebackup_nuvem_estacao_vinculada | chave_primaria_para_linha_unica | ✔ |
| `gebackup_nuvem_logs_consultar` | consultar | gebackup_nuvem_logs | — | ✔ |
| `gebackup_nuvem_logs_obter` | obter | gebackup_nuvem_logs | chave_primaria | ✔ |
| `gebackup_nuvem_logs_origens_consultar` | consultar | gebackup_nuvem_logs_origens | — | ✔ |
| `gebackup_nuvem_logs_origens_obter` | obter | gebackup_nuvem_logs_origens | codigo | ✔ |
| `gebackup_nuvem_notificacoes_configuracao_consultar` | consultar | gebackup_nuvem_notificacoes_configuracao | — | ✔ |
| `gebackup_nuvem_notificacoes_configuracao_obter` | obter | gebackup_nuvem_notificacoes_configuracao | chave_primaria_para_linha_unica | ✔ |
| `gebackup_nuvem_parada_processo_consultar` | consultar | gebackup_nuvem_parada_processo | — | ✔ |
| `gebackup_nuvem_parada_processo_obter` | obter | gebackup_nuvem_parada_processo | chave_primaria_para_linha_unica | ✔ |
| `gebackup_nuvem_tipo_dados_envio_consultar` | consultar | gebackup_nuvem_tipo_dados_envio | — | ✔ |
| `gebackup_nuvem_tipo_dados_envio_obter` | obter | gebackup_nuvem_tipo_dados_envio | codigo_do_tipo_de_dado_de_envio | ✔ |
| `gebackup_nuvem_versao_consultar` | consultar | gebackup_nuvem_versao | — | ✔ |
| `gebackup_nuvem_versao_obter` | obter | gebackup_nuvem_versao | chave_primaria_para_linha_unica | ✔ |
| `gebackup_realizado_consultar` | consultar | gebackup_realizado | — | ✔ |
| `gebackup_realizado_obter` | obter | gebackup_realizado | codigo_do_backup_auto_incrementado | ✔ |
