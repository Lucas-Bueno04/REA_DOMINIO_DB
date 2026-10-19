# FOFUNCOES_ALTERACAO — Tabela de alterações.
142 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_FUNCAO | integer(4) | PK |  | Código da função. |
| VIGENCIA | date(4) | PK |  | Vigência da alteração. |
| NOME | varchar(100) |  |  | Nome da função. |
| CBO_2002 | integer(4) |  | S | CBO 2002. |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| ORIGEM_ALTERACAO | smallint(2) |  | S | Origem do registro ( 1=Sistema/2=Alteração de Faseamento do eSocial). |
| CODIGO_ESOCIAL | varchar(30) |  | S | Código no eSocial |
