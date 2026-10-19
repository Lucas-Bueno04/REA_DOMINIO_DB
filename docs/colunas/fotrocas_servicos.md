# fotrocas_servicos — Trocas de servicos
11.405 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | codigo da empresa |
| i_empregados | integer(4) | PK |  | Codigo do empregado |
| data_troca | date(4) | PK |  | Data da troca |
| i_servicos | integer(4) |  |  | Codigo do servicos |
| data_gravacao | timestamp(8) |  |  | Data da gravacao da alteracao |
| usuario | char(15) |  |  | Nome do usuario que fez a troca |
| periodo_ctrl | tinyint(1) |  |  | Controle do 1=ativo 0 = inativo |
| periodo_inicio | date(4) |  |  | periodo inicial do empregado |
| periodo_fim | date(4) |  |  | periodo final do empregado |
| origem_reg | tinyint(1) |  | S | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| HORAS_TRABALHADAS_PRIMEIRO_DIA | numeric(5) |  |  | Quantidade de horas trabalhadas no primeiro dia no serviço. |
| HORAS_TRABALHADAS_ULTIMO_DIA | numeric(5) |  |  | Quantidade de horas trabalhadas no último dia no serviço. |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| GUID_CONTABIL | uniqueidentifier(16) |  |  | Identificador único do registro no banco do Contábil |
| GUID_ONVIO | uniqueidentifier(16) |  | S | Identificador único do registro no banco do Atendimento Onvio |
| ENDPOINT_EXCLUSAO | varchar(1024) |  | S | Endpoint utilizado para a exclusão do registro. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
