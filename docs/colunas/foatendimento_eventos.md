# FOATENDIMENTO_EVENTOS — EVENTOS DOMINIO ATENDIMENTO
238 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_ATENDIMENTO_EVENTO | integer(4) | PK |  | Código do atendimento |
| NOME | varchar(50) |  |  | Nome |
| TIPO_PROCESO | integer(4) |  |  | Tipo da folha (11=Mensal/41=Adiantamento/70=Participação de lucros/...) |
| COMPETENCIA | date(4) |  |  | Competência |
| TIPO_LACAMENTO_HORAS | char(1) |  |  | Lançamento de hora (D = Horas decimais/M = Horas minutos) |
| GUID_CONTABIL | uniqueidentifier(16) |  |  | Identificador único do registro no banco do Contábil |
| GUID_ONVIO | uniqueidentifier(16) |  | S | Identificador único do registro no banco do Atendimento Onvio |
| ENDPOINT_EXCLUSAO | varchar(1024) |  | S | Endpoint utilizado para a exclusão do registro. |
