# FOMEMORIA_CALCULO_INSS — Memória de cálculo do INSS
1.167.319 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| COMPETENCIA | date(4) | PK |  | Competência |
| TIPO_PROCESSO | integer(4) | PK |  | Tipo de processo. |
| I_EVENTOS | integer(4) | PK |  | Código da rubrica. |
| RATEIO | integer(4) | PK |  | Rateio. |
| I_SERVICOS | integer(4) | PK |  | Código do serviço. |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo - Renomeado |
| SEQUENCIAL | integer(4) | PK |  | Sequencial. |
| TIPO | integer(4) |  |  | Tipo de descrição/valor. |
| DESCRICAO | varchar(255) |  | S | Descrição. |
| VALOR | numeric(15) |  | S | Valor. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo |
