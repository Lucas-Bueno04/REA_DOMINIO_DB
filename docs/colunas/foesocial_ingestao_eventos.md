# FOESOCIAL_INGESTAO_EVENTOS — Controle de eventos eSocial enviados para a API de ingestão (imediato e noturno)
3.521 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| GUID_EVENTO | uniqueidentifier(16) | PK |  | Identificador único do evento (eventId / UUID) |
| SEQUENCIAL | integer(4) |  |  | Ordem sequencial de criação do evento (FIFO da fila) |
| CODI_EMP | integer(4) |  |  | Código da empresa (accountingInfo.companyCode / agrupador noturno) |
| I_EMPREGADOS | integer(4) |  | S | Sequencial do empregado (join/dedup/arrependimento) |
| I_DADOS_EVENTOS | integer(4) |  | S | Vínculo com FOESOCIAL_DADOS_EVENTOS |
| TIPO_EVENTO | varchar(40) |  |  | eventType: ADMISSION_REGISTERED, TERMINATION_REGISTERED, ADMISSION_CANCELLED |
| MODO_ENVIO | smallint(2) |  |  | Janela de envio: 1 Imediato (/esocial-event) / 2 Noturno (/status) |
| DATA_EVENTO | date(4) |  | S | Data de referência do evento (dedup) |
| ORIGEM_VALIDACAO | smallint(2) |  | S | Origem do registro: 0 Sistema / 1 Importação de tabelas / 2 Importação de leiaute / 3 Conversão |
| ORIGEM_CARGA | smallint(2) |  |  | Origem do evento: 0 Incremental (trigger) / 1 Carga inicial (dia zero) |
| EMPRESA_TIPO_INSCRICAO | varchar(4) |  | S | hiringEntity.documentType (CNPJ/CPF) |
| EMPRESA_INSCRICAO | varchar(14) |  | S | hiringEntity.documentValue (inscrição da empresa) |
| EMPRESA_NOME | varchar(150) |  | S | hiringEntity.name (razão social) |
| EMPREGADO_CPF | varchar(11) |  | S | employee.documentValue (CPF; documentType fixo CPF) |
| EMPREGADO_NOME | varchar(120) |  | S | employee.name (nome do colaborador) |
| TIPO_COLABORADOR | varchar(15) |  | S | employee.employeeType: EMPREGADO/ESTAGIARIO/CONTRIBUINTE |
| NUMERO_RECIBO | varchar(40) |  | S | additionalData.receiptNumber (recibo eSocial) |
| DATA_ADMISSAO | date(4) |  | S | additionalData.admissionDate |
| SALARIO_CONTRATUAL | numeric(15) |  | S | additionalData.contractualSalary (salário/bolsa/pró-labore) |
| MOTIVO_ESOCIAL_CODIGO | smallint(2) |  | S | Código do motivo eSocial (Tabela 19 - auditoria; exceção motivo 6/27) |
| MOTIVO_ESOCIAL_TEXTO | varchar(200) |  | S | additionalData.eSocialReason (texto descritivo do motivo) |
| DATA_DEMISSAO | date(4) |  | S | additionalData.terminationDate (Demitido em) |
| TIPO_AVISO_PREVIO | varchar(20) |  | S | additionalData.noticePeriodType: TRABALHADO/INDENIZADO/AUSENCIA_DISPENSA |
| DATA_PAGAMENTO | date(4) |  | S | additionalData.paymentDate |
| DATA_REGISTRO_RESCISAO | timestamp(8) |  | S | additionalData.systemRegistrationDate (data de registro da rescisão no sistema) |
| ESOCIAL_EMPLOYMENT_STATUS | varchar(20) |  | S | statuses.esocialEmploymentStatus (ACTIVE/TERMINATED) |
| TR_EMPLOYMENT_STATUS | varchar(25) |  | S | statuses.trEmploymentStatus (ACTIVE/NOTICE_PERIOD/TERMINATION_REGISTERED) |
| TR_STATUS | varchar(15) |  | S | statuses.trStatus (WORKING/ON_LEAVE) |
| SITUACAO_ENVIO | smallint(2) |  |  | Situação: 0 Pendente / 1 Enviado / 2 Erro / 3 Retido (aguarda S-3000) / 4 Cancelado (arrependimento) |
| TENTATIVAS | integer(4) |  |  | Número de tentativas de envio do evento |
| DATA_HORA_PROXIMA_TENTATIVA | timestamp(8) |  | S | Data/Hora da próxima tentativa de envio (backoff) |
| STATUS_ENVIO | integer(4) |  | S | último status HTTP retornado pela API |
| MENSAGEM_ERRO | varchar(2048) |  | S | Mensagem de erro da última tentativa |
| DATA_CRIACAO | timestamp(8) |  | S | Data/Hora de criação do registro |
| DATA_ENVIO | timestamp(8) |  | S | Data/Hora do último envio com sucesso |
