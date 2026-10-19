# EFTABELA_CLASSIFICACAO_TRIBUTARIA_IS — Tabela Classificacao de classificação tributaria do imposto seletivo - IS
30 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_TABELA_IS | integer(4) | PK |  | SEQUENCIAL TABELA IS |
| VIGENCIA | date(4) | PK |  | Vigencia |
| CCLASSTRIB | varchar(6) | PK |  | Código Classificação tributaria IS |
| DESCRICAO_CCLASSTRIB | varchar(2000) |  |  | Descrição classificação tributaria |
| CST | integer(4) |  |  | CST |
| DESCRICAO_CST | varchar(1000) |  |  | Descrição CST |
