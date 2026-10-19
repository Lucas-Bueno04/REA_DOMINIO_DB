# GEEMPRE_ALTERACAO — Empresa - Alterações
4.910 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| DATA_ALTERACAO | date(4) | PK |  | Data da alteração |
| CAMPO | tinyint(1) | PK |  | Campo alterado |
| DE | varchar(255) |  |  | Valor anterior a alteracao |
| PARA | varchar(255) |  |  | Valor posterior a aleracao |
| ORIGEM | tinyint(1) |  |  | Origem da alteração (1=Cadastro de empresa/ 2=Alteração contratual) |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
