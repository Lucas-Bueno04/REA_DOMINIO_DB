# fofiliais — Filiais - Cadastro
1.672 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_filiais | integer(4) | PK |  | Codigo |
| nome | char(40) |  |  | Nome |
| endereco | char(40) |  | S | Endereco |
| numero | integer(4) |  | S | Numero |
| complemento | char(60) |  | S | Complemento |
| cidade | char(25) |  | S | Cidade |
| estado | char(2) |  | S | Estado |
| cep | char(8) |  | S | CEP |
| tipo_insc | tinyint(1) |  | S | Tipo inscricao |
| cgc | char(14) |  | S | Inscricao |
| inscricao | char(22) |  | S | Inscr. Estadual |
| telefone | char(14) |  | S | Telefone |
| cnae | double(8) |  | S | CNAE |
| i_municipio | integer(4) |  | S | Cod. Municipio |
| bairro | char(20) |  | S | Bairro |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| codigo_municipio | integer(4) |  | S | Codigo do municipio |
| i_cnae20 | char(15) |  | S | CNAE 2.2 |
| i_sindicatos_p | integer(4) |  | S | ** SEM USO ** Codigo do sindicato patronal |
| sind_centralizador | tinyint(1) |  | S | Indica se o sindicato e centralizador |
| sind_capital_social | numeric(13) |  | S | ** SEM USO ** Capital social |
| cnpj_centralizador | char(14) |  | S | CNPJ da filial centralizadora |
| SINDICALIZADA | char(1) |  |  | EMPRESA E FILIADA A SINDICATO |
| CODI_EMP_ATENDIMENTO | integer(4) |  | S | Código da empresa no módulo Domínio Atendimento |
| PERMITE_CADASTRAR_EMPREGADOS_DOMINIO_ATENDIMENTO | smallint(2) |  |  | Permite cadastrar empregados no Domínio Atendimento. (0=Não/1=Sim) |
| CENTRALIZACAO_EVENTOS_ESOCIAL | smallint(2) |  |  | Centralização dos eventos do eSocial. (1=Centralizada/2=Centralizadora) |
| POSSUI_ESTABELECIMENTOS_OUTRO_BANCO_DADOS | smallint(2) |  |  | Possui estabelecimentos em outro banco de dados. (0=Não/1=Sim) |
| RAZAO_SOCIAL | varchar(255) |  | S | Razão social. |
| TIPO_ENDERECO | smallint(2) |  | S | Tipo do endereço. |
| TODAS_FILIAIS_CENTRALIZADAS_POSSUEM_MESMA_TABELA_RUBRICAS | smallint(2) |  |  | Todas as filiais centralizadas possuem a mesma tabela de rubricas. (0=Não/1=Sim) |
| POSSUI_EMPRESA_CENTRALIZADORA_RUBRICAS_ESOCIAL_OUTRO_BANCO_DADOS | smallint(2) |  |  | Possui a empresa centralizadora dos eventos do eSocial em outro banco de dados. (0=Não/1=Sim) |
| IDENTIFICADOR_TABELA_RUBRICAS_ESOCIAL | varchar(8) |  | S | Identificador da tabela de rubricas para o eSocial. |
| CALCULAR_CONTRIBUICAO_SINDICAL_PATRONAL_A_PARTIR_11_2017 | smallint(2) |  |  | Calcular contribuição sindical patronal a partir de 11/2017. (0=Não/1=Sim) |
| COMP_INICIO_DESC_CONTRIB_SINDICAL_PATRONAL_A_PARTIR_11_2017 | date(4) |  | S | Competência de início do desconto da contribuição sindical patronal a partir de 11/2017. |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| NOME_FANTASIA | varchar(60) |  | S | Nome fantasia |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
