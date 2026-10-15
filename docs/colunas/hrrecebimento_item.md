# HRRECEBIMENTO_ITEM — Recebimento de contas a receber - Itens
43.603 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_FATURAMENTO | integer(4) | PK |  | Faturamento |
| I_PARCELA | integer(4) | PK |  | Parcela |
| I_RECEBIMENTO | integer(4) | PK |  | Recebimento |
| I_EVENTO | integer(4) | PK |  | Evento |
| PAGO_ESCRITORIO | char(1) | PK |  | Pago pelo escritorio S N |
| I_MOVIMENTO_CLIENTE | integer(4) |  | S | Conta corrente cliente |
| I_MOVIMENTO_CLIENTE_SEQ | integer(4) |  | S | Conta corrente cliente sequencial |
| VALOR | numeric(13) |  |  | Valor liquido do recebimento do item |
| VALOR_RECEBIDO | numeric(13) |  |  | Valor bruto do recebimento do item |
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
