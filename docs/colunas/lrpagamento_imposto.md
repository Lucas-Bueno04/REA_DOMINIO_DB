# LRPAGAMENTO_IMPOSTO — Pagamento de impostos do Lalur
49 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| COMPETENCIA | date(4) | PK |  | Competência |
| IMPOSTO | char(1) | PK |  | Imposto (C=Contribuição Social/ I=IRPJ) |
| TIPO_CALCULO | char(1) | PK |  | Tipo de cálculo (R=Real/ E=Estimado) |
| I_PARCELA | integer(4) | PK |  | Sequencial da parcela |
| NUMERO_PARCELA | integer(4) | PK |  | Número da parcela |
| I_PAGAMENTO | integer(4) | PK |  | Sequencial |
| DATA_PAGAMENTO | date(4) |  |  | Data de pagamento |
| VALOR | numeric(13) |  |  | Valor líquido do pagamento |
| VALOR_PAGO | numeric(13) |  |  | Valor bruto do pagamento |
| VALOR_JUROS | numeric(13) |  |  | Valor de juros |
| VALOR_MULTA | numeric(13) |  |  | Valor de multa |
| AJUSTE_ANUAL | integer(4) | PK |  | Ajuste Anual |
| VALOR_COMPENSADO | numeric(13) |  |  | Valor compensado |
| VALOR_PAGO_MAIOR | numeric(13) |  | S | Valor pago a maior. |
