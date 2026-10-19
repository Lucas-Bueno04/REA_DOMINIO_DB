# fopagtoparcialepr — Pagamentos parciais - Empregados
2.458 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_pagto | integer(4) | PK |  | Sequencia de pagamento |
| i_pagtoitem | integer(4) | PK |  | Sequencial de Pagamentos |
| i_empregados | integer(4) | PK |  | Codigo do empregado |
| codi_emp | integer(4) | PK |  | Codigo da empresa |
| codi_emp_lan | integer(4) |  | S | Codigo da empresa lancamento |
| nume_lan | integer(4) |  | S | numero do lancamento |
| valor | numeric(13) |  |  | Valor pago |
| NUMERO_RPA | numeric(10) |  | S | Número do RPA. |
| I_CONVOCACAO | numeric(10) |  | S | Convocação Intermitente Relacionada |
