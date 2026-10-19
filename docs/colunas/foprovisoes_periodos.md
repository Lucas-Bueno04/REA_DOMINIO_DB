# FOPROVISOES_PERIODOS — PROVISOES CALCULADAS - PERIODOS DE FERIAS
115.036 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | CODIGO DA EMPRESA |
| I_EMPREGADOS | integer(4) | PK |  | CÓDIGO DO EMPREGADO |
| COMPETENCIA | date(4) | PK |  | COMPETÊNCIA |
| TIPO | tinyint(1) | PK |  | TIPO DA PROVISAO |
| I_FERIAS_AQUISITIVOS | integer(4) | PK |  | SEQUENCIA DE PERIODOS AQUISITIVOS |
| QTDE_DIAS | numeric(13) |  |  | NUMERO DE DIAS DE DIREITO NO PERIODO |
| NO_AVOS | integer(4) |  |  | NUMERO DE AVOS ADQUIRIDOS |
| MES_FERIAS | numeric(13) |  | S | ** SEM USO ** VALOR DE FERIAS DO MES |
| MES_ADICIONAL | numeric(13) |  | S | ** SEM USO ** VALOR DO ADICIONAL NO MES |
| MES_MEDIAS | numeric(13) |  | S | ** SEM USO ** VALOR DE MEDIAS NO MES |
| MES_INSS | numeric(13) |  | S | ** SEM USO ** VALOR DE INSS NO MES |
| MES_FGTS | numeric(13) |  | S | ** SEM USO ** VALOR DE FGTS NO MES |
| MES_PIS | numeric(13) |  | S | ** SEM USO ** VALOR DE PIS NO MES |
| DIF_FERIAS | numeric(13) |  | S | ** SEM USO ** DIFERENCA DE FERIAS NO MES |
| DIF_ADICIONAL | numeric(13) |  | S | ** SEM USO ** DIFERENCA DE ADICIONAL NO MES |
| DIF_MEDIAS | numeric(13) |  | S | ** SEM USO ** DIFERENCA DE MEDIAS |
| DIF_INSS | numeric(13) |  | S | ** SEM USO ** DIFERENCA DE INSS NO MES |
| DIF_FGTS | numeric(13) |  | S | ** SEM USO ** DIFERENCA DE FGTS NO MES |
| DIF_PIS | numeric(13) |  | S | ** SEM USO ** DIFERENCA DE PIS |
| TOTAL_FERIAS | numeric(13) |  | S | ** SEM USO ** TOTAL DE FERIAS |
| TOTAL_ADICIONAL | numeric(13) |  | S | ** SEM USO ** TOTAL DE ADICIONAL |
| TOTAL_MEDIAS | numeric(13) |  | S | ** SEM USO ** TOTAL DE MEDIAS |
| TOTAL_INSS | numeric(13) |  | S | ** SEM USO ** TOTAL DE INSS |
| TOTAL_FGTS | numeric(13) |  | S | ** SEM USO ** TOTAL DE FGTS |
| TOTAL_PIS | numeric(13) |  | S | ** SEM USO ** TOTAL DE PIS |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| CONSIDERAR_PROVISAO_MES | smallint(2) |  |  | Considerar na provisão do mês: (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
