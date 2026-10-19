# FODEPTO_ALTERACAO — Alterações da tabela do departamento.
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_DEPTO | integer(4) | PK |  | Código do departamento. |
| CAMPO | smallint(2) | PK |  | Campo alterado. (1=Nome |
| DATA_ALTERACAO | date(4) | PK |  | Data da alteração. |
| DE | varchar(40) |  |  | Valor anterior a alteração. |
| PARA | varchar(40) |  |  | Valor posterior a alteração. |
| DATA_GRAVACAO | date(4) |  |  | Data de gravação da alteração. |
| HORARIO_GRAVACAO | time(8) |  |  | Horário de gravação da alteração. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro (0=Sistema/ 1=Imp Tabelas/ 2=Imp Layout) |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
