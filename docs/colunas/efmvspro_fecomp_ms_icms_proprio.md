# EFMVSPRO_FECOMP_MS_ICMS_PROPRIO — Notas Fiscais de Saída - Produtos - FECOMP MS
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_SAI | integer(4) | PK |  | Código sequencial da nota de saída |
| NUME_MSP | integer(4) | PK |  | Código sequencial do estoque |
| CODI_PDI | char(14) |  |  | Código do produto |
| BASE_CALCULO_FECOMP_MS_ICMS_PROPRIO | numeric(15) |  |  | Base cálculo ICMS |
| ALIQUOTA_FECOMP_MS_ICMS_PROPRIO | numeric(5) |  |  | Alíquota ICMS |
| VALOR_FECOMP_MS_ICMS_PROPRIO | numeric(15) |  |  | Valor ICMS |
