# FOJORNADAS_ALTERACAO — Tabela de alteração das jornadas
3 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_JORNADA | integer(4) | PK |  | Código da jornada. |
| CAMPO | smallint(2) | PK |  | Campo alterado. (1=Tipo de jornada/2=Tipo de escala/3=Horários) |
| DATA_ALTERACAO | date(4) | PK |  | Data da alteração. |
| DE | varchar(150) |  |  | Valor anterior a alteração. |
| PARA | varchar(150) |  |  | Valor posterior a alteração. |
| DATA_GRAVACAO | date(4) |  |  | Data de gravação da alteração. |
| HORARIO_GRAVACAO | time(8) |  |  | Horário de gravação da alteração. |
| ORIGEM_REG | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
