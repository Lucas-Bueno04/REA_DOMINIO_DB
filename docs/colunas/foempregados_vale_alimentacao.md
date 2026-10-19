# FOEMPREGADOS_VALE_ALIMENTACAO — Vale alimentação - Empregados
88 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| I_VALE_ALIMENTACAO | integer(4) | PK |  | Código do vale alimentação. |
| TIPO_LANCAMENTO | smallint(2) |  |  | Tipo de lançamento. (1=Diário/2=Semanal/3=Mensal) |
| QUANTIDADE | integer(4) |  |  | Quantidade de vales. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout) |
