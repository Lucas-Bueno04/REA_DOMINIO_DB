# PMCALCULO — Cálculo patrimonial
142.997 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CALCULO | integer(4) | PK |  | Código |
| I_BEM | numeric(16) |  |  | Bem |
| COMPETENCIA | date(4) |  |  | Competência |
| USUARIO | varchar(128) |  |  | Usuário que efetuou o cálculo |
| DATA_HORA | timestamp(8) |  |  | Data e hora do cálculo |
