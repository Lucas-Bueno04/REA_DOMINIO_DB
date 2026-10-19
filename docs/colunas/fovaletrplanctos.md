# fovaletrplanctos — Vale transporte - Lancamentos
3.161 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Código da empresa |
| i_linhas | integer(4) | PK |  | Código da linha |
| i_empregados | integer(4) | PK |  | Código do empregado |
| competencia | date(4) | PK |  | Competência |
| tipo_proces | smallint(2) | PK |  | Tipo de processo |
| i_eventos | integer(4) |  |  | Código do evento |
| ndias | integer(4) |  |  | Número de dias |
| nvales | integer(4) |  |  | Número de vales |
| valor_pagar | numeric(13) |  |  | Valor a pagar pelos vales |
| valor_desc | numeric(13) |  |  | Valor a descontar do empregado |
| TIPO_LANCAMENTO | smallint(2) | PK |  | Tipo do lançamento: 1=Mensal/2=Fixo |
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
| COMPETENCIA_INICIO | date(4) |  |  | Competência início. |
| PERCENTUAL_MAXIMO_DESCONTO_VALE_TRANSPORTE | numeric(5) |  | S | Percentual máximo para desconto de vale transporte. |
| DEMONSTRAR_RUBRICA_PARTE_PAGA_EMPRESA | smallint(2) |  |  | Demonstrar rubrica informativa no recibo de pagamento referente a parte paga pela empresa sobre o vale-transporte(1-Sim/0-Não) |
| DEMONSTRAR_RUBRICA_VALOR_TOTAL | smallint(2) |  |  | Demonstrar rubrica informativa no recibo de pagamento referente ao valor total de vale transporte(1-Sim/0-Não) |
