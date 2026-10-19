# EFMVSPRO_ICMS_STAT — Notas Fiscais de Saída - Produtos - ICMS STAT
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_SAI | integer(4) | PK |  | Código sequencial da nota de saída |
| NUME_MSP | integer(4) | PK |  | Código sequencial do estoque |
| CODI_PDI | char(14) |  |  | Código do produto |
| BASE_CALCULO | numeric(13) |  |  | Base de Cálculo - ICMS ST Antecipação Total |
| ALIQUOTA | numeric(7) |  |  | Alíquota - ICMS ST Antecipação Total |
| VALOR_IMPOSTO | numeric(13) |  |  | Valor - ICMS ST Antecipação Total |
| CODIGO_RECOLHIMENTO | char(6) |  | S | Código do Recolhimento - Substituição Tributária |
| I_RECOLHIMENTO | integer(4) |  | S | Código Sequencial do Recolhimento - Substituição Tributária |
