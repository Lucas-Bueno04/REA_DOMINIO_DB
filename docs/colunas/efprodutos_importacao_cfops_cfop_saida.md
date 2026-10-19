# EFPRODUTOS_IMPORTACAO_CFOPS_CFOP_SAIDA — Produtos - Cadastro - Importação - Relacionamento de CFOPs - CFOP saída
66 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_PDI | char(14) | PK |  | Produto |
| I_CFOP_ENTRADA | integer(4) | PK |  | Sequencial do CFOP de entrada |
| I_CFOP_SAIDA | integer(4) | PK |  | Sequencial do CFOP de saída |
| CFOP | integer(4) |  |  | CFOP de saída |
| VERSAO_CFOP | smallint(2) |  |  | Versão do CFOP de saída |
