# FOATENDIMENTO_EVENTOS_ITENS — ITENS DOS EVENTOS DOMINIO ATENDIMENTO
1.825 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_ATENDIMENTO_EVENTO | integer(4) | PK |  | Código do atendimento referente a FOATENDIMENTO_EVENTOS |
| CODI_EMP_EVE | integer(4) |  |  | Código da empresa referente a FOEVENTOS |
| I_EVENTOS | integer(4) | PK |  | Código do evento referente a FOEVENTOS |
| NOME | varchar(50) |  |  | Nome |
| PROV_DESC | char(2) |  |  | Tipo provento (I=Informativa/P=Provento/D=Desconto/ID=Informativa dedutora) |
| TIPO_INF | char(1) |  |  | Unidade (H=Horas/V=Valor/D=Dias/P=Percentual/A=Automático/G=Horas-Aulas) |
| ORDEM | integer(4) |  | S | Ordem |
| GUID_CONTABIL | uniqueidentifier(16) |  |  | Identificador único do registro no banco do Contábil |
| GUID_ONVIO | uniqueidentifier(16) |  | S | Identificador único do registro no banco do Atendimento Onvio |
| ENDPOINT_EXCLUSAO | varchar(1024) |  | S | Endpoint utilizado para a exclusão do registro. |
