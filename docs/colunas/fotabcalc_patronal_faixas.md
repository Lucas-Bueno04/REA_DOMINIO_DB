# fotabcalc_patronal_faixas — Tabela de Contribuição Sindical Patronal - Faixas
459 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_fotabcalc_patronal | integer(4) | PK |  | Código |
| ano | integer(4) | PK |  | Ano |
| valor_inicial | numeric(13) | PK |  | Valor de |
| valor_final | numeric(13) |  |  | Valor até |
| perc | numeric(7) |  |  | Percentual |
| valor | numeric(13) |  |  | Valor a adicionar |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
