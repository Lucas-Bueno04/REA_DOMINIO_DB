# foconfarquivo — Configuracao de arquivos
8 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_confarquivo | integer(4) | PK |  | Codigo arquivo |
| i_codigo | integer(4) | PK |  | Codigo |
| tipo_separacao | tinyint(1) |  |  | Tipo da separacao |
| nome | char(30) |  | S | Nome |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| codi_emp | integer(4) |  | S | Codigo da empresa |
