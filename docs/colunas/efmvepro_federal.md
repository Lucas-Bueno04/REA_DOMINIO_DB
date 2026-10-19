# EFMVEPRO_FEDERAL — Valor ICMS desonerado Estoque
39 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_ENT | integer(4) | PK |  | Código sequencial da nota de entrada |
| NUME_MEP | integer(4) | PK |  | Código sequencial do estoque |
| VALOR_ICMS_DESONERADO | numeric(13) |  |  | Valor ICMS desonerado |
| I_MOTIVO_DESONERACAO | integer(4) |  | S | Motivo Desoneração |
| BASE_CALCULO_ICMS_DIFERIDO | numeric(13) |  |  | Base de Cálculo ICMS Diferido |
| PERCENTUAL_ICMS_DIFERIDO | numeric(5) |  |  | Percentual ICMS Diferido |
| VALOR_ICMS_DIFERIDO | numeric(13) |  |  | Valor ICMS Diferido |
