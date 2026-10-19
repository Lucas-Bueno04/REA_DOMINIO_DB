# FOINSTITUICAO_ENSINO — Cadastro de instituições de ensino.
212 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_INSTITUICAO_ENSINO | integer(4) | PK |  | Código da instituição de ensino. |
| NOME | varchar(100) |  |  | Nome da instituição de ensino. |
| DATA_CADASTRO | date(4) |  | S | Data de cadastro da instituição de ensino. |
| CNPJ | varchar(14) |  | S | CNPJ da instituição de ensino. |
| ENDERECO | varchar(80) |  | S | Endereço da instituição de ensino. |
| NUMERO | integer(4) |  | S | Número |
| COMPLEMENTO | varchar(40) |  | S | Complemento do endereço da instituição de ensino. |
| BAIRRO | varchar(30) |  | S | Bairro da instituição de ensino. |
| CEP | varchar(8) |  | S | CEP |
| CODIGO_MUNICIPIO | integer(4) |  | S | Município da instituição de ensino. |
| CODIGO_PAIS | integer(4) |  | S | País da instituição de ensino. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro (0=Sistema/ 1=Imp Tabelas/ 2=Imp Layout/ 3=Imp tabelas concorrentes) |
| NOME_REITOR | varchar(80) |  | S | Nome do reitor. |
| DDD_TELEFONE | varchar(3) |  | S | DDD do telefone. |
| TELEFONE | varchar(11) |  | S | Telefone. |
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
