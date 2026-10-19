# EFPOSSE_PRODUTOS_COMPETENCIA_PRODUTOS_POSSE — Posse dos Produtos - Produtos - Posse
246 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_POSSE | integer(4) | PK |  | Código da posse |
| CODI_PDI | char(14) | PK |  | Produto |
| I_SEQUENCIAL | integer(4) | PK |  | Sequêncial |
| DATA_INVENTARIO | date(4) |  |  | Data do iventário |
| INDICADOR_PROPRIEDADE | integer(4) |  |  | Indicador de propriedade (0/ 1/ 2/ 3/ 4) |
| TIPO_POSSUIDOR | char(1) |  |  | Tipo possuidor (C/ F ) |
| CODIGO_POSSUIDOR | integer(4) |  |  | Código do possuidor |
| QUANTIDADE | numeric(17) |  |  | Quantidade |
| VALOR_TOTAL | numeric(13) |  |  | Valor total |
| CODI_CTA | integer(4) |  | S | Codigo da conta contábil |
| ORIGEM_REG | integer(4) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
