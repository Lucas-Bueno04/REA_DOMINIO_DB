# FOEMPREGADOS_VALE_ALIMENTACAO_DESCONTO — Vale alimentação - Desconto
89 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| COMPETENCIA | date(4) | PK |  | Competência. |
| TIPO_PROCESSO | smallint(2) | PK |  | Tipo de processo. |
| TIPO_LANCAMENTO | smallint(2) | PK |  | Tipo de lançamento. |
| I_EVENTOS | integer(4) | PK |  | Código da rubrica de desconto. |
| SEQUENCIAL | integer(4) | PK |  | Sequencial. |
| FORMA_DESCONTO | smallint(2) |  |  | Forma de desconto. (1=Percentual/2=Valor) |
| VALOR | numeric(13) |  |  | Valor para desconto. |
| BASE_CALCULO | smallint(2) |  |  | Base de cálculo para o desconto. (1=Salário base/2=Salário mínimo/3=Piso salarial/4=20% do valor de vale alimentação fornecido/5=% do valor de Vale Alimentação fornecido) |
| VALOR_DESCONTAR | numeric(13) |  |  | Valor do desconto. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout) |
