# FOEMPREGADOS_ATESTADOS_OCUPACIONAIS — Cadastro de Empregados - Atestados Ocupacionais
2.297 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| I_ATESTADO_OCUPACIONAL | integer(4) | PK |  | Código do atestado ocupacional |
| DATA | date(4) |  |  | Data |
| TIPO | smallint(2) |  |  | Tipo: (1=Admissional/2=Periódico/3=Retorno ao trabalho/4=Mudança de função/5=Demissional/6=Monitorização pontual) |
| RESULTADO | smallint(2) |  | S | Resultado. (1=Apto/2=Inapto) |
| NOME_MEDICO | char(60) |  | S | /** SEM USO **/ |
| CRM_MEDICO | char(8) |  | S | /** SEM USO **/ |
| UF | char(2) |  | S | /** SEM USO **/ |
| DATA_VENCIMENTO | date(4) |  | S | Data de vencimento |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro: 0=Sistema/1=Importação de tabelas/2=Importação de leiaute/3=Conversão |
| EXAME | char(1) |  | S | Exame realizado(R-Referencial; S-Sequencial). |
| NATUREZA | varchar(50) |  | S | Natureza do exame. |
| RESULTADO_ALTERADO | smallint(2) |  |  | Indicação do resultado. (1=Normal/2=Alterado/3=Estável/4=Agravamento/5=Ocupacional/6=Não Ocupacional) |
| TIPO_RESULTADO_ALTERADO | smallint(2) |  |  | Tipo de resultado alterado. (0=NA/1=Estável/2=Agravamento). |
| TIPO_AGRAVAMENTO_RESULTADO_ALTERADO | smallint(2) |  |  | Tipo do agravamento do resultado alterado. (0=NA/1=Ocupacional/2=Não ocupacional). |
| ORIGEM | smallint(2) |  |  | Origem do atestado. (1=Processo de cadastro de atestado ocupacional/2=Cadastro de empregados/3=Histórico PPP) |
| TELEFONE | varchar(15) |  | S | /** SEM USO **/ |
| NIS_MONITORACAO_BIOLOGICA | varchar(11) |  | S | NIS da monitoração biológica |
| NOME_MONITORACAO_BIOLOGICA | varchar(60) |  | S | Nome da monitoração biológica |
| CRM_MONITORACAO_BIOLOGICA | varchar(8) |  | S | CRM do responsável pela monitoração biológica |
| CODIGO_ESTADO_MONITORACAO_BIOLOGICA | integer(4) |  | S |  |
| FORMA_CONTATO_MEDICO | varchar(100) |  | S | /** SEM USO **/ |
| NOME_SERVICO_SAUDE_RESPONSAVEL | varchar(100) |  | S | Nome do serviço de saúde responsável. |
| CODIGO_CNES_SERVICO_SAUDE_RESPONSAVEL | varchar(7) |  | S | Código CNES do serviço de saúde responsável. |
| FORMA_CONTATO_SERVICO_SAUDE_RESPONSAVEL | varchar(100) |  | S | Forma de contato com o serviço de saúde responsável. |
| EMAIL_SERVICO_SAUDE_RESPONSAVEL | varchar(60) |  | S | E-mail do serviço de saúde responsável. |
| I_MEDICOS | integer(4) |  | S | Código do médico/dentista. |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
