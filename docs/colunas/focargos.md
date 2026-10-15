# focargos — Cargo - Cadastro
6.043 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_cargos | integer(4) | PK |  | Codigo |
| nome | char(100) |  |  | Nome |
| cbo | integer(4) |  | S | CBO 1994 |
| cbo_2002 | integer(4) |  | S | CBO 2002 |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes, 4-Importação eSocial |
| atividade | varchar(1000) |  | S | Atividade |
| PPP_CAMPO_1 | smallint(2) |  |  | tentativa a implementaCAo de medidas de proteCAo coletiva |
| PPP_CAMPO_2 | smallint(2) |  |  | condiCOes de funcionamento e do uso ininterrupto do epi |
| PPP_CAMPO_3 | smallint(2) |  |  | observado o prazo de validade |
| PPP_CAMPO_4 | smallint(2) |  |  | observada a periodicidade de troca definida pelos programas ambientais |
| PPP_CAMPO_5 | smallint(2) |  |  | observada a higienizaCAo |
| PPP_OBSERVACOES | varchar(400) |  | S | ObservaCOes para o PP |
| GERENCIA_SUPERVISAO | smallint(2) |  |  | GerÊncia ou supervisão. (0=Não/1=Sim) |
| DATA_INICIO | date(4) |  |  | Data de início do cargo. |
| SITUACAO | smallint(2) |  | S | Situação do cargo. (0=Inativo/1=Ativo) |
| DATA_INATIVACAO | date(4) |  | S | Data de inativação do cargo. |
| CODIGO_ESOCIAL | varchar(30) |  | S | Código no eSocial. |
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
| ACUMULA_CARGO | smallint(2) |  |  | Cargo, Emprego ou Função pública acumulável. (0=Não/1=Sim |
