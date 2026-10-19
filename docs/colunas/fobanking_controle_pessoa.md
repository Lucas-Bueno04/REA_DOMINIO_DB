# FOBANKING_CONTROLE_PESSOA — Controla o que deve ou não ser enviado ao banking em relação ao cadastro de pessoas.
9.873 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Código sequencial |
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| GUID_ONVIO_EMPREGADO | uniqueidentifier(16) |  | S | Identificador único do empregado no ONVIO |
| CPF | char(11) |  | S | CPF da pessoa |
| DATA_HORA_INSERCAO | timestamp(8) |  |  | Data em que a pessoa foi inserida na tabela |
| DATA_HORA_PROCESSAMENTO | timestamp(8) |  | S | Data em que foi processado pelo agente |
| STATUS | integer(4) |  |  | 0 - Disponível para envio / 1- Indisponível para envio |
| COMPETENCIA_CONTROLE_ENVIO_MENSAL | date(4) |  | S | Competência do controle de envio mensal |
| STATUS_ENVIO_MENSAL | integer(4) |  |  | Status envio mensal |
