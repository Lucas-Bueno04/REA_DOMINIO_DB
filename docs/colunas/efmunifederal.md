# efmunifederal — Municipios Federais - Cadastro
5.559 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| sigl_est | char(2) | PK |  | Estado |
| codigo_fed | integer(4) | PK |  | Codigo |
| nome_fed | varchar(40) |  |  | Nome |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
