# foservicos — Servico - Cadastro
1.770 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_servicos | integer(4) | PK |  | Codigo |
| cgc | char(14) |  | S | ** SEM USO ** CNPJ/CPF/CEI |
| tipo_insc | smallint(2) |  | S | ** SEM USO ** Tipo inscricao |
| codigo_terceiro | numeric(4) |  | S | ** SEM USO ** Codigo terceiro |
| perc_terceiro | numeric(5) |  | S | ** SEM USO ** Terceiro(%) |
| perc_inss_empresa | numeric(5) |  | S | ** SEM USO ** INSS Empresa(%) |
| perc_acid_trabalho | numeric(5) |  | S | ** SEM USO ** Acid. Trabalho(%) |
| codigo_sat | numeric(5) |  | S | ** SEM USO ** Codigo do SAT |
| perc_autonomos | numeric(5) |  | S | ** SEM USO ** Pro-Lab./Aut.(%) |
| codigo_fpas | numeric(3) |  | S | ** SEM USO ** Codigo FPAS |
| codigo_atividade | numeric(7) |  | S | ** SEM USO ** CNAE |
| codigo_gfip | numeric(3) |  | S | ** SEM USO ** Codigo SEFIP |
| codigo_gps | numeric(4) |  | S | ** SEM USO ** Codigo GPS |
| i_bancos | integer(4) |  | S | ** SEM USO ** Banco |
| numero_fgts | numeric(14) |  | S | ** SEM USO ** Numero |
| nome | char(40) |  | S | Nome |
| endereco | char(31) |  | S | ** SEM USO ** Endereco |
| numero | integer(4) |  | S | ** SEM USO ** Numero |
| bairro | char(20) |  | S | ** SEM USO ** Bairro |
| cep | char(8) |  | S | ** SEM USO ** CEP |
| cidade | char(20) |  | S | ** SEM USO ** Cidade |
| estado | char(2) |  | S | ** SEM USO ** UF |
| i_filiais | integer(4) |  | S | ** SEM USO ** Filial |
| sequencia_gps | integer(4) |  | S | ** SEM USO ** Sequencia |
| filantropia | numeric(6) |  | S | ** SEM USO ** Isencao Filantropia(%) |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| tipo | integer(4) |  | S | ** SEM USO ** |
| codi_mun | integer(4) |  | S | ** SEM USO ** Codigo do municipio |
| codigo_municipio | integer(4) |  | S | ** SEM USO ** Codigo do municipio |
| I_FPAS | integer(4) |  | S | ** SEM USO ** Código Sequencial FPAS |
| DATA_INICIO | date(4) |  |  | Data de início do serviço. |
| SITUACAO | smallint(2) |  |  | Situação do serviço. (0=Inativo/1=Ativo) |
| DATA_INATIVACAO | date(4) |  | S | Data de inativação do serviço. |
| CODIGO_ESOCIAL | varchar(30) |  | S | Código no eSocial. |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
