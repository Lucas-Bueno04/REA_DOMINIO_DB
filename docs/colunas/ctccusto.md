# ctccusto — Cadastro - Cadastro de centro de custos da contabilidade
1.383 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_ccu | integer(4) | PK |  | Codigo |
| desc_ccu | char(40) |  |  | Descricao |
| codi_dep | integer(4) |  |  | Departamento |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| DATA_CCU | date(4) |  |  | Data cadastro |
