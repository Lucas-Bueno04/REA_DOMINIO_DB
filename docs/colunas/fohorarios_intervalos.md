# FOHORARIOS_INTERVALOS — Cadastro de intervalo dos horários
2.494 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_HORARIO | integer(4) | PK |  | Código do horário. |
| I_INTERVALO | integer(4) | PK |  | Código do intervalo |
| HORA_INICIO | time(8) |  | S | Hora de início do intervalo. |
| HORA_FIM | time(8) |  | S | Hora do fim do intervalo. |
| INTERVALO_PRINCIPAL | smallint(2) |  | S | Tipo de intervalo. (0=Não/1=Sim) |
| ORIGEM_REG | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
