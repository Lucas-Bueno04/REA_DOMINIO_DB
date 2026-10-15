# HRCONTA_CORRENTE_ESCRITORIO — Conta corrente do escritorio
65.980 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_MOVIMENTO_ESCRITORIO | integer(4) | PK |  | Codigo |
| DATA_MOVIMENTO | date(4) |  |  | Data |
| TIPO | char(1) |  |  | Tipo E Entrada S Saida T Transferencia |
| ORIGEM | char(1) |  |  | Origem - M-Manual/F-Pagamento fornecedor/I-Pagamento imposto/P-Pagamento funcionario/C-Pagamento de item para cliente/R-Recebimento/A-Adiantamento/H-Cheque/X-Extrato Bancário |
| VALOR | numeric(13) |  |  | Valor |
| I_CONTA_FINANCEIRA_ORIGEM | integer(4) |  | S | Conta financeira origem |
| I_CONTA_FINANCEIRA_DESTINO | integer(4) |  | S | Conta financeira destino |
| I_CATEGORIA_RECEBER | integer(4) |  | S | Categoria a receber |
| I_CATEGORIA_PAGAR | integer(4) |  | S | Categoria a pagar |
| I_HISTORICO | integer(4) |  | S | Codigo do historico |
| HISTORICO | varchar(512) |  |  | Historico |
