# FOANTECIPACAO_SALARIAL_RAIS — Valores de antecipação calculados por competência
34 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| COMPETENCIA | date(4) | PK |  | Competência do cálculo. |
| TIPO_PROCESSO | integer(4) | PK |  | Tipo do cálculo. |
| RATEIO | integer(4) | PK |  | Rateio. |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo - Renomeado |
| VALOR_CAL | numeric(30) |  | S | Valor total de antecipação. |
| VALOR_CAL_SEM_FERIAS | numeric(30) |  | S | Valor de antecipação desconsiderando ferias. |
| VALOR_CAL_PARA_RECIBO_RESCISAO | numeric(30) |  | S | Valor total de antecipação para recibo de rescisão. |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo. |
