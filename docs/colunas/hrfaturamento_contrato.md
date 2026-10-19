# HRFATURAMENTO_CONTRATO — Faturamento - Contratos
35.038 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_FATURAMENTO | integer(4) | PK |  | Faturamento |
| I_CONTRATO | integer(4) |  |  | Contrato |
| I_EVENTO | integer(4) |  |  | Evento do contrato |
| VALOR | numeric(13) |  |  | Valor |
| VALOR_DESCONTO | numeric(13) |  |  | Valor de desconto |
| VALOR_DESCONTO_ADIMPLENTE | numeric(13) |  |  | Valor de desconto concedido por adimplente |
| VALOR_ORIGINAL | numeric(13) |  |  | Valor original |
| CONTABIL_LIMITE | integer(4) |  |  | Limite de numero de lancamentos contabeis |
| CONTABIL_FATURADO | integer(4) |  |  | Numero de lancamentos contabeis faturados |
| FISCAL_LIMITE | integer(4) |  |  | Limite de numero de notas ficais |
| FISCAL_FATURADO | integer(4) |  |  | Numero de notas ficais faturados |
| HORA_LIMITE | integer(4) |  |  | Limite de numero de horas trabalhadas |
| HORA_FATURADO | integer(4) |  |  | Numero de horas trabalhadas faturadas |
| HORA_CONTABILIDADE_LIMITE | integer(4) |  |  | Limite de numero de horas trabalhadas na contabilidade |
| HORA_CONTABILIDADE_FATURADO | integer(4) |  |  | Numero de horas trabalhadas na contabilidade faturadas |
| HORA_FOLHA_LIMITE | integer(4) |  |  | Limite de numero de horas trabalhadas na folha |
| HORA_FOLHA_FATURADO | integer(4) |  |  | Numero de horas trabalhadas na folha faturadas |
| HORA_ESCRITA_LIMITE | integer(4) |  |  | Limite de numero de horas trabalhadas na escrita |
| HORA_ESCRITA_FATURADO | integer(4) |  |  | Numero de horas trabalhadas na escrita faturadas |
| HORA_PATRIMONIO_LIMITE | integer(4) |  |  | Limite de numero de horas trabalhadas no patrimonio |
| HORA_PATRIMONIO_FATURADO | integer(4) |  |  | Numero de horas trabalhadas no patrimonio faturadas |
| HORA_LALUR_LIMITE | integer(4) |  |  | Limite de numero de horas trabalhadas no lalur |
| HORA_LALUR_FATURADO | integer(4) |  |  | Numero de horas trabalhadas no lalur faturadas |
| HORA_ATUALIZAR_LIMITE | integer(4) |  |  | Limite de numero de horas trabalhadas no atualizar |
| HORA_ATUALIZAR_FATURADO | integer(4) |  |  | Numero de horas trabalhadas no atualizar faturadas |
| HORA_REGISTRO_LIMITE | integer(4) |  |  | Limite de numero de horas trabalhadas no registro |
| HORA_REGISTRO_FATURADO | integer(4) |  |  | Numero de horas trabalhadas no registro faturadas |
| FUNCIONARIO_LIMITE | integer(4) |  |  | Limite de numero de empregados |
| FUNCIONARIO_FATURADO | integer(4) |  |  | Numero de empregados faturados |
| FATURAMENTO_LIMITE | numeric(13) |  |  | Limite do valor do faturamento |
| FATURAMENTO_FATURADO | numeric(13) |  |  | Valor do faturamento fatudado |
