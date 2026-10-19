# HRRENEGOCIACAO_FATURAMENTO — Renegociacao - Faturamento
483 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_RENEGOCIACAO | integer(4) | PK |  | Renegociacao |
| I_FATURAMENTO_ORIGEM | integer(4) | PK |  | Faturamento origem |
| I_PARCELA_ORIGEM | integer(4) | PK |  | Parcela origem |
| I_FATURAMENTO_DESTINO | integer(4) | PK |  | Faturamento destino |
| I_PARCELA_DESTINO | integer(4) | PK |  | Parcela destino |
| TIPO_RENEGOCIACAO | char(1) |  |  | Tipo de renegociacao que originou o faturamento F Refaturado R Reparcelado |
