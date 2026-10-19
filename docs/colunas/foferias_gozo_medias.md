# FOFERIAS_GOZO_MEDIAS — MEDIAS DE FERIAS CALCULADAS NO GOZO
8.578 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | CODIGO EMPRESA |
| I_EMPREGADOS | integer(4) | PK |  | CODIGO |
| I_FERIAS_GOZO | integer(4) | PK |  | SEQUENCIAL DE PERIODOS DE GOZO |
| TIPO_INF | smallint(2) | PK |  | HORAS, VALOR, VANTAGEM OU HORA-AULA |
| TIPO_CALCULO | smallint(2) | PK |  | FERIAS VENCIDAS OU 13O. SALARIO |
| VALOR | decimal(17) |  |  | VALOR DA MEDIA |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
