# EFENTRADAS_VALOR_PRESENTE_PROVISAO — Notas Fiscais de Entrada - Valor Presente Provisao
69 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_ENT | integer(4) | PK |  | Codigo da nota de entrada |
| DATA_PROVISAO | date(4) | PK |  | Data da provisao |
| DATA_LANCAMENTO | date(4) |  |  | Data do lancamento |
| NUMERO_DIAS | integer(4) |  |  | Numero de dias |
| VALOR_PRESENTE | numeric(13) |  |  | Valor presente |
| VALOR_TAXA | numeric(13) |  |  | Valor da taxa |
| VALOR_JUROS | numeric(13) |  |  | Valor de juros |
| VALOR_DEVOLUCAO | numeric(13) |  |  | Valor de devolucao |
| VALOR_FUTURO | numeric(13) |  |  | Valor futuro |
| VALOR_SALDO_JUROS | numeric(13) |  |  | Valor de saldo juros |
