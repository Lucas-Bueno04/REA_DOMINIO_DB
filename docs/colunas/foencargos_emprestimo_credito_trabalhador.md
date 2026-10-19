# FOENCARGOS_EMPRESTIMO_CREDITO_TRABALHADOR — Encargos do empréstimo do crédito do trabalhador da competência
465 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| COMPETENCIA | date(4) | PK |  | Competência |
| TIPO_PROCESSO | smallint(2) | PK |  | Tipo cálculo folha |
| VALOR_TOTAL | numeric(13) |  |  | Valor total |
| VENCIMENTO | date(4) |  |  | Data de vencimento |
| I_FILIAIS | integer(4) | PK |  | Sequêncial da filial |
| I_PAGTO | integer(4) |  | S | Sequêncial de pagamento |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
