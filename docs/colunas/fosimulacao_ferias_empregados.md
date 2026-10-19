# FOSIMULACAO_FERIAS_EMPREGADOS — Simulação de férias - Empregados
551 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_SIMULACAO_FERIAS | integer(4) | PK |  | Sequencial de simulação de férias. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| I_FERIAS_AQUISITIVOS | integer(4) |  |  | Sequencial do período aquisitivo. |
| I_FERIAS_GOZO | integer(4) |  |  | Sequencial do período de gozo. |
| GOZO_INICIO | date(4) |  |  | Data de início do período de gozo. |
| GOZO_FIM | date(4) |  |  | Data do fim do período de gozo. |
| PAGA_ABONO | smallint(2) |  |  | Pagar abono pecuniário. (0=Não/1=Sim) |
| ABONO_INICIO | date(4) |  |  | Data de início do período de abono. |
| ABONO_FIM | date(4) |  |  | Data do fim do período de abono. |
| DIAS_DIREITO | numeric(10) |  |  | Dias de direito do período aquisitivo com as configurações da simulação. |
| GOZO_INICIO_DN | numeric(13) |  |  | Início do período de gozo numérico. |
| GOZO_FIM_DN | numeric(13) |  |  | Fim do período de gozo numérico. |
| ABONO_INICIO_DN | numeric(13) |  |  | Início do período de abono numérico. |
| ABONO_FIM_DN | numeric(13) |  |  | Fim do período de abono numérico. |
| MEDIA_MANUAL | smallint(2) |  |  | Usa média manual. (0=Não/1=Sim) |
| VALOR_MANUAL_MEDIA_VALOR_FERIAS | numeric(13) |  | S | Média valor de férias |
| VALOR_MANUAL_MEDIA_HORA_FERIAS | numeric(13) |  | S | Média hora de férias |
| VALOR_MANUAL_MEDIA_HORA_AULA_FERIAS | numeric(13) |  | S | Média hora aula de férias |
| VALOR_MANUAL_VANTAGEM_FERIAS | numeric(13) |  | S | Vantagem de férias |
| VALOR_MANUAL_MEDIA_VALOR_13 | numeric(13) |  | S | Média valor de 13º |
| VALOR_MANUAL_MEDIA_HORA_13 | numeric(13) |  | S | Média hora de 13º |
| VALOR_MANUAL_MEDIA_HORA_AULA_13 | numeric(13) |  | S | Média hora aula de 13º |
| VALOR_MANUAL_VANTAGEM_13 | numeric(13) |  | S | Vantagem de 13º |
