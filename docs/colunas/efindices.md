# efindices — Indices Diarios - Cadastro
19.901 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| nome_ind | char(8) |  |  | Nome |
| data_ind | date(4) | PK |  | Data |
| vlor_ind | numeric(13) |  |  | Valor |
| codi_ind | integer(4) | PK |  | Codigo |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
