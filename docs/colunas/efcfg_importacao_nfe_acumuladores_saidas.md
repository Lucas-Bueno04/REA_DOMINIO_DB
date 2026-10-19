# EFCFG_IMPORTACAO_NFE_ACUMULADORES_SAIDAS — Configuracao de importacao da Nota Fiscal Eletronica - Acumuladores
45 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Codigo da empresa |
| I_ACUMULADOR | integer(4) | PK |  | Sequencial do acumulador |
| CODI_ACU | integer(4) |  |  | Código do acumulador |
| SELECAO_SITUACAO | char(1) |  |  | Seleção da situação |
| SELECAO_ITEM_SERVICO | char(1) |  |  | Seleção do item do serviço |
| SELECAO_CLIENTE | char(1) |  |  | Clientes do acumulador (T = Todos, S = Selecionados) |
