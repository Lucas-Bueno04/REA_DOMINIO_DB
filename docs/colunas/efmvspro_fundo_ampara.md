# EFMVSPRO_FUNDO_AMPARA — Notas Fiscais de Saída - Produtos - Ampara RS
8 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_SAI | integer(4) | PK |  | Código sequencial da nota de saída |
| NUME_MSP | integer(4) | PK |  | Código sequencial do estoque |
| CODI_PDI | char(14) | PK |  | Código do produto |
| BASE_ICMS_PROPRIO | numeric(13) |  |  | Base cálculo ICMS |
| ALIQUOTA_ICMS_PROPRIO | numeric(5) |  |  | Alíquota ICMS |
| VALOR_ICMS_PROPRIO | numeric(13) |  |  | Valor ICMS |
| BASE_ICMS_ST | numeric(13) |  |  | Base cálculo ICMS ST |
| ALIQUOTA_ST_PROPRIO | numeric(5) |  |  | Alíquota ICMS ST |
| VALOR_ICMS_ST | numeric(13) |  |  | Valor ICMS ST |
