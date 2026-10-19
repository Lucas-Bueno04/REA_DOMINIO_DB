# FOAFASTAMENTOS_PERIODO_AQUISITIVO — AFASTAMENTOS SEPARADOS POR PERIODO AQUISITIVO
480 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | CODIGO EMPRESA |
| I_EMPREGADOS | integer(4) | PK |  | CODIGO |
| I_FERIAS_AQUISITIVOS | integer(4) | PK |  | SEQUENCIA DE PERIODOS AQUISITIVOS |
| DATA_INICIO | date(4) | PK |  | Data de início do afastamento |
| DATA_FIM | date(4) |  |  | Data final do afastamento |
| DATA_REAL | date(4) |  |  | Data real do afastamento |
| I_AFASTAMENTOS | integer(4) |  |  | Código do afastamento |
| NUMERO_DIAS | numeric(10) |  |  | Número de dias |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| DATA_REAL_DN | numeric(10) |  |  | Data numérica do afastamento |
| ONUS_REMUNERACAO_MANDATO_SINDICAL | smallint(2) |  | S | Ônus da remuneração do exercício do mandato sindical. (1=Empregador/2=Sindicato/3=Diferença salarial paga pelo sindicato/null=Sem dados informado, conversao) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| DILATAR_PERIODO_AQUISITIVO | smallint(2) |  |  | Dilatar período aquisitivo. 0=Não/1=Sim |
