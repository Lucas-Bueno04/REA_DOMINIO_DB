# FOTROCAS_HORAS — Trocas da quantidade de horas trabalhadas pelo empregado.
33.110 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| DATA_TROCA | date(4) | PK |  | Data da alteração. |
| CAMPO | smallint(2) | PK |  | Campo alterado. (1=Horas dia/2=Horas semana/3=Horas mês/4=Horas compensadas) |
| VALOR | numeric(5) |  |  | Valor alterado. |
| DATA_GRAVACAO | date(4) |  |  | Data da gravação. |
| HORARIO_GRAVACAO | time(8) |  |  | Horário da gravação. |
| RETIFICACAO | smallint(2) |  | S | Retificação. (0=Não/1=Sim) |
| PERIODO_CTRL | smallint(2) |  | S | Período de controle. (0=Inativo/1=Ativo) |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro (0=Sistema/ 1=Imp Tabelas/ 2=Imp Layout) |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
