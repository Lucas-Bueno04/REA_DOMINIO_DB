# GECHATBOT_RELATORIOS — Tabela com os relatórios configurados para o chatbot.
32 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Código do relatório. |
| GUID_RELATORIO | uniqueidentifier(16) |  |  | GUID do relatório |
| RELATORIO | varchar(256) |  |  | Descrição do relatório. |
| CODIGO_MODULO | integer(4) |  |  | Código do módulo do relatório. |
| TEMPO_LIMITE_EXECUCAO | integer(4) |  |  | Tempo limite para a execução do relatório |
| VERSAO_CONTABIL | char(8) |  |  | Versão mínima do contábil para a execução do relatório |
| POSSUI_SUB_RELATORIO | integer(4) |  |  | Definir que o relatorio possui sub-relatorios que são executados a partir deste relatorio. |
| PARAMETRO_LINK_DOCUMENTO | varchar(2048) |  | S | Campos responsavel por controlar o nome do parametro onde o link do documento sera disponibilizado na mensagem de resposta. |
| LAYOUT_MENSAGEM_RESPOSTA | varchar(2048) |  | S | Layout da mensagem para ser enviada ao cliente quando o relatorio for gerado. |
| LAYOUT_NOME_DOCUMENTO | varchar(2048) |  |  | Campo que define o formato do nome do documento publicado pelo Onvio Messenger |
