# GEPRPERGUNTAS_RESPOSTAS — Perguntas e Respostas do Checkpoint
1.529 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| ID | uniqueidentifier(16) | PK |  |  |
| ID_FISCO | integer(4) |  |  |  |
| ID_ASSUNTO | uniqueidentifier(16) |  |  |  |
| PERGUNTA | long varchar(32767) |  | S |  |
| RESPOSTA | long varchar(32767) |  | S |  |
| DATA_HORA | timestamp(8) |  | S |  |
| REPLICA | integer(4) |  | S |  |
| TIPO_ATENDIMENTO | varchar(32) |  | S |  |
| DATA_ALTERACAO | timestamp(8) |  | S |  |
| STATUS | integer(4) |  | S |  |
| DATA_VIGENCIA_ATE | date(4) |  | S |  |
| DATA_HORA_INSERCAO | timestamp(8) |  | S |  |
| DATA_HORA_ATUALIZACAO | timestamp(8) |  | S |  |
| EXCLUIDO | integer(4) |  | S |  |
| MAIOR_DATA_HORA_VERSAO | timestamp(8) |  | S |  |
| GUID_CONTABIL | uniqueidentifier(16) |  | S | Identificador Único do registro no banco do Contábil |
| GUID_ONVIO | uniqueidentifier(16) |  | S | Identificador Único do registro no banco do Atendimento Onvio |
