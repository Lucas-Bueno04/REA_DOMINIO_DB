# FOLANCAMENTOS_EVENTOS_SERVICOS — Lançamento de evento por serviço.
642 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| I_EVENTOS | integer(4) | PK |  | Código do evento |
| TIPO_PROCESSO | smallint(2) | PK |  | Tipo do processo. (11=Mensal/31=1ª semana/32=2ª semana/33=3ª semana/34=4ª semana/35=Última semana/36=Todas as semanas/41=Adiantamento/42=Complementar/51=Adiantamento de 13º salário/52=13º salário integral) |
| TIPO_LANCAMENTO | smallint(2) | PK |  | Tipo de lançamento. (1=Mensal/2=Fixo) |
| COMPETENCIA_INICIAL | date(4) | PK |  | Competência inicial. |
| SEQUENCIAL | integer(4) | PK |  | Sequencial. |
| I_SERVICOS | integer(4) | PK |  | Código do serviço. |
| VALOR_INFORMADO | numeric(30) |  |  | Valor informado. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=importação de tabelas/2=importação de leiaute/3=conversão) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
