# effornece — Fornecedores - Cadastro
61.984 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_for | integer(4) | PK |  | Codigo |
| sigl_est | char(2) |  |  | Estado |
| codm_for | integer(4) |  | S | Codigo do municipio |
| codi_cta | integer(4) |  | S | Conta contabil |
| nomr_for | char(40) |  | S | Nome |
| nome_for | char(150) |  |  | Razao social |
| ende_for | char(40) |  | S | Endereco |
| nume_for | integer(4) |  | S | Numero |
| cida_for | char(30) |  | S | Cidade |
| cepe_for | char(8) |  | S | CEP |
| cgce_for | char(14) |  | S | CNPJ |
| insc_for | char(20) |  | S | Inscricao estadual |
| fone_for | char(14) |  | S | Fone |
| faxe_for | char(14) |  | S | Fax |
| agro_for | char(1) |  |  | Fornecedor agropecuario (S/N) |
| icms_for | char(1) |  |  | Contribuinte do ICMS (S/N) |
| tins_for | integer(4) |  | S | TIPO DA INSCRICAO (1 - CNPJ/2 - CPF/3 - CEI/6 - CAEPF) |
| dddf_for | integer(4) |  | S | DDD |
| imun_for | char(20) |  | S | Inscricao Municipal |
| bair_for | char(60) |  | S | Bairro |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes, 4 - Iceberg |
| categoria_estabel_for | char(3) |  | S | Categoria do Estabelecimento |
| iestst_for | char(22) |  | S | Inscricao Estadual ST |
| email_for | char(255) |  | S | Email |
| regime_for | char(1) |  |  | REGIME DE APURACAO (N - NORMAL/M- ME/E - EPP/O - OUTROS/S - ME - SIMPLES NACIONAL/P - EPP - SIMPLES NACIONAL/U - IMUNE/I - ISENTA)) |
| codigo_pais | integer(4) |  |  | Codigo do pais |
| codigo_municipio | integer(4) |  | S | Codigo do municipio |
| insc_suframa | char(9) |  | S | Numero de inscricao na Suframa |
| complemento_for | char(40) |  | S | Complemento do endereco |
| CADASTRO_FOR | date(4) |  | S | Data do cadastro do fornecedor |
| CONTA_CLIENTE_FOR | integer(4) |  | S | Conta contabil do cliente |
| TIPO_ASSINANTE_FOR | integer(4) |  | S | Tipo de assinante utilizado na última nota lançada |
| POSSUI_INTERDEPENDENCIA_FOR | char(1) |  | S | Interdependência com a empresa(S/N) |
| AGENTE_REGULADO_FOR | char(1) |  |  | Agente Regulado |
| CODIGO_INSTALACAO_FOR | varchar(7) |  |  | Código Instalação |
| PARTICIPANTE_FOME_ZERO | char(1) |  |  | Participante do Fome Zero |
| INSC_PROG_AQUISICAO_ALIMENTOS | char(1) |  |  | Inscrito no Programa de Aquisição de Alimentos |
| I_CNAE20 | char(15) |  | S | Codigo CNAE 20 |
| POSSUI_NIF | char(1) |  | S | Possui NIF (S - Sim / D - Beneficiário dispensado do NIF / N - País não exige NIF) |
| NIF | varchar(30) |  |  | NIF |
| VAREJISTA_OU_CONSUMIDOR_FINAL_FOR | char(1) |  |  | Varejista ou Consumidor Final |
| CONTA_COMPENSACAO_FOR | integer(4) |  | S | Conta compensação |
| CENTRO_DISTRIBUICAO_FOR | char(1) |  |  | Centro de distribuição |
| CONTRIBUINTE_CPRB_FOR | char(1) |  |  | Contribuinte da CPRB |
| PRODUTOR_RURAL_PF_FOR | char(1) |  |  | Produtor Rural Pessoa Física |
| PRODUTOR_RURAL_CPF_FOR | char(14) |  | S | Produtor Rural Pessoa Física - CPF |
| SEQUENCIAL_PAJ_FOR | integer(4) |  | S | Sequencial dos Processos Administrativos Judiciais |
| GUID_CONTABIL | uniqueidentifier(16) |  | S | Identificador Único do registro no banco do Contábil |
| GUID_ONVIO | uniqueidentifier(16) |  | S | Identificador Único do registro no banco do Atendimento Onvio |
| INSCRITO_PROGRAMA_REGULARIZACAO_TRIBUTARIA_RURAL_FOR | char(1) |  |  | Inscrito no Programa de Regularização Tributária Rural (PRR) |
| POSSUI_TRIBUTACAO_SOBRE_FOLHA_PAGAMENTO_FOR | char(1) |  |  | Possui tributação sobre a folha de pagamento |
| POSSUI_CONTRATO_FIDELIDADE | char(1) |  |  | Possui contrato de fidelidade |
| ISENCAO_IMUNIDADE | integer(4) |  |  | Isenção e Imunidade Opções Cadastro Fornecedor |
| CONTA_DEBITO_FOR | integer(4) |  | S | Conta débito |
| INFORMAR_CNPJ_PJ_BENEFICIARIA_RENDIMENTOS | char(1) |  |  | Informar CNPJ da PJ beneficiária dos rendimentos |
| CNPJ_PJ_BENEFICIARIA_RENDIMENTOS | char(14) |  | S | CNPJ da PJ beneficiária dos rendimentos |
| TIPO_BENEFICIARIO | char(1) |  | S | Tipo do beneficiário ( F-Pessoa Fisica ou J-Pessoa Juridica - Sit.fornec. exterior) |
| I_CNAE_FORTALEZA | char(15) |  | S | Código CNAE Fortaleza |
| DATA_ATUALIZACAO_REG_APURACAO_FOR | date(4) |  | S | Data de atualização do Regime de apuração |
| FORMA_ATUALIZACAO_REG_APURACAO_FOR | char(1) |  |  | Forma de atualização do Regime de apuração |
| SEGURADO_ESPECIAL_FOR | char(1) |  |  | Segurado Especial |
| DATA_NASCIMENTO | date(4) |  | S | Data de nascimento do fornecedor pessoa fisica (CPF) |
