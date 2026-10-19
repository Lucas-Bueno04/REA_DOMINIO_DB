# pohorarios — Cadastro de horarios do ponto
3 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  |  |
| i_horarios | integer(4) | PK |  |  |
| nome | char(40) |  |  |  |
| trab | char(1) |  |  |  |
| tipo | char(1) |  |  |  |
| hada | integer(4) |  | S |  |
| nbat | smallint(2) |  |  |  |
| chdia | integer(4) |  | S |  |
| tofa | integer(4) |  | S |  |
| toex | integer(4) |  | S |  |
| por_sem | char(1) |  | S |  |
| msg_cartao | char(20) |  | S |  |
| ENTRADA_1_HORARIO_LIVRE | time(8) |  | S | Horário de início do trabalho que será demonstrado no cartão ponto para o horário livre. |
| SAIDA_1_HORARIO_LIVRE | time(8) |  | S | Horário de saída para o intervalo que será demonstrado no cartão ponto para o horário livre. |
| ENTRADA_2_HORARIO_LIVRE | time(8) |  | S | Horário de volta do intervalo que será demonstrado no cartão ponto para o horário livre. |
| SAIDA_2_HORARIO_LIVRE | time(8) |  | S | Horário de fim do trabalho que será demonstrado no cartão ponto para o horário livre. |
