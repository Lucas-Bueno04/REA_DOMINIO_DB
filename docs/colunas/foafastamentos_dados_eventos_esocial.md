# FOAFASTAMENTOS_DADOS_EVENTOS_ESOCIAL — Dados de envio do afastamento para o eSocial.
42 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| DATA_REAL_DN | numeric(10) | PK |  | Data do afastamento. |
| SEQUENCIAL | integer(4) | PK |  | Código sequencial |
| EVENTO_INCLUSAO_AFASTAMENTO | smallint(2) |  |  | Evento de inclusão de afastamento (0 = Não/1 = Sim) |
| EVENTO_INCLUSAO_DATA_FIM_AFASTAMENTO | smallint(2) |  |  | Evento de inclusão de data fim de afastamento (0 = Não/1 = Sim) |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
