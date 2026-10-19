# EFIMPORTANDO — Usuários importando
33 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| USUARIO | varchar(128) | PK |  | Usuário |
| TABELA_IMPORTADA | varchar(128) | PK |  | Tabela que está sendo importada |
| CONNECTION_ID | integer(4) | PK |  | Identificador da conexão |
| LOGIN_TIME | varchar(32) |  |  | Propriedade LoginTime do connection ID |
