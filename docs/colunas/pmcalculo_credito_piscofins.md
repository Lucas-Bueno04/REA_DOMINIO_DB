# PMCALCULO_CREDITO_PISCOFINS — Cálculo patrimonial - Crédito PIS/COFINS
6 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CALCULO | integer(4) | PK |  | Código |
| PARCELA | integer(4) |  |  | Número da parcela |
| VALOR_PIS | numeric(13) |  |  | Valor do PIS |
| VALOR_PIS_ACUMULADO | numeric(13) |  |  | Valor do PIS acumulado |
| VALOR_COFINS | numeric(13) |  |  | Valor do COFINS |
| VALOR_COFINS_ACUMULADO | numeric(13) |  |  | Valor do COFINS acumulado |
| BASE_CALCULO | numeric(13) |  |  | Base de cÃ¡lculo da PIS/COFINS |
