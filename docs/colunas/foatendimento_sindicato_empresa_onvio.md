# FOATENDIMENTO_SINDICATO_EMPRESA_ONVIO — Tabela referente a view BETHADBA.SINDICATO_EMPRESA_ATENDIMENTO do DA antigo.
398 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
| CODIGO_EMPRESA | integer(4) |  |  | Código da empresa |
| CODIGO_FILIAL | integer(4) |  |  | Código da filial |
| CODIGO_EMPRESA_ATENDIMENTO | integer(4) |  |  | Código da empresa no ONVIO |
| CODIGO_SINDICATO | integer(4) |  |  | Código do sindicato |
| GUID_CONTABIL | uniqueidentifier(16) |  |  | Identificador único do registro no banco do Contábil |
| GUID_ONVIO | uniqueidentifier(16) |  | S | Identificador único do registro no banco do Atendimento Onvio |
| ENDPOINT_EXCLUSAO | varchar(1024) |  | S | Endpoint utilizado para a exclusão do registro. |
