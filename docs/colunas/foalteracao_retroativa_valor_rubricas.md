# FOALTERACAO_RETROATIVA_VALOR_RUBRICAS — Alteração retroativa de valor das rubricas.
376 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| I_EVENTOS | integer(4) | PK |  | Código do evento. |
| COMPETENCIA_ALTERACAO | date(4) | PK |  | Competência da alteração. |
| COMPETENCIA_RETROATIVA | date(4) |  |  | Competência retroativa. |
| FORMA_AJUSTE | smallint(2) |  |  | Forma de ajuste. (1=Complementar mês a mês/2=Folha mensal do mês do aumento/3=Folha complementar do mês do aumento/4=1ª semana/5=2ª semana/6=3ª semana/7=4ª semana/8=Última semana) |
| VALOR | numeric(13) |  |  | Valor ajustado. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
