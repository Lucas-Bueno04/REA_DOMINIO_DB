# FOMEMORIA_CALCULO_SALARIO_PROPORCIONAL — Memória de cálculo do salário proporcional.
129.546 linhas

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
| PERIODO_INICIO | date(4) |  |  | Data de início do período |
| PERIODO_FIM | date(4) |  |  | Data de fim do período |
| DIAS_MES | integer(4) |  |  | Quantidade de dias no mês |
| DIAS_PROPORCIONAL | integer(4) |  |  | Quantidade de dias proporcionais |
| SALARIO_BASE_CALCULO | numeric(15) |  | S | Valor do salário base para cálculo |
| VALOR_PROPORCIONAL | numeric(15) |  | S | Valor proporcional |
| REDUCAO | numeric(5) |  | S | Valor do percentual de redução |
| DATA_INICIO_REDUCAO | date(4) |  | S | Data de início da redução |
| DATA_FIM_REDUCAO | date(4) |  | S | Data final da redução |
| TIPO_CALCULO | integer(4) |  | S | Tipo de cálculo 1=Integral/2=Com redução. |
| TIPO_SALARIO | integer(4) |  | S | Tipo de memória de cálculo 1=Salário/2=Sindicato. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo. |
