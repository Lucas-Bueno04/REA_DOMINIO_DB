# FOCONTRIBUICAO_SINDICAL_SINDICATOS_P — Tabela de valores de contribuições sindicais por sindicato patronal
6 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CONTRIBUICAO_SINDICAL_OLD | integer(4) |  | S | Código da contribuição sindical - Renomeado |
| I_SINDICATOS_P | integer(4) | PK |  | Código do sindicato patronal |
| VALOR | numeric(13) |  |  | Valor da contribuição |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CONTRIBUICAO_SINDICAL | uniqueidentifier(16) | PK |  | Código da contribuição sindical |
