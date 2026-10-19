# FOCONVOCACAO_TRABALHO_INTERMITENTE — Convocação para trabalho intermitente.
5 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| I_CONVOCACAO | integer(4) | PK |  | Código da convocação |
| DESCRICAO | varchar(100) |  | S | Descrição |
| DATA_INICIO | date(4) |  |  | Data de início |
| DATA_FIM | date(4) |  |  | Data final |
| CARGA_HORARIA_FIXA | smallint(2) |  |  | Carga horária fixa (0=Não/1=Sim) |
| I_JORNADA | integer(4) |  | S | Sem uso |
| DESCRICAO_CARGA_VARIAVEL | varchar(300) |  | S | Descrição da carga variável |
| TIPO_PRESTACAO_SERVICO | smallint(2) |  |  | Tipo da prestação de serviço (1=Prestação de serviços no estabelecimento do empregador/2=Prestação de serviços em apenas um local e fora do estabelecimento do empregador/3=Prestação de serviços de natureza externa ou em mais de um local) |
| CEP | char(8) |  | S | CEP |
| TIPO_ENDERECO | smallint(2) |  | S | Tipo do endereço |
| ENDERECO | varchar(100) |  | S | Endereço |
| NUMERO_ENDERECO | varchar(10) |  | S | Número do endereço |
| COMPLEMENTO_ENDERECO | varchar(30) |  | S | Complemento do endereço |
| BAIRRO_ENDERECO | varchar(90) |  | S | Bairro do endereço |
| CODIGO_MUNICIPIO | integer(4) |  | S | Código do município referente a GEMUNICIPIO |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| DATA_PAGAMENTO_PREVISTA | date(4) |  | S | Data prevista do pagamento. |
| I_HORARIO | integer(4) |  | S | Código do horário vinculado. |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
