# efestados — Estados - Cadastro
28 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_est | integer(4) |  |  | Codigo |
| sigl_est | char(2) | PK |  | Sigla |
| nome_est | char(40) |  |  | Nome |
| aliq_est | numeric(7) |  |  | Aliquota |
| regi_est | integer(4) |  |  | Regiao |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
