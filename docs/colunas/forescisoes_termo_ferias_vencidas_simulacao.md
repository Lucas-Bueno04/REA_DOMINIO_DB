# FORESCISOES_TERMO_FERIAS_VENCIDAS_SIMULACAO — Simulação do termo de férias vencidas da rescisão
1.020 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| TIPO | integer(4) | PK |  | Tipo da rescisão |
| I_FERIAS_AQUISITIVOS | integer(4) | PK |  | Código do período aquisitivo |
| VALOR | numeric(13) |  |  | Valor |
| VALOR_DOBRO | numeric(13) |  | S | Valor em dobro |
| ORIGEM_REG | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| VALOR_FERIAS | decimal(13) |  |  | Valor das férias. |
| VALOR_ADICIONAL | decimal(13) |  |  | Valor do 1/3 de férias. |
| VALOR_MEDIAS_VANTAGENS | decimal(13) |  |  | Valor de médias e vantagens. |
| VALOR_PIS | decimal(13) |  |  | Valor do Pis. |
| VALOR_ADICIONAL_DOBRO | numeric(13) |  | S | Valor do 1/3 de férias em dobro |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo - Renomeado |
| VALOR_ADICIONAL_SEM_MEDIAS_VANTAGENS | numeric(13) |  | S | Valor adicional sem médias/vantagens |
| VALOR_ADICIONAL_MEDIAS_VANTAGENS | numeric(13) |  | S | Valor adicional de médias/vantagens |
| VALOR_DIRIGENTE_SINDICAL | numeric(13) |  |  | Valor de férias vencidas do dirigente sindical. |
| BASE_DIRIGENTE_SINDICAL | numeric(13) |  |  | Base de férias vencidas do dirigente sindical. |
| BASE_FERIAS | numeric(13) |  |  | Base de férias vencidas. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo |
