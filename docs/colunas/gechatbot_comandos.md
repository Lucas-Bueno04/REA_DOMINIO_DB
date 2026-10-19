# GECHATBOT_COMANDOS — Tabela com os comandos em ordem de execução para cada relatório.
191 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Código do comando. |
| CODIGO_RELATORIO | integer(4) | PK |  | Código do relatório. |
| TIPO_COMPONENTE | integer(4) |  |  | Tipo do componente? 1 - Command button; 2 - Radio button; 3 - Edit mask; 4 - Dropdown list box; 5 - Datawindow; 6 - Single line edit; 7 - Check box; 8 - Menu |
| COMPONENTE | varchar(128) |  |  | Class name do componente. |
| TEXTO_COMPONENTE | varchar(128) |  |  | Descrição do componente. |
| PARAMETRO | varchar(128) |  | S | Nome do parâmetro. |
| JANELA | varchar(128) |  |  | Nome da janela a ser aberta. |
| NOME_DATAOBJECT | varchar(128) |  |  | Nome do dataobject (utilizado quando o componente for do tipo datawindow). |
| NOME_COLUNA | varchar(128) |  |  | Nome da coluna sobre a qual será realizada a ação (utilizado quando o componente for do tipo datawindow). |
| TIPO_ACAO | integer(4) |  |  | Tipo da ação: 1 - Preencher; 2 - Selecionar |
| PARAMETRO_VALOR_PADRAO | varchar(128) |  | S | Caso o parametro de busca no JSON não for informado ou o mesmo for informado porem nao for encontrado, será utilizado o valor informado nesta coluna. |
