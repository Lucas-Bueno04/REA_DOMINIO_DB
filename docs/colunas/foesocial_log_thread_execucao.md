# FOESOCIAL_LOG_THREAD_EXECUCAO — Tabela de log das threads relacionadas com o eSocial
44.897 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| ID_LOG_THREAD_EXECUCAO | uniqueidentifier(16) | PK |  | Identificador único do log |
| SEQUENCIAL_EXECUCAO_THREAD | integer(4) |  |  | Sequencial de execução da thread |
| DATA_HORA_INICIO | timestamp(8) |  |  | Data e hora inicial |
| DATA_HORA_FIM | timestamp(8) |  | S | Data e hora final |
| ID_CONEXAO | integer(4) |  | S | ID da conexão |
| USER_CONEXAO | varchar(80) |  | S | Usuário da conexão |
| NAME_CONEXAO | varchar(80) |  | S | Nome da conexão |
| USER_CONTABIL | varchar(80) |  | S | Usuário do contábil |
