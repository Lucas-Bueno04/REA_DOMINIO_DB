# FOMEDIASCALC_SIMULACAO — Médias da simulação da rescisão
7.204 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Codigo empresa |
| I_EMPREGADOS | integer(4) | PK |  | Empregado |
| TIPO_INF | tinyint(1) | PK |  | Tipo informado |
| TIPO_CALCULO | tinyint(1) | PK |  | Tipo Calculo |
| VALOR | numeric(13) |  |  | Valor |
| TIPO | integer(4) | PK |  | Tipo |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo - Renomeado |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo |
