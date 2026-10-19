# GEATENDIMENTO_DIGITALBANK_CATALOGO — 
2.155 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI | integer(4) | PK |  |  |
| CODI_EMP | integer(4) |  |  |  |
| VALOR | numeric(13) |  |  |  |
| MSG_WEBSOCKET | long varchar(32767) |  | S |  |
| ID_TRANSACAO | char(50) |  |  |  |
| DATA_VENCIMENTO | date(4) |  |  |  |
| DATA_PAGAMENTO | date(4) |  |  |  |
| DATA_HORA_PROCESSAMENTO | timestamp(8) |  | S |  |
| ACAO_PROCESSADA | bit(1) |  |  |  |
| CPF | char(11) |  | S |  |
| ORIGEM | varchar(100) |  | S |  |
| MODULO | smallint(2) |  | S |  |
| CODIGO_BANCO | integer(4) |  |  | Codigo de identificacão do banco |
