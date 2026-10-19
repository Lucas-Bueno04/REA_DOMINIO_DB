# GEATENDIMENTOWEBSOCKET_SGD_NOTIFICACOES — Notificações de suporte e notícias recebidas pelo websocket
3.035 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Codigo auto numeração |
| CODI_EMP | integer(4) |  | S | Codigo da empresa |
| MSG_WEBSOCKET | long varchar(32767) |  |  | Mensagem retornada do WS |
| DATA_HORA_INSERCAO | timestamp(8) |  |  | Data hora da gravação |
| DATA_HORA_PROCESSAMENTO | timestamp(8) |  | S | Data hora do processamento |
| ACAO_PROCESSADA | bit(1) |  |  | Marca se a mensagem foi processada |
| TIPO_ATIVACAO | tinyint(1) |  | S | Tipo de ativação |
