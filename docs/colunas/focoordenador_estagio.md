# FOCOORDENADOR_ESTAGIO — Coordenadores de estágio.
264 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_COORDENADOR_ESTAGIO | integer(4) | PK |  | Código do coordenador de estágio. |
| NOME | varchar(80) |  | S | Nome |
| DATA_CADASTRO | date(4) |  | S | Data de cadastro do coordenador de estágio. |
| CPF | char(11) |  | S | CPF do coordenador de estágio. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro (0=Sistema/ 1=Imp Tabelas/ 2=Imp Layout/ 3=Imp tabelas concorrentes) |
| TIPO | smallint(2) | PK |  | Tipo. (1=Coordenador/2=Supervisor) |
| GRAU_INSTRUCAO | smallint(2) |  |  | Grau de instrução. |
| EMAIL | varchar(120) |  | S | E-mail. |
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
