# HRPAGAMENTO — Pagamentos de contas a pagar
8.118 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_PAGAR | integer(4) | PK |  | Lancamento a pagar |
| I_PARCELA | integer(4) | PK |  | Parcela |
| I_PAGAMENTO | integer(4) | PK |  | Codigo |
| I_MOVIMENTO_ESCRITORIO | integer(4) |  | S | Conta corrente escritorio |
| I_CONTA_FINANCEIRA | integer(4) |  |  | Conta financeira |
| I_HISTORICO | integer(4) |  | S | Codigo do historico |
| HISTORICO | varchar(512) |  |  | Historico |
| DATA_PAGAMENTO | date(4) |  |  | Data do pagamento |
| GERAR_VALOR | char(1) |  |  | Gerar valor I Individual por parcela A Agrupado por fornecedor T Total geral das parcelas |
| VALOR | numeric(13) |  |  | Valor liquido do pagamento |
| VALOR_PAGO | numeric(13) |  |  | Valor bruto do pagamento |
| VALOR_JUROS | numeric(13) |  |  | Valor do juros |
| VALOR_MULTA | numeric(13) |  |  | Valor da multa |
| VALOR_DESCONTO | numeric(13) |  |  | Valor de desconto |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| REALIZAR_PAGAMENTO_COM_CHEQUE | char(1) |  |  | Realizar pagamento com cheques (S/N) |
| REALIZAR_PAGAMENTO_COM_CHEQUE_RECEBIDO_DE_CLIENTE | char(1) |  |  | Realizar pagamento com cheques recebidos de clientes |
| ORIGEM | char(1) |  |  | Origem do lançamento (M - Manual/A - Automática) |
