# EFMVEPRO_ICMSI — Notas Fiscais de Entrada - Produtos - ICMS Importação
789 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_ENT | integer(4) | PK |  | Código sequencial da nota de entrada |
| NUME_MEP | integer(4) | PK |  | Código sequencial do estoque |
| CODI_PDI | char(14) |  |  | Código do produto |
| BASE_CALCULO_ICMSI | numeric(13) |  |  | Base cálculo ICMS Importação |
| ALIQUOTA_ICMSI | numeric(7) |  |  | Alíquota ICMS Importação |
| VALOR_ICMSI | numeric(13) |  |  | Valor ICMS Importação |
