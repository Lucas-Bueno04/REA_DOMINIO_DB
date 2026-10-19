# FOSIMULACAO_RESCISAO_EMPREGADOS — Simulação de rescisão - Empregados
1.889 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_SIMULACAO_RESCISAO | integer(4) | PK |  | Sequencial de simulação da rescisão. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo de rescisão vinculado à simulação - Renomeado |
| MEDIA_MANUAL | smallint(2) |  |  | Usa média manual. (0=Não/1=Sim) |
| VALOR_MANUAL_MEDIA_VALOR_FERIAS | numeric(13) |  | S | Média valor de férias |
| VALOR_MANUAL_MEDIA_HORA_FERIAS | numeric(13) |  | S | Média hora de férias |
| VALOR_MANUAL_MEDIA_HORA_AULA_FERIAS | numeric(13) |  | S | Média hora aula de férias |
| VALOR_MANUAL_VANTAGEM_FERIAS | numeric(13) |  | S | Vantagem de férias |
| VALOR_MANUAL_MEDIA_VALOR_13 | numeric(13) |  | S | Média valor de 13º |
| VALOR_MANUAL_MEDIA_HORA_13 | numeric(13) |  | S | Média hora de 13º |
| VALOR_MANUAL_MEDIA_HORA_AULA_13 | numeric(13) |  | S | Média hora aula de 13º |
| VALOR_MANUAL_VANTAGEM_13 | numeric(13) |  | S | Vantagem de 13º |
| I_CALCULOS | uniqueidentifier(16) |  |  | Código do cálculo de rescisão vinculado à simulação. |
