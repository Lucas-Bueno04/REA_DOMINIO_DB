# GEBACKUP_NUVEM_LOGS — Tabela com os processos de backup.
5.081 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| SEQUENCIAL | bigint(8) | PK |  | Chave primária. |
| MENSAGEM | long varchar(32767) |  | S | Mensagem emitida pelo LOG. |
| DATA_HORA | timestamp(8) |  |  | Data e hora do registro do LOG. |
| TIPO | integer(4) |  |  |  |
| ORIGEM | integer(4) |  |  | Origem do log referenciado na tabela GEBACKUP_NUVEM_LOGS_ORIGENS |
| SEQUENCIAL_BACKUP | uniqueidentifier(16) |  | S | Chave primária do backup que gerou o LOG. |
| SITUACAO_BACKUP | integer(4) |  |  | Situacao atual do backup relacionada com a tabela GEBACKUP_NUVEM_BACKUPS_SITUACOES quando o LOG foi gerado. |
| SEQUENCIAL_DADO_ENVIO | bigint(8) |  |  | Tipo do log: 0 - Informação, 1 - Callback, -1 - Erro |
