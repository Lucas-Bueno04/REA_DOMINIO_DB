# FOATENDIMENTO_EVENTOS_ITENS_BACKUP — Tabela apenas para backup de dados
16 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  |  |
| I_ATENDIMENTO_EVENTO | integer(4) | PK |  |  |
| CODI_EMP_EVE | integer(4) |  |  |  |
| I_EVENTOS | integer(4) | PK |  |  |
| NOME | varchar(50) |  |  |  |
| PROV_DESC | char(1) |  |  |  |
| TIPO_INF | char(1) |  |  |  |
| ORDEM | integer(4) |  | S |  |
| GUID_CONTABIL | uniqueidentifier(16) |  |  |  |
| GUID_ONVIO | uniqueidentifier(16) |  | S |  |
| ENDPOINT_EXCLUSAO | varchar(1024) |  | S |  |
