# FOOPERADORAPLANOSAUDE — Operadora de plano de saúde - Cadastro
28 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_OPERADORAPLANOSAUDE | integer(4) | PK |  | Código da operadora de plano de saúde |
| NOME | char(150) |  |  | Nome |
| CNPJ | char(14) |  |  | CNPJ |
| ENDERECO | char(60) |  |  | Endereço |
| NUMERO | integer(4) |  |  | Número |
| COMPLEMENTO | char(60) |  |  | Complemento |
| BAIRRO | char(60) |  |  | Bairro |
| CODIGO_MUNICIPIO | integer(4) |  | S | Código do município |
| CEP | char(8) |  |  | CEP |
| DDD | integer(4) |  |  | DDD |
| FONE | char(14) |  |  | Telefone |
| FAX | char(14) |  |  | Fax |
| ORIGEM_REG | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| REGISTRO_ANS | varchar(6) |  | S | Registro da ANS Agencia Nacional de Saude |
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
