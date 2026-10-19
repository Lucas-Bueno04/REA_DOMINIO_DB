# fopagtoparcial — Pagamentos parciais
8.520 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_pagto | integer(4) | PK |  | Sequencia de pagamento |
| i_pagtoitem | integer(4) | PK |  | Sequencial de Pagamentos |
| data_pagto | date(4) |  |  | Data do pagamento |
| valor | numeric(13) |  |  | Valor do pagamento |
| multa | numeric(13) |  |  | Valor da multa |
| juros | numeric(13) |  |  | Valor de juros |
| gps_inss | numeric(13) |  |  | Valor pago de GPS referente a inss |
| gps_terceiros | numeric(13) |  |  | Valor pago de GPS referente a terceiros |
| i_pagtogrupos | integer(4) |  | S | Sequencial de pagamentos em grupos |
| CODIGO_ESCRITORIO | integer(4) |  | S | Codigo do escritorio Honorarios |
| I_MOVIMENTO_ESCRITORIO | integer(4) |  | S | Conta corrente escritorio Honorarios |
| I_MOVIMENTO_CLIENTE | integer(4) |  | S | Conta corrente cliente Honorarios |
| I_MOVIMENTO_CLIENTE_SEQ | integer(4) |  | S | Conta corrente cliente sequencial Honorarios |
| I_HISTORICO_HR | integer(4) |  | S | Codigo do historico Honorarios |
| HISTORICO_HR | varchar(512) |  | S | Historico Honorarios |
| AJUSTE_GFIP | numeric(13) |  | S | Valor de ajuste para a GFIP. |
| VALOR_PAGO_MAIOR | numeric(13) |  | S | Valor pago a maior. |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_PAGAMENTO_CONTA_AZUL | integer(4) |  | S | Sequencial Baixa parcial Conta Azul |
| GUID_CONTABIL | varchar(36) |  | S | Identificador integração Conta Azul |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout/3=Importação tabelas concorrentes/4=Importação de baixas Conta Azul/5=Importação de baixas Banco Digital) |
