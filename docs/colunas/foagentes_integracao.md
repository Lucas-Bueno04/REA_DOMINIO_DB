# FOAGENTES_INTEGRACAO — Cadastro de agentes de integração.
8 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_AGENTES_INTEGRACAO | integer(4) | PK |  | Código do agente de integração. |
| NOME | varchar(100) |  | S | Nome do agente de integração. |
| DATA_CADASTRO | date(4) |  | S | Data de cadastro do agente de integração. |
| CNPJ | varchar(14) |  | S | CNPJ do agente de integração. |
| ENDERECO | varchar(80) |  | S | Endereço do agente de integração. |
| NUMERO | integer(4) |  | S | Número |
| COMPLEMENTO | varchar(40) |  | S | Complemento do endereço do agente de integração. |
| BAIRRO | varchar(30) |  | S | Bairro do agente de integração. |
| CEP | varchar(8) |  | S | CEP |
| CODIGO_MUNICIPIO | integer(4) |  | S | Município do agente de integração. |
| CODIGO_PAIS | integer(4) |  | S | País do agente de integração. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro (0=Sistema/ 1=Imp Tabelas/ 2=Imp Layout/ 3=Imp tabelas concorrentes) |
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
