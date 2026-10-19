# EFMVEPRO_ESTADUAL_MG — Notas Fiscais de Entrada - Produtos - Estadual MG
170 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_ENT | integer(4) | PK |  | Código sequencial da nota de entrada |
| NUME_MEP | integer(4) | PK |  | Código sequencial do estoque |
| DIFALI_BASE_CALCULO | numeric(13) |  |  | Base de Cálculo - DIFALI |
| DIFALI_ALIQUOTA | numeric(7) |  |  | Alíquota - DIFALI |
| DIFALI_VALOR | numeric(13) |  |  | Valor - DIFALI |
| ICMS_ST_ANTECIPACAO_TOTAL_BASE_CALCULO | numeric(13) |  |  | Base de Cálculo - ICMS ST Antecipação Total |
| ICMS_ST_ANTECIPACAO_TOTAL_ALIQUOTA | numeric(7) |  |  | Alíquota - ICMS ST Antecipação Total |
| ICMS_ST_ANTECIPACAO_TOTAL_VALOR | numeric(13) |  |  | Valor - ICMS ST Antecipação Total |
| RECALI_BASE_CALCULO | numeric(13) |  |  | Base de Cálculo - RECALI |
| RECALI_ALIQUOTA | numeric(5) |  |  | Alíquota - RECALI |
| RECALI_VALOR | numeric(13) |  |  | Valor - RECALI |
| RECALI_CODIGO_RECOLHIMENTO | char(6) |  | S | Código Recolhimento - RECALI |
| RECALI_I_RECOLHIMENTO | integer(4) |  | S | Sequencial Recolhimento - RECALI |
