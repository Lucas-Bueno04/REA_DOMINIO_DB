# EFMVEPRO_ESTADUAL_ES — Notas Fiscais de Entrada - Produtos - Estadual ES
7 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_ENT | integer(4) | PK |  | Código sequencial da nota de entrada |
| NUME_MEP | integer(4) | PK |  | Código sequencial do estoque |
| CODI_PDI | char(14) |  |  | Código do produto |
| DIFALI_BASE_CALCULO | numeric(13) |  |  | Base de Cálculo - DIFALI |
| DIFALI_ALIQUOTA | numeric(7) |  |  | Alíquota - DIFALI |
| DIFALI_VALOR | numeric(13) |  |  | Valor - DIFALI |
| SITUACAO_TRIBUTARIA_DIEF_CAFE_CRU | integer(4) |  | S | Situação Tributária DIEF |
| ICMS_COMPLEMENTAR_BASE_CALCULO | numeric(13) |  |  | Base de Calculo ICMS Complementar |
| ICMS_COMPLEMENTAR_ALIQUOTA | numeric(5) |  |  | Aliquota - ICMS Complementar |
| ICMS_COMPLEMENTAR_VALOR | numeric(13) |  |  | Valor - ICMS Complementar |
