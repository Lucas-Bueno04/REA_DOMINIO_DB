# FOMEMORIA_CALCULO_SALARIO_INDENIZACAO_MP_936 — Memória de cálculo da indenização MP 936.
7 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| COMPETENCIA | date(4) | PK |  | Competência |
| TIPO_PROCESSO | integer(4) | PK |  | Tipo da folha |
| I_SERVICOS | integer(4) | PK |  | Código do serviço |
| RATEIO | integer(4) | PK |  | Rateio do serviço |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo - Renomeado |
| SEQUENCIAL | integer(4) | PK |  | Código sequencial |
| PERIODO_INICIO_ESTABILIDADE | date(4) |  |  | Data de início do período de estabilidade |
| PERIODO_FIM_ESTABILIDADE | date(4) |  |  | Data de fim do período de estabilidade |
| DIAS_ESTABILIDADE | integer(4) |  |  | Dias de estabilidade |
| TIPO_MEDIDA | integer(4) |  |  | Tipo de medida |
| DIAS_MES | integer(4) |  |  | Quantidade de dias no mês |
| PERCENTUAL_REDUCAO | numeric(5) |  | S | Valor do percentual de redução |
| PERCENTUAL_INDENIZACAO | numeric(5) |  | S | Valor do percentual de indenização |
| SALARIO_BASE_CALCULO | numeric(13) |  | S | Valor do salário base para cálculo |
| VALOR_INDENIZACAO | numeric(13) |  | S | Valor da indenização |
| DATA_INICIO_REDUCAO | date(4) |  | S | Data de início da redução |
| DATA_FIM_REDUCAO | date(4) |  | S | Data final da redução |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo. |
