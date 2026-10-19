# FOATENDIMENTO_EVENTOS_ITENS_FILIAIS — ITENS DOS EVENTOS DOMINIO ATENDIMENTO
1.825 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_ATENDIMENTO_EVENTO | integer(4) | PK |  | Código do atendimento referente a FOATENDIMENTO_EVENTOS_ITENS |
| I_EVENTOS | integer(4) | PK |  | Código do evento referente a FOATENDIMENTO_EVENTOS_ITENS |
| I_FILIAIS | integer(4) | PK |  | Código filial |
| GUID_CONTABIL | uniqueidentifier(16) |  |  | Identificador único do registro no banco do Contábil |
| GUID_ONVIO | uniqueidentifier(16) |  | S | Identificador único do registro no banco do Atendimento Onvio |
| ENDPOINT_EXCLUSAO | varchar(1024) |  | S | Endpoint utilizado para a exclusão do registro. |
