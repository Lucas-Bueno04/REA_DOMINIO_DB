# EFCONFIGURACAO_PRODUTO_POR_NCM_VIGENCIA_ITENS_NCM — Configuração de Impostos para Produtos - Definição de NCMs
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da Empresa |
| I_CONFIGURACAO_NCM | integer(4) | PK |  | Código da Configuração de Produto por NCM |
| DATA_VIGENCIA | date(4) | PK |  | Vigência |
| I_SEQUENCIAL | integer(4) | PK |  | Sequencial |
| I_SEQUENCIAL_NCM | integer(4) | PK |  | Sequencial NCM |
| NCM | char(8) |  |  | Código NCM |
| CODIGO_CEST | char(7) |  | S | Codigo CEST |
