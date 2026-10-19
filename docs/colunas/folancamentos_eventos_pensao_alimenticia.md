# FOLANCAMENTOS_EVENTOS_PENSAO_ALIMENTICIA — Valores de pensão alimentícia por dependente.
270 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| I_EVENTOS | integer(4) | PK |  | Código do evento. |
| TIPO_PROCESSO | smallint(2) | PK |  | Tipo de processo. |
| TIPO_LANCAMENTO | smallint(2) | PK |  | Tipo de lançamento. (1=Mensal/2=Fixo) |
| COMPETENCIA_INICIAL | date(4) | PK |  | Competência do lançamento. |
| SEQUENCIAL | integer(4) | PK |  | Sequencial. |
| I_FILHOS | integer(4) | PK |  | Código do dependente. |
| VALOR | numeric(13) |  |  | Valor. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/ 1=Imp Tabelas/ 2=Imp Layout) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
