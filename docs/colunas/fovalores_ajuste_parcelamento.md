# FOVALORES_AJUSTE_PARCELAMENTO — Valores de diferenças de competências retroativas do ajuste conforme parcelamento
1.438 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CALCULOS_DIFERENCA_OLD | integer(4) |  | S | Código do cálculo da diferença - Renomeado |
| I_CALCULOS_AJUSTADO_OLD | integer(4) |  | S | Código do cálculo ajustado - Renomeado |
| I_EVENTOS | integer(4) | PK |  | Código do evento de diferença. |
| I_FORMA_AJUSTE_PARCELAMENTO | integer(4) |  |  | Código da forma de ajuste conforme parcelamento. |
| VALOR | numeric(13) |  |  | Valor |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro: (0=Sistema, 1=Importação de tabelas, 2=Importação de leiaute, 3=Conversão) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS_AJUSTADO | uniqueidentifier(16) | PK |  | Código do cálculo ajustado |
| I_CALCULOS_DIFERENCA | uniqueidentifier(16) | PK |  | Código do cálculo da diferença |
