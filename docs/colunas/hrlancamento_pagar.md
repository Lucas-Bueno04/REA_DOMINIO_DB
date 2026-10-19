# HRLANCAMENTO_PAGAR — Lancamentos de contas a pagar
6.681 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_PAGAR | integer(4) | PK |  | Codigo |
| TIPO | char(1) |  |  | Tipo do lancamento V A vista P A prazo |
| I_CATEGORIA_PAGAR | integer(4) |  |  | Categoria |
| I_FORNECEDOR | integer(4) |  |  | Fornecedor |
| I_CONTA_FINANCEIRA | integer(4) |  | S | Conta financeira ou possivel conta para pagamento |
| DOCUMENTO | integer(4) |  |  | Documento |
| SERIE | varchar(7) |  |  | Serie |
| EMISSAO | date(4) |  |  | Data de emissao |
| LANCAR | char(1) |  |  | Lancar P Valor da parcela T Valor total |
| VALOR | numeric(13) |  |  | Valor total |
| VALOR_DESCONTO | numeric(13) |  |  | Valor de desconto |
| VALOR_ORIGINAL | numeric(13) |  |  | Valor sem original sem desconto |
| DATA_PAGAMENTO | date(4) |  | S | Data de pagamento |
| I_HISTORICO | integer(4) |  | S | Codigo do historico |
| HISTORICO | varchar(512) |  |  | Historico |
| QUANTIDADE | integer(4) |  |  | Quantidade de parcelas |
| VENCIMENTO_INICIAL | date(4) |  |  | Data de vencimento inicial |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| VALOR_IRRF | numeric(13) |  |  | Valor IRRF |
| VALOR_ISS_RETIDO | numeric(13) |  |  | Valor de ISS Retido |
| VALOR_INSS_RETIDO | numeric(13) |  |  | Valor de INSS Retido |
| VALOR_CRF | numeric(13) |  |  | Valor de CRF |
