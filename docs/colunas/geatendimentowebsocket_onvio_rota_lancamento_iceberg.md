# GEATENDIMENTOWEBSOCKET_ONVIO_ROTA_LANCAMENTO_ICEBERG — Armazena mensagens recebidos pelo websocket referente a rota que busca as transações do Iceberg
6.948 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI | integer(4) | PK |  | Código sequencial. |
| MSG_WEBSOCKET | long varchar(32767) |  |  | Mensagem recebida pelo websocket. |
| DATA_HORA_INSERCAO | timestamp(8) |  |  | Data em que foi inserida a mensagem na base de dados pelo Agente de Comunicação. |
| DATA_HORA_PROCESSAMENTO | timestamp(8) |  | S | Data em que foi processada a mensagem pela thread que efetua a regra de negócio. |
| ACAO_PROCESSADA | integer(4) |  |  | -2 - Transações ignoradas, -1 - Automação, 0 - Pendentes, 1 - Processadas, 2 - Não implementado, 4 - Pendente de Reprocessar |
| MESSAGE_ID | varchar(50) |  | S | messageID do PayLoad |
| CLIENT_ID | varchar(50) |  | S | clientId do PayLoad |
| MESSAGE_ORIGIN | varchar(50) |  | S | messageOrigin do PayLoad |
| ID_TRANSACAO | varchar(50) |  | S | Identificador da transação |
| TRANSACTION_ID | varchar(50) |  | S | Identificador da transação por client_id |
| PARTNER | varchar(100) |  | S | Parceiro de conexão Open Banking |
| SCHEMA_VERSION | varchar(10) |  | S | Versão do schema do payload da fintech |
| STATUS_TRANSACAO | integer(4) |  |  | Situação da transação após processamento (1=Transação Original/2=Atualizada/3=Atualizada Apos Fechamento/4=Excluida Apos Fechamento/5=Atualizada Com Vinculo/6=Excluida Com Vinculo) |
| CODI_HISTORY | integer(4) |  | S | Sequencial do JSON que atualizou a linha original |
| DATA_TRANSACAO | timestamp(8) |  | S | Data da transação |
| CONSENT_ID | varchar(100) |  | S | Consent_id da transação |
