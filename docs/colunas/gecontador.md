# GeContador — Empresa - Cadastro - Contadores
11 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_con | integer(4) | PK |  | Codigo |
| nome_con | varchar(255) |  |  | Nome |
| rcrc_con | char(15) |  | S | CRC |
| cpfc_con | char(14) |  | S | CPF |
| ende_con | char(40) |  | S | Endereco |
| nume_con | integer(4) |  | S | Numero do Endereco |
| bair_con | char(20) |  | S | Bairro |
| cida_con | char(25) |  | S | Cidade |
| cmun_con | integer(4) |  | S | Codigo do municipio |
| cepe_con | char(8) |  | S | CEP |
| ufed_con | char(2) |  | S | Estado |
| fone_con | char(10) |  | S | Telefone |
| dddf_con | integer(4) |  | S | DDD do fone |
| faxe_con | char(14) |  | S | FAX |
| email_con | varchar(255) |  | S | e-mail |
| cfdf_con | char(13) |  | S | CF/DF Somente para o Distrito Federal |
| tins_con | tinyint(1) |  | S | Tipo de inscricao (1=CNPJ, 2=CPF) |
| categoria_con | char(1) |  |  | Categoria (T - Tecnico/C - Contador) |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| cmunrais_con | integer(4) |  | S | Codigo do municipio do IBGE |
| codigo_municipio | integer(4) |  | S | Codigo do municipio |
| cnpj | char(14) |  | S | CNPJ |
| identidade | char(15) |  | S | Carteira de identidade |
| data_exp_ident | date(4) |  | S | Data expedicao |
| org_exp_ident | char(8) |  | S | Orgao expedidor |
| uf_exp_ident | char(2) |  | S | UF expedidor |
| MATRICULA | char(6) |  | S | Matrícula |
| CERTIFICADO_DIGITAL | char(1) |  | S | Possui o Certificado digital para assinatura dos atos da Junta Comercial(S/N) |
| COMPLEMENTO | varchar(60) |  | S | Complemento endereco |
| UF_CRC | char(2) |  | S | UF CRC |
| ACESSO_PORTAL_SEFAZ | char(1) |  | S | SEFAZ - Acesso ao portal |
| TIPO_PESSOA_PORTAL_SEFAZ | char(1) |  | S | SEFAZ - Tipo de pessoa |
| SENHA_PORTAL_SEFAZ | varchar(16) |  | S | SEFAZ - Senha |
| TIPO_CRC_SEFAZ | integer(4) |  | S | SEFAZ - Tipo do CRC |
| DATA_VALIDADE_CRC | date(4) |  | S | Data de validade do CRC |
| SEQUENCIAL_CRC | varchar(20) |  | S | Sequencial do CRC |
| ARQUIVO_CERTIFICADO_DIGITAL | varchar(256) |  | S | Arquivo Certificado Digital (SEFAZ) |
| RAZAO_SOCIAL | varchar(255) |  |  | Razão Social |
| CRC_ESCRITORIO | varchar(15) |  | S | Número de inscrição do CRC do Escritório |
| CERTIFICADO_DIGITAL_A3 | char(1) |  | S | Certificado Digital A3 (SEFAZ) |
| RESPONSAVEL_LEGAL_EMPRESA_JUNTO_BASE_RFB | char(1) |  |  | (ESTA COLUNA NÃO É MAIS UTILIZADA) |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| ARQUIVO_CERTIFICADO_DIGITAL_NOME_REAL | varchar(256) |  | S | Nome real do certificado digital (SEFAZ) |
| TIPO_ENDERECO | tinyint(1) |  |  | Tipo do endereço |
| ASSINATURA_DIGITAL_CONTADOR | char(1) |  |  | Possui assinatura digital |
| DAS_API_CONTADOR_CONSUMER_KEY | char(50) |  | S | Chave de consumo da API Contador |
| DAS_API_CONTADOR_CONSUMER_SECRET | char(50) |  | S | Senha de consumo da API Contador |
| GUID_BRCLIENT | uniqueidentifier(16) |  | S | Id do Contador no BR Client Service |
| INFORMAR_CERTIFICADO_ESPECIFICO_SEFAZ | char(1) |  |  | Informar um certificado especÃ­fico para a importaÃ§Ã£o de notas atravÃ©s do Web Service SEFAZ |
| NAO_PERMITE_HABILITAR_ACESSO_SEFAZ | char(1) |  | S | NÃ£o permitir habilitar guia Acesso SEFAZ |
