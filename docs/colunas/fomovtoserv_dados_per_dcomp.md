# FOMOVTOSERV_DADOS_PER_DCOMP — Informações do cálculo da fórmula.
9 linhas

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
| SEQUENCIAL | integer(4) | PK |  | Sequencial. |
| I_FILHOS | integer(4) |  | S | Código do filho. |
| VALOR_CALCULADO | numeric(13) |  |  | Valor calculado. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout) |
| TIPO | smallint(2) |  |  | Tipo do calculo que a rubrica pertence (1=Salário Familia/2=Maternidade/3=Maternidade 13o) |
| PROV_DESC | varchar(2) |  |  | Provento/Desconto |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo |
