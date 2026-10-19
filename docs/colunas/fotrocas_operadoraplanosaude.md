# FOTROCAS_OPERADORAPLANOSAUDE — ** SEM USO ** Trocas de operadora de plano de saúde
5 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| DATA_TROCA | date(4) | PK |  | Data da troca |
| I_OPERADORAPLANOSAUDE | integer(4) |  | S | Código da operadora do plano de saúde |
| DATA_GRAVACAO | timestamp(8) |  |  | Data da gravação da troca |
| USUARIO | char(15) |  |  | Usuário que realizou a troca |
| PERIODO_CTRL | smallint(2) |  |  | Controle: 0=Inativo/1=Ativo |
| PERIODO_INICIO | date(4) |  |  | Período inicial |
| PERIODO_FIM | date(4) |  |  | Período final |
| ORIGEM_REG | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
