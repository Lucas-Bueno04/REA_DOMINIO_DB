# FOEVENTOS_ALTERACAO_CONTROLE_ENVIO_ESOCIAL — Tabela de controle de envio da rubrica ao eSocial.
3.750.710 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa do evento. |
| I_EVENTOS | integer(4) | PK |  | Código da rubrica. |
| VIGENCIA | date(4) | PK |  | Vigência da alteração. |
| CODI_EMP_ENVIO | integer(4) | PK |  | Codigo da empresa de envio do evento ao eSocial. |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
