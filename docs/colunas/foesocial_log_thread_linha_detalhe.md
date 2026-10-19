# FOESOCIAL_LOG_THREAD_LINHA_DETALHE — Tabela de log das threads relacionadas com o eSocial
5.261 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| ID_LOG_THREAD_EXECUCAO | uniqueidentifier(16) | PK |  | Identificador único do log referente a FOESOCIAL_LOG_THREAD_EXECUCAO_LINHA |
| SEQUENCIAL_LINHA | integer(4) | PK |  | Código sequencial da linha referente a FOESOCIAL_LOG_THREAD_EXECUCAO_LINHA |
| SEQUENCIAL_DETALHE | integer(4) | PK |  | Código sequencial do detalhe |
| DATA_HORA | timestamp(8) |  |  | Data e hora |
| MENSAGEM | varchar(200) |  |  | Mensagem |
