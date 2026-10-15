# HRCONTA_CORRENTE_CLIENTE — Conta corente do cliente
88.987 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_MOVIMENTO_CLIENTE | integer(4) | PK |  | Codigo |
| I_MOVIMENTO_CLIENTE_SEQ | integer(4) | PK |  | Sequencial |
| DETALHE | char(1) |  |  | DETALHE DO MOVIMENTO (P=PRINCIPAL/ J=JUROS E MULTA/ D=DESCONTO/ R=RETENCOES/ U=JUROS/ M=MULTA) |
| I_CLIENTE | integer(4) |  |  | Cliente |
| DATA_MOVIMENTO | date(4) |  |  | Data |
| TIPO | char(1) |  |  | Tipo E Entrada S Saida |
| ORIGEM | char(1) |  |  | ORIGEM (F=FATURAMENTO/ P=PAGAMENTO/ A=ADIANTAMENTO/ C=CANCELAMENTO DE NOTA FISCAL/ E=PAGO PELO ESCRITORIO/ R=RENEGOCIAÇÃO) |
| VALOR | numeric(13) |  |  | Valor |
| I_HISTORICO | integer(4) |  | S | Codigo do historico |
| HISTORICO | varchar(512) |  |  | Historico |
