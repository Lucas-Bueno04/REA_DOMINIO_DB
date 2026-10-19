# FOHORARIOS — Horários.
4.005 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_HORARIO | integer(4) | PK |  | Código do horário. |
| NOME | varchar(30) |  |  | Nome do horário. |
| DATA_INICIO | date(4) |  |  | Data de início do horário. |
| SITUACAO | smallint(2) |  |  | Situação do horário. (0=Inativo/1=Ativo) |
| DATA_INATIVACAO | date(4) |  | S | Data de inativação do horário. |
| TIPO | smallint(2) |  |  | Tipo de horário. (1=Trabalhado/2=Compensado/3=Folga) |
| HORA_ENTRADA | time(8) |  | S | Hora de entrada. |
| HORA_SAIDA | time(8) |  | S | Hora de saída. (1=Trabalhado/2=Compensado/3=Folga) |
| TIPO_INTERVALO | smallint(2) |  |  | Tipo de intervalo (0,1,2,3) 0=Não possui/1=Em horário variável/2=Em horário fixo/3=Em horário variável noturno |
| DURACAO_INTERVALO | time(8) |  | S | /** SEM USO **/ |
| ORIGEM_REG | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes, 4-Importação eSocial |
| CODIGO_ESOCIAL | varchar(30) |  | S | Código no eSocial. |
| VARIACAO_DIARIA_ENTRADA_SAIDA | smallint(2) |  |  | Variação diária entrada/saída. (0=Não/1=Sim) |
| DURACAO_JORNADA | time(8) |  | S | /** SEM USO **/ |
| DURACAO_JORNADA_MINUTOS | smallint(2) |  | S | Duração da jornada em minutos. |
| DURACAO_INTERVALO_MINUTOS | smallint(2) |  | S | Duração do intervalo em minutos. |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| DURACAO_HORA_NOTURNA | numeric(13) |  | S | Duração da hora noturna. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
