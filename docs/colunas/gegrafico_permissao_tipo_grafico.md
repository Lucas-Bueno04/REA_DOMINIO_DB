# GEGRAFICO_PERMISSAO_TIPO_GRAFICO — Tipo de gráficos permitidos na configuração dos dashboards
75 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO_GRAFICO | integer(4) | PK |  | Código do gráfico, referencia a tabela GEGRAFICO_CONFIGURACAO_CONTAS_CONTABEIS |
| CODIGO_MODULO | integer(4) | PK |  | Código do módulo, referencia aos códigos dos módulos do sistema Dominio Contábil |
| CODIGO_TIPO_GRAFICO | integer(4) | PK |  | Tipo do gráfico, referencia a tabela GEGRAFICO_TIPO |
