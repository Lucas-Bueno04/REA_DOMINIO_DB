# FOAFASTAMENTOS — AFASTAMENTOS DOS EMPREGADOS
38.146 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | CODIGO EMPRESA |
| I_EMPREGADOS | integer(4) | PK |  | CODIGO |
| DATA_REAL | date(4) |  |  | Data Real |
| DATA_FOLHA | date(4) |  |  | Data Folha |
| I_AFASTAMENTOS | integer(4) |  |  | Código do afastamento referente ao tipo de afastamento da FOAFASTAMENTOS_TIPO |
| DATA_FIM | date(4) |  | S | Data fim |
| DATA_FIM_TMP | date(4) |  |  | Data fim |
| REQ_BENEFICIO | smallint(2) |  | S | Não requereu o benefício junto ao INSS até 31/08/2003. (0 = Opção marcada, 1 = Opção desmarcada) |
| DT_CALC_LEI10710 | date(4) |  | S | Data para cálculo conforme lei 10710 |
| DATA_CAT | date(4) |  | S | ** SEM USO ** |
| NUMERO_CAT | char(13) |  | S | ** SEM USO ** |
| NUMERO_DIAS | numeric(10) |  | S | Número de dias |
| DATA_BAIXA | date(4) |  | S | DATA DA BAIXO DO SERVIÇO MILITAR |
| TRANSFERENCIA | tinyint(1) |  |  | SE O AFASTAMENTO E UMA TRANSFERENCIA OU NAO / 1 - SIM, 0 - NAO |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| DATA_REAL_DN | numeric(10) | PK |  | Data numérica do afastamento |
| DATA_ORIGEM_TRANSF | date(4) |  | S | DATA ORIGINAL DO RETORNO DO AFASTAMENTO POR MATERNIDADE DO EMPREGADO ORIGEM |
| ORIGEM | smallint(2) |  |  | Origem: 0=Afastamento/1=Replicação por rescisao por transferencia/2=Replicação por interrupção por outro afastamento |
| TIPO_CAT | smallint(2) |  | S | ** SEM USO ** Tipo CAT (1=Típico/2=Doença profissional ou do trabalho/3=Trajeto) |
| I_CAT | integer(4) |  | S | Código da CAT |
| CODIGO_DOENCA | char(10) |  | S | Código da doença (CID) |
| NOME_MEDICO | char(100) |  | S | /** SEM USO **/ |
| CRM_MEDICO | char(10) |  | S | /** SEM USO **/ |
| UF_ATESTADO | char(2) |  | S | /** SEM USO **/ |
| ACIDENTE_TRANSITO | smallint(2) |  |  | Acidente de trânsito. (0=Não/1=Sim) |
| TIPO_ACIDENTE_TRANSITO | smallint(2) |  | S | Tipo de acidente de trânsito. (1=Atropelamento/2=Colisão/3=Outros) |
| NOME_SINDICATO_MANDATO_SINDICAL | varchar(80) |  | S | Nome do sindicato do exercício do mandato sindical. |
| CNPJ_SINDICATO_MANDATO_SINDICAL | varchar(14) |  | S | CNPJ do sindicato do exercício do mandato sindical. |
| ONUS_REMUNERACAO_MANDATO_SINDICAL | smallint(2) |  | S | Ônus da remuneração do exercício do mandato sindical. (1=Empregador/2=Sindicato/3=Diferença salarial paga pelo sindicato/null=Sem dados informado, conversao) |
| DATA_PARTO | date(4) |  | S | Data do parto. |
| GERAR_COMPENSACAO_PER_DCOMP | smallint(2) |  |  | Gerar compensação para o PER/DCOMP. (0=Não/1=Sim) |
| COMPETENCIA_INICIO_COMPENSACAO_PER_DCOMP | date(4) |  | S | Competência de início da compensação para o PER/DCOMP. |
| TIPO_DOCUMENTO_AUSENCIA_JUSTIFICADA | varchar(200) |  | S | Tipo de documento da ausência justificada. |
| NUMERO_DOCUMENTO_AUSENCIA_JUSTIFICADA | varchar(50) |  | S | Número do documento da ausência justificada. |
| EMISSOR_DOCUMENTO_AUSENCIA_JUSTIFICADA | varchar(200) |  | S | Emissor do documento da ausência justificada. |
| DATA_ORIGEM_INTERRUPCAO | date(4) |  | S | Data original do retorno do afastamento interrompido por outro afastamento |
| REGISTRO_OBITO_GENITORA | varchar(32) |  | S | Registro do óbito da genitora. |
| DATA_OBITO_GENITORA | date(4) |  | S | Data do óbito da genitora. |
| DETERMINAR_COMPETENCIA_FIM_COMPENSACAO_PER_DCOMP | smallint(2) |  |  | Determinar fim para as compensações PER/DCOMP. (0=Não/1=Sim) |
| COMPETENCIA_FIM_COMPENSACAO_PER_DCOMP | date(4) |  | S | Competência fim para as compensações PER/DCOMP. |
| OBSERVACAO_LICENCA_SEM_VENCIMENTO | varchar(255) |  | S | Observação para a licença sem vencimento. |
| ORGAO_CLASSE | smallint(2) |  | S | /** SEM USO **/ |
| MOTIVO_AUSENCIA_JUSTIFICADA | smallint(2) |  | S | Motivo da ausência justificada. (1=Morte/2=Casamento/3=Outros motivos/4=Problemas decorrentes de doença em família) |
| SOMAR_DIAS_AFASTAMENTO_ANTERIOR | smallint(2) |  |  | Somar os dias do afastamento anterior. (0=Não/1=Sim) |
| DATA_PERICIA | date(4) |  | S | Data da perícia. |
| HORARIO_PERICIA | time(8) |  | S | Horário da perícia. |
| LOCAL_PERICIA | varchar(60) |  | S | Local da perícia. |
| NUMERO_BENEFICIO_INSS | varchar(10) |  | S | Número benefício INSS. |
| I_MEDICOS | integer(4) |  | S | Código do médico/dentista. |
| MEDIAS_MANUAL | smallint(2) |  |  | Médias manuais. (0=Não/1=Sim) |
| MEDIA_HORAS | numeric(13) |  | S | Média horas. |
| MEDIA_VALOR | numeric(13) |  | S | Média valor. |
| MEDIA_HORA_AULA | numeric(13) |  | S | Média hora-aula. |
| I_DADOS_EVENTOS_ESOCIAL_S_2230_INCLUSAO | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL_S_2230_INCLUSAO | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL_S_2230_INCLUSAO | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL_S_2230_INCLUSAO | smallint(2) |  |  | Enviar para o eSocial a inclusão do evento S-2230. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL_S_2230_INCLUSAO | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL_S_2230_INCLUSAO | smallint(2) |  |  | Gerar retificação para o eSocial do evento S-2230. (0=Não/1=Sim) |
| I_DADOS_EVENTOS_ESOCIAL_S_2230_DATA_FIM | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL_S_2230_DATA_FIM | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL_S_2230_DATA_FIM | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL_S_2230_DATA_FIM | smallint(2) |  |  | Enviar para o eSocial a data fim do evento S-2230. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL_S_2230_DATA_FIM | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL_S_2230_DATA_FIM | smallint(2) |  |  | Gerar retificação para o eSocial da data fim do evento S-2230. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL_S_2230_INCLUSAO | smallint(2) |  |  | Marcação do evento S-2230 para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL_S_2230_DATA_FIM | smallint(2) |  |  | Marcação do evento S-2230 de data fim para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| GUID_CONTABIL | uniqueidentifier(16) |  |  | Identificador único do registro no banco do Contábil |
| GUID_ONVIO | uniqueidentifier(16) |  | S | Identificador único do registro no banco do Atendimento Onvio |
| ENDPOINT_EXCLUSAO | varchar(1024) |  | S | Endpoint utilizado para a exclusão do registro. |
| AFASTAMENTO_DECORRENTE_CONTAMINACAO_CORONAVIRUS | smallint(2) |  |  | Afastamento decorrente de contaminação pelo coronavírus (Covid-19). (0=Não/1=Sim) |
| ENVIAR_INCLUSAO_ESOCIAL_ANTECIPADA | smallint(2) |  |  | Enviar inclusão eSocial antecipada. (0=Não/1=Sim) |
| AFASTAMENTO_INTERROMPIDO_POR_MORTE | smallint(2) |  |  | Afastamento interrompido por morte. (0=Não/1=Sim) |
| DADOS_DO_ARQUIVO_BOLSA_QUALIFICACAO | smallint(2) |  |  | Tem informação de bolsa qualificação. (0=Não/1=Sim) |
| NUMERO_PROCESSO_SEI_BOLSA_QUALIFICACAO | varchar(25) |  | S | Número processo SEI. |
| CARGA_HORARIA_BOLSA_QUALIFICACAO | smallint(2) |  |  | Carga horária. (1=120 horas/2=180 horas/3=240 horas/4=300 horas) |
| PERCENTUAL_CURSOS_LABORATORIOS_BOLSA_QUALIFICACAO | numeric(3) |  | S | Percentual cursos/laboratórios |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| ENVIAR_ESOCIAL_PERIODO_ANTERIOR_INICIO_BANCO_CONTABIL | smallint(2) |  | S | Enviar evento eSocial anterior ao início da utilização do banco de dados (0=Não/1=Sim) |
| CONSIDERAR_SABADO_COMPENSADO_AVO_13_FERIAS | smallint(2) |  | S | Considerar o sabado compensado para contagem de avos de 13 e ferias: 0=Não/1=Sim |
