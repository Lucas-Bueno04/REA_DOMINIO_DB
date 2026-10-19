# PMCALCULO_CREDITO_ICMS — Cálculo patrimonial - Crédito ICMS
6 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CALCULO | integer(4) | PK |  | Código |
| MENSAL_QUINZENAL | tinyint(1) | PK |  | Periodicidade (0=Mensal, 1=Primeira Quinzena, 2=Segunda Quinzena) |
| PARCELA | integer(4) |  |  | Número da parcela |
| VALOR_CREDITO | numeric(13) |  |  | Valor do crédito |
| VALOR_CREDITO_ACUMULADO | numeric(13) |  |  | Valor do crédito acumulado |
| VALOR_NAO_CREDITAVEL | numeric(13) |  |  | Valor não creditável |
| VALOR_NAO_CREDITAVEL_ACUMULADO | numeric(13) |  |  | Valor não creditável acumulado |
| VALOR_CREDITO_ORIGINAL | numeric(13) |  |  | Valor do crédito - Original |
| VALOR_CREDITO_ACUMULADO_ORIGINAL | numeric(13) |  |  | Valor do crédito acumulado - Original |
| VALOR_NAO_CREDITAVEL_ORIGINAL | numeric(13) |  |  | Valor não creditável - Original |
| VALOR_NAO_CREDITAVEL_ACUMULADO_ORIGINAL | numeric(13) |  |  | Valor não creditável acumulado - Original |
| BASE_CALCULO | numeric(13) |  |  | Base de cálculo |
| VALOR_CREDITO_TOTAL | numeric(13) |  |  | Valor do crédito total calculado na competência(Creditavel e não Creditável) |
