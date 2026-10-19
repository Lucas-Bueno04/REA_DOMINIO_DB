# FOFERIAS_GOZO_TIPO_SIMULACAO — Simulação do tipo de gozo de férias
12.062 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | CODIGO EMPRESA |
| I_EMPREGADOS | integer(4) | PK |  | CODIGO |
| I_FERIAS_GOZO | integer(4) | PK |  | SEQUENCIAL DE PERIODOS DE GOZO |
| I_FERIAS_GOZO_TIPO | integer(4) | PK |  | TIPO DE GOZO (GOZO,ABONO,LIC.REMUM) |
| COMPETENCIA | date(4) | PK |  | COMPETENCIA |
| INICIO | numeric(10) | PK |  | Data numérica inicial |
| FIM | numeric(10) |  |  | Data numérica final |
| NUMERO_DIAS | numeric(10) |  |  | NUMERO DE DIAS |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
