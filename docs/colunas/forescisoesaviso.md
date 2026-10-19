# forescisoesaviso — Avisos de rescisao
1.225 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| i_empregados | integer(4) | PK |  | Empregado |
| data_aviso | date(4) |  |  | Data aviso previo |
| data_demissao | date(4) |  |  | Data demissao |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| DIAS_SUSPENSO | integer(4) |  |  | Dias suspensos no aviso prévio |
| MODELO_RELATORIO | char(80) |  | S | Nome do modelo de relatório |
| CONCESSOR | smallint(2) |  | S | Concessor. (1=Empregador/2=Empregado/3=Acordo entre as partes) |
| REDUCAO_HORARIO | smallint(2) |  | S | Tipo de redução do horário. (1=2(duas) horas diárias/2=7(sete) dias corridos/3=Conforme CCT/4=1(um) dia por semana) |
| TIPO | smallint(2) |  |  | Tipo: (1=Trabalhado/2=Indenizado) |
| DATA_COMPARECIMENTO | date(4) |  | S | Data do comparecimento |
| HORA_COMPARECIMENTO | time(8) |  | S | Hora do comparecimento |
| OBSERVACAO_COMPARECIMENTO | varchar(255) |  | S | Observações do comparecimento |
| MOTIVO | smallint(2) |  | S | Motivo da rescisão: (1-45) |
| DIAS_REDUCAO | numeric(13) |  | S | Dias para redução do aviso prévio. |
| SEQUENCIAL | integer(4) | PK |  | Sequencial do aviso prévio |
| DATA_CANCELAMENTO | date(4) |  | S | Data do cancelamento. |
| MOTIVO_CANCELAMENTO | smallint(2) |  |  | Motivo do cancelamento (1=Reconsideração prevista no artigo 489 da CLT/ 2=Determinação judicial/ 3=Cumprimento de norma legal / 4=Outros) |
| OBSERVACAO_CANCELAMENTO | varchar(255) |  | S | Observação do cancelamento. |
| DIAS_AVISO_INDENIZADO | numeric(5) |  | S | Dias indenizados no aviso prévio. |
| DIAS_AVISO_TRABALHADO | numeric(5) |  | S | Dias trabalhados no aviso prévio. |
| DIAS_SUSPENSAO_FERIAS_COLETIVAS | numeric(5) |  |  | Dias de suspensão por férias coletivas. |
| DIAS_PRORROGACAO_INICIO_CONTAGEM | smallint(2) |  |  | Dias de prorrogação para início da contagem do aviso prévio. |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| GERAR_DADOS_COMPARECIMENTO | smallint(2) |  |  | Gerar dados do comparecimento. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| ENVIAR_ESOCIAL_CANCELAMENTO | smallint(2) |  |  | Enviar para o eSocial o evento S-2250 de cancelamento. (0=Não/1=Sim) |
| GERAR_RETIFICACAO_ESOCIAL_CANCELAMENTO | smallint(2) |  |  | Gerar retificação para o eSocial do evento S-2250 de cancelamento. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL_CANCELAMENTO | smallint(2) |  |  | Marcação do evento S-2250 de cancelamento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| INICIAR_CONTAGEM_AVISO_PREVIO_A_PARTIR_DATA_INICIO_ESTABELECIDA | smallint(2) |  |  | Iniciar a contagem do aviso prévio a partir da data de início estabelecida (Opção do Sindicato). (0=Não/1=Sim) |
