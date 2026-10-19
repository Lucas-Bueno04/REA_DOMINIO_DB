# fobancos — Banco - Cadastro
1.218 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_bancos | integer(4) | PK |  | Codigo |
| numero | integer(4) |  |  | Numero |
| agencia | varchar(10) |  |  | Agencia |
| dig_agencia | char(2) |  | S | Digito |
| nome | char(30) |  |  | Nome |
| praca | char(20) |  | S | Praca |
| nome_agencia | char(30) |  | S | Nome agencia |
| modelo_cheque | char(80) |  | S | Modelo cheque |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| GUID_CONTABIL | uniqueidentifier(16) |  |  | Identificador único do registro no banco do Contábil |
| GUID_ONVIO | uniqueidentifier(16) |  | S | Identificador único do registro no banco do Atendimento Onvio |
| ENDPOINT_EXCLUSAO | varchar(1024) |  | S | Endpoint utilizado para a exclusão do registro. |
