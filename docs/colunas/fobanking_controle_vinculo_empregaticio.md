# FOBANKING_CONTROLE_VINCULO_EMPREGATICIO — Controla o que deve ou não ser enviado ao banking em relação aos vinculos empregatícios das pessoas.
10.025 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Código sequencial |
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| GUID_ONVIO_EMPRESA | uniqueidentifier(16) |  | S | Identificador único da empresa no ONVIO |
| DATA_HORA_INSERCAO | timestamp(8) |  |  | Data em que a pessoa foi inserida na tabela |
| DATA_HORA_PROCESSAMENTO | timestamp(8) |  | S | Data em que foi processado pelo agente |
| COMPETENCIA_CONTROLE_ENVIO_MENSAL | date(4) |  | S | Competência para controle do envio mensal. |
| STATUS_ENVIO_MENSAL | integer(4) |  |  | Status do envio mensal (dia 15): 0 - Disponível para envio / 1- Indisponível para envio |
| STATUS | integer(4) |  |  | Status por alteração de afastamento: 0 - Disponível para envio / 1- Indisponível para envio |
| ULTIMO_STATUS_AFASTAMENTO_ENVIADO | char(32) |  | S | Armazena o último status de afastamento enviado ao banking |
