# EFECF_REDUCAO_Z_ESTOQUE_APURACAO_ESTOQUE — ECF - Dados da Redução Z - Estoque - Apuração de estoque
37.754 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_REDUCAO | integer(4) | PK |  | Sequêncial da Redução Z |
| I_ESTOQUE | integer(4) | PK |  | Sequêncial do estoque |
| DATA_MOVIMENTACAO | date(4) |  |  | Data da movimentação |
| CODI_PDI | char(14) |  |  | Código do produto |
| QUANTIDADE | numeric(13) |  |  | Quantidade |
| VALOR_UNITARIO | numeric(15) |  |  | Valor unitário |
| VALOR_TOTAL | numeric(15) |  |  | Valor total |
| QUANTIDADE_ACUMULADA | numeric(13) |  |  | Quantidade acumulada |
| VALOR_UNITARIO_MEDIO | numeric(15) |  |  | Valor unitário médio |
| VALOR_ACUMULADO | numeric(15) |  |  | Valor acumulado |
| ICMS_UNITARIO | numeric(19) |  |  | Valor do ICMS unitário |
| ICMS_TOTAL | numeric(13) |  |  | Valor do ICMS total |
| ICMS_UNITARIO_MEDIO | numeric(19) |  |  | Valor do ICMS unitário médio |
| ICMS_ACUMULADO | numeric(13) |  |  | Valor do ICMS acumulado |
| ICMS_ST_QUANTIDADE | numeric(13) |  |  | Quantidade ICMS ST |
| ICMS_ST_UNITARIO | numeric(19) |  |  | Valor do ICMS ST unitário |
| ICMS_ST_TOTAL | numeric(13) |  |  | Valor do ICMS ST total |
| ICMS_ST_QUANTIDADE_ACUMULADO | numeric(13) |  |  | Quantidade ICMS ST acumulado |
| ICMS_ST_UNITARIO_MEDIO | numeric(19) |  |  | Valor do ICMS ST unitário médio |
| ICMS_ST_ACUMULADO | numeric(13) |  |  | Valor do ICMS acumulado |
