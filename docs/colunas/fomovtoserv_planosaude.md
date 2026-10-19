# FOMOVTOSERV_PLANOSAUDE — Movimentação - Cálculo - Plano de saúde
115.080 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| DATA | date(4) | PK |  | Competência |
| TIPO_PROCES | integer(4) | PK |  | Tipo de cálculo |
| I_EVENTOS | integer(4) | PK |  | Código do evento |
| RATEIO | integer(4) | PK |  | Rateio |
| I_SERVICOS | integer(4) | PK |  | Código do serviço |
| I_BENEFICIARIO | integer(4) | PK |  | Sequencial de beneficiário |
| I_FILHOS | integer(4) |  | S | Código do dependente |
| VALOR | numeric(13) |  |  | Valor |
| ORIGEM_REG | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| I_OPERADORAPLANOSAUDE | integer(4) |  |  | Código da operadora de plano de saúde |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo - Renomeado |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo |
