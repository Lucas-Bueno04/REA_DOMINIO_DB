# FOEMPREGADOS_EXAMES_TOXICOLOGICOS — Exames toxicológicos dos empregados
13 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| DATA | date(4) |  |  | Data do exame. |
| TIPO | smallint(2) | PK |  | Tipo do exame. (1=Admissional/2=Demissional/3=Periódico) |
| CODIGO_EXAME | varchar(17) |  | S | Codigo do exame |
| CNPJ_LABORATORIO | varchar(14) |  |  | CNPJ do laboratório. |
| I_MEDICOS | integer(4) |  |  | Código do médico. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout) |
| SEQUENCIAL | integer(4) | PK |  | Sequencial para exames periódicos. |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| ENVIAR_ESOCIAL_PERIODO_ANTERIOR_INICIO_BANCO_CONTABIL | smallint(2) |  | S | Enviar evento eSocial anterior ao início da utilização do banco de dados (0=Não/1=Sim) |
