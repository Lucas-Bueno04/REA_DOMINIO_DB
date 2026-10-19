# EFSAIDAS_ICMS_DESONERADO — ICMS desonerado
72 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_SAI | integer(4) | PK |  | Código da nota |
| I_ICMS_DESONERADO | integer(4) | PK |  | Sequencial |
| CST_ICMS_DESONERADO | integer(4) |  | S | CST do ICMS desonerado |
| VALOR_DESONERADO | numeric(13) |  |  | Valor desonerado |
| I_MOTIVO_DESONERACAO | integer(4) |  | S | Motivo da desoneração (1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) |
