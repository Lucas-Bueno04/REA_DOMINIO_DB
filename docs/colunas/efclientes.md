# efclientes — Clientes - Cadastro
689.035 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_cli | integer(4) | PK |  | Codigo |
| sigl_est | char(2) |  |  | Estado |
| codi_cta | integer(4) |  | S | Conta contabil |
| codm_cli | integer(4) |  | S | Codigo do Municipio |
| nomr_cli | char(40) |  | S | Nome |
| nome_cli | char(150) |  |  | Razao Social |
| ende_cli | char(40) |  | S | Endereco |
| nume_cli | integer(4) |  | S | Numero |
| cida_cli | char(30) |  | S | Cidade |
| cepe_cli | char(8) |  | S | CEP |
| cgce_cli | char(14) |  | S | CNPJ |
| insc_cli | char(20) |  | S | Inscricao estadual |
| fone_cli | char(14) |  | S | Fone |
| faxe_cli | char(14) |  | S | Fax |
| agro_cli | char(1) |  | S | Cliente agropecuario (S/N) |
| icms_cli | char(1) |  | S | Contribuinte de ICMS (S/N) |
| tins_cli | integer(4) |  | S | TIPO DA INSCRICAO (1 - CNPJ/2 - CPF/3 - CEI/6 - CAEPF) |
| dddf_cli | integer(4) |  | S | DDD |
| aliq_cli | numeric(5) |  | S | Aliquota alternativa do cliente |
| imun_cli | char(20) |  | S | Inscricao Municipal |
| bair_cli | char(60) |  | S | Bairro |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes, 4 - Iceberg |
| categoria_estabel_cli | char(3) |  | S | Categoria do Estabelecimento |
| regime_cli | char(1) |  |  | REGIME DE APURACAO (N - NORMAL/M- ME - SIMPLES NACIONAL/E - EPP - SIMPLES NACIONAL/O - OUTROS/U - IMUNE/I - ISENTA) |
| orgao_pub_federal_cli | char(1) |  | S | Natureza jurídica |
| codigo_pais | integer(4) |  |  | Codigo do pais |
| codigo_municipio | integer(4) |  | S | Codigo do municipio |
| insc_suframa | char(9) |  | S | Numero de inscricao na Suframa |
| complemento_cli | char(40) |  | S | Complemento do endereco |
| CADASTRO_CLI | date(4) |  | S | Data do cadastro do cliente |
| CONTA_FORNECEDOR_CLI | integer(4) |  | S | Conta contabil do fornecedor |
| TIPO_ASSINANTE_CLI | integer(4) |  | S | Tipo de assinante utilizado na última nota lançada |
| POSSUI_INTERDEPENDENCIA_CLI | char(1) |  | S | Interdependência com a empresa(S/N) |
| IESTST_CLI | char(22) |  | S | Inscricao Estadual ST |
| AGENTE_REGULADO_CLI | char(1) |  |  | Agente Regulado |
| CODIGO_INSTALACAO_CLI | varchar(7) |  |  | Código Instalação |
| PARTICIPANTE_FOME_ZERO | char(1) |  |  | Participante do Fome Zero |
| I_CNAE20 | char(15) |  | S | Codigo CNAE 20 |
| PERCENTUAL_CARGA_MEDIA | numeric(5) |  |  | Percentual Carga Média |
| VAREJISTA_OU_CONSUMIDOR_FINAL_CLI | char(1) |  |  | Varejista ou consumidor final |
| CONTA_COMPENSACAO_CLI | integer(4) |  | S | Conta compensação |
| CENTRO_DISTRIBUICAO_CLI | char(1) |  |  | Centro de distribuição |
| INSCRITO_PROGRAMA_AQUISICAO_ALIMENTOS_CLI | char(1) |  |  | Inscrito no Programa de Aquisição de Alimentos |
| PRODUTOR_RURAL_PF_CLI | char(1) |  |  | Produtor Rural Pessoa Física |
| PRODUTOR_RURAL_CPF_CLI | char(14) |  | S | Produtor Rural Pessoa Física - CPF |
| GUID_CONTABIL | uniqueidentifier(16) |  | S | Identificador Único do registro no banco do Contábil |
| GUID_ONVIO | uniqueidentifier(16) |  | S | Identificador Único do registro no banco do Atendimento Onvio |
| SEQUENCIAL_PAJ_CLI | integer(4) |  | S | Sequencial dos Processos Administrativos Judiciais |
| INFORMA_CNPJ_FONTE_PAG_RET | char(1) |  |  | Informar CNPJ da fonte pagadora da retenção |
| INFORMA_CNPJ_FONTE_PAG_RET_CNPJ | char(14) |  | S | Informar CNPJ da fonte pagadora da retenção - CNPJ |
| DATA_ATUALIZACAO_REG_APURACAO_CLI | date(4) |  | S | Data de atualização do Regime de apuração |
| FORMA_ATUALIZACAO_REG_APURACAO_CLI | char(1) |  |  | Forma de atualização do Regime de apuração |
| IBS_CBS_CLI | char(1) |  |  | Contribuinte IBS/CBS (S, N) |
