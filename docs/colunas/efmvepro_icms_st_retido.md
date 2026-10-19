# EFMVEPRO_ICMS_ST_RETIDO — Notas Fiscais de Entrada - Produtos - ICMS ST Retido
931 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_ENT | integer(4) | PK |  | Código sequencial da nota de entrada |
| NUME_MEP | integer(4) | PK |  | Código sequencial do estoque |
| CODI_PDI | char(14) | PK |  | Código do produto |
| ICMS_ST_RETIDO_BASE_CALCULO | numeric(13) |  |  | ICMS ST Retido - Base Cálculo |
| ICMS_ST_RETIDO_VALOR | numeric(13) |  |  | ICMS ST Retido - Valor |
| ICMS_ST_RETIDO_MONTANTE_IMPOSTO_PRESUMIDO | numeric(13) |  |  | ICMS ST Retido - Montante Imposto Presumido |
