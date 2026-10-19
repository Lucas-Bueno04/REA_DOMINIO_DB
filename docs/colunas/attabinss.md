# attabinss — SELIC - Cadastro
549 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| comp_tin | date(4) | PK |  | Competencia |
| cufi_tin | numeric(10) |  | S | Coeficiente de UFIR |
| juro_tin | numeric(6) |  | S | Percentual de juros |
| valor_sel | numeric(13) |  | S | Valor da Selic |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
