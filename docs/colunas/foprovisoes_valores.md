# FOPROVISOES_VALORES — Valores da provisão.
782.189 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| COMPETENCIA | date(4) | PK |  | Competência |
| TIPO | tinyint(1) | PK |  | Tipo de provisão |
| TIPO_VALOR | smallint(2) | PK |  | Tipo de valor |
| VALOR | numeric(13) |  |  | Valor |
| VALOR_ADICIONAL_FERIAS | numeric(13) |  |  | Valor do 1/3 de férias |
| VALOR_MEDIAS_VANTAGENS | numeric(13) |  |  | Valor de médias e vantagens |
| VALOR_INSS_EMPRESA | numeric(13) |  |  | Valor do INSS Empresa |
| VALOR_INSS_RAT | numeric(13) |  |  | Valor do INSS RAT |
| VALOR_INSS_TERCEIROS | numeric(13) |  |  | Valor do INSS Terceiros |
| VALOR_FGTS | numeric(13) |  |  | Valor do FGTS |
| VALOR_PIS | numeric(13) |  |  | Valor do PIS |
| ORIGEM_REG | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| VALOR_ADICIONAL_FERIAS_SEM_MEDIAS_VANTAGENS | numeric(13) |  | S | Valor do adicional de férias sem considerar as médias/vantagens. |
| VALOR_ADICIONAL_FERIAS_MEDIAS_VANTAGENS | numeric(13) |  | S | Valor do adicional de férias das médias/vantagens. |
| VALOR_ADICIONAL_FERIAS_MP_927 | numeric(13) |  | S | Valor do 1/3 de férias MP 927 |
| VALOR_ADICIONAL_FERIAS_SEM_MEDIAS_VANTAGENS_MP_927 | numeric(13) |  | S | Valor do adicional de férias sem considerar as médias/vantagens  MP 927. |
| VALOR_ADICIONAL_FERIAS_MEDIAS_VANTAGENS_MP_927 | numeric(13) |  | S | Valor do adicional de férias das médias/vantagens  MP 927. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
