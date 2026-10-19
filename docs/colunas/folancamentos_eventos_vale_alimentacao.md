# FOLANCAMENTOS_EVENTOS_VALE_ALIMENTACAO — Lançamentos de vale alimentação.
528 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_VALE_ALIMENTACAO | integer(4) | PK |  | Código do vale alimentação. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| COMPETENCIA | date(4) | PK |  | Competência do lançamento. |
| TIPO_PROCESSO | smallint(2) | PK |  | Tipo de processo do lançamento. |
| TIPO_LANCAMENTO | smallint(2) | PK |  | Tipo do lançamento |
| SEQUENCIAL | integer(4) | PK |  | Sequencial do lançamento. |
| I_EVENTOS | integer(4) |  |  | Código da rubrica do lançamento. |
| NUMERO_DIAS | integer(4) |  |  | Número de dias. |
| NUMERO_VALES | integer(4) |  |  | Número de vales. |
| VALOR_PAGAR | numeric(13) |  |  | Valor a pagar. |
