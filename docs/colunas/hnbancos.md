# hnbancos — Bancos - Cadastro
9 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_banco | integer(4) | PK |  | Sequencial |
| nome_ban | varchar(50) |  |  | Nome |
| codi_ban | integer(4) |  |  | Codigo do Banco |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
