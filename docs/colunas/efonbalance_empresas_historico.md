# EFONBALANCE_EMPRESAS_HISTORICO — log de alteraÃ§Ãµes da tabela EFONBALANCE_EMPRESAS
7 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  |  |
| DATA_OPERACAO | timestamp(8) |  |  |  |
| TIPO_OPERACAO | integer(4) |  |  |  |
| USUARIO | char(128) |  |  | UsuÃ¡rio responsÃ¡vel pelo log gerado |
| ENVIO_CONCLUIDO_ANTES | integer(4) |  | S |  |
| ENVIO_CONCLUIDO_DEPOIS | integer(4) |  | S |  |
| GUID_ONVIO_EMPRESA_ANTES | uniqueidentifier(16) |  | S |  |
| GUID_ONVIO_EMPRESA_DEPOIS | uniqueidentifier(16) |  | S |  |
| TIPO_LICENCA_ANTES | integer(4) |  | S |  |
| TIPO_LICENCA_DEPOIS | integer(4) |  | S |  |
| ENVIAR_PRODUTOS_ANTES | integer(4) |  | S |  |
| ENVIAR_PRODUTOS_DEPOIS | integer(4) |  | S |  |
| ENVIAR_ICMS_SIMPLES_ANTES | integer(4) |  | S |  |
| ENVIAR_ICMS_SIMPLES_DEPOIS | integer(4) |  | S |  |
| ENVIAR_ICMS_INTERESTADUAL_ANTES | integer(4) |  | S |  |
| ENVIAR_ICMS_INTERESTADUAL_DEPOIS | integer(4) |  | S |  |
| ENVIAR_FORNECEDORES_ANTES | integer(4) |  | S |  |
| ENVIAR_FORNECEDORES_DEPOIS | integer(4) |  | S |  |
| ENVIAR_CLIENTES_ANTES | integer(4) |  | S |  |
| ENVIAR_CLIENTES_DEPOIS | integer(4) |  | S |  |
| EMPRESA_ATIVA_ONBALANCE_ANTES | integer(4) |  | S |  |
| EMPRESA_ATIVA_ONBALANCE_DEPOIS | integer(4) |  | S |  |
| CODI_SEQ_ATENDIMENTO_ANTES | integer(4) |  | S |  |
| CODI_SEQ_ATENDIMENTO_DEPOIS | integer(4) |  | S |  |
