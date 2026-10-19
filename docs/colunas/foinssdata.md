# foinssdata — Data de contribuicao de INSS
75 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| i_empregados | integer(4) | PK |  | Empregado |
| competencia | date(4) | PK |  | Competencia |
| tipo_process | integer(4) | PK |  | is Tipo da folha |
| data_pag | date(4) |  | S | Data pagamento |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
