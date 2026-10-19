# EFPLANEJAMENTO_TRIBUTARIO_VALOR_DESPESA — Planejamento Tributário - Despesas
24 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| REGIME | char(1) | PK |  | Regime de Planejamento (P - Presumido, R - Real, S - Simples) |
| PERIODO | date(4) | PK |  | Periodo Planejamento |
| VALOR_DESPESA | numeric(13) |  |  | Valor despesa |
| AUMENTO | numeric(13) |  |  | Aumento |
| REDUCAO | numeric(13) |  |  | Reducao |
| VALOR_DESPESA_ESTIMATIVA | numeric(13) |  |  | Valor Despesa Estimativa |
