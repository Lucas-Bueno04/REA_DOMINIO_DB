# GEGRAFICO_PLANO_CONTAS_EMPRESA — Tabela referente ao plano de conta selecionado para cada gráfico.
83 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO_GRAFICO | integer(4) | PK |  | Código do gráfico. |
| CODIGO_EMPRESA | integer(4) | PK |  | Empresa selecionado. |
| TIPO_SALDO_CONTA_CONTABIL | integer(4) |  |  | 1- Saldo do período; 2-Saldo do exercício; 3-Total de débitos; 4-Total de créditos |
