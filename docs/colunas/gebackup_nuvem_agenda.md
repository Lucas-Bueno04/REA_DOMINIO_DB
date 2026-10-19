# GEBACKUP_NUVEM_AGENDA — Tabela de configurações do agendamento dos backups do Backup na Nuvem.
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Chave primária para linha única. |
| COMPLETO_DIA_SEMANA | integer(4) |  |  | Dia da semana em que o backup completo é realizado: 0 - Domingo, 1 - Segunda, 2 - Terça, 3 - Quarta, 4 - Quinta, 5 - Sexta, 6 - Sábado |
| COMPLETO_HORA | time(8) |  |  | Hora em que o backup completo é realizado. |
| MODIFICACOES_HORA_INICIO | time(8) |  |  | Horário inicial dos backups de modificações. |
| MODIFICACOES_HORA_FIM | time(8) |  |  | Horário final dos backups de modificações. |
| MODIFICACOES_INTERVALO | integer(4) |  |  | Intervalo entre a realização dos backups de modificações em horas. |
| MODIFICACOES_DOMINGO | integer(4) |  |  | Faz backup de modificações no Domingo. |
| MODIFICACOES_SEGUNDA | integer(4) |  |  | Faz backup de modificações na Segunda. |
| MODIFICACOES_TERCA | integer(4) |  |  | Faz backup de modificações na Terça. |
| MODIFICACOES_QUARTA | integer(4) |  |  | Faz backup de modificações na Quarta. |
| MODIFICACOES_QUINTA | integer(4) |  |  | Faz backup de modificações na Quinta. |
| MODIFICACOES_SEXTA | integer(4) |  |  | Faz backup de modificações na Sexta. |
| MODIFICACOES_SABADO | integer(4) |  |  | Faz backup de modificações no Sábado. |
