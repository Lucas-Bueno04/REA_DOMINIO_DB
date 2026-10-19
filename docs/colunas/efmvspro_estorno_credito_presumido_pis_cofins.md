# EFMVSPRO_ESTORNO_CREDITO_PRESUMIDO_PIS_COFINS — Notas Fiscais de Saída - Produtos - Estorno Crédito Presumido PIS/COFINS
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_SAI | integer(4) | PK |  | Código sequencial da nota de saída |
| NUME_MSP | integer(4) | PK |  | Código sequencial do estoque |
| CODI_PDI | char(14) |  |  | Código do produto |
| VALOR_PIS | numeric(13) |  |  | Valor PIS |
| VALOR_COFINS | numeric(13) |  |  | Valor COFINS |
