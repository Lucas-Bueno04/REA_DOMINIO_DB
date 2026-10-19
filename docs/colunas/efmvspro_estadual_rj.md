# EFMVSPRO_ESTADUAL_RJ — Notas Fiscais de Saída - Produtos - Estadual RS
199 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_SAI | integer(4) | PK |  | Código sequencial da nota de saída |
| NUME_MSP | integer(4) | PK |  | Código sequencial do estoque |
| CODI_PDI | char(14) |  |  | Código produto |
| BASE_CALCULO_ICMS_EFETIVO | numeric(13) |  |  | Base de cálculo |
| ALIQUOTA_ICMS_EFETIVO | numeric(13) |  |  | Alíquota |
| VALOR_ICMS_EFETIVO | numeric(13) |  |  | Valor |
