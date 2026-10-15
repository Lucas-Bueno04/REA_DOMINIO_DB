# foliquidosfilepr — Liquidos por filial - Empregados
216.930 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_LIQUIDOSFIL_OLD | integer(4) |  | S | Sequencial - Renomeado |
| i_empregados | integer(4) | PK |  | Codigo do empregado |
| codi_emp | integer(4) | PK |  | Codigo da empresa |
| liquido | numeric(13) |  |  | Liquido |
| SEQUENCIAL | smallint(2) | PK |  | Sequencial. |
| NUMERO_RPA | numeric(10) |  | S | Número do RPA. |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo que está sendo pago - Renomeado |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_LIQUIDOSFIL | uniqueidentifier(16) | PK |  | Sequencial |
| I_CALCULOS | uniqueidentifier(16) |  | S | Código do cálculo que está sendo pago. |
| I_CONVOCACAO | numeric(10) |  | S | Convocação Intermitente Relacionada |
