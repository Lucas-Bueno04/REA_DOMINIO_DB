# FORESCISOES_TERMO — Discriminação das verbas rescisórias do TRCT - (13º salário e férias)
5.750 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| TIPO | integer(4) | PK |  | Tipo de cálculo de rescisão. (1=Normal/2=Complementar/3=Parcial/4=Simulação) |
| AVOS_13 | smallint(2) |  | S | Quantidade de avos de 13º salário pagos |
| AVOS_FERIAS | smallint(2) |  | S | Quantidade de avos de férias pagos |
| ORIGEM_REG | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| VALOR_FERIAS_VENCIDAS | numeric(13) |  | S | Valor das férias vencidas (Valor lançado/alterado) |
| VALOR_FERIAS_DOBRO | numeric(13) |  | S | Valor das férias em dobro (Valor lançado/alterado) |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo - Renomeado |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo |
