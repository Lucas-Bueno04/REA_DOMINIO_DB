# FOPARMTO_ALTERACAO — Tabela de alterações de parâmetros.
1.457 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| VIGENCIA | date(4) | PK |  | Vigência da alteração. |
| CLASSIFICACAO_TRIBUTARIA | smallint(2) |  |  | Classificação tributária. |
| COOPERATIVA | smallint(2) |  |  | Cooperativa. (0=Não/1=Sim, cooperativa de trabalho/2=Sim, cooperativa de produção/3=Sim, outras cooperativas) |
| CONSTRUTORA | smallint(2) |  |  | Construtora. (0=Não/1=Sim) |
| OPTANTE_REGISTRO_ELETRONICO_EMPREGADOS | smallint(2) |  |  | Optante pelo registro eletrônico de empregados. (0=Não/1=Sim) |
| POSSUI_ACORDO_INTERNACIONAL_ISENCAO_MULTA | smallint(2) |  |  | Possui acordo internacional para isenção de multa. (0=Não/1=Sim) |
| ENTIDADE_SEM_FINS_LUCRATIVOS | smallint(2) |  | S | **SEM USO** |
| EMPRESA_TRABALHO_TEMPORARIO | smallint(2) |  | S | **SEM USO** |
| NUMERO_REGISTRO_MINISTERIO_TRABALHO | varchar(30) |  | S | **SEM USO** |
| POSSUI_SITUACAO_ESPECIAL_SITUACAO | smallint(2) |  | S | Situação especial. (1=Extinção/2=Fusão/3=Cisão/4=Incorporação) |
| SIGLA_MINISTERIO_CONCEDEU_ENTIDADE_BENEFICENTE | smallint(2) |  | S | Sigla do ministério que concedeu a classificação de Entidade Beneficente. (1=CNAS/2=MEC/3=MS/4=MDS/5=Lei) |
| NUMERO_CERTIFICADO_LEI_ENTIDADE_BENEFICENTE | varchar(40) |  | S | Número do certificado/lei que concedeu a classificação de Entidade Beneficente. |
| DATA_EMISSAO_ENTIDADE_BENEFICENTE | date(4) |  | S | Data de emissão da classificação de Entidade Beneficente. |
| DATA_VENCIMENTO_ENTIDADE_BENEFICENTE | date(4) |  | S | Data de vencimento da classificação de Entidade Beneficente. |
| NUMERO_PROTOCOLO_RENOVACAO_ENTIDADE_BENEFICENTE | varchar(40) |  | S | Número do protocolo de renovação da classificação de Entidade Beneficente. |
| DATA_PROTOCOLO_RENOVACAO_ENTIDADE_BENEFICENTE | date(4) |  | S | Data do protocolo de renovação da Entidade Beneficente. |
| DATA_DIARIO_OFICIAL_UNIAO_ENTIDADE_BENEFICENTE | date(4) |  | S | Data do diário oficial da união da classificação de Entidade Beneficente. |
| PAGINAL_DIARIO_OFICIAL_UNIAO_ENTIDADE_BENEFICENTE | varchar(5) |  | S | Página do diário oficial da união da classificação de Entidade Beneficente. |
| CONTRATACAO_PESSOA_COM_DEFICIENCIA | smallint(2) |  |  | Contratação de pessoa com deficiência. (1=Dispensado de acordo com a lei/2=Dispensado, mesmo que parcialmente/3=Com a exigibilidade suspensa/4=Obrigado) |
| I_PROCESSO_PESSOA_DEFICIENCIA | integer(4) |  | S | Código do processo judicial para contratação de pessoa com deficiência. |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| ORIGEM_ALTERACAO | smallint(2) |  | S | Origem do registro ( 1=Sistema/2=Alteração de Faseamento do eSocial). |
| CALCULAR_FUNRURAL_SOBRE_FOLHA_PAGAMENTO | smallint(2) |  |  | Calcular FUNRURAL sobre a de folha pagamento. (0=Não/1=Sim) |
| UTILIZA_MODULO_WEB_SIMPLIFICADO_ME_EPP_ESOCIAL | smallint(2) |  |  | Utiliza módulo Web Simplificado ME e EPP. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| UTILIZA_FORMA_UNIFICADA_ESOCIAL | smallint(2) |  | S | Utiliza forma unificada a orgãos públicos. (0=Não/1=Sim) |
| CNPJ_ENTE_FEDERATIVO_RESPONSAVEL | varchar(14) |  | S | CNPJ do Ente Federativo Responsável a orgãos públicos. |
| NUMERO_PROCESSO_DEFICIENTE | varchar(20) |  | S | Numero do processo para contratação de deficiente. |
| GERA_DADOS_ISENCAO_ENTIDADE_BENEFICIENTE | char(1) |  |  | Entidade Beneficiente - Informações Complementares - Dados da Isenção |
