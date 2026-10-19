# FOHORARIOS_ALTERACAO — Tabela de alterações dos horários
4.019 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_HORARIO | integer(4) | PK |  | Código do horário. |
| VIGENCIA | date(4) | PK |  | Vigência da alteração. |
| TIPO | smallint(2) |  |  | Tipo de horário. (1=Trabalhando/2=Compensado/3=folga) |
| HORA_ENTRADA | time(8) |  | S | Hora de entrada. |
| HORA_SAIDA | time(8) |  | S | Hora de saída. |
| TIPO_INTERVALO | smallint(2) |  |  | Tipo de intervalo (0,1,2,3) 0=Não possui/1=Em horário variável/2=Em horário fixo/3=Em horário variável noturno |
| DURACAO_JORNADA_MINUTOS | smallint(2) |  | S | Duração da jornada em minutos. |
| VARIACAO_DIARIA_ENTRADA_SAIDA | smallint(2) |  |  | Variação diário entrada/saída. (0=Não/1=Sim) |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| ORIGEM_ALTERACAO | smallint(2) |  | S | Origem do registro ( 1=Sistema/2=Alteração de Faseamento do eSocial). |
| CODIGO_ESOCIAL | varchar(30) |  | S | Código no eSocial |
| DURACAO_HORA_NOTURNA | numeric(13) |  | S | Duração da hora noturna. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
