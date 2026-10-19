# GEATENDIMENTOWEBSOCKET_ONVIO_ROTA_LANCAMENTOS_CONTABEIS — Armazena mensagens recebidos pelo websocket referente a rota que informa as empresas que utilizam Lançamentos Contábeis.
128.090 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI | integer(4) | PK |  | Código sequencial. |
| FILE_GUID | uniqueidentifier(16) | PK |  |  |
| SHORT_URL | long varchar(32767) |  |  |  |
| LOCATION | long varchar(32767) |  |  |  |
| CREATED | timestamp(8) |  |  |  |
| SHORT_URL_CREATEDAT | timestamp(8) |  |  |  |
| HASMORE | bit(1) |  |  |  |
| PACKAGE | bit(1) |  |  |  |
| DATA_HORA_INSERCAO | timestamp(8) |  |  | Data em que foi inserida a mensagem na base de dados pelo Agente de Comunicação. |
| DATA_HORA_PROCESSAMENTO | timestamp(8) |  | S | Data em que foi processada a mensagem pela thread que efetua a regra de negócio. |
| ACAO_PROCESSADA | bit(1) |  |  | 0-Não/1-Sim. Informa se a mensagem foi processada pela thread responsável. |
| GUID_ONVIO | uniqueidentifier(16) |  | S | Identificador único do registro no banco do Atendimento Onvio |
