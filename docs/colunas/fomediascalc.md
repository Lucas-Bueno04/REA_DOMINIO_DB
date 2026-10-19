# fomediascalc — Medias da rescisao
13.362 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_empregados | integer(4) | PK |  | Empregado |
| tipo_inf | tinyint(1) | PK |  | Tipo informado |
| tipo_calculo | tinyint(1) | PK |  | Tipo Calculo |
| valor | numeric(13) |  |  | Valor |
| tipo | integer(4) | PK |  | Tipo de cálculo de rescisão. (1=Normal/2=Complementar/3=Parcial/4=Simulação) |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo - Renomeado |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo |
