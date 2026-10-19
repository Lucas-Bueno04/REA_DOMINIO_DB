# FOJORNADAS — Jornadas.
2.804 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_JORNADA | integer(4) | PK |  | Código do jornada. |
| NOME | varchar(100) |  |  | Nome da jornada. |
| DATA_INICIO | date(4) |  |  | Data de início da jornada. |
| SITUACAO | smallint(2) |  |  | Situação da jornada. (0=Inativo/1=Ativo) |
| DATA_INATIVACAO | date(4) |  | S | Data de inativação da jornada. |
| TIPO | smallint(2) |  |  | Tipo de jornada. (1=Padrão/2=Turno fixo/3=Turno variável/4=Especial/Escala) |
| TIPO_ESCALA | smallint(2) |  |  | Tipo de escala. (0=Não possui/1=12x36/2=24x72/3=Outras) |
| ESCALA | varchar(15) |  | S | Descrição da escala. |
| ORIGEM_REG | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
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
| JORNADA_ESOCIAL | smallint(2) |  |  | Tipo de jornada eSocial |
| DESCRICAO_JORNADA | varchar(999) |  | S | Descrição da jornada |
