# GEATENDIMENTOWEBSOCKET_ONVIO_ROTA_CONTA_ICEBERG — Armazena mensagens recebidos pelo websocket referente a rota que busca as contas financeiras do Iceberg
86 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI | integer(4) | PK |  | Código sequencial. |
| MSG_WEBSOCKET | long varchar(32767) |  |  | Mensagem recebida pelo websocket. |
| DATA_HORA_INSERCAO | timestamp(8) |  |  | Data em que foi inserida a mensagem na base de dados pelo Agente de Comunicação. |
| DATA_HORA_PROCESSAMENTO | timestamp(8) |  | S | Data em que foi processada a mensagem pela thread que efetua a regra de negócio. |
| ACAO_PROCESSADA | integer(4) |  |  | 0-Não/1-Sim/2-aguardando. Informa se a mensagem foi processada pela thread responsável. |
| MESSAGE_ID | varchar(50) |  | S | messageId do Payload |
| CONSENT_ID | varchar(50) |  | S | Identificador do consentimento Open Banking |
| PARTNER | varchar(100) |  | S | Parceiro de conexão Open Banking |
| SCHEMA_VERSION | varchar(10) |  | S | Versão do schema do payload da fintech |
| DATA_HORA_ULTIMA_VERIFICACAO | timestamp(8) |  | S | Data para controle de reprocessamento |
