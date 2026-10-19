# FOTABELA_CALCULO_IRRF_PARTICIPACAO_LUCROS_FAIXAS — Faixas da tabela de cálculo de IRRF sobre participação nos lucros.
227 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| COMPETENCIA | date(4) | PK |  | Competência. |
| VALOR_ATE | numeric(13) | PK |  | Valor máximo da faixa. |
| ALIQUOTA | numeric(13) |  |  | Valor da alíquota para o cálculo. |
| VALOR_DESCONTO | numeric(13) |  |  | Valor do desconto. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
