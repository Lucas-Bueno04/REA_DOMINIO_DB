# EFCREDITO_PRESUMIDO_PISCOFINS_VIGENCIA — Tabela de Crédito Presumido PIS e COFINS - Vigência
3 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CREDITO_PRESUMIDO | integer(4) | PK |  | Sequencial do Crédito Presumido |
| VIGENCIA | date(4) | PK |  | Vigência |
| DESCRICAO | varchar(80) |  |  | Descrição |
| PERCENTUAL_AQUISICAO_SIMPLES_NACIONAL_PIS | numeric(7) |  |  | Percentual do Crédito Presumido na aquisição de contribuinte optante pelo Simples Nacional - PIS |
| PERCENTUAL_AQUISICAO_SIMPLES_NACIONAL_COFINS | numeric(7) |  |  | Percentual do Crédito Presumido na aquisição de contribuinte optante pelo Simples Nacional - COFINS |
