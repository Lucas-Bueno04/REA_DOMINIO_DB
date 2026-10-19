# FOFILIAIS_HISTORICO — Histórico de alterações no cadastro de filiais.
1.769 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_FILIAIS | integer(4) | PK |  | Código da filial. |
| DATA_TROCA | date(4) | PK |  | Data da troca. |
| CAMPO | smallint(2) | PK |  | Campo. |
| DE | char(255) |  |  | Valor antigo. |
| PARA | char(255) |  |  | Valor novo. |
| DATA_GRAVACAO | date(4) |  |  | Data da gravação. |
| HORARIO_GRAVACAO | time(8) |  |  | Horário da gravação. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout) |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
