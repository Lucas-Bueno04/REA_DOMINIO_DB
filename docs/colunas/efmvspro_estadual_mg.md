# EFMVSPRO_ESTADUAL_MG — Notas Fiscais de Saída - Produtos - Estadual MG
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_SAI | integer(4) | PK |  | Código sequencial da nota de saída |
| NUME_MSP | integer(4) | PK |  | Código sequencial do estoque |
| RECALI_BASE_CALCULO | numeric(13) |  |  | Base de Cálculo - RECALI |
| RECALI_ALIQUOTA | numeric(5) |  |  | Alíquota - RECALI |
| RECALI_VALOR | numeric(13) |  |  | Valor - RECALI |
| RECALI_CODIGO_RECOLHIMENTO | char(6) |  | S | Código Recolhimento - RECALI |
| RECALI_I_RECOLHIMENTO | integer(4) |  | S | Sequencial Recolhimento - RECALI |
