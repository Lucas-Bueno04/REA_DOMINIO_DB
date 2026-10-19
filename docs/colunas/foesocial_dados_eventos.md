# FOESOCIAL_DADOS_EVENTOS — Dados dos eventos para envio ao eSocial.
912.947 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_DADOS_EVENTOS | integer(4) | PK |  | Código do registro de envio. |
| I_LOTE | integer(4) |  |  | Código do lote. |
| CODIGO_ESOCIAL | varchar(30) |  |  | Código do eSocial |
| I_EVENTO_ESOCIAL | integer(4) |  |  | Código do evento do eSocial. |
| TIPO_ENVIO | smallint(2) |  |  | Tipo de envio. (1=Inclusão/2=Alteração/3=Exclusão/4=Retificação) |
| TABELA_DADOS | varchar(128) |  |  | Nome da tabela de dados que gerou o registro. |
| CHAVE_TABELA_DADOS | varchar(256) |  |  | Chave do registro da tabela de dados. |
| ID | varchar(70) |  |  | ID de envio ao eSocial. |
| XML_EVENTO | long varchar(32767) |  | S | XML do evento. |
| NUMERO_RECIBO | varchar(50) |  | S | Número do recibo. |
| I_RESPOSTA | integer(4) |  | S | Código da resposta para o evento. |
| DESCRICAO_RESPOSTA | varchar(1000) |  | S | Descrição da resposta para o evento. |
| VALIDADO | smallint(2) |  |  | Evento validado. (0=Não/1=Sim) |
| AGUARDANDO_AJUSTE | smallint(2) |  |  | Quando invalidado, indica se o evento necessita de ajuste antes de ser reenviado. (0=Não/1=Sim) |
| DATA_HORA_CONCLUSAO | timestamp(8) |  | S | Data/hora da conclusão do evento. |
| NOME_ARQUIVO | varchar(128) |  | S | Nome do arquivo a ser exportado, coluna criada para GT/Suporte |
| DATA_ALTERACAO | date(4) |  | S | Preencher com a data de alteração quando for um evento de alteração. Exemplo: 2205, 2206, 2306. |
| I_EVENTO_ESOCIAL_EXCLUIDO | integer(4) |  | S | Código evento esocial excluido no evento 3000. |
| NUMERO_RECIBO_EXCLUIDO | varchar(50) |  | S | Numero do recibo excluido no evento 3000. |
| CODI_EMP_EVENTO_RETIFICADO | integer(4) |  | S | Empresa do evento esocial que esta sendo retificado. |
| I_DADOS_EVENTOS_EVENTO_RETIFICADO | integer(4) |  | S | Codigo sequencial do evento esocial que esta sendo retificado. |
| COMPETENCIA_CALCULO | date(4) |  | S | Competência para gerar os dados do cálculo. |
| GERAR_REMUNERACAO_13_SALARIO | smallint(2) |  |  | Gerar os dados do evento. |
| I_RESPONSAVEL | integer(4) |  | S | Responsável pelo envio do fechamento. |
| EXISTE_MOVIMENTACAO_PERIODO | smallint(2) |  |  | Existe movimentação no período. (0=Não/1=Sim) |
| I_SERVICOS | integer(4) |  | S | Código do serviço. |
| TIPO_VALIDACAO | smallint(2) |  |  | Tipo de validação. (1=Sistema/2=Manual/3=Conversão/4=Importação) |
| XML_ALTERADO | smallint(2) |  |  | Indica se o XML foi alterado pelo usuario. 0=Nao/1=Sim |
| MOSTRAR_PAINEL_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| NIS_EMPREGADO | char(11) |  | S | Numero do NIS do empregado no momento do envio para o eSocial. |
| DATA_CRIACAO_REGISTRO | timestamp(8) |  | S | Data de inserção do registro no banco de dados. |
| DATA_ALTERACAO_REGISTRO | timestamp(8) |  | S | Data da última alteração do registro no banco de dados. |
| DATA_PROCESSAMENTO_REGISTRO | timestamp(8) |  | S | Data de processamento do registro. |
| VERSAO_SISTEMA | varchar(50) |  | S | Versão do sistema no momento da inserção/alteração do registro. |
| INCLUSAO_DUPLICADA | smallint(2) |  |  | Registro duplicado (retorno 537) |
| COMPETENCIA_REENVIAR_CALCULO_APOS_VALIDACAO | date(4) |  | S | Competência pra reenviar os eventos 1200 e 1210 após validação desse evento. |
| XSD_VALIDADO | smallint(2) |  |  | XSD validado (0)-Não (1)-Sim |
| INICIO_AFASTAMENTO | smallint(2) |  |  | Inclusão do afastamento no evento S-2230. (0=Não/1=Sim) |
| FIM_AFASTAMENTO | smallint(2) |  |  | Fim do afastamento no evento S-2230. (0=Não/1=Sim) |
| REENVIAR | smallint(2) |  |  | Evento marcado para reenviar. (0=Não/1=Sim) |
| GERAR_LIMPEZA_DADOS_ESOCIAL | smallint(2) |  |  | Gerar limpeza de dados no eSocial. |
| COMPETENCIA_INICIO_VALIDADE | date(4) |  | S | Competencia da tag iniValid dos eventos de tabelas |
| UTILITARIO_CONVERSAO_REGISTROS_ENVIADOS_OUTRO_BANCO | smallint(2) |  |  | Identifica se o registro de fila foi gerado pelo utilitário de conversão de outros bancos. (0=Não/1=Sim) |
| CODIGO_PROCESSO_AUDITOR | integer(4) |  | S | Código do processo da auditoria. |
| CANCELAMENTO_AVISO_PREVIO | smallint(2) |  |  | Cancelamento de aviso prévio do evento 2250. (0=Não/1=Sim) |
| ID_DUPLICADO_ALTERADO | smallint(2) |  |  | ID estava duplicado no banco de dados e foi alterado para a criação do índice único na tabela. |
| ADVERTENCIA_AJUSTADA | smallint(2) |  |  | Registro validado com advertência ajustado pelo usuário. (0=Não/1=Sim) |
| POSSUI_VERBAS_RESCISORIAS_PERIODO | smallint(2) |  |  | Possui verbas rescisórias (tag verbasResc) no S-2299/S-2399. |
| EMPRESA_RESPONSAVEL | integer(4) |  | S | Código da empresa que o responsavel esta vinculado |
| VERSAO_LEIAUTE | varchar(12) |  | S | Versão do leiaute do eSocial que foi gerado o evento. |
| ADMISSAO_TSVE_COM_MATRICULA | smallint(2) |  |  | Evento de admissão trabalhador sem vinculo com matricula . |
| EXISTE_ENVIO_AQUISICAO_RURAL | smallint(2) |  |  | Empregado possui evento de aquisição rural enviado na competência do evento S-1299. |
| EFETUAR_TRANSMISSAO_IMEDIATA_DCTFWEB | smallint(2) |  |  | Efetuar a transmissão imediata da DCTF no 1299 para MEI. |
| EXISTE_ENVIO_TREINAMENTOS | smallint(2) |  |  | Existe envio de treinamentos. (0=Não/1=Sim) |
| NUMERO_RECIBO_RETIFICACAO | varchar(40) |  | S | Número do recibo de retificação invalidados. |
| REENVIAR_INVALIDADO | smallint(2) |  | S | Reenviar um evento invalidado |
| REENVIAR_EVENTO_AUTOMATICAMENTE | smallint(2) |  |  | Reenviar o evento automaticamente. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| DATA_EFEITO | date(4) |  | S | Data de efeito da alteração contratual retroativa |
| CODIGO_COLABORADOR | integer(4) |  | S | Código do colaborador |
| ENVIO_FORCADO_ANTES_INICIO_ESOCIAL | smallint(2) |  |  | Enviar o evento antes do início do eSocial. (0=Não/1=Reclamatória) |
| POSSUI_GRUPO_INFO_IR_COMPLEMEM_S_1210_ANT | bit(1) |  |  | Indica se o evento S-1210 possui o grupo infoIRComplem. (0=Não/1=Sim) |
