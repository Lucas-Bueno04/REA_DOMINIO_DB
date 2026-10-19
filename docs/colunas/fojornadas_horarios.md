# FOJORNADAS_HORARIOS — Horários da jornada.
11.086 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_JORNADA | integer(4) | PK |  | Código do jornada. |
| SEQUENCIAL | integer(4) | PK |  | Sequencial. |
| DIA_SEMANA | smallint(2) |  |  | Dia da semana. (1=Segunda a sexta/2=Segunda/3=Terça/4=Quarta/5=Quinta/6=Sexta/7=Sábado/8=Domingo/9=1º dia/10=2º dia/11=3º dia/12=Escala) |
| I_HORARIO | integer(4) |  |  | Código do horário. |
| ORIGEM_REG | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| SEQUENCIAL_DIA_SEMANA | smallint(2) |  | S | Sequencial do dia da semana para jornadas do tipo escala. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
