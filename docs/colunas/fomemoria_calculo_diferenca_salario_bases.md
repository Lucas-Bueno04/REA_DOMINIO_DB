# FOMEMORIA_CALCULO_DIFERENCA_SALARIO_BASES — Memória de cálculo de diferença de salário - Bases de cálculo
419.415 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CALCULOS_DIFERENCA_OLD | integer(4) |  | S | Código do cálculo da diferença - Renomeado |
| I_CALCULOS_AJUSTADO_OLD | integer(4) |  | S | Código do cálculo ajustado - Renomeado |
| I_CADBASES | integer(4) | PK |  | Código da base de cálculo |
| BASE | numeric(13) |  |  | Base ajustada. |
| ORIGEM_REG | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| VALOR | numeric(17) |  |  | Valor da base ajustada. |
| I_FORMA_AJUSTE_PARCELAMENTO | integer(4) |  | S | Código da forma de ajuste conforme parcelamento. |
| I_SERVICOS | integer(4) | PK |  | Serviço. |
| RATEIO | smallint(2) | PK |  | Rateio. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS_AJUSTADO | uniqueidentifier(16) | PK |  | Código do cálculo ajustado |
| I_CALCULOS_DIFERENCA | uniqueidentifier(16) | PK |  | Código do cálculo da diferença |
