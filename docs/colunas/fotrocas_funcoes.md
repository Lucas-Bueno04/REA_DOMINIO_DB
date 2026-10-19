# FOTROCAS_FUNCOES — Trocas de funções
2.175 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | codigo da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Codigo do empregado |
| DATA_TROCA | date(4) | PK |  | Data da troca |
| I_FUNCAO | integer(4) |  | S | Codigo da função |
| DATA_GRAVACAO | timestamp(8) |  |  | Data da gravacao da alteracao |
| USUARIO | char(15) |  |  | Nome do usuario que fez a troca |
| PERIODO_CTRL | smallint(2) |  |  | Controle do 1=ativo 0 = inativo |
| PERIODO_INICIO | date(4) |  |  | periodo inicial do empregado |
| PERIODO_FIM | date(4) |  |  | periodo final do empregado |
| ORIGEM_REG | smallint(2) |  | S | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
