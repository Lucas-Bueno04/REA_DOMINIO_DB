# GEBACKUP_NUVEM_BACKUPS — Tabela com os processos de backup.
11.314 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| SEQUENCIAL | uniqueidentifier(16) | PK |  | Chave primária. |
| DATA_HORA_AGENDADA | timestamp(8) |  |  | Data e hora agendada para realização do backup. |
| TIPO | integer(4) |  |  | Tipo do backup: 1 - Modificações, 2 - Completo. |
| SITUACAO | integer(4) |  |  | Situação do backup relacionada com a tabela GEBACKUP_NUVEM_BACKUPS_SITUACOES. |
| PRAZO | integer(4) |  |  | Prazo da execução do backup: -1 - Backup atrasado, 0 - Backup em dia, 1 - Backup reagendado |
| CAMINHO_ARQUIVO_RESULTADO | varchar(512) |  | S | Caminho do arquivo compactado para upload. |
| TAMANHO_ARQUIVO | bigint(8) |  | S | Tamanho do arquivo resultado. |
| HASH_ARQUIVO_RESULTADO | varchar(40) |  | S | Hash do CheckSum do arquivo compactado para upload. |
| SENHA_ARQUIVO_COMPACTADO | varchar(32) |  | S | Senha do arquivo compactado. |
| QUANTIDADE_TENTATIVA_REENVIO | integer(4) |  |  | Quantidade de tentativas de reenvio realizadas até o envio com sucesso. |
| DATA_HORA_ULTIMA_MUDANCA_SITUACAO | timestamp(8) |  |  | Data e hora da última mudança de situação do backup |
| UPLOAD_ID | varchar(512) |  | S | Upload ID gerado pelo S3 |
| HASH_ARQUIVO_RESULTADO_S3 | varchar(40) |  | S | Hash do CheckSum gerado pela request de finalização do multipartUpload do S3. |
| ADAPTAR_UPLOAD_PARA_S3 | integer(4) |  |  | 1- Não adaptado ou concluido antes da alteração para o S3; 2- Adaptado; 3- nativo |
