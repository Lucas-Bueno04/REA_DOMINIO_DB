# EFMVSPRO_ICMS_EFETIVO — Notas Fiscais de Saída - Produtos - ICMS Efetivo Geral
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_SAI | integer(4) | PK |  | Código sequencial da nota de saída |
| NUME_MSP | integer(4) | PK |  | Código sequencial do estoque |
| CODI_PDI | char(14) |  |  | Código produto |
| BASE_CALCULO | numeric(13) |  |  | Base de cálculo |
| ALIQUOTA | numeric(13) |  |  | Alíquota |
| VALOR | numeric(13) |  |  | Valor |
