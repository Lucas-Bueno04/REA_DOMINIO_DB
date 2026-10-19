# EFMVSPRO_FECOMP_MS_ICMS_ST — Notas Fiscais de Saída - Produtos - FECOMP ST MS
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_SAI | integer(4) | PK |  | Código sequencial da nota de saída |
| NUME_MSP | integer(4) | PK |  | Código sequencial do estoque |
| CODI_PDI | char(14) |  |  | Código do produto |
| BASE_CALCULO_FECOMP_MS_ICMS_ST | numeric(15) |  |  | Base cálculo ICMS ST |
| ALIQUOTA_FECOMP_MS_ICMS_ST | numeric(5) |  |  | Alíquota ICMS ST |
| VALOR_FECOMP_MS_ICMS_ST | numeric(15) |  |  | Valor ICMS ST |
