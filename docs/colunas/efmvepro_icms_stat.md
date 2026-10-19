# EFMVEPRO_ICMS_STAT — Notas Fiscais de Entrada - Produtos - ICMS STAT
727 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_ENT | integer(4) | PK |  | Código sequencial da nota de entrada |
| NUME_MEP | integer(4) | PK |  | Código sequencial do estoque |
| CODI_PDI | char(14) |  |  | Código do produto |
| CODIGO_TRIBUTACAO | integer(4) |  | S | Código de tributação do produto |
| BASE_CALCULO | numeric(13) |  |  | Base de Cálculo - ICMS ST Antecipação Total |
| ALIQUOTA | numeric(7) |  |  | Alíquota - ICMS ST Antecipação Total |
| VALOR_IMPOSTO | numeric(13) |  |  | Valor - ICMS ST Antecipação Total |
| CODIGO_RECOLHIMENTO_STAT | char(6) |  | S | Código do Recolhimento - Substituição Tributária |
| I_RECOLHIMENTO_STAT | integer(4) |  | S | Código Sequencial do Recolhimento - Substituição Tributária |
| BASE_CALCULO_ST | char(1) |  |  | Base cálculo ST |
| VALOR_ICMS_PROPRIO | numeric(13) |  |  | Valor ICMS Próprio |
| VALOR_ICMS_RETIDO | numeric(13) |  |  | Valor ICMS Retido |
