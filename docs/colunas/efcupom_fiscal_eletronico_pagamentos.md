# EFCUPOM_FISCAL_ELETRONICO_PAGAMENTOS — Cupom Fiscal Eletrônico - CF-e - Parcelas - Pagamentos
376 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_CFE | integer(4) | PK |  | Código do CF-e |
| I_PARCELA | integer(4) | PK |  | Número da parcela |
| I_PAGAMENTO | integer(4) | PK |  | Número do pagamento |
| DATA_PAGAMENTO | date(4) |  |  | Data do pagamento |
| NUMERO_TITULO | varchar(60) |  | S | Número do título |
| VALOR_PAGO | numeric(13) |  |  | Valor do pagamento |
| VALOR_JUROS | numeric(13) |  |  | Valor dos juros |
| VALOR_MULTA | numeric(13) |  |  | Valor da multa |
| VALOR_OUTRAS | numeric(13) |  |  | Valor de outras |
| VALOR_DESCONTO | numeric(13) |  |  | Valor do desconto |
| VALOR_DEVOLUCAO | numeric(13) |  |  | Valor da devolução |
| CODI_ACU | integer(4) |  | S | Acumulador |
| ORIGEM_BAIXA | char(1) |  |  | Origem do pagamento (B - Baixa/L - Lançamento) |
| HISTORICO_DE_RECEBIMENTO | varchar(200) |  | S | Histórico de recebimento |
| CODI_ENT | integer(4) |  | S | Código da Nota de devolução |
| I_NOTA_DEVOLVIDA | integer(4) |  | S | Sequencial da Nota de devolução |
