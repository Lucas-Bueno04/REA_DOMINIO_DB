# EFONBALANCE_EMPRESAS — OnBalance - LicenÃ§a das empresas
778 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_SEQ_ATENDIMENTO | integer(4) | PK |  | CÃ³digo sequencial da empresa no Atendimento |
| TIPO_LICENCA | integer(4) |  |  | Tipo da licenÃ§a |
| ENVIAR_CLIENTES | integer(4) |  |  |  |
| ENVIAR_FORNECEDORES | integer(4) |  |  |  |
| ENVIAR_PRODUTOS | integer(4) |  |  |  |
| ENVIAR_ICMS_INTERESTADUAL | integer(4) |  |  |  |
| ENVIAR_ICMS_SIMPLES | integer(4) |  |  |  |
| ENVIO_CONCLUIDO | integer(4) |  |  |  |
| GUID_ONVIO_EMPRESA | uniqueidentifier(16) |  | S | Identificador único da empresa banco do Atendimento Onvio |
| ATIVA | integer(4) |  |  | Empresa Ativo no OnBalance |
