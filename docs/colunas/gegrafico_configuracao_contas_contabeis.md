# GEGRAFICO_CONFIGURACAO_CONTAS_CONTABEIS — Dados dos gráficos criado pelo usuário e gráficos padrões.
30 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  |  |
| CODIGO_USUARIO | integer(4) |  |  | Código do usuário, para gráico padrão informar 0. |
| NOME | varchar(128) |  |  | Nome do gráfico. |
| TITULO | varchar(128) |  | S | Titulo do gráfico. |
| TIPO_GRAFICO | integer(4) |  |  | Tipo do gráfico, consultar tabela GEGRAFICO_TIPO. |
| INTERVALO_EMISSAO | integer(4) |  |  | Intervalo de emissão dos dados. 1-Mensal; 2-Trimestral |
| ITENS_AGRUPAMENTO | integer(4) |  |  | Informa a quantidade de contas contábeis que serão agrupadas. |
| GRAFICO_PADRAO | integer(4) |  |  | Gráfico padrão, inserido na atualização de banco. 0-Não; 1-Sim |
| CODIGO_MODULO | integer(4) | PK |  | Código do módulo que o gráfico pertence |
