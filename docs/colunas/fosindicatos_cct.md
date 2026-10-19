# FOSINDICATOS_CCT — Sindicato - Cadastro - Convencao Coletiva
63 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_SINDICATOS | integer(4) | PK |  | Codigo do Sindicato |
| DATA_REGISTRO | date(4) | PK |  | Data do registro |
| PROCESSO | char(20) |  |  | Numero do Processo |
| DESCRICAO | char(115) |  |  | Descricao da Convencao Coletiva |
| RETROATIVO | tinyint(1) |  |  | Aumento Retroativo -  0=Nao Retroativo\1=Retroativo |
| COMPETENCIA_ALTERACAO | date(4) |  | S | Competência da alteração |
| RETROATIVO_DATA | date(4) |  | S | Competencia Retroativa |
| RETROATIVO_AJUSTE | tinyint(1) |  | S | Forma do ajuste: (0-4) |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| GERAR_FOLHA_COMPLEMENTAR_ESPECIFICA | smallint(2) |  |  | Gerar folhas complementares específicas para essa alteração salarial: (0=Não, 1=Sim) |
| VIGENCIA_INICIO | date(4) |  | S | Início vigência |
| VIGENCIA_FIM | date(4) |  | S | Fim vigência |
| PERCENTUAL_REAJUSTE | numeric(6) |  |  | Percentual de reajuste |
| ALTERACAO_PROPORCIONAL_MESES_TRABALHADOS | smallint(2) |  |  | Alteração proporcional conforme percentual de reajuste: (0=Não, 1=Sim) |
| PERCENTUAL_REAJUSTE_01_MESES | numeric(6) |  | S | Percentual de reajuste proporcional a 1 mês trabalhado anterior à vigência |
| PERCENTUAL_REAJUSTE_02_MESES | numeric(6) |  | S | Percentual de reajuste proporcional a 2 meses trabalhados anteriores à vigência |
| PERCENTUAL_REAJUSTE_03_MESES | numeric(6) |  | S | Percentual de reajuste proporcional a 3 meses trabalhados anteriores à vigência |
| PERCENTUAL_REAJUSTE_04_MESES | numeric(6) |  | S | Percentual de reajuste proporcional a 4 meses trabalhados anteriores à vigência |
| PERCENTUAL_REAJUSTE_05_MESES | numeric(6) |  | S | Percentual de reajuste proporcional a 5 meses trabalhados anteriores à vigência |
| PERCENTUAL_REAJUSTE_06_MESES | numeric(6) |  | S | Percentual de reajuste proporcional a 6 meses trabalhados anteriores à vigência |
| PERCENTUAL_REAJUSTE_07_MESES | numeric(6) |  | S | Percentual de reajuste proporcional a 7 meses trabalhados anteriores à vigência |
| PERCENTUAL_REAJUSTE_08_MESES | numeric(6) |  | S | Percentual de reajuste proporcional a 8 meses trabalhados anteriores à vigência |
| PERCENTUAL_REAJUSTE_09_MESES | numeric(6) |  | S | Percentual de reajuste proporcional a 9 meses trabalhados anteriores à vigência |
| PERCENTUAL_REAJUSTE_10_MESES | numeric(6) |  | S | Percentual de reajuste proporcional a 10 meses trabalhados anteriores à vigência |
| PERCENTUAL_REAJUSTE_11_MESES | numeric(6) |  | S | Percentual de reajuste proporcional a 11 meses trabalhados anteriores à vigência |
| PERCENTUAL_REAJUSTE_12_MESES | numeric(6) |  | S | Percentual de reajuste proporcional a 12 meses trabalhados anteriores à vigência |
| CONSIDERAR_MES_ADMISSAO_ATE_15_DIAS_TRABALHO | smallint(2) |  | S | Considerar o mês da admissão apenas se trabalhou período superior a 15 dias: (0=Não, 1=Sim) |
| I_FORMA_AJUSTE_PARCELAMENTO | integer(4) |  | S | Código da forma de ajuste conforme parcelamento |
| TIPO_ACORDO | smallint(2) |  |  | Tipo de acordo: (1=Acordo Coletivo, 2=Convenção, 3=Dissídio) |
| TIPO_PERCENTUAL_REAJUSTE | smallint(2) |  |  | Tipo percentual de reajuste. (1=Fixo/2=Conforme cargo) |
| ALTERAR_SALARIO_EMPREGADO_ADMITIDO_DENTRO_VIGENCIA_CONVENCAO | smallint(2) |  |  | Alterar salário de empregado admitido dentro da vigência da convenção coletiva. (0=Não/1=Sim) |
| PERMITIR_ALTERACAO_EMPREGADO_RETORNO_AFASTAMENTO_MES_ANTERIOR_VIGENCIA | smallint(2) |  |  | Permitir alteração salarial de empregado que retornou do afastamento no mês anterior ao início da vigência. (0=Não/1=Sim) |
| CONSIDERAR_MES_ADMISSAO_INDEPENDENTEMENTE_QUANTIDADE_DIAS_TRABALHADOS | smallint(2) |  |  | Considerar o mês da admissão independentemente da quantidade de dias trabalhados. (0=Não/1=Sim) |
| POSSUI_TERMO_ADITIVO | smallint(2) |  |  | Possui termo aditivo. (0=Não/1=Sim) |
| TERMO_ADITIVO | smallint(2) |  |  | Indica se o registro de convenção é um termo aditivo. (0=Não/1=Sim) |
| DATA_REGISTRO_CONVENCAO_COLETIVA | date(4) |  | S | Data de registro da convenção coletiva que possui o termo aditivo. |
| COMPETENCIA_PERCENTUAL_REAJUSTE_01_MES | date(4) |  | S | Competência para pagamento do percentual de reajuste de 01 mês. |
| COMPETENCIA_PERCENTUAL_REAJUSTE_02_MESES | date(4) |  | S | Competência para pagamento do percentual de reajuste de 02 meses. |
| COMPETENCIA_PERCENTUAL_REAJUSTE_03_MESES | date(4) |  | S | Competência para pagamento do percentual de reajuste de 03 meses. |
| COMPETENCIA_PERCENTUAL_REAJUSTE_04_MESES | date(4) |  | S | Competência para pagamento do percentual de reajuste de 04 meses. |
| COMPETENCIA_PERCENTUAL_REAJUSTE_05_MESES | date(4) |  | S | Competência para pagamento do percentual de reajuste de 05 meses. |
| COMPETENCIA_PERCENTUAL_REAJUSTE_06_MESES | date(4) |  | S | Competência para pagamento do percentual de reajuste de 06 meses. |
| COMPETENCIA_PERCENTUAL_REAJUSTE_07_MESES | date(4) |  | S | Competência para pagamento do percentual de reajuste de 07 meses. |
| COMPETENCIA_PERCENTUAL_REAJUSTE_08_MESES | date(4) |  | S | Competência para pagamento do percentual de reajuste de 08 meses. |
| COMPETENCIA_PERCENTUAL_REAJUSTE_09_MESES | date(4) |  | S | Competência para pagamento do percentual de reajuste de 09 meses. |
| COMPETENCIA_PERCENTUAL_REAJUSTE_10_MESES | date(4) |  | S | Competência para pagamento do percentual de reajuste de 10 meses. |
| COMPETENCIA_PERCENTUAL_REAJUSTE_11_MESES | date(4) |  | S | Competência para pagamento do percentual de reajuste de 11 meses. |
| COMPETENCIA_PERCENTUAL_REAJUSTE_12_MESES | date(4) |  | S | Competência para pagamento do percentual de reajuste de 12 meses. |
| CONSIDERAR_PERIODO_AFASTADO_ALTERACAO_SALARIAL | smallint(2) |  |  | Considerar o período afastado do empregado para a alteração salarial. (0=Não/1=Sim) |
| CONSIDERAR_PERIODO_AFASTADO_ALTERACAO_SALARIAL_CONFORME_CARGO | smallint(2) |  |  | Considerar o período afastado do empregado para alteração salarial conforme cargo. (0=Não/1=Sim) |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
