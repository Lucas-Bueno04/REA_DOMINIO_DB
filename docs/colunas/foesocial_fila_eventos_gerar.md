# FOESOCIAL_FILA_EVENTOS_GERAR — Fila de eventos para gerar o XML do eSocial.
24.762 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EVENTO_ESOCIAL | integer(4) | PK |  | Código do evento do eSocial. |
| SEQUENCIAL | integer(4) | PK |  | Sequencial. |
| STATUS | smallint(2) |  |  | Status. (1=Pendente/2=Em processamento/3=Concluído/4=Em espera) |
| GERAR_EVENTO_EXCLUSAO | smallint(2) |  |  | Gerar evento de exclusão. |
| CADASTRAMENTO_INICIAL | smallint(2) |  |  | Cadastramento inicial. (0=Não/1=Sim) |
| DATA_EXECUCAO_EVENTO | date(4) |  |  | Preencher com a data que o evento deve ser executado, para casos como o aviso prévio que pode ser cadastrado em data futura, mas não pode ser enviado em data futura. |
| COMPETENCIA_CALCULO | date(4) |  | S | Competência para gerar os dados do cálculo. |
| GERAR_REMUNERACAO_13_SALARIO | smallint(2) |  |  | Gerar os dados do evento. |
| I_RESPONSAVEL | integer(4) |  | S | Responsável pelo envio do fechamento. |
| EXISTE_MOVIMENTACAO_PERIODO | smallint(2) |  |  | Existe movimentação no período. (0=Não/1=Sim) |
| DATA_CRIACAO_REGISTRO | timestamp(8) |  | S | Data de inserção do registro no banco de dados. |
| DATA_ALTERACAO_REGISTRO | timestamp(8) |  | S | Data da última alteração do registro no banco de dados. |
| DATA_PROCESSAMENTO_REGISTRO | timestamp(8) |  | S | Data de processamento do registro. |
| VERSAO_SISTEMA | varchar(50) |  | S | Versão do sistema no momento da inserção/alteração do registro. |
| COMPETENCIA_REENVIAR_CALCULO_APOS_VALIDACAO | date(4) |  | S | Competência pra reenviar os eventos 1200 e 1210 após validação dos eventos criados nessa fila. |
| GERAR_LIMPEZA_DADOS_ESOCIAL | smallint(2) |  |  | Gerar limpeza de dados no eSocial. |
| EXISTE_ENVIO_AQUISICAO_RURAL | smallint(2) |  |  | Existe envio de aquisição rural no período. (0=Não/1=Sim) |
| EXISTE_ENVIO_COMERCIALIZACAO_RURAL | smallint(2) |  |  | Existe envio de comercialização rural no período. (0=Não/1=Sim) |
| UTILITARIO_CONVERSAO_REGISTROS_ENVIADOS_OUTRO_BANCO | smallint(2) |  |  | Identifica se o registro de fila foi gerado pelo utilitário de conversão de outros bancos. (0=Não/1=Sim) |
| I_CONEXAO | integer(4) |  | S | Número da conexão que está processando a fila na thread. |
| ATUALIZAR_HISTORICO_CONTRATUAL | integer(4) |  | S | Atualizar o historico contratual dos empregados na data da execucao |
| EXISTE_ENVIO_REMUNERACAO | smallint(2) |  |  | Existe envio de remuneracao no período. (0=Não/1=Sim) |
| EXISTE_ENVIO_PAGAMENTO | smallint(2) |  |  | Existe envio de pagamento no período. (0=Não/1=Sim) |
| EXISTE_ENVIO_CONTRATACAO_TRABALHADORES_AVULSOS_NAO_PORTUARIOS | smallint(2) |  |  | Existe envio de contratação de trabalhadores avulsos não portuários no período. (0=Não/1=Sim) |
| EMPRESA_ENVIO_FECHAMENTO_S_1299 | integer(4) |  | S | Código da empresa que sera enviado o evento S-1299 |
| EFETUAR_TRANSMISSAO_IMEDIATA_DCTFWEB | smallint(2) |  |  | Efetuar a transmissão imediata da DCTF no 1299 para MEI. |
| REENVIAR_EVENTO_AUTOMATICAMENTE | smallint(2) |  |  | Reenviar o evento automaticamente. (0=Não/1=Sim) |
| ENVIO_FORCADO_ANTES_INICIO_ESOCIAL | smallint(2) |  |  | Enviar o evento antes do início do eSocial. (0=Não/1=Reclamatória) |
| EXISTE_SELECAO_EVENTO | smallint(2) |  |  | Evento com seleção(0=Não/1=Sim |
| I_EVENTO_ESOCIAL_EXCLUIDO_S_3000 | integer(4) |  | S | Evento excluido |
| GERAR_RETIFICACAO_INFO_IR_COMPLEMEM_S_1210_ANT | bit(1) |  |  | Indica que o S-1210 tem retificação para ser feita. (0=Não/1=Sim) |
