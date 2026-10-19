# FOFERIAS_GOZO_AFASTAMENTOS — Tabela de relacionamento entre o cálculo de férias e o afastamento de férias.
7.381 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| I_FERIAS_GOZO | integer(4) | PK |  | Sequencial do cálculo de férias. |
| SEQUENCIAL | smallint(2) | PK |  | Sequencial. |
| DATA_REAL_DN | numeric(10) |  |  | Data do afastamento. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
