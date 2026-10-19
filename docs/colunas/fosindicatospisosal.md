# fosindicatospisosal — Sindicato - Cadastro - Piso Salarial
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_sindicatos | integer(4) | PK |  | Codigo |
| competencia | date(4) | PK |  | A partir de |
| valor_piso | numeric(13) |  |  | Valor do Piso |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
