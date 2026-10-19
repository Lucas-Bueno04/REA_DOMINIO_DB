# GERAEXECUTAR_SEMANAS — Configuração de agendamento semanal das rotinas automáticas (SAI 101818)
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_EXECUTARRA | integer(4) | PK |  | Código da rotina automática (FK GERAEXECUTAR) |
| I_SISTEMA | smallint(2) | PK |  | Código do sistema (FK GERAEXECUTAR) |
| DIA_SEMANA | smallint(2) |  |  | Dia da semana (1=Segunda..7=Domingo) |
| SEMANA_1 | smallint(2) |  |  | 1ª semana do mês (0=Não, 1=Sim) |
| SEMANA_2 | smallint(2) |  |  | 2ª semana do mês (0=Não, 1=Sim) |
| SEMANA_3 | smallint(2) |  |  | 3ª semana do mês (0=Não, 1=Sim) |
| SEMANA_4 | smallint(2) |  |  | 4ª semana do mês (0=Não, 1=Sim) |
| SEMANA_ULTIMA | smallint(2) |  |  | Última semana do mês (0=Não, 1=Sim) |
| DATA_ULTIMA_NOTIFICACAO_SEMANAL | date(4) |  | S | Data da última ocorrência semanal notificada ao usuário (SAI 101818) |
