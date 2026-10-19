# FOTABCALCIRRF_EXTERIOR_FAIXAS — Faixas da tabela de IRRF para residentes no exterior.
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_TABCALCIRRF_EXTERIOR | date(4) | PK |  | Competência |
| VALOR_ATE | numeric(13) | PK |  | Valor até |
| TAXA | numeric(13) |  |  | Taxa |
| DESCONTO | numeric(13) |  |  | Desconto |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
