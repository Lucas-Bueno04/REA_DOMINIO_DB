# FOVIGENCIA_REGIME — Tabela de vigências do regime da empresa
1.464 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| COMPETENCIA | date(4) | PK |  | Competência |
| DESCRICAO | char(40) |  |  | Descrição |
| REGIME_FEDERAL | smallint(2) |  |  | Regime federal |
| SIMPLES_FEDERAL | smallint(2) |  |  | Simples federal até 06/2007 |
| SIMPLES_NACIONAL | smallint(2) |  |  | Simples nacional |
| POSSUI_INSS_EMPRESA_RECEITA_BRUTA | smallint(2) |  |  | Possui INSS Empresa sobre a receita bruta. (0=Não/1=Sim) |
| ATIVIDADE_EMPRESA_LEI_12546 | smallint(2) |  | S | Atividade empresa lei 12546. (1=Indústria/Comércio/2=Serviço/3=Indústria/Comércio e Serviço) |
| SERVICOS_EXCLUSIVOS_TI_TIC | smallint(2) |  | S | Empresa exclusivamente prestadora de serviços de TI e TIC. (0=Não/1=Sim) |
| FABRICANTE_EXCLUSIVO_PRODUTOS_RELACIONADOS | smallint(2) |  | S | Empresa exclusivamente prestadora atividades relacionadas. (0=Não/1=Sim) |
| ALIQUOTA_IMPOSTO_NAO_RELACIONADA_LEI_12546 | smallint(2) |  | S | Alíquota para receitas não relacionadas quando inferior a 5% da receita total. (1=1,00% - Art 8º da Lei 12.546/2=2,00% - Art 7º da Lei 12.546/3=Alíquota com maior receita) |
| CALCULAR_INSS_EMPRESA_13_RESCISAO_SEM_PROPORCIONALIDADE | smallint(2) |  | S | Calcular INSS Empresa sobre valor do 13º salário pago em rescisão sem considerar a proporcionalidade no ano base. (0=Não/1=Sim) |
| CALC_INSS_EMPRESA_13_SALARIO_RESCISAO_CONFORME_ULTIMO_SERVICO | smallint(2) |  | S | Calcular INSS Empresa sobre valor do 13º salário pago em rescisão conforme último serviço alocado. (0=Não/1=Sim) |
| CALC_PERC_INSS_EMP_13_SAL_PROPORC_AVO_DES_SERV_NAO_ENQUADRA_DES | smallint(2) |  |  | Calcular INSS Empresa sobre 13º salário proporcional aos avos desonerados quando o serviço não estiver enquadrado na desoneração. (0=Não/1=Sim) |
| UTILIZAR_PERC_REDUCAO_ACUMULADO_COMP_13_SALARIO_PAGO_NOVEMBRO | smallint(2) |  |  | Utilizar o percentual de receita bruta acumulado na competência de novembro, para o cálculo do INSS Empresa sobre o 13º salário quando calculado em novembro. (0=Não/1=Sim) |
| PIS_CONTRIBUI | smallint(2) |  |  | Contribui com o PIS. (0=Não/1=Sim) |
| PIS_PERCENTUAL | numeric(13) |  | S | Percentual de contribuição do PIS. |
| CALCULAR_PIS_COMPETENCIA_PAGAMENTO_FERIAS | smallint(2) |  |  | Calcular o valor do PIS na competência da data de pagamento das férias. (0=Não/1=Sim). |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| CALCULAR_INSS_EMPRESA_13_SEM_PROPORCIONALIDADE | smallint(2) |  |  | Calcular INSS Empresa sobre o valor de 13º integral sem considerar a proporcionalidade no ano base. (0=Não/1=Sim) |
