# FOEMPREGADOS_PLANO_SAUDE — Cadastro de empregados - Plano de saúde
3.501 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| I_OPERADORAPLANOSAUDE | integer(4) | PK |  | Código da operadora de plano de saúde |
| DATA_INICIO | date(4) | PK |  | Data início período |
| DATA_FIM | date(4) |  | S | Data fim período |
| TIPO_BENEFICIARIO | smallint(2) |  |  | Tipo de beneficiário: 1=Somente titular/2=Titular e dependentes/3=Somente dependentes |
| ORIGEM_REG | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| GUID_CONTABIL | uniqueidentifier(16) |  |  | Identificador único do registro no banco do Contábil |
| GUID_ONVIO | uniqueidentifier(16) |  | S | Identificador único do registro no banco do Atendimento Onvio |
| ENDPOINT_EXCLUSAO | varchar(1024) |  | S | Endpoint utilizado para a exclusão do registro. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| POSSUI_DESCONTO_FAIXA_ETARIA | smallint(2) |  |  | Desconto por faixa etária (0=Não/1=Sim) |
| I_PLANO_SAUDE_FAIXA_ETARIA | integer(4) |  | S | Código da faixa etária |
