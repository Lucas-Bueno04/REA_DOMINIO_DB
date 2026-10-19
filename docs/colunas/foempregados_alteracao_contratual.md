# FOEMPREGADOS_ALTERACAO_CONTRATUAL — Registros de alteração cadastral para envio ao eSocial.
33.276 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| DATA_ALTERACAO | date(4) | PK |  | Data da alteração. |
| I_SERVICOS | integer(4) |  | S | Código do serviço. |
| I_CARGOS | integer(4) |  | S | Código do cargo. |
| I_SINDICATOS | integer(4) |  | S | Código da convenção coletiva |
| CATEGORIA | smallint(2) |  | S | Categoria. |
| VINCULO | smallint(2) |  | S | Vínculo empregatício. |
| TIPO_HORARIO | smallint(2) |  | S | Tipo de horário. |
| SALARIO | numeric(30) |  | S | Salário. |
| I_REMUNERACAO_VARIAVEL | integer(4) |  | S | Código da remuneração variável. |
| I_LOCAL_TRABALHO | integer(4) |  | S | Código do local de trabalho. |
| HORAS_SEMANA | numeric(5) |  | S | Total de horas trabalhadas por semana. |
| CARGA_HORARIA_VARIAVEL | smallint(2) |  | S | Carga horário variável. (0=Não/1=Sim) |
| I_JORNADA | integer(4) |  | S | Código da jornada. |
| SINDICALIZADO | smallint(2) |  | S | Sindicalizado. (0=Não/1=Sim) |
| I_FUNCAO | integer(4) |  | S | Código da função. |
| ALVARA_JUDICIAL | smallint(2) |  | S | Possui alvará judicial. (0=Não/1=Sim) |
| I_PROCESSO_ALVARA_JUDICIAL | integer(4) |  | S | Código do processo do alvará judicial. |
| I_SUPERVISOR_ESTAGIO | integer(4) |  | S | Código do Supervisor do estágio |
| I_AGENTE_INTEGRACAO | integer(4) |  | S | Código do agente de integração |
| I_INSTITUICAO_ENSINO | integer(4) |  | S | Código da instituição de ensino |
| NATUREZA_ESTAGIO | smallint(2) |  | S | Natureza de estágio (0=Não obrigatório/1=Obrigatório) |
| NIVEL_ESTAGIO | smallint(2) |  | S | Nível do estágio |
| AREA_ATUACAO_ESTAGIARIO | char(100) |  | S | Área de atuação do estagiário |
| APOLICE_SEGURO_ESTAGIARIO | varchar(30) |  | S | Apólice seguro do estagiário |
| QUANTIDADE_DIAS_CONTRATO_PRAZO_DETERMINADO | integer(4) |  | S | Quantidade de dias de contrato de prazo determinado |
| DATA_INICIO_CONTRATO_PRAZO_DETERMINADO | date(4) |  | S | Data de início do contrato por prazo determinado |
| DATA_FIM_CONTRATO_PRAZO_DETERMINADO | date(4) |  | S | Data fim do contrato por prazo determinado. |
| QUANTIDADE_DIAS_PRORROGACAO_CONTRATO_PRAZO_DETERMINADO | integer(4) |  | S | Quantidade de dias da prorrogação do contrato de prazo determinado |
| DATA_FIM_PRORROGACAO_CONTRATO_PRAZO_DETERMINADO | date(4) |  | S | Data final da prorrogação do contrato de prazo determinado |
| MOTIVO_PRORROGACAO_CONTRATO_PRAZO_DETERMINADO | varchar(50) |  | S | Motivo da prorrogação do contrato de prazo determinado |
| TIPO_CONTRIBUINTE | char(1) |  | S | Tipo contribuinte |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes, 4-Importação eSocial |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| DESCRICAO_INDICATIVO_OBJETO_DETERMINANTE_CONTRATACAO_PRAZO_DETERMINADO | varchar(255) |  | S | Indicativo do objeto determinante da contratação por prazo determinado - Contrato experiência |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| NUMERO_RECIBO_ESOCIAL_VALIDACAO_AUTOMATICA | varchar(50) |  | S | Numero do recibo importado do eSocial |
| ID_ESOCIAL_VALIDACAO_AUTOMATICA | varchar(70) |  | S | ID do evento importado do eSocial |
| NUMERO_PROCESSO | varchar(20) |  | S | Numero do processo - menor de 16 anos. |
| ENVIAR_ESOCIAL_PERIODO_ANTERIOR_INICIO_BANCO_CONTABIL | smallint(2) |  | S | Enviar evento eSocial anterior ao início da utilização do banco de dados (0=Não/1=Sim) |
| CATEGORIA_ESOCIAL_EMPREGADO | integer(4) |  | S | Categoria eSocial do Empregado. |
| MODALIDADE_CONTRATACAO | integer(4) |  | S | Modalidade da Contratação. |
| CNPJ_ENTIDADE_QUALIFICADORA | varchar(14) |  | S | CNPJ da Entidade Qualificadora. |
| CNPJ_ESTABELECIMENTO_ATIVIDADE_PRATICA | varchar(14) |  | S | CNPJ do Estabelecimento da atividade pratica. |
| ESTABELECIMENTO_CONTRATACAO_INDIRETA | varchar(50) |  | S | Estabelecimento de Contratação Indireta |
| ENVIAR_ESOCIAL_MANUALMENTE | integer(4) |  |  | Enviar eSocial Manualmente |
| I_SINDICATOS_CADASTRO | integer(4) |  | S | Código do cadastro do sindicato |
