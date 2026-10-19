# FOMOVTOSERV_PENSAO_ALIMENTICIA — Valores de pensão alimentícia nas férias por dependente.
2.205 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| DATA | date(4) | PK |  | Competência. |
| TIPO_PROCESSO | integer(4) | PK |  | Tipo de processo. |
| I_EVENTOS | integer(4) | PK |  | Código do evento. |
| RATEIO | integer(4) | PK |  | Rateio. |
| I_SERVICOS | integer(4) | PK |  | Código do serviço. |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo - Renomeado |
| I_FILHOS | integer(4) | PK |  | Código do dependente. |
| VALOR | numeric(13) |  |  | Valor. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/ 1=Imp Tabelas/ 2=Imp Layout) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo |
| I_CONVOCACAO | numeric(10) |  | S | Código da Convocacao Intermitente Relacionada |
| NUMERO | numeric(10) |  | S | Número do RPA |
