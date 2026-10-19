# GERAEXECUTAR — EXECUÇÃO DE ROTINAS AUTOMÁTICAS
501 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_EXECUTARRA | integer(4) | PK |  | CÓDIGO DA EXECUÇÃO |
| I_SISTEMA | smallint(2) | PK |  | CÓDIGO DO SISTEMA |
| I_SECUSUARIOS | integer(4) |  |  | CÓDIGO DO USUÁRIO |
| DESCRICAO | char(60) |  |  | DESCRIÇÃO DA EXECUÇÃO |
| PERIODICIDADE | smallint(2) |  |  | PERIODICIDADE DO AGENDAMENTO (0-NA/1-MENSAL/2-DATA/3-ANUAL/4-QUINZE/5-DECENDE/6-SEMANA/7-DIARIO/8-CALCULO FÉRIAS PROGRAMADAS/9-TRIMESTRAL) |
| AGENDAMENTO_DIA | smallint(2) |  | S | DIA AGENDADO |
| AGENDAMENTO_HORA | time(8) |  | S | HORA AGENDADA |
| AGENDAMENTO_DATA | date(4) |  | S | DATA AGENDADA |
| AGENDAMENTO_APARTIR_DE | date(4) |  | S | COMPETÊNCIA INICIAL |
| AGENDAMENTO_COMP | smallint(2) |  |  | COMPETÊNCIA AGENDADA |
| EMAIL_SUCESSO | smallint(2) |  |  | ENVIA EMAIL EM CASO DE SUCESSO |
| EMAIL_ERRO | smallint(2) |  |  | ENVIA EMAIL EM CASO DE ERRO |
| EMAIL_END_PARA | varchar(128) |  | S | ENDEREÇO DO EMAIL |
| EMAIL_END_CC | varchar(128) |  | S | ENDEREÇO PARA CÓPIA DO EMAIL |
| ULTIMA_EXECUCAO | date(4) |  | S | DATA DA ÚLTIMA EXECUÇÃO |
| NOTIFICADO | smallint(2) |  |  | EXIBIDA NOTIFICAÇÃO DE NÃO EXECUÇÃO |
| GERAR_RELATORIOS_INDIVIDUALIZADOS_EMPRESA | smallint(2) |  |  | Gerar os relatórios individualizados por empresa. (0=Não/1=Sim) |
| AGENDAMENTO_ANO_HORA | time(8) |  | S | Ano - Hora Agendada |
| AGENDAMENTO_ANO_APARTIR_DE | integer(4) |  | S | Ano - Competência Inicial |
| AGENDAMENTO_ANO_DIA | integer(4) |  | S | Ano - Dia Agendado |
| AGENDAMENTO_ANO_MES | integer(4) |  | S | Ano - Mês Agendado |
| AGENDAMENTO_MES | integer(4) |  | S | Mês - Agendado |
| QUANTIDADE_DIAS_ANTERIORES_FERIAS_PROGRAMADA | integer(4) |  | S | Quantidade de dias anteriores ao gozo programado |
| EMPRESA_FILTRAR_ATIVAS | smallint(2) |  |  | Empresa - Filtrar apenas ativas |
| INIBIR_MENSAGENS_ERROS_OU_AVISOS_DURANTE_EXECUCAO | smallint(2) |  |  | Inibir as mensagens de erros e avisos durante a execução das rotinas automáticas |
| PASTA_DESTINO_SALVA_RELATORIO_ERROS_OU_AVISOS | varchar(255) |  | S | Pasta de destino para salvar relatório de erros e avisos |
| QUANTIDADE_DIAS_APOS_DATA_RESCISAO | integer(4) |  | S | Quantidade de dias após a data de Rescisão |
| EXECUTAR_ROTINA_SOMENTE_USUARIO_RESPONSAVEL | smallint(2) |  |  | Excutar estas rotinas somente pelo usuário responsável |
| TIPO_ROTINA | integer(4) |  | S | Tipo de Rotina, 0 - rotina cliente, 1 - rotina interna |
| EXECUTAR_EM_SEGUNDO_PLANO | bit(1) |  |  | Indica se a rotina deve ser executada em segundo plano. |
| MENSAGEM | long varchar(32767) |  | S | Informações para o usuário, como mensagens de erro. |
| ESTADO_EXECUCAO | smallint(2) |  | S | Indica em qual estado se encontra a execução da Rotina (-1=Erro/0=Aguardando/1=EmProcessamento/2=Processada) |
| DATA_INICIO_EXECUCAO | timestamp(8) |  | S | Indica a data em que se iníciou a execucão da Rotina. |
| DATA_TERMINO_EXECUCAO | timestamp(8) |  | S | Indica a data em que se finalizou a execucão da Rotina. |
| GUID_EXECUCAO | uniqueidentifier(16) |  | S | GUID do Agendamento no Orquestrador |
| KEEPALIVE | timestamp(8) |  | S | Timestamp de keepalive atualizado periodicamente durante a execucao. Usado pelo monitoramento externo para detectar processos travados. |
| STATUS_DOWNLOAD | smallint(2) |  | S | Status do download do arquivo gerado pela rotina (0=N/A, 1=Pronto para download, 2=Realizando download, 3=Download realizado, 4=Concluido sem download, 5=Erro ao realizar download) |
| DATA_DOWNLOAD | timestamp(8) |  | S | Data e hora em que o download dos arquivos foi realizado pelo usuario. |
| OBSERVACAO_REPROCESSAMENTO | varchar(255) |  | S | Observacao de falha transitoria durante a execucao da rotina, indicando que sera realizado reprocessamento automatico. |
| TENTATIVAS_EXECUCAO | smallint(2) |  | S | Contador de tentativas de execucao da rotina. Maximo de 3 tentativas para erros transitorios. |
| VISUALIZADO | bit(1) |  |  | Indica se a rotina processada com sucesso foi visualizada pelo usuario no Painel de Acompanhamento. |
| PASTA_DESTINO_SALVAR_RELATORIO | varchar(255) |  | S | Caminho de destino para salvamento automatico de relatorios em PDF durante execucao de rotinas automaticas. |
