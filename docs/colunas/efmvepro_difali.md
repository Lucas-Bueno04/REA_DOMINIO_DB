# EFMVEPRO_DIFALI — Notas Fiscais de Entrada - Produtos - DIFALI
22.026 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_ENT | integer(4) | PK |  | Código sequencial da nota de entrada |
| NUME_MEP | integer(4) | PK |  | Código sequencial do estoque |
| CODI_PDI | char(14) |  |  | Código do produto |
| CODIGO_TRIBUTACAO_DIFALI | integer(4) |  | S | Código de tributação do produto DIFALI |
| BASE_CALCULO_DIFALI | numeric(13) |  |  | Base cálculo DIFALI |
| ALIQUOTA_DIFALI | numeric(7) |  |  | Alíquota DIFALI |
| VALOR_DIFALI | numeric(13) |  |  | Valor DIFALI |
| I_RECOLHIMENTO_DIFALI | integer(4) |  | S | Código Sequencial do Recolhimento - DIFALI |
| CODIGO_RECOLHIMENTO_DIFALI | char(6) |  | S | Código do Recolhimento - DIFALI |
