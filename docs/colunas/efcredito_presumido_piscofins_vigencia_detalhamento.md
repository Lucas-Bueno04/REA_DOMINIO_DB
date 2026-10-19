# EFCREDITO_PRESUMIDO_PISCOFINS_VIGENCIA_DETALHAMENTO — Tabela de Crédito Presumido PIS e COFINS - Relação de NCM
9 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CREDITO_PRESUMIDO | integer(4) | PK |  | Sequencial do Crédito Presumido |
| VIGENCIA | date(4) | PK |  | Vigência |
| I_CREDITO_PRESUMIDO_DETALHAMENTO | integer(4) | PK |  | Sequencial do Detalhamento |
| NCM | char(8) |  | S | NCM |
| DESCRICAO | varchar(1024) |  | S | Descrição do NCM |
| EX_TIPI | char(3) |  | S | EX TIPI |
| VALOR_PIS | numeric(13) |  |  | Valor de PIS |
| VALOR_COFINS | numeric(13) |  |  | Valor de COFINS |
