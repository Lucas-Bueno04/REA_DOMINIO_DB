# GEIMPOSTO_VIGENCIA_PAGAMENTOS_CTB — Impostos - Cadastro - Contas para Pagamento
81.815 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| VIGENCIA_IMP | date(4) | PK |  | Vigencia |
| CTDB_CTP | integer(4) |  | S | Conta debito |
| CTCR_CTP | integer(4) |  | S | Conta credito |
| CHIS_CTP | integer(4) |  | S | Historico padrao |
| JRDB_CTP | integer(4) |  | S | Conta debito dos juros |
| JRCR_CTP | integer(4) |  | S | Conta credito dos juros |
| JRCH_CTP | integer(4) |  | S | Historico padrao dos juros |
| MTDB_CTP | integer(4) |  | S | Conta debito da multa |
| MTCR_CTP | integer(4) |  | S | Conta credito da multa |
| MTCH_CTP | integer(4) |  | S | Historico padrao da multa |
| CTPARCELAMENTOCREDITO | integer(4) |  | S | Conta credito do parcelamento |
| HTPARCELAMENTO | integer(4) |  | S | Historico padrao do parcelamento |
| CTDEBITO_VALOR_PAGO_A_MAIOR | integer(4) |  | S | Débito Valor Pago a Maior - Conta |
| CTCREDITO_VALOR_PAGO_A_MAIOR | integer(4) |  | S | Crédito Valor Pago a Maior  - Conta |
| HT_VALOR_PAGO_A_MAIOR | integer(4) |  | S | Valor Pago a Maior - Histórico |
| CTCORRECAO_DEBITO | integer(4) |  | S | Correção - Conta Débito |
| CTCORRECAO_CREDITO | integer(4) |  | S | Correção - Conta Crédito |
| HTCORRECAO | integer(4) |  | S | Correção - Histórico |
| CTACRESCIMO_DEBITO | integer(4) |  | S | Acrescimo - Conta Débito |
| CTACRESCIMO_CREDITO | integer(4) |  | S | Acrescimo - Conta Crédito |
| HTACRESCIMO | integer(4) |  | S | Acrescimo - Histórico |
| CTDESCONTO_DEBITO | integer(4) |  | S | Desconto - Débito |
| CTDESCONTO_CREDITO | integer(4) |  | S | Desconto - Crédito |
| HTDESCONTO | integer(4) |  | S | Desconto - Histórico |
