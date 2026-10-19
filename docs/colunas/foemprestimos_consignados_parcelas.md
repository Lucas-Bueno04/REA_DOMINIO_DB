# FOEMPRESTIMOS_CONSIGNADOS_PARCELAS — Parcelas dos empréstimos consignados.
4.435 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| I_EMPRESTIMO | integer(4) | PK |  | Código do empréstimo. |
| PARCELA | smallint(2) | PK |  | Número da parcela. |
| COMPETENCIA_DESCONTO | date(4) |  | S | Competência de pagamento da parcela |
| VALOR | numeric(13) |  |  | Valor da parcela. |
| PAGO | smallint(2) |  |  | Parcela paga. (0=Não/1=Sim) |
| I_CALCULOS_PAGAMENTO_OLD | integer(4) |  | S | Código do cálculo que pagou a parcela - Renomeado |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| VALOR_PAGO | numeric(13) |  |  | Valor efetivamente pago. |
| VALOR_RESTANTE | numeric(13) |  |  | Valor restante a ser pago da parcela. |
| CALCULO_PARCELAS | smallint(2) |  |  | Verifica a situação de calculo das parcelas. (0=Não/1=Sim) |
| I_CALCULOS_PAGAMENTO | uniqueidentifier(16) |  | S | Código do cálculo que pagou a parcela |
| COMPETENCIA_DESCONTO_INFORMADA | date(4) |  | S | Competência de desconto da parcela |
