# FOVIGENCIAS_SERVICO_ENTIDADES_EDUCATIVAS — Entidades educativas para contratação de aprendiz no cadastro de serviços.
9 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_SERVICOS | integer(4) | PK |  | Código do serviço. |
| VIGENCIA | date(4) | PK |  | Vigência. |
| SEQUENCIAL | integer(4) | PK |  | Sequencial. |
| NOME | varchar(50) |  |  | Nome da entidade educativa. |
| CNPJ | varchar(14) |  |  | CNPJ da entidade educativa. |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
