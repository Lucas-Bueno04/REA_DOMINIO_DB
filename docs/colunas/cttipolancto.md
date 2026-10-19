# cttipolancto — Tipo de lancamento - Cadastro
17.351 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| i_tipolancto | integer(4) | PK |  | Codigo tipo lancamento |
| descricao | char(40) |  |  | Descricao |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
