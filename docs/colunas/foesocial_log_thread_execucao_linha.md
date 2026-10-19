# FOESOCIAL_LOG_THREAD_EXECUCAO_LINHA — Tabela de log das threads relacionadas com o eSocial
357.987 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| ID_LOG_THREAD_EXECUCAO | uniqueidentifier(16) | PK |  | Identificador único do log referente a FOESOCIAL_LOG_THREAD_EXECUCAO |
| SEQUENCIAL_LINHA | integer(4) | PK |  | Código sequencial da linha |
| DATA_HORA | timestamp(8) |  |  | Data e hora |
| TIPO_REGISTRO | integer(4) |  | S | Tipo de registro |
| MENSAGEM | varchar(200) |  |  | Mensagem |
