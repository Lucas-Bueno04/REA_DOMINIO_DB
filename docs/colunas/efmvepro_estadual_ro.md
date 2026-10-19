# EFMVEPRO_ESTADUAL_RO — Notas Fiscais de Entrada - Produtos - Estadual RO
110 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_ENT | integer(4) | PK |  | Código sequencial da nota de saída |
| NUME_MEP | integer(4) | PK |  | Código sequencial do estoque |
| CODI_PDI | char(14) |  |  | Código do produto |
| BC_ICMSA_MEP | numeric(13) |  |  | Base de cálculo ICMS Antecipado |
| ALIQ_ICMSA_MEP | numeric(7) |  |  | Aíquota ICMS Antecipado |
| VALOR_ICMSA_MEP | numeric(13) |  |  | Valor ICMS Antecipado |
