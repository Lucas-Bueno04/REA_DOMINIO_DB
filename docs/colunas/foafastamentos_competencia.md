# FOAFASTAMENTOS_COMPETENCIA — AFASTAMENTOS SEPARADOS POR COMPETENCIA
429.060 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | CODIGO EMPRESA |
| I_EMPREGADOS | integer(4) | PK |  | CODIGO |
| DATA_REAL | date(4) |  |  | Data real |
| COMPETENCIA | date(4) | PK |  | Competência |
| DATA_INICIO | date(4) |  |  | Data de início |
| I_AFASTAMENTOS | integer(4) |  |  | Código do afastamento referente ao tipo de afastamento da FOAFASTAMENTOS_TIPO |
| DATA_FIM | date(4) |  |  | Data fim |
| NUMERO_DIAS | numeric(10) |  |  | Número de dias |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| DATA_REAL_DN | numeric(10) | PK |  | Data numérica do afastamento |
| DATA_INICIO_DN | numeric(10) | PK |  | Data de inicio numérica |
| DATA_FIM_DN | numeric(10) |  |  | Data fim numérica |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
