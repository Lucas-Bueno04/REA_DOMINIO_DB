# GEGRAFICO_LEGENDA — Tabela referente as legendas do gráfico.
6 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Chave primária. |
| CODIGO_GRAFICO | integer(4) |  | S | Código do gráfico que a legenda pertence. |
| LEGENDA_1 | varchar(128) |  | S | Coluna referente a legenda 1 do gráfico. Cada gráfico pode possui até 5 legendas. |
| LEGENDA_2 | varchar(128) |  | S |  |
| LEGENDA_3 | varchar(128) |  | S |  |
| LEGENDA_4 | varchar(128) |  | S |  |
| LEGENDA_5 | varchar(128) |  | S |  |
