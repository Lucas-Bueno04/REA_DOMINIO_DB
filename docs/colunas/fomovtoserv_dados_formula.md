# FOMOVTOSERV_DADOS_FORMULA — Informações do cálculo da fórmula.
725 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| COMPETENCIA | date(4) | PK |  | Competência do cálculo. |
| TIPO_PROCESSO | integer(4) | PK |  | Tipo de cálculo. |
| I_EVENTOS | integer(4) | PK |  | Código do evento. |
| RATEIO | integer(4) | PK |  | Rateio. |
| I_SERVICOS | integer(4) | PK |  | Código do serviço. |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo - Renomeado |
| BASE_CALCULO | numeric(13) |  | S | Base de cálculo utilizada. |
| PERCENTUAL | numeric(13) |  | S | Percentual utilizado para o cálculo. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout) |
| DIAS_DSR | smallint(2) |  | S | Dias DSR utilizados no cálculo da fórmula do evento. |
| DIAS_TRABALHADOS | smallint(2) |  | S | Dias trabalhados utilizados no cálculo da fórmula do evento. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo |
