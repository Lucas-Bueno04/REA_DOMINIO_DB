# FOATENDIMENTO_EVENTOS_ITENS_FILIAIS_BACKUP — Tabela apenas para backup de dados
16 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  |  |
| I_ATENDIMENTO_EVENTO | integer(4) | PK |  |  |
| I_EVENTOS | integer(4) | PK |  |  |
| I_FILIAIS | integer(4) | PK |  |  |
| GUID_CONTABIL | uniqueidentifier(16) |  |  |  |
| GUID_ONVIO | uniqueidentifier(16) |  | S |  |
| ENDPOINT_EXCLUSAO | varchar(1024) |  | S |  |
