# EFMVSPRO_ESTADUAL_RN — Notas Fiscais de Saída - Produtos - Estadual RN
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_SAI | integer(4) | PK |  | Código sequencial da nota de saída |
| NUME_MSP | integer(4) | PK |  | Código sequencial do estoque |
| CODI_PDI | char(14) |  |  | Código produto |
| BASE_CALCULO_FECOP_PROPRIO | numeric(13) |  |  | FECOP - ICMS Próprio - Base de cálculo |
| ALIQUOTA_FECOP_PROPRIO | numeric(5) |  |  | FECOP - ICMS Próprio - Alíquota |
| VALOR_FECOP_PROPRIO | numeric(13) |  |  | FECOP - ICMS Próprio - Valor |
| BASE_CALCULO_FECOP_ST | numeric(13) |  |  | FECOP - ICMS ST - Base de cálculo |
| ALIQUOTA_FECOP_ST | numeric(5) |  |  | FECOP - ICMS ST - Alíquota |
| VALOR_FECOP_ST | numeric(13) |  |  | FECOP - ICMS ST - Valor |
