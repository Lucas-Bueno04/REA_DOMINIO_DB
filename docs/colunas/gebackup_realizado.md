# GEBACKUP_REALIZADO — Log de ciência de backup pré atualização do banco
210 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_BACKUP | integer(4) | PK |  | Código do backup (auto incrementado) |
| USUARIO | char(30) |  |  | Usuário que iniciou o backup |
| DATAHORA | timestamp(8) |  |  | Data/Hora do backup |
