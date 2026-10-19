# GEGRAFICO_CONTAS_CONTABEIS — Tabela referente as contas contabeis que devem ser emitidas no grafico.
217 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO_GRAFICO | integer(4) | PK |  | Código do gráfico. |
| CODIGO_EMPRESA | integer(4) | PK |  | Empresa selecionado. |
| CODIGO_CONTA_CONTABIL | integer(4) | PK |  | Código da conta contábil |
| CLASSIFICACAO | varchar(32) |  |  | Classificação da conta contábil |
| DESCRICAO | varchar(256) |  |  | Descrição da conta contábil |
| POSICAO_ITEM | integer(4) |  |  | Posição do item |
