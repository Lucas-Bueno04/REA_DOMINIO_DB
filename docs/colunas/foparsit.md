# foparsit — Parametros das situacoes
1.238 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_situacao | integer(4) | PK |  | Situacao de afastamento |
| dias_estab | integer(4) |  |  | dias estabilidade |
| pp_mes_estab | numeric(5) |  |  | Percentual do salario |
| evento1 | integer(4) |  |  | Evento 1 |
| evento2 | integer(4) |  |  | Evento 2 |
| evento3 | integer(4) |  |  | Evento 3 |
| evento4 | integer(4) |  |  | Evento 4 |
| evento5 | integer(4) |  |  | Evento 5 |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
