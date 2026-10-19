# FOFERIAS_LANCAMENTOS_PENSAO_ALIMENTICIA — Valores de pensão alimentícia nas férias por dependente.
20 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| I_FERIAS_GOZO | integer(4) | PK |  | Código do período de gozo. |
| I_EVENTOS | integer(4) | PK |  | Código do evento. |
| I_FILHOS | integer(4) | PK |  | Código do dependente. |
| VALOR | numeric(13) |  |  | Valor. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/ 1=Imp Tabelas/ 2=Imp Layout) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
