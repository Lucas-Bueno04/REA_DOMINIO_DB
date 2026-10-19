# lairincentivo — Incentivos Fiscais - Cadastro
5 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_inc | integer(4) | PK |  | Incentivo |
| desc_inc | char(140) |  |  | Descricao |
| padr_inc | tinyint(1) |  | S | Padrao (1=Sim, 2=Nao) |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
