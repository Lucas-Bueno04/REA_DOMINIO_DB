# foempreg_contrsind — Empregados - Cadastro - Contribuicao Sindical
3.721 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_empregados | integer(4) | PK |  | Codigo empregado |
| competencia | date(4) | PK |  | Competencia |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| ANO_REFERENCIA | integer(4) |  |  | Ano de referência |
| ORIGEM | smallint(2) |  |  | Origem: (1=Normal/2=Replicação por rescisão por transferência) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
