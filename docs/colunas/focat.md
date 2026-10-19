# FOCAT — Comunicação de Acidente do trabalho - CAT
10 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| I_CAT | integer(4) | PK |  | Código da CAT |
| DATA_CAT | date(4) |  |  | Data da CAT |
| NUMERO | char(13) |  | S | Número da CAT |
| EMITENTE | smallint(2) |  |  | Emitente: (1=Empregador/2=Sindicato/3=Médico/4=Empregado/5=Autoridade pública/6=Cooperativa/7=Sindicato de trabalhadores avulsos não portuários/8=Órgão gestor de mão de obra/9=Dependente do emrpegado/10=Empregador doméstico) |
| TIPO_CAT | smallint(2) |  |  | Tipo da CAT: (1=Inicial/2=Reabertura/3=Comunicação de óbito) |
| DATA_OBITO | date(4) |  | S | Data do óbito |
| DATA_ACIDENTE | date(4) |  |  | Data do acidente |
| TIPO_ACIDENTE | smallint(2) |  |  | /** SEM USO **/ |
| HORA_ACIDENTE | time(8) |  | S | Hora do acidente |
| HORAS_ACIDENTE_APOS_TRABALHO | time(8) |  | S | Horas após o acidente de trabalho |
| HOUVE_AFASTAMENTO | smallint(2) |  |  | Houve afastamento: (0=Não/1=Sim) |
| ULTIMO_DIA_TRABALHADO | date(4) |  | S | Data do último dia trabalhado |
| LOCAL_ACIDENTE | smallint(2) |  |  | Local do acidente: (1=Estabelecimento da empregadora/2=Empresa onde a empregadora presta serviço/3=Via pública/4=Área rural/5=Outros/6=Embarcação) |
| TIPO_INSCRICAO | smallint(2) |  | S | Tipo de inscrição (1=CNPJ/2=CPF/3=CEI/6=CAEPF/7=CNO). |
| INSCRICAO | char(14) |  | S | Inscrição |
| ESPECIFICACAO_LOCAL | varchar(80) |  | S | Especificação do local |
| MUNICIPIO | integer(4) |  | S | Código do município |
| HOUVE_REGISTRO_POLICIAL | smallint(2) |  |  | Houve registro policial: (0=Não/1=Sim) |
| HOUVE_MORTE | smallint(2) |  |  | Houve morte: (0=Não/1=Sim) |
| PARTES_CORPO_ATINGIDAS | char(30) |  | S | Partes do corpo atingidas |
| AGENTE_CAUSADOR | char(30) |  | S | Agente causador |
| DESCRICAO_SITUACAO_CAUSADORA | char(250) |  | S | Descrição da situação geradora do acidente ou doença |
| OBSERVACAO_CAT | varchar(32000) |  | S | Observações |
| UNIDADE_ATENDIMENTO | char(40) |  | S | Unidade de atendimento |
| DATA_HORA_ATESTADO | timestamp(8) |  | S | Data e hora do atestado |
| HOUVE_INTERNACAO | smallint(2) |  |  | Houve internação: (1=Não informado/2=Não/3=Sim) |
| DIAS_TRATAMENTO | integer(4) |  | S | Dias de tratamento |
| DEVE_AFASTAR_TRABALHO_TRATAMENTO | smallint(2) |  |  | Deverá afastar-se do trabalho durante o tratamento: (1=Não informado/2=Não/3=Sim) |
| CODIGO_DOENCA | char(10) |  | S | Código da doença (CID) |
| DESCRICAO_LESAO | char(380) |  | S | Descrição e natureza da lesão |
| DIAGNOSTICO_PROVAVEL | varchar(100) |  | S | Diagnóstico provável |
| OBSERVACAO_ATESTATO | char(550) |  | S | Observações do atestado |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro: (0=Sistema/1=Importação de tabelas/2=Importação de leiaute/3=Conversão) |
| CAT_PARCIAL | smallint(2) |  |  | **SEM USO** |
| DATA_CAT_ORIGEM | date(4) |  | S | **SEM USO** |
| NUMERO_ENDERECO | varchar(10) |  | S | Número do endereço do acidente/doença. |
| CODIGO_SITUACAO_GERADORA | varchar(10) |  | S | Código da situação geradora. |
| CODIGO_PARTE_CORPO_ATINGIDA | varchar(10) |  | S | Código da parte do corpo atingida. |
| CODIGO_AGENTE_CAUSADOR | varchar(10) |  | S | Código do agente causador. |
| CODIGO_CNES | varchar(7) |  | S | Código CNES. |
| NOME_MEDICO | varchar(80) |  | S | /** SEM USO **/ |
| NUMERO_ORGAO_CLASSE | varchar(14) |  | S | /** SEM USO **/ |
| UF_ATESTADO_MEDICO | integer(4) |  | S | /** SEM USO **/ |
| ENDERECO | varchar(80) |  | S | Endereço do local do acidente. |
| INICIATIVA_EMISSAO | smallint(2) |  | S | Iniciativa da emissão. (1=Iniciativa do empregador/2=Ordem judicial/3=Determinação de orgão fiscalizador) |
| TIPO_INSCRICAO_EMITENTE | smallint(2) |  | S | Tipo de inscrição do emitente. (1=CPF/2=CNPJ) |
| INSCRICAO_EMITENTE | varchar(14) |  | S | Inscrição do emitente. |
| ORGAO_CLASSE_ATESTADO_MEDICO | smallint(2) |  | S | /** SEM USO **/ |
| CODIGO_NATUREZA_LESAO | varchar(10) |  | S | Código da natureza da lesão. |
| I_MEDICOS | integer(4) |  | S | Código do médico/dentista. |
| CODIGO_PAIS | integer(4) |  | S | Código do país. |
| CODIGO_POSTAL | varchar(10) |  | S | Código postal. |
| CODIGO_TIPO_ACIDENTE | varchar(10) |  |  | Código do tipo de acidente. |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| ORIGEM_NO_BANCO_DADOS | smallint(2) |  |  | CAT origem no banco de dados. (0=Não/1=Sim) |
| CODI_EMP_CAT_ORIGEM_REABERTURA | integer(4) |  | S | Código da CAT origem. |
| I_EMPREGADOS_CAT_ORIGEM_REABERTURA | integer(4) |  | S | Código da CAT origem. |
| I_CAT_ORIGEM_REABERTURA | integer(4) |  | S | Código da CAT origem. |
| RECIBO_ESOCIAL_CAT_ORIGEM_NO_BANCO_DADOS | varchar(40) |  | S | Recibo do eSocial da CAT origem no banco de dados. (0=Não/1=Sim) |
| DATA_MORTE | date(4) |  | S | Data da morte. |
| TIPO_ENDERECO | integer(4) |  | S | Tipo de endereço. |
| CEP | varchar(8) |  | S | CEP do endereço. |
| BAIRRO | varchar(80) |  | S | Bairro do endereço. |
| COMPLEMENTO | varchar(80) |  | S | Bairro do endereço. |
| ENVIAR_ESOCIAL_PERIODO_ANTERIOR_INICIO_BANCO_CONTABIL | smallint(2) |  | S | Enviar evento eSocial anterior ao início da utilização do banco de dados (0=Não/1=Sim) |
