# FOBASESSERV_CALCULOS_RATEIO_SERVICO — Relacionamento entre o cálculo principal e os cálculos de rateio por serviço.
628.958 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa do cálculo integral. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado do cálculo integral. |
| COMPETENCIA | date(4) | PK |  | Competência do cálculo integral. |
| TIPO_PROCESS | integer(4) | PK |  | Tipo de processo do cálculo integral. |
| I_SERVICOS | integer(4) | PK |  | Código do serviço do cálculo integral. |
| RATEIO | integer(4) | PK |  | Rateio do cálculo integral. |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo do cálculo integral - Renomeado |
| I_CALCULOS_COMPLEMENTOS_OLD | integer(4) |  | S | Código do complemento de cálculo do cálculo integral - Renomeado |
| CODI_EMP_RELACIONADO | integer(4) | PK |  | Código da empresa do cálculo relacionado. |
| I_EMPREGADOS_RELACIONADO | integer(4) | PK |  | Código do empregado do cálculo relacionado. |
| COMPETENCIA_RELACIONADO | date(4) | PK |  | Competência do cálculo relacionado. |
| TIPO_PROCESS_RELACIONADO | integer(4) | PK |  | Tipo de processo do cálculo relacionado. |
| I_SERVICOS_RELACIONADO | integer(4) | PK |  | Código do serviço do cálculo relacionado. |
| RATEIO_RELACIONADO | integer(4) | PK |  | Rateio do cálculo relacionado. |
| I_CALCULOS_RELACIONADO_OLD | integer(4) |  | S | Código do cálculo do cálculo relacionado - Renomeado |
| I_CALCULOS_COMPLEMENTOS_RELACIONADO_OLD | integer(4) |  | S | Código do complemento de cálculo do cálculo relacionado - Renomeado |
| EXISTE_CALCULO_RATEIO | smallint(2) |  |  | Existe registro de rateio para o cálculo principal.(0=Não/1=Sim) |
| SITUACAO_MES | integer(4) |  |  | Situação mês do cálculo. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo do cálculo integral. |
| I_CALCULOS_RELACIONADO | uniqueidentifier(16) | PK |  | Código do cálculo do cálculo relacionado. |
| I_CALCULOS_COMPLEMENTOS | uniqueidentifier(16) |  | S | Código do complemento de cálculo do cálculo integral. |
| I_CALCULOS_COMPLEMENTOS_RELACIONADO | uniqueidentifier(16) |  | S | Código do complemento de cálculo do cálculo relacionado. |
