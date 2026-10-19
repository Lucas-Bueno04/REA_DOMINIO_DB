# FOCAT_PARTE_CORPO_ATINGIDA_LISTA — Lista de partes do corpo atingida da CAT.
7 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| I_CAT | integer(4) | PK |  | Código da CAT. |
| SEQUENCIAL | integer(4) | PK |  | Sequencial da lista. |
| CODIGO_PARTE_CORPO_ATINGIDA | varchar(10) |  | S | Código da parte do corpo atingida. |
| LATERALIDADE | smallint(2) |  |  | Lateralidade. (0=Não aplicável/1=Esquerda/2=Direita/3=Ambas) |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
