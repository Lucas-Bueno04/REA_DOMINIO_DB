# FOLANCAMENTOS_EVENTOS_COMPLEMENTOS — Lançamentos de eventos para complementos de cálculos
446 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| I_EVENTOS | integer(4) | PK |  | Código do evento |
| TIPO_PROCESSO | smallint(2) | PK |  | Tipo do processo: (42=Complementar) |
| TIPO_LANCAMENTO | smallint(2) | PK |  | Tipo do lançamento: (1=Mensal, 2=Fixo) |
| COMPETENCIA_INICIAL | date(4) | PK |  | Competência inicial do lançamento |
| SEQUENCIAL | integer(4) | PK |  | Sequencial do lançamento |
| I_CALCULOS_COMPLEMENTOS_OLD | integer(4) |  | S | Código do complemento de cálculo - Renomeado |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro: (0=Sistema, 1=Importação de tabelas, 2=Importação de leiaute, 3=Conversão) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS_COMPLEMENTOS | uniqueidentifier(16) | PK |  | Código do complemento de cálculo |
