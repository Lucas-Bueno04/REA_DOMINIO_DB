# FOVALE_ALIMENTACAO_VIGENCIAS — Vale alimentação - Vigências
13 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_VALE_ALIMENTACAO | integer(4) | PK |  | Código do vale alimentação. |
| COMPETENCIA | date(4) | PK |  | Competência. |
| VALOR_DIARIO | numeric(13) |  |  | Valor diário. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout) |
