# EFMVEPRO_DIFAL_NC — Notas Fiscais de Entrada - Produtos - DIFAL NC
27 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_ENT | integer(4) | PK |  | Código sequencial da nota de entrada |
| NUME_MEP | integer(4) | PK |  | Código sequencial do estoque |
| CODI_PDI | char(14) |  |  | Código do produto |
| BASE_CALCULO | numeric(15) |  |  | Base Cálculo |
| ALIQUOTA | numeric(5) |  |  | Alíquota |
| VALOR_UF_ORIGEM | numeric(15) |  |  | Valor UF Origem |
| VALOR_UF_DESTINO | numeric(15) |  |  | Valor UF Destino |
| VALOR_TOTAL | numeric(15) |  |  | Valor Total |
| VALOR_FCP | numeric(15) |  |  | Valor FCP |
