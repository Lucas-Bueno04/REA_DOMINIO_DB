# EFMVEPRO_MEDICAMENTO_LOTE — Notas Fiscais de Entrada - Produtos - Medicamento - Lote
14 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_ENT | integer(4) | PK |  | Código sequencial da nota de entrada |
| NUME_MEP | integer(4) | PK |  | Código sequencial do estoque |
| I_LOTE | integer(4) | PK |  | Código sequencial do lote |
| CODI_PDI | char(14) |  |  | Código do produto |
| LOTE | varchar(255) |  | S | Lote |
| QUANTIDADE_ITEM_POR_LOTE | integer(4) |  | S | Qtd. item/lote |
| DATA_FABRICACAO | date(4) |  | S | Data Fabricação |
| DATA_VALIDADE | date(4) |  | S | Data Validade |
| REFERENCIA_BASE_CALCULO | integer(4) |  | S | REF. BASE DE CÁLCULO (0 / 1 / 2 / 3 / 4 / 5 / 6) |
| PRECO_TABELADO_MAXIMO | numeric(13) |  | S | Preço Tab./Máx |
