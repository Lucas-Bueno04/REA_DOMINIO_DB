# GEATENDIMENTOLOG_FRP — Log das requisições de FRP do Portal do Empregado
72 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  |  |
| REQUEST_DATA | timestamp(8) |  |  |  |
| ENDPOINT | char(255) |  | S |  |
| REQUEST_USUARIO_LOGADO | char(180) |  | S |  |
| REQUEST_USUARIO_AUTENTICACAO | char(180) |  | S |  |
| THREAD_ID | integer(4) |  | S |  |
| PROCESS_ID | integer(4) |  | S |  |
| REQUEST_TOOL | char(80) |  | S |  |
| REQUEST_FIRMID | integer(4) |  | S |  |
| REQUEST_LONGTOKEN | uniqueidentifier(16) |  | S |  |
| RESPONSE_CHAINID | uniqueidentifier(16) |  | S |  |
| RESPONSE_LONGTOKEN | uniqueidentifier(16) |  | S |  |
| RESPONSE_COMPANYID | uniqueidentifier(16) |  | S |  |
| RESPONSE_CONTACTID | uniqueidentifier(16) |  | S |  |
| RESPONSE_CONTABILFIRMID | integer(4) |  | S |  |
| RESPONSE_FRP | long varchar(32767) |  | S |  |
