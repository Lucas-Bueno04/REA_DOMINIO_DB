# HRRECEBIMENTO — Recebimento de contas a receber
43.042 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_FATURAMENTO | integer(4) | PK |  | Faturamento |
| I_PARCELA | integer(4) | PK |  | Parcela |
| I_RECEBIMENTO | integer(4) | PK |  | Codigo |
| I_MOVIMENTO_ESCRITORIO | integer(4) |  | S | Conta corrente escritorio |
| I_CONTA_FINANCEIRA | integer(4) |  | S | Conta financeira |
| I_HISTORICO | integer(4) |  | S | Codigo do historico |
| HISTORICO | varchar(512) |  |  | Historico |
| DATA_RECEBIMENTO | date(4) |  |  | Data do recebimento |
| GERAR_VALOR | char(1) |  |  | Gerar valor I Individual por parcela A Agrupado por cliente T Total geral das parcelas |
| ORIGEM | char(1) |  |  | Origem D Individual G Em grupo R Reneg recebimento P Reneg reparcelada Q Reneg quitada N Reneg novo fat A Adiantamento F Faturamento I Consulta Fat Integral E Consulta Fat Evento C Consulta Cliente S Cancelar NF B Imp Boletos M Recebimento Automatico Boleto X Recebimento Automatico qrcode |
| VALOR | numeric(13) |  |  | Valor liquido do recebimento |
| VALOR_RECEBIDO | numeric(13) |  |  | Valor bruto do recebimento |
| VALOR_JUROS | numeric(13) |  |  | Valor de juros |
| VALOR_MULTA | numeric(13) |  |  | Valor de multa |
| VALOR_DESCONTO | numeric(13) |  |  | Valor de desconto |
| VALOR_IRRF | numeric(13) |  |  | Valor IRRF |
| VALOR_CRF | numeric(13) |  |  | Valor CRF |
| VALOR_CRF_PIS | numeric(13) |  |  | Valor de CRF PIS |
| VALOR_CRF_COFINS | numeric(13) |  |  | Valor de CRF COFINS |
| VALOR_CRF_CSLL | numeric(13) |  |  | Valor de CRF CSLL |
| VALOR_REFATURADO | numeric(13) |  |  | Valor refaturado |
| VALOR_REPARCELADO | numeric(13) |  |  | Valor reparcelado |
| VALOR_QUITADO | numeric(13) |  |  | Valor quitado sem recebimento |
| DIMINUIR_BOLETO | char(1) |  |  | Diminuir este recebimento na emissao do boleto S N |
| DIMINUIR_COBRANCA | char(1) |  |  | Diminuir este recebimento na emissao do documento de cobranca S N |
| USUARIO | varchar(128) |  |  | Usuario que efetuou o recebimento |
| DATA_HORA | timestamp(8) |  |  | Data e hora do recebimento |
| PERMITIR_RECEBER_VALOR_MAIOR_COMO_ADIANTAMENTO | char(1) |  |  | Permitir receber valor maior que o devido e gerar como adiantamento(S/N) |
| VALOR_RECEBIDO_A_MAIOR | numeric(13) |  |  | Valor recebido a maior |
| I_ADIANTAMENTO | integer(4) |  | S | Código do adiantamento |
| ID_TRANSACAO | char(150) |  | S | id da transacao que gerou o recebimento |
