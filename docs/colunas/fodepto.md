# fodepto — Departamento - Cadastro
1.403 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_depto | integer(4) | PK |  | Codigo |
| nome | char(40) |  |  | Nome |
| endereco | char(40) |  | S | Endereco |
| numero | integer(4) |  | S | Numero |
| bairro | char(20) |  | S | Bairro |
| cidade | char(20) |  | S | Cidade |
| estado | char(2) |  | S | Estado |
| cep | char(8) |  | S | CEP |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| DATA_INICIO | date(4) |  |  | Data de início do departamento. |
| SITUACAO | smallint(2) |  | S | Situação do departamento. (0=Inativo/1=Ativo) |
| DATA_INATIVACAO | date(4) |  | S | Data de inativação do departamento. |
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
