# geresponsavel — Responsavel - Cadastro
1.986 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| empresa | char(40) |  |  | Empresa |
| nome | char(40) |  |  | Nome |
| endereco | char(40) |  |  | Endereco |
| bairro | char(30) |  |  | Bairro |
| cidade | char(30) |  | S | Cidade |
| estado | char(2) |  |  | UF |
| cep | char(8) |  |  | CEP |
| fone | char(14) |  |  | Fone |
| tipo_insc | tinyint(1) |  |  | Tipo inscricao |
| cgc | char(14) |  |  | CNPJ |
| email | varchar(255) |  |  | Email |
| dddfone | char(3) |  |  | DDD |
| ramal | char(5) |  |  | Ramal |
| numero | integer(4) |  | S | Numero |
| i_municipio | integer(4) |  | S | Cod. Municipio |
| codi_emp | integer(4) | PK |  | Codigo empresa |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| i_responsavel | integer(4) | PK |  | Código |
| nit | char(11) |  | S | NIT |
| cargo | char(40) |  | S | Cargo |
| codigo_municipio | integer(4) |  | S | Codigo do municipio |
| DATA_NASCIMENTO | date(4) |  | S | DATA DE NASCIMENTO |
| CPF | char(11) |  | S | CPF |
| DOCUMENTO_IDENTIDADE | char(15) |  | S | Identidade |
| ORGAO_EMISSOR_IDENTIDADE | char(8) |  | S | Orgão expedição identidade |
| UF_EMISSAO_IDENTIDADE | char(2) |  | S | UF expedição identidade |
| DATA_EMISSAO_IDENTIDADE | date(4) |  | S | Data emissão identidade |
| FAX | char(9) |  | S | Fax |
| COMPLEMENTO | char(30) |  | S | Complemento do endereço |
| TELEFONE_CELULAR | varchar(12) |  | S | Telefone celular. |
| NOME_PAI | varchar(60) |  | S | Nome do pai. |
| NOME_MAE | varchar(60) |  | S | Nome da mãe. |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
