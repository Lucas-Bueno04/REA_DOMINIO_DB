# fovaletrp — Vale transporte - Cadastro
1.611 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_linhas | integer(4) | PK |  | Linha |
| i_empregados | integer(4) | PK |  | empregado |
| quantidade | integer(4) |  |  | Quantidade |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| unidade_lancto | tinyint(1) |  |  | Unidade de lançamento (1=Diário,2=Mensal) |
| COMPETENCIA_INICIO | date(4) | PK |  | Competência início. |
| DETERMINAR_FIM | smallint(2) |  |  | Determinar fim. (0=Não/1=Sim) |
| COMPETENCIA_FIM | date(4) |  | S | Competência fim. |
