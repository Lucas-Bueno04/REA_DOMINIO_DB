# EFECF_REDUCAO_Z_SITUACAO_TRIBUTARIA — ECF - Dados da redução Z - Situação tributária
1.608 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_REDUCAO | integer(4) | PK |  | Código da redução Z |
| I_SITUACAO | integer(4) | PK |  | Sequencial da situação tributária |
| OPERACAO | integer(4) |  |  | Operação |
| VALOR | numeric(13) |  |  | Valor da operação |
| ALIQUOTA | numeric(5) |  |  | Alíquota da operação |
| IMPOSTO | numeric(13) |  |  | Valor do imposto da operação |
