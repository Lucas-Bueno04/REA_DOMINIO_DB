# FOMOVTOSERV_SALARIO_FAMILIA — Dependentes que foram considerados para o cálculo do salário família na rubrica.
1.689 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| DATA | date(4) | PK |  | Competência |
| TIPO_PROCES | integer(4) | PK |  | Tipo de folha. |
| I_EVENTOS | integer(4) | PK |  | Código do evento. |
| RATEIO | integer(4) | PK |  | Rateio. |
| I_SERVICOS | integer(4) | PK |  | Código do serviço |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo - Renomeado |
| I_FILHOS | integer(4) | PK |  | Código do dependente. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo |
