# GECONSULTA_WEB_SERVICE_PORTAL_FEDERAL — Consulta NF-e Webservice Portal Federal
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Código |
| NOME_CONEXAO | varchar(128) |  |  | Nome da conexão |
| HORARIO_DOWNLOAD_XML | char(1) |  |  | Horário para download do XML |
| HORARIO_DOWNLOAD_XML_INICIO | time(8) |  | S | Horário início para download do XML |
| HORARIO_DOWNLOAD_XML_FIM | time(8) |  | S | Horário fim para download do XML |
| ENVIO_BOXE | char(1) |  |  | Envio de notas para o BOX-e |
| HORARIO_ENVIO_BOXE_INICIO | time(8) |  | S | Horário início para envio de notas para o BOX-e |
| HORARIO_ENVIO_BOXE_FIM | time(8) |  | S | Horário fim para envio de notas para o BOX-e |
| EMAIL_RETORNO | varchar(128) |  | S | E-mail de retorno |
| TIPO_INICIALIZACAO | char(1) |  |  | Tipo de inicialização |
| INICIAR_PARAR | integer(4) |  |  | Iniciar / Parar agora |
| CONFIGURAR_PROXY | char(1) |  |  | Configurar proxy |
| ENDERECO_PROXY | varchar(128) |  | S | Endereço do Proxy |
| PORTA_PROXY | integer(4) |  | S | Porta do Proxy |
| USUARIO_PROXY | varchar(128) |  | S | Usuário do Proxy |
| SENHA_PROXY | varchar(128) |  | S | Senha do Proxy |
| NUMERO_PORTA_CONEXOES_ENTRADA | integer(4) |  | S | Número da porta a ser utilizada nas conexões de entrada |
| DESATIVAR_UPNP | char(1) |  |  | Desativar uPnP |
| CODIGO_IDENTIFICADOR | varchar(50) |  | S | Código identificador gerado em cima do número de série |
