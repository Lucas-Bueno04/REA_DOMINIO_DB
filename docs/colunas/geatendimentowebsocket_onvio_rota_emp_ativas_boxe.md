# GEATENDIMENTOWEBSOCKET_ONVIO_ROTA_EMP_ATIVAS_BOXE — Armazena mensagens recebidos pelo websocket referente a rota que informa as empresas que utilizam box-e/manifesto.
9.084 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI | integer(4) | PK |  | CÃ³digo sequencial. |
| MSG_WEBSOCKET | long varchar(32767) |  |  | Mensagem recebida pelo websocket. |
| DATA_HORA_INSERCAO | timestamp(8) |  |  | Data em que foi inserida a mensagem na base de dados pelo Agente de ComunicaÃ§Ã£o. |
| DATA_HORA_PROCESSAMENTO | timestamp(8) |  | S | Data em que foi processada a mensagem pela thread que efetua a regra de negÃ³cio. |
| ACAO_PROCESSADA | bit(1) |  |  | 0-NÃ£o/1-Sim. Informa se a mensagem foi processada pela thread responsÃ¡vel. |
| TIPO_ATIVACAO | tinyint(1) |  |  | 1-Boxe/2-Manifesto |
