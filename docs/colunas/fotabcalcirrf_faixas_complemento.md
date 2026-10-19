# FOTABCALCIRRF_FAIXAS_COMPLEMENTO — Tabela de faixas para complementar o IRRF a partir de 01/2026 conforme LEI Nº 1,087 DE 2025
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| DATA | date(4) | PK |  | Competência |
| VALOR_ATE | numeric(13) | PK |  | Valor máximo da faixa |
| REDUCAO | numeric(13) |  |  | Valor de redução da faixa |
| FATOR_CORRECAO | numeric(13) |  |  | Fator de correcao aplicado |
