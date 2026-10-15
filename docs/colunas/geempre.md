# geempre — Empresa - Cadastro
1.969 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| nome_emp | char(40) |  |  | Nome |
| ende_emp | char(40) |  | S | Endereco |
| cepe_emp | char(8) |  | S | CEP |
| cida_emp | char(25) |  | S | Cidade |
| cgce_emp | char(14) |  | S | CNPJ |
| iest_emp | char(22) |  | S | Inscricao estadual |
| imun_emp | char(20) |  | S | Inscricao municipal |
| ijuc_emp | char(30) |  | S | Inscricao na junta comercial |
| bair_emp | char(60) |  | S | Bairro |
| ramo_emp | char(180) |  | S | Ramo de atividade |
| codi_emp | integer(4) | PK |  | Codigo |
| apel_emp | char(20) |  |  | Apelido |
| codi_mun | integer(4) |  | S | Codigo do municipio |
| nume_emp | integer(4) |  | S | Numero |
| djuc_emp | date(4) |  | S | Data de inscricao na junta comercial |
| fone_emp | char(14) |  | S | Telefone |
| rleg_emp | char(60) |  | S | Responsavel legal |
| esta_emp | char(2) |  | S | Estado |
| tins_emp | integer(4) |  | S | Tipo da inscrição(1 - CNPJ/2 - CPF/3 - CEI/6 - CAEPF) |
| stat_emp | char(1) |  | S | A - Ativa / I - Inativa / C - Em Constituicao / M - Ativo sem movimento / B - Em processo de baixa / E - Excluindo |
| dina_emp | date(4) |  | S | Data que ficou inativo |
| dcad_emp | date(4) |  | S | Data do cadastramento |
| sele_emp | tinyint(1) |  | S | Selecionada (1 - Sim/0 - Nao) |
| codi_cla | tinyint(1) |  | S | Este campo nao e mais usado a partir da versao 6.1A-01 do Contabil |
| ucta_emp | tinyint(1) |  | S | Usa contabilidade (1 - Sim/0 - Nao) |
| ucxa_emp | tinyint(1) |  | S | Usa livro caixa (1 - Sim/0 - Nao) |
| uhon_emp | tinyint(1) |  | S | Usa honorarios (1 - Sim/0 - Nao) |
| uefi_emp | tinyint(1) |  | S | Usa escrita fiscal (1 - Sim/0 - Nao) |
| upat_emp | tinyint(1) |  | S | Usa patrimonio (1 - Sim/0 - Nao) |
| ulal_emp | tinyint(1) |  | S | Usa lalur (1 - Sim/0 - Nao) |
| uatu_emp | tinyint(1) |  | S | Usa atualizar (1 - Sim/0 - Nao) |
| upro_emp | tinyint(1) |  | S | Usa protocolo (1 - Sim/0 - Nao) |
| ccae_emp | double(8) |  | S | CAE |
| isub_emp | char(20) |  | S | Inscricao Substituto Tributario |
| empreg_emp | integer(4) |  | S | Nro de empregados da empresa |
| vlfat_emp | numeric(13) |  | S | Valor Medio do Faturamento |
| vlhon_emp | numeric(13) |  | S | Valor dos honorarios |
| cpf_leg_emp | char(14) |  | S | CPF do responsavel legal |
| end_leg_emp | char(40) |  | S | Endereco do responsavel legal |
| mun_leg_emp | char(25) |  | S | Municipio do responsavel legal |
| uf_leg_emp | char(2) |  | S | Estado do responsavel legal |
| cep_leg_emp | char(8) |  | S | CEP do responsavel legal |
| njud_emp | integer(4) |  | S | Natureza juridica |
| comp_emp | char(30) |  | S | Complemento |
| nume_leg_emp | integer(4) |  | S | Numero do responsavel legal |
| bair_leg_emp | char(15) |  | S | Bairro do responsavel legal |
| codm_leg_emp | integer(4) |  | S | Codigo do municipio do responsavel legal |
| fone_leg_emp | char(14) |  | S | Telefone do responsavel legal |
| cnae_emp | double(8) |  | S | CNAE |
| dddf_emp | integer(4) |  | S | DDD |
| codi_con | integer(4) |  | S | Contador |
| cargo_leg_emp | char(30) |  | S | Cargo do responsavel legal |
| dddf_leg_emp | integer(4) |  | S | DDD do responsavel legal |
| livro_cart_emp | char(10) |  | S | Nro do livro no cartorio de registros Especiais |
| folha_cart_emp | char(10) |  | S | Folha do livro no cartorio de registros Especiais |
| nliv_cart_emp | char(10) |  | S | Nro na folha do livro no cartorio de registros Especiais |
| soc_civis_emp | char(1) |  | S | Sociedade Civil (S/N) |
| cfdf_emp | char(13) |  | S | CF/DF Somente para o Distrito Federal |
| simples_emp | char(1) |  | S | Enquadramento no simples - folha |
| dsimples_emp | date(4) |  | S | Data de enquadramento no simples - folha |
| munirais_emp | numeric(7) |  | S | Codigo federal do municipio |
| rfed_emp | integer(4) |  | S | Regime federal - folha |
| ufol_emp | tinyint(1) |  | S | Usa folha (1 - Sim/0 - Nao) |
| upto_emp | tinyint(1) |  |  | Usa ponto (1 - Sim/0 - Nao) |
| comp_leg_emp | char(30) |  | S | Complemento do responsavel legal |
| email_emp | char(255) |  | S | email |
| i_classificacoes | integer(4) |  | S | Codigo da classificacao |
| ctahono_emp | integer(4) |  | S | Conta Contabil para integracao do Honorarios |
| rg_resp_emp | char(15) |  | S | RG do responsavel legal |
| caedesm_emp | integer(4) |  | S | Codigo de desmembramento do CAE - MG |
| nome_cartorio_emp | varchar(100) |  |  | Nome do cartorio |
| selehono_emp | tinyint(1) |  | S | Selecionado no novo honorarios (1 - Sim/0 - Nao) |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| fantasia_emp | char(50) |  | S | Nome fantasia |
| foro_emp | char(50) |  | S | Foro da comarca |
| obj_social_emp | varchar(3000) |  | S | Objeto social |
| dtinicio_emp | date(4) |  | S | Data de inicio das atividades |
| pais_emp | varchar(50) |  | S | Pais |
| duracao_emp | char(1) |  |  | Duracao do contrato (D - Determinado/I - Indeterminado) |
| data_cart | date(4) |  | S | Data de registro no cartorio |
| dttermino_emp | date(4) |  | S | Data de termino do contrato |
| fax_emp | char(14) |  | S | Numero do Fax |
| ureg_emp | tinyint(1) |  | S | Usa registro (1 - Sim/0 - Nao) |
| razao_emp | varchar(255) |  |  | Razao Social |
| tipoi_emp | tinyint(1) |  | S | Motivo da inatividade da empresa(1-Outros/2-Baixada/3-Transferida/4-Inadimplente)) |
| tipo_end_emp | tinyint(1) |  |  | Tipo do endereco |
| codigo_pais | integer(4) |  |  | Codigo do pais |
| codigo_municipio | integer(4) |  | S | Codigo do municipio |
| insc_suframa | char(9) |  | S | Numero de inscricao na Suframa |
| i_cnae20 | char(15) |  | S | Codigo do CNAE 2.0 |
| usa_cnae20 | char(1) |  |  | Usa o CNAE 2.0 (S/N) |
| email_leg_emp | char(255) |  | S | Email do responsavel legal |
| upto_tec_emp | tinyint(1) |  |  | Usa teclado(1 - Sim/0 - Nao) |
| observacao_emp | varchar(32000) |  | S | Observacoes |
| uf_emissao_resp | varchar(2) |  | S | UF emissão Responsavel Legal |
| caixa_postal_emp | char(6) |  | S | Caixa Postal |
| usa_dominio_web | smallint(2) |  | S | Usa Dominio Web(1 - Sim/0 - Nao) |
| CERTIFICADO_DIGITAL | char(1) |  | S | Possui o Certificado digital para assinatura dos atos da Junta Comercial(S/N) |
| SITE_EMP | char(40) |  | S | Página da Internet da empresa |
| QUALIFICACAO_LEG_EMP | integer(4) |  |  | Qualificação do responsável legal |
| HONORARIO_TIPO | char(1) |  |  | Usar o modulo honorarios como Escritorio ou Cliente (E=Escritorio/C=Cliente) |
| CNAE_20_DESMENBRAMENTO | integer(4) |  | S | Desmembramento do CNAE 2.0 |
| TIPO_REGISTRO | char(1) |  |  | Registro (C=Cartório/ O=OAB) |
| IDENTIFICACAO_LIVRO_DEMONSTRATIVO | char(1) |  |  | Identificação da empresa nos livros e demonstrativos (E=Empresa/ N=Entidade/ S=Sociedade/ A=Sociedade de advogados) |
| ORGAO_EMISSOR_LEG_EMP | char(14) |  | S | Orgão emissor do responsável legal |
| DATA_EMISSAO_LEG_EMP | date(4) |  | S | Data de emissão do responsável legal |
| IDENTIDADE_PROFISSIONAL_LEG_EMP | varchar(30) |  | S | Identidade profissional do responsável legal |
| CODIGO_MUNICIPIO_CARTORIO | integer(4) |  | S | Município do cartório |
| PROFISSAO_LEG_EMP | varchar(40) |  | S | Profissão |
| NACIONALIDADE_LEG_EMP | varchar(40) |  | S | Nacionalidade |
| ESTADO_CIVIL_LEG_EMP | tinyint(1) |  | S | Estado Civil (1=Solteiro/2=Casado/3=Viúvo/4=Divorciado/5=Concubinato/6=Separado(a) judicialmente/7=União estável) |
| GERAR_INTEGRA | char(1) |  |  | Gera informação para o INTEGRA - Thomson Reuters |
| OBS_GERAL | varchar(32000) |  | S |  |
| OBS_SOCIETARIO | varchar(32000) |  | S |  |
| OBS_CONTABIL | varchar(32000) |  | S |  |
| OBS_FISCAL | varchar(32000) |  | S |  |
| OBS_PESSOAL | varchar(32000) |  | S |  |
| RESPONSAVEL_LEGAL_EMPRESA_JUNTO_BASE_RFB | char(1) |  |  | É responsável legal da empresa junto as bases da RFB |
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
| CNPJ_PRODUTOR_RURAL_EMP | char(14) |  | S | CNPJ Produtor Rural |
| ESCRITORIO_USA_CUSTOS | integer(4) |  |  | 1- Empresa é um escritorio que utiliza custos nos modulos, 0 - Empresa não é um escritorio que utiliza custos |
| CODIGO_MUNICIPIO_RESPONSAVEL_LEGAL | integer(4) |  | S | Código Municipio |
| USA_PORTAL_EMPREGADO | bit(1) |  |  | 1- Empresa utiliza portal do empregado, 0 - Empresa não utiliza portal do empregado |
| USA_EMPRESA_CENTRALIZADORA | char(1) |  |  | Campo vai ser utilizado para saber se utiliza empresa Transmissora |
| EMPRESA_CENTRALIZADORA | integer(4) |  | S | Valor Encargos Honorarios |
| USA_PROCESSOS_GESTTA | bit(1) |  |  | Coluna não é mais utilizada, controle do gestta processos é feito na tabela GEONVIO_DADOS_SESSAO_COMPANY |
| EXCLUSAO_COMPLETA_DADOS | char(1) |  |  | Status da exclusão de dados (S-Sim/N-Não/P-Parcial) |
| ACESSO_MODULOS_ANTERIOR_EXCLUSAO_DADOS | varchar(150) |  | S | Situação de acesso aos módulos anterior ao início da exclusão de dados |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| ASSINATURA_DIGITAL_RESPONSAVEL_LEGAL_EMPRESA | char(1) |  |  | Possui assinatura digital para o responsável legal |
| ORIGEM_EMP | integer(4) |  |  | Origem da empresa 0: ContÃ¡bil 1: Onvio |
| PERMITE_INCLUIR_BRCLIENT | smallint(2) |  |  | Permite incluir cliente BRClient: 0 - Não, 1 - Sim |
| IMPORTAR_APURACAO_ASSISTIDA_API_CBS | char(1) |  |  | Importar apuração assistida via API do CBS |
