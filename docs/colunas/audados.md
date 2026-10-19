# audados — Movimentos da auditoria
31.761.864 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| sequencial | numeric(15) | PK |  | Sequencial |
| table_id | integer(4) |  |  | Codigo da tabela |
| codi_emp | integer(4) |  |  | Empresa |
| usuario | char(30) |  |  | Usuario |
| data_hora | timestamp(8) |  |  | Data/Hora do Movimento |
| tipo | tinyint(1) |  |  | Tipo do movimento (1 - Inclusao/2 - Alteracao/3 - Exclusao) |
| conteudo | long varchar(32767) |  |  | Conteudo do movimento |
