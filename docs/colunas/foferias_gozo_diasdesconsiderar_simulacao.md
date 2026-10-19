# FOFERIAS_GOZO_DIASDESCONSIDERAR_SIMULACAO — Simulação dos dias a desconsiderar no gozo de férias
36 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | CODIGO EMPRESA |
| I_EMPREGADOS | integer(4) | PK |  | CODIGO |
| I_FERIAS_GOZO | integer(4) | PK |  | SEQUENCIAL DE PERIODOS DE GOZO |
| DIA | date(4) | PK |  | DIA A SER DESCONSIDERADO |
| ORIGEM | tinyint(1) |  |  | ORIGEM DO DIA (1=SINDICATO, 2=DOMINGO/FERIADO) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
