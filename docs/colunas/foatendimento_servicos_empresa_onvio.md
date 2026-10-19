# FOATENDIMENTO_SERVICOS_EMPRESA_ONVIO — Tabela para controle das GUIDs de envio pro ONVIO, mantendo comportamento do DA antigo que era feito select envolvendo multiplas tabelas.
1.494 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
| CODI_EMP | integer(4) |  |  | Código da empresa |
| I_SERVICOS | integer(4) |  |  | Código do serviço |
| NOME | varchar(40) |  | S | Nome |
| CODI_EMP_ATENDIMENTO | integer(4) |  |  | Código da empresa no ONVIO |
| GUID_CONTABIL | uniqueidentifier(16) |  |  | Identificador único do registro no banco do Contábil |
| GUID_ONVIO | uniqueidentifier(16) |  | S | Identificador único do registro no banco do Atendimento Onvio |
| ENDPOINT_EXCLUSAO | varchar(1024) |  | S | Endpoint utilizado para a exclusão do registro. |
