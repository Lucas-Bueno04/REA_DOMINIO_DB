# foparmto — Tabela de parâmetros
1.355 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| valor_arredonda | numeric(8) |  | S | ** SEM USO ** Valor para arredondamento |
| tem_folha_semanal | char(1) |  |  | Trabalha com folha semanal |
| tem_folha_quinzenal | char(1) |  |  | Trabalha com folha quizenal |
| data_proces | date(4) |  |  | Competencia atual |
| tipo_proces | integer(4) |  |  | tipo folha atual |
| codi_emp_eve | integer(4) |  |  | Usa eventos da empresa |
| adiant_tiposal | tinyint(1) |  |  | Base de cálculo |
| adiant_percentual | numeric(13) |  |  | Percentual de adiantamento |
| calc13_pag_media | char(1) |  |  | Pagar médias horas/valor |
| calc13_pag_adic | char(1) |  |  | Pagar adicionais |
| calc13_nao_calc_dir | char(1) |  |  | Não calcula para diretores |
| calc13_percentual | numeric(6) |  |  | Percentual |
| calc13_maisde1adiant | char(1) |  |  | Permite mais de um adiantamento |
| tipo_data_afas | char(1) |  |  | Tipo para afastamento (sem uso) |
| fer_desc_faltas | char(1) |  |  | Descontar faltas automaticamente |
| fer_paga_adic | char(1) |  |  | Pagar adicionais |
| fer_paga_med | char(1) |  |  | Pagar Medias |
| fer_33_sob_total | char(1) |  |  | 33% sobre total (sem uso) |
| fer_decimo_1p | char(1) |  |  | Adiantar 1a. parcela do 13o. |
| separador | tinyint(1) |  |  | Separa lançamentos por |
| mes_conversao | date(4) |  |  | Competencia conversao folha 34 |
| ajusta_med_13 | char(1) |  |  | Ajustar cálculo do 13º salário em dezembro favorável ao empregado: (N=Não/S=Sim) |
| mes_encerrado | date(4) |  |  | Data do fechamento |
| perm_alt_calc | char(1) |  |  | Permite alteracao no calculo (sem uso) |
| mov_fer_mes | char(1) |  |  | movimento de ferias na folha mensal |
| calc_rest_interferencia | char(1) |  |  | Permite interferencia no calculo (sem uso) |
| cta_gera | tinyint(1) |  |  | Gera lancamentos contabeis |
| cta_codi_emp | integer(4) |  |  | Gera os lancamentos na empresa |
| cta_sep_rescisao | tinyint(1) |  |  | rescisao |
| cta_sep_ferias | tinyint(1) |  |  | Ferias |
| cta_data_lanc | tinyint(1) |  |  | Data integracao contabil (sem uso) |
| cta_provisao | tinyint(1) |  |  | Forma de integracao contabil (sem uso) |
| cta_tipo_exp | tinyint(1) |  |  | Tipo de exportação contábil |
| gps_conta_debito | tinyint(1) |  |  | Conta debito GPS Eletronica |
| pis_contribui | tinyint(1) |  |  | ** SEM USO ** |
| pis_percentual | numeric(13) |  |  | ** SEM USO ** |
| ordenar_eventos | tinyint(1) |  |  | Ordena eventos |
| cta_data_lanc_resc | tinyint(1) |  |  | Data do lancamento para rescisao |
| cta_data_lanc_fer | tinyint(1) |  |  | Data do lancamento para ferias |
| calcinss_movto_comp | date(4) |  | S | Controle de compensacao INSS a partir de |
| adiant_afast | tinyint(1) |  |  | Empregados afastados |
| contrato_tf | char(10) |  | S | Contrato Ticket Farma |
| fer_col_medlic | tinyint(1) |  | S | medias e adicionais na licenca remunerada |
| separar_dsr | tinyint(1) |  |  | Discriminar DSR |
| calc13_estagiario | tinyint(1) |  | S | Pagar para estagiário |
| fer_estagiario | tinyint(1) |  | S | Pagar para estagiario |
| fer_domestico | tinyint(1) |  | S | ** SEM USO ** |
| calc13_faltas | tinyint(1) |  | S | Descontar faltas automaticamente |
| calc13_avos_adm | tinyint(1) |  | S | Pagar adiant. até dezembro para empregados admitidos no ano |
| adiant_contr | tinyint(1) |  | S | Calcular para contribuintes |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| usa_rateio | tinyint(1) |  | S | Usa rateio por servico (1=Sim, 0=Nao) |
| cta_data_lanc_mes | tinyint(1) |  | S | Data do lançamento para folha mensal |
| cta_data_lanc_comp | tinyint(1) |  | S | Data do lançamento para folha complementar |
| cta_data_lanc_adiant | tinyint(1) |  | S | Data do lançamento para adiantamento |
| cta_data_lanc_13ad | tinyint(1) |  | S | Data do lançamento para 13o. Adiantamento |
| cta_data_lanc_13int | tinyint(1) |  | S | Data do lançamento para 13o. Integral |
| adiant_afast_condic | tinyint(1) |  |  | Condição para pagto de adiantamento quando afastado |
| adiant_afast_condic_dias | integer(4) |  | S | Numero de dias trabalhados no mes para direito ao adiantamento |
| cta_ccus_rateio | tinyint(1) |  | S | Contabilidade por centro de custo |
| cta_ccus_rateio_tipo | tinyint(1) |  | S | Tipo do rateio. |
| usa_rateio_inicio | date(4) |  | S | Inicio do rateio do calculo por servicos |
| simples_072007 | tinyint(1) |  | S | Opção simples nacional |
| simples_072007_limite_receita | tinyint(1) |  |  | Receita bruta até 36.000,00 |
| tem_folha_professor | char(1) |  |  | Trabalha com folha de professores |
| dsr_categoria | tinyint(1) |  |  | Categorias DSR (Soma binaria) |
| TIPO_LANCTO_HORAS | char(1) |  |  | TIPO DE LANCAMENTO DE HORAS |
| DATA_PAGTO_MES | tinyint(1) |  |  | Data de pagamento da folha mensal do empregado. 1-Último dia útil do mês de competência, 2-Quinto dia útil do mês seguinte e 3-Primeiro dia útil do mês seguinte |
| CTA_EXP_L18 | integer(4) |  |  | GERA LANCAMENTOS PARA A CONTABILIDADE DE ACORDO COM O LAYOUT 18. |
| FER_DILATAR_LIMITE_GOZO | smallint(2) |  |  | CONSIDERAR OS DIAS AFASTADOS NO PERÍODO CONCESSIVO PARA DILATAR O LIMITE DE GOZO |
| TIPO_CALCULO_PROP | tinyint(1) |  |  | TIPO DO CALCULO PROPORCIONAL (1=MES COMERCIAL,2=MES CIVIL) |
| TIPO_CALCULO_PROP_CATEGORIA | tinyint(1) |  |  | CATEGORIAS PARA O TIPO DO CALCULO PROPORCIONAL |
| FER_PROP_RESC_JUSTA_CAUSA | tinyint(1) |  |  | CALCULAR FÉRIAS PROPORCIONAL PARA RESCISÃO COM JUSTA CAUSA |
| INF_LANCTO_FALTAS | smallint(2) |  |  | INFORMAR DATAS NOS LANÇAMENTOS DE HORAS |
| NAO_SOMA_SAL_FAM_EST_MES | tinyint(1) |  |  | Nao considera o salario familia no calculo do estouro do mes. |
| NAO_CALC_SAL_FAM_FER | tinyint(1) |  |  | Nao calcula salario familia nas ferias. |
| AVO_MEDIA_13_ADMISSAO | smallint(2) |  |  | Considerar avo de média 13º no mês da admissão com menos de 15 dias trabalhados: 0=Não/1=Sim |
| CALC_CONTR_SIND_FER | smallint(2) |  |  | Calcula contribuição sindical nas férias: 0=Não/1=Sim |
| CALCULAR_ADIANTAMENTO_13_SALARIO_MES_ANTERIOR | smallint(2) |  |  | Calcular adiantamento 13º com base no salário do mês anterior ao cálculo (0=Não/1=Sim) |
| EXTENDE_LIMITE_GOZO_FERIAS_AFASTAMENTO_03 | smallint(2) |  |  | Extende limite de gozo de férias paar os afastamentos 03 e 10 |
| EXTENDE_LIMITE_GOZO_FERIAS_AFASTAMENTO_06 | smallint(2) |  |  | Extende limite de gozo de férias paar os afastamentos 06 e 12 |
| EXTENDE_LIMITE_GOZO_FERIAS_AFASTAMENTO_19 | smallint(2) |  |  | Extende limite de gozo de férias paar os afastamentos 19 |
| EXTENDE_LIMITE_GOZO_FERIAS_AFASTAMENTO_05 | smallint(2) |  |  | Extende limite de gozo de férias paar os afastamentos 05 |
| EXTENDE_LIMITE_GOZO_FERIAS_AFASTAMENTO_20 | smallint(2) |  |  | Extende limite de gozo de férias paar os afastamentos 20,21 e 22 |
| EXTENDE_LIMITE_GOZO_FERIAS_AFASTAMENTO_11 | smallint(2) |  |  | Extende limite de gozo de férias paar os afastamentos 11 |
| EXTENDE_LIMITE_GOZO_FERIAS_AFASTAMENTO_26 | smallint(2) |  |  | Extende limite de gozo de férias paar os afastamentos 26 |
| EXTENDE_LIMITE_GOZO_FERIAS_AFASTAMENTO_27 | smallint(2) |  |  | Extende limite de gozo de férias paar os afastamentos 27,28 e 29 |
| EXTENDE_LIMITE_GOZO_FERIAS_AFASTAMENTO_13 | smallint(2) |  |  | Extende limite de gozo de férias paar os afastamentos 13 |
| EXTENDE_LIMITE_GOZO_FERIAS_AFASTAMENTO_07 | smallint(2) |  |  | Extende limite de gozo de férias paar os afastamentos 07 |
| EXTENDE_LIMITE_GOZO_FERIAS_AFASTAMENTO_04 | smallint(2) |  |  | Extende limite de gozo de férias paar os afastamentos 04 |
| EXTENDE_LIMITE_GOZO_FERIAS_AFASTAMENTO_14 | smallint(2) |  |  | Extende limite de gozo de férias paar os afastamentos 14,15 e 16 |
| EXTENDE_LIMITE_GOZO_FERIAS_AFASTAMENTO_24 | smallint(2) |  |  | Extende limite de gozo de férias paar os afastamentos 24 |
| ATIVIDADE_EMPRESA_LEI_12546 | smallint(2) |  | S | **SEM USO** |
| ADIANTAMENTO_FORMA_CALCULO_ADMISSAO | smallint(2) |  |  | Forma de cálculo do adiantamento (admissão): (1=Não calcular/2=Proporcional/3=Integral) |
| ADIANTAMENTO_FORMA_CALCULO_FERIAS | smallint(2) |  |  | Forma de cálculo do adiantamento (férias): (1=Não calcular/2=Proporcional/3=Integral) |
| ADIANTAMENTO_FORMA_CALCULO_MATERNIDADE | smallint(2) |  |  | Forma de cálculo do adiantamento (maternidade): (1=Não calcular/2=Proporcional/3=Integral) |
| ADIANTAMENTO_FORMA_CALCULO_OUTROS | smallint(2) |  |  | Forma de cálculo do adiantamento (outros afastamentos): (1=Não calcular/2=Proporcional/3=Integral) |
| ADIANTAMENTO_CONDICAO_ADMISSAO | smallint(2) |  |  | Condição para calcular (admissão): (1=Sempre/2=Se estiver trabalhando na data do pagamento/3=Se estiver trabalhado o mínimo de dias especificado) |
| ADIANTAMENTO_CONDICAO_FERIAS | smallint(2) |  |  | Condição para calcular (férias): (1=Sempre/2=Se estiver trabalhando na data do pagamento/3=Se estiver trabalhado o mínimo de dias especificado) |
| ADIANTAMENTO_CONDICAO_MATERNIDADE | smallint(2) |  |  | Condição para calcular (maternidade): (1=Sempre/2=Se estiver trabalhando na data do pagamento/3=Se estiver trabalhado o mínimo de dias especificado) |
| ADIANTAMENTO_CONDICAO_OUTROS | smallint(2) |  |  | Condição para calcular (outros afastamentos): (1=Sempre/2=Se estiver trabalhando na data do pagamento/3=Se estiver trabalhado o mínimo de dias especificado) |
| ADIANTAMENTO_DIAS_ADMISSAO | integer(4) |  | S | Quantidade mínima de dias trabalhados (admissão) |
| ADIANTAMENTO_DIAS_FERIAS | integer(4) |  | S | Quantidade mínima de dias trabalhados (férias) |
| ADIANTAMENTO_DIAS_MATERNIDADE | integer(4) |  | S | Quantidade mínima de dias trabalhados (maternidade) |
| ADIANTAMENTO_DIAS_OUTROS | integer(4) |  | S | Quantidade mínima de dias trabalhados (outros afastamentos) |
| GERA_VARIAVEIS_HONORARIOS | smallint(2) |  |  | Gerar variáveis do honorários com o valor dos encargos: (0=Não/1=Sim) |
| EMPRESA_ESCRITORIO_HONORARIOS | integer(4) |  | S | Empresa escritório Honorários |
| CALCULAR_DIFERENCA_CONTRIBUICAO_SINDICAL | smallint(2) |  |  | Calcular diferença de contribuição sindical devido alteração salarial: (0=Não/1=Sim) |
| CALCULAR_13_SALARIO_RESCISAO_JUSTA_CAUSA | smallint(2) |  |  | Calcular 13º salário para rescisão com justa causa: (0=Não/1=Sim) |
| LIMITAR_TOTAL_PARCELAS | smallint(2) |  |  | Limitar o total das parcelas de 13º salário: (0=Não/1=Sim) |
| LIMITAR_TOTAL_PARCELAS_PERCENTUAL | numeric(5) |  | S | Percentual de limite do total das parcelas de 13º salário |
| AJUSTAR_CALCULO_13_DEZEMBRO_FAVORAVEL_EMPREGADOR | smallint(2) |  |  | Ajustar cálculo do 13º salário em dezembro favorável ao empregador: (0=Não/1=Sim) |
| PAGAR_ADIANTAMENTO_13_MES_ANTERIOR_ADMITIDO_ANO | smallint(2) |  |  | Pagar adiantamento até o mês anterior para empregados admitidos no ano: (0=Não/1=Sim) |
| SERVICOS_EXCLUSIVOS_TI_TIC | smallint(2) |  | S | **SEM USO** |
| INICIO_CALCULO_LEI_12506_2011 | smallint(2) |  |  | Início do cálculo proporcional para o aviso prévio - Lei 12.506/2011: (1=A partir do primeiro ano trabalhado completo/2=A partir do segundo ano trabalhado completo) |
| MOTIVO_DEMISSAO_LEI_12506_2011 | smallint(2) |  |  | Motivos de demissão para o aviso prévio - Lei 12.506/2011: (0=Todos/2=Demitido sem justa causa/244= 2-Demitido sem justa causa e 44-Rescisão por acordo entre as partes/45=Rescisão contrato intermitente) |
| TIPO_EMPREGADO_CALCULA_ARREDONDAMENTO | smallint(2) |  |  | ***SEM USO*** |
| CALCULA_ARREDONDAMENTO_MENSAL | smallint(2) |  |  | Calcula arredondamento: (0=Não/1=Sim) |
| VALOR_ARREDONDAMENTO_MENSAL | numeric(5) |  | S | Valor de arredondamento |
| FORMA_DESCONTO_ARREDONDAMENTO_MENSAL | smallint(2) |  | S | Forma de Desconto: (0=Não descontar/1=Na próxima folha mensal calculada) |
| CALCULA_ARREDONDAMENTO_COMPLEMENTAR | smallint(2) |  |  | Calcula arredondamento: (0=Não/1=Sim) |
| VALOR_ARREDONDAMENTO_COMPLEMENTAR | numeric(5) |  | S | Valor de arredondamento |
| FORMA_DESCONTO_ARREDONDAMENTO_COMPLEMENTAR | smallint(2) |  | S | Forma de Desconto: (0=Não descontar/1=Na folha mensal seguinte a competência do cálculo/2=Na próxima competência de folha mensal calculada) |
| CALCULA_ARREDONDAMENTO_ADIANTAMENTO | smallint(2) |  |  | Calcula arredondamento: (0=Não/1=Sim) |
| VALOR_ARREDONDAMENTO_ADIANTAMENTO | numeric(5) |  | S | Valor de arredondamento |
| FORMA_DESCONTO_ARREDONDAMENTO_ADIANTAMENTO | smallint(2) |  | S | Forma de Desconto: (0=Não descontar/1=Na folha mensal da competência de cálculo/2=Na próxima folha de adiantamento calculada) |
| CALCULA_ARREDONDAMENTO_FERIAS | smallint(2) |  |  | Calcula arredondamento: (0=Não/1=Sim) |
| VALOR_ARREDONDAMENTO_FERIAS | numeric(5) |  | S | Valor de arredondamento |
| FORMA_DESCONTO_ARREDONDAMENTO_FERIAS | smallint(2) |  | S | Forma de Desconto: (0=Não descontar/1=Na folha mensal da competência de cálculo integral/2=Na folha mensal da competência de cálculo proporcional/3=Na próxima férias calculada) |
| CALCULA_ARREDONDAMENTO_RESCISAO | smallint(2) |  |  | Calcula arredondamento: (0=Não/1=Sim) |
| VALOR_ARREDONDAMENTO_RESCISAO | numeric(5) |  | S | Valor de arredondamento |
| FORMA_DESCONTO_ARREDONDAMENTO_RESCISAO | smallint(2) |  | S | Forma de Desconto: (0=Não descontar/1=Em rescisão complementar) |
| CALCULA_ARREDONDAMENTO_RESCISAO_COMPLEMENTAR | smallint(2) |  |  | Calcula arredondamento: (0=Não/1=Sim) |
| VALOR_ARREDONDAMENTO_RESCISAO_COMPLEMENTAR | numeric(5) |  | S | Valor de arredondamento |
| CALCULA_ARREDONDAMENTO_13_ADIANTAMENTO | smallint(2) |  |  | Calcula arredondamento: (0=Não/1=Sim) |
| VALOR_ARREDONDAMENTO_13_ADIANTAMENTO | numeric(5) |  | S | Valor de arredondamento |
| FORMA_DESCONTO_ARREDONDAMENTO_13_ADIANTAMENTO | smallint(2) |  | S | Forma de Desconto: (0=Não descontar/1=Na folha mensal da competência do cálculo/2=Na folha de 13º salário integral) |
| CALCULA_ARREDONDAMENTO_13_INTEGRAL | smallint(2) |  |  | Calcula arredondamento: (0=Não/1=Sim) |
| VALOR_ARREDONDAMENTO_13_INTEGRAL | numeric(5) |  | S | Valor de arredondamento |
| FORMA_DESCONTO_ARREDONDAMENTO_13_INTEGRAL | smallint(2) |  | S | Forma de Desconto: (0=Não descontar/1=Na folha mensal da competência do cálculo/2=Na próxima folha de 13º salário adiantado calculada/3=Na próxima folha de 13º salário integral calculada) |
| CALCULA_ARREDONDAMENTO_SEMANAL | smallint(2) |  |  | Calcula arredondamento: (0=Não/1=Sim) |
| VALOR_ARREDONDAMENTO_SEMANAL | numeric(5) |  | S | Valor de arredondamento |
| FORMA_DESCONTO_ARREDONDAMENTO_SEMANAL | smallint(2) |  | S | Forma de Desconto: (0=Não descontar/1=Na próxima semana calculada/2=No cálculo da última semana) |
| CONSIDERAR_SABADO_DIA_UTIL_RESCISAO | smallint(2) |  |  | Utilizar o sábado como dia útil para o pagamento de rescisão: (0=Não/1=Sim) |
| CONSIDERAR_ANTECIPACAO_FERIAS_PROPORCIONAL_RESCISAO | smallint(2) |  |  | Considerar a antecipação do período de férias proporcional na rescisão.(0-Não/1-Sim) |
| CONSIDERAR_PROJECAO_AVISO_PREVIO_TEMPO_TRABALHADO | smallint(2) |  |  | Considerar projeção do aviso prévio indenizado como dias trabalhados: (0=Não/1=Sim) |
| CALCULAR_ADICIONAL_FERIAS_ESTAGIARIOS | smallint(2) |  |  | Calcular 1/3 de férias para estagiários. (0=Não/1=Sim) |
| CONSIDERAR_LICENCA_SEM_VENCIMENTO_DILATAR_PERIODO_AQUISITIVO | smallint(2) |  |  | Considerar os dias afastados por licença sem vencimento para dilatar o período aquisitivo. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTOS_DIAS_DIREITO_FERIAS | smallint(2) |  |  | Considerar os afastamentos para o cálculo dos dias de direito. (0=Não/1=Sim) |
| ALIQUOTA_IMPOSTO_RECEITA_ATIVIDADE_NAO_RELACIONADA_LEI_12546 | smallint(2) |  | S | **SEM USO** |
| CALCULAR_SALARIO_PROPORCIONAL_DATA_ALTERACAO | smallint(2) |  |  | Calcular salário no mês da alteração salarial de forma proporcional a data da alteração: (0=Não, 1=Sim) |
| CONSIDERAR_PERIODO_AFASTAMENTO_EM_MESES | smallint(2) |  |  | Considerar período afastamento em meses. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_ACIDENTE_TRABALHO_EM_MESES | smallint(2) |  |  | Considerar afastamento por acidente de trabalho em meses. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_DOENCA_EM_MESES | smallint(2) |  |  | Considerar afastamento por doença em meses. (0=Não/1=Sim) |
| FABRICANTE_EXCLUSIVO_PRODUTOS_RELACIONADOS | smallint(2) |  | S | **SEM USO** |
| EXTENDE_LIMITE_GOZO_FERIAS_AFASTAMENTO_35 | smallint(2) |  |  | Extende limite de gozo de férias para o afastamento 35 |
| EXTENDE_LIMITE_GOZO_FERIAS_AFASTAMENTO_36 | smallint(2) |  |  | Estende limite de gozo de férias para o afastamento 36 (0=Não/1=Sim) |
| CLASSIFICACAO_TRIBUTARIA | smallint(2) |  |  | Classificação tributária. |
| COOPERATIVA | smallint(2) |  |  | Cooperativa. (0=Não/1=Sim, cooperativa de trabalho/2=Sim, cooperativa de produção/3=Sim, outras cooperativas) |
| CONSTRUTORA | smallint(2) |  |  | Construtora. (0=Não/1=Sim) |
| SIGLA_MINISTERIO_CONCEDEU_ENTIDADE_BENEFICENTE | smallint(2) |  | S | Sigla do ministério que concedeu a classificação de Entidade Beneficente. (1=CNAS/2=MEC/3=MS/4=MDS/5=Lei) |
| NUMERO_CERTIFICADO_LEI_ENTIDADE_BENEFICENTE | varchar(40) |  | S | Número do certificado/lei que concedeu a classificação de Entidade Beneficente. |
| DATA_EMISSAO_ENTIDADE_BENEFICENTE | date(4) |  | S | Data de emissão da classificação de Entidade Beneficente. |
| DATA_VENCIMENTO_ENTIDADE_BENEFICENTE | date(4) |  | S | Data de vencimento da classificação de Entidade Beneficente. |
| NUMERO_PROTOCOLO_RENOVACAO_ENTIDADE_BENEFICENTE | varchar(40) |  | S | Número do protocolo de renovação da classificação de Entidade Beneficente. |
| DATA_PROTOCOLO_RENOVACAO_ENTIDADE_BENEFICENTE | date(4) |  | S | Data do protocolo de renovação da Entidade Beneficente. |
| DATA_DIARIO_OFICIAL_UNIAO_ENTIDADE_BENEFICENTE | date(4) |  | S | Data do diário oficial da união da classificação de Entidade Beneficente. |
| PAGINAL_DIARIO_OFICIAL_UNIAO_ENTIDADE_BENEFICENTE | varchar(5) |  | S | Página do diário oficial da união da classificação de Entidade Beneficente. |
| POSSUI_SITUACAO_ESPECIAL | smallint(2) |  |  | Possui Situação especial. (0=Não/1=Sim) |
| POSSUI_SITUACAO_ESPECIAL_SITUACAO | smallint(2) |  | S | Situação especial. (1=Extinção/2=Fusão/3=Cisão/4=Incorporação/5=Encerramento de espólio/6=Saída do país em caráter permanente) |
| PAGAR_MEDIAS_13_ADIANTAMENTO | smallint(2) |  | S | Pagar médias no 13º adiantamento. (0=Não/1=Sim) |
| PAGAR_ADICIONAIS_13_ADIANTAMENTO | smallint(2) |  | S | Pagar adicionais no 13º adiantamento. (0=Não/1=Sim) |
| DESCONTAR_FALTAS_DSR_COMPETENCIA_DATA_FALTA | smallint(2) |  |  | Descontar as faltas de DSR na competência da data da falta. (0=Não/1=Sim) |
| DESCONTAR_DSR_SEMANA_FALTA | smallint(2) |  |  | Descontar o DSR na mesma semana da falta. (0=Não/1=Sim) |
| ADQUIRE_PRODUCAO_RURAL | smallint(2) |  | S | Adquire produção rural. (0=Não/1=Sim) |
| LANCAMENTO_NOTAS_FISCAIS_AQUISICAO_PRODUCAO_RURAL | smallint(2) |  | S | Módulo de lançamento das notas fiscais de adquisição de produção rural. (1=Folha/2=Escrita Fiscal) |
| DATA_INICIO_LANCAMENTO_NOTAS_FISCAIS_AQUISICAO_PRODUCAO_RURAL | date(4) |  | S | Data de início do lançamento das notas fiscais de aquisição de produção rural. |
| COMERCIALIZA_PRODUCAO_RURAL | smallint(2) |  | S | Comercializa produção rural. (0=Não/1=Sim) |
| LANCAMENTO_NOTAS_FISCAIS_COMERCIALIZACAO_PRODUCAO_RURAL | smallint(2) |  | S | Módulo de lançamento das notas fiscais de comercialização de produção rural. (1=Folha/2=Escrita Fiscal) |
| DATA_INICIO_LANCTO_NOTAS_FISCAIS_COMERCIALIZACAO_PRODUCAO_RURAL | date(4) |  | S | Data de início do lançamento das notas fiscais de comercialização de produção rural. |
| CALCULAR_ARREDONDAMENTO_EMPREGADOS | smallint(2) |  |  | Calcular arredondamento para empregados. (0=Não/1=Sim) |
| CALCULAR_ARREDONDAMENTO_ESTAGIARIOS | smallint(2) |  |  | Calcular arredondamento para estagiários. (0=Não/1=Sim) |
| CALCULAR_ARREDONDAMENTO_CONTRIBUINTES | smallint(2) |  |  | Calcular arredondamento para contribuintes. (0=Não/1=Sim) |
| CALCULAR_FOLHA_ADIANTAMENTO_ESTAGIARIOS | smallint(2) |  |  | Calcular folha de adiantamento para estagiários. (0=Não/1=Sim) |
| CONSIDERAR_DIAS_AVISO_INDENIZADO_FERIAS_DOBRO | smallint(2) |  |  | Considerar os dias de aviso prévio indenizado para o cálculo das férias em dobro. (0=Não/1=Sim) |
| TOMADOR_SERVICOS | smallint(2) |  |  | Tomador de serviços. (0=Não/1=Sim) |
| LANCAMENTO_NOTAS_FISCAIS_TOMADOR_SERVICOS | smallint(2) |  |  | Módulo de lançamento das notas fiscais de tomador de serviços. (1=Folha/2=Escrita Fiscal) |
| DATA_INICIO_LANCAMENTO_NOTAS_FISCAIS_TOMADOR_SERVICOS | date(4) |  | S | Data de início do lançamento das notas fiscais de tomador de serviços. |
| PRESTADOR_SERVICOS | smallint(2) |  |  | Prestador de serviços. (0=Não/1=Sim) |
| LANCAMENTO_NOTAS_FISCAIS_PRESTADOR_SERVICOS | smallint(2) |  |  | Módulo de lançamento das notas fiscais de prestador de serviços. (1=Folha/2=Escrita Fiscal) |
| DATA_INICIO_LANCAMENTO_NOTAS_FISCAIS_PRESTADOR_SERVICOS | date(4) |  | S | Data de início do lançamento das notas fiscais de prestador de serviços. |
| RECURSOS_CLUBE_FUTEBOL | smallint(2) |  |  | Recursos de clube de futebol. (0=Não/1=Sim) |
| TIPO_RECURSO_CLUBE_FUTEBOL | smallint(2) |  | S | Tipos de recurso de clube de futebol. |
| POSSUI_SCP | smallint(2) |  |  | Possui Sociedade em Conta de Participação - SCP. (0=Não/1=Sim) |
| CALCULAR_DSR_DIURNO | smallint(2) |  |  | Calcular DSR diurno. (0=Não/1=Sim) |
| CALCULAR_DSR_NOTURNO | smallint(2) |  |  | Calcular DSR noturno. (0=Não/1=Sim) |
| PERMITIR_SALARIO_CONTRATUAL_ABAIXO_DO_PISO_SALARIAL | smallint(2) |  |  | Permitir salário contratual abaixo do piso salarial. (0=Não/1=Sim) |
| CALC_13_SAL_PROPORC_RESCISAO_ANTEC_EMPREGADOR_FALTA_DISC_APREND | smallint(2) |  |  | Calcular 13º salário proporcional para a rescisão com motivo antecipado pelo empregador por falta disciplinar grave do aprendiz. |
| CALCULAR_TERCO_FERIAS_LICENCA_REMUNERADA | smallint(2) |  |  | Calcular 1/3 de férias na licença remunerada. |
| CONS_COMISSAO_COMP_ANTERIOR_CALCULO_ADIANTAMENTO_COMISSIONADO | smallint(2) |  |  | Considerar para empregado comissionado o valor pago de comissão na competência anterior ao cálculo da folha de adiantamento. (0=Não/1=Sim) |
| CALCULAR_MEDIA_ADICIONAL_MULTA_ATRASO_PAGAMENTO_ART_477 | smallint(2) |  | S | Calcular média e adicional na multa atraso pagamento Art. 477, §8º/CLT. (0=Não/1=Sim) |
| FORMA_DATA_PAGAMENTO_FOLHA_MENSAL_CONTRIBUINTE | smallint(2) |  |  | 1-Último dia útil do mês de competência, 2-Quinto dia útil do mês seguinte e 3-Primeiro dia útil do mês seguinte |
| ANTECIPA_DATA_PAGTO_RESCISAO_CONTRATO_ANTECIPADO_EMPREGADOR | smallint(2) |  |  | Antecipar data de pagamento da rescisão de contrato antecipado pelo empregado. (0=Não/1=Sim) |
| CONSIDERAR_DIAS_AFASTADOS_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  | S | Considerar os dias afastados durante o contrato de experiência para dilatar o limite do término do contrato. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_02_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  | S | Considerar os dias afastados pelo afastamento 02 para dilatar o contrato de experiência. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_03_10_17_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  | S | **SEM USO** |
| CONSIDERAR_AFASTAMENTO_18_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  | S | Considerar os dias afastados pelo afastamento 18 para dilatar o contrato de experiência. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_04_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  | S | Considerar os dias afastados pelo afastamento 04 para dilatar o contrato de experiência. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_19_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  | S | Considerar os dias afastados pelo afastamento 19 para dilatar o contrato de experiência. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_05_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  | S | Considerar os dias afastados pelo afastamento 05 para dilatar o contrato de experiência. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_20_21_22_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  | S | Considerar os dias afastados pelos afastamentos 20, 21 e 22 para dilatar o contrato de experiência. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_11_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  | S | Considerar os dias afastados pelo afastamento 11 para dilatar o contrato de experiência. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_26_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  | S | Considerar os dias afastados pelo afastamento 26 para dilatar o contrato de experiência. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_27_28_29_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  | S | Considerar os dias afastados pelos afastamentos 27, 28 e 29 para dilatar o contrato de experiência. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_32_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  | S | Considerar os dias afastados pelo afastamento 32 para dilatar o contrato de experiência. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_07_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  | S | Considerar os dias afastados pelo afastamento 07 para dilatar o contrato de experiência. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_13_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  | S | Considerar os dias afastados pelo afastamento 13 para dilatar o contrato de experiência. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_14_15_16_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  | S | Considerar os dias afastados pelos afastamentos 14, 15, 16 para dilatar o contrato de experiência. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_24_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  | S | Considerar os dias afastados pelo afastamento 24 para dilatar o contrato de experiência. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_35_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  | S | Considerar os dias afastados pelo afastamento 35 para dilatar o contrato de experiência. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_36_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  | S | Considerar os dias afastados pelo afastamento 36 para dilatar o contrato de experiência. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_30_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  | S | Considerar os dias afastados pelo afastamento 30 para dilatar o contrato de experiência. (0=Não/1=Sim) |
| CALCULAR_TERCO_FERIAS_SOBRE_VALOR_SALARIO_CONTRATUAL | smallint(2) |  | S | Calcular 1/3 de férias sobre o valor do salário contratual. (0=Não/1=Sim) |
| CALCULAR_PROPORCIONALIDADE_RESCISAO_CONFORME_DIAS_MES | smallint(2) |  |  | Cálculo proporcionalidade na rescisão conforme dias mês. (0=Não/1=Sim) |
| DESCONTAR_FALTAS_AVOS_FERIAS_INDENIZADOS | smallint(2) |  |  | Descontar faltas sobre os avos de férias indenizados. (0=Não/1=Sim) |
| EXTENDE_LIMITE_GOZO_FERIAS_AFASTAMENTO_39 | smallint(2) |  |  | Extende o limite de gozo de férias para o afastamento 39. (0=Não/1=Sim) |
| CONSIDERAR_HORAS_MES_EMPREGADO_PARA_CALCULO_HORAS_FALTAS | smallint(2) |  |  | Considerar para cálculo de horas faltas o total de horas mês do empregado. (0=Não/1=Sim) |
| CALC_INSS_EMPRESA_13_SALARIO_RESCISAO_PERC_REDUCAO_ULT_12_MESES | smallint(2) |  |  | Calcular o INSS Empresa correspondente ao 13º salário pago na rescisão conforme o percentual de redução obtido pelo resultado das receitas dos últimos 12 meses. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_CALCULO_DIAS_DIREITO_13_SALARIO | smallint(2) |  |  | Considerar os afastamentos para o cálculo dos dias de direito de 13º salário. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_03_CALCULO_DIAS_DIREITO_13_SALARIO | smallint(2) |  |  | Considerar o afastamento 03 para o cálculo dos dias de direito de 13º salário. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_06_CALCULO_DIAS_DIREITO_13_SALARIO | smallint(2) |  |  | Considerar o afastamento 06 para o cálculo dos dias de direito de 13º salário. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_07_CALCULO_DIAS_DIREITO_13_SALARIO | smallint(2) |  |  | Considerar o afastamento 07 para o cálculo dos dias de direito de 13º salário. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_20_21_22_CALCULO_DIAS_DIREITO_13_SALARIO | smallint(2) |  |  | Considerar os afastamentos 20, 21 e 22 para o cálculo dos dias de direito de 13º salário. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_13_CALCULO_DIAS_DIREITO_13_SALARIO | smallint(2) |  |  | Considerar o afastamento 13 para o cálculo dos dias de direito de 13º salário. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_04_CALCULO_DIAS_DIREITO_13_SALARIO | smallint(2) |  |  | Considerar o afastamento 04 para o cálculo dos dias de direito de 13º salário. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_14_15_16_CALCULO_DIAS_DIREITO_13_SALARIO | smallint(2) |  |  | Considerar os afastamentos 14, 15 e 16 para o cálculo dos dias de direito de 13º salário. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_35_CALCULO_DIAS_DIREITO_13_SALARIO | smallint(2) |  |  | Considerar o afastamento 35 para o cálculo dos dias de direito de 13º salário. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_24_CALCULO_DIAS_DIREITO_13_SALARIO | smallint(2) |  |  | Considerar o afastamento 24 para o cálculo dos dias de direito de 13º salário. (0=Não/1=Sim) |
| CONSIDERAR_MES_AFASTADO_PERIODO_MEDIA_13_SALARIO | smallint(2) |  |  | Considerar o mês do afastamento no cálculo de médias e adicionais de 13º salário, mesmo que não tenha direito ao avo do mês. (0=Não/1=Sim) |
| CONSIDERAR_MES_AFASTADO_AFASTAMENTO_07_PERIODO_MEDIA_13_SALARIO | smallint(2) |  |  | Considerar o mês do afastamento 07 no cálculo de médias e adicionais de 13º salário, mesmo que não tenha direito ao avo do mês. (0=Não/1=Sim) |
| CONSIDERAR_MES_AFASTADO_AFASTAMENTO_13_PERIODO_MEDIA_13_SALARIO | smallint(2) |  |  | Considerar o mês do afastamento 13 no cálculo de médias e adicionais de 13º salário, mesmo que não tenha direito ao avo do mês. (0=Não/1=Sim) |
| CONSIDERAR_MES_AFAST_AFASTAMENTOS_14_15_16_PER_MEDIA_13_SALARIO | smallint(2) |  |  | Considerar o mês dos afastamentos 14, 15 e 16 no cálculo de médias e adicionais de 13º salário, mesmo que não tenha direito ao avo do mês. (0=Não/1=Sim) |
| CONSIDERAR_MES_AFASTADO_AFASTAMENTO_24_PERIODO_MEDIA_13_SALARIO | smallint(2) |  |  | Considerar o mês do afastamento 24 no cálculo de médias e adicionais de 13º salário, mesmo que não tenha direito ao avo do mês. (0=Não/1=Sim) |
| CONSIDERAR_MES_AFASTADO_AFASTAMENTO_35_PERIODO_MEDIA_13_SALARIO | smallint(2) |  |  | Considerar o mês do afastamento 35 no cálculo de médias e adicionais de 13º salário, mesmo que não tenha direito ao avo do mês. (0=Não/1=Sim) |
| CONSIDERAR_MES_AFASTADO_AFASTAMENTO_36_PERIODO_MEDIA_13_SALARIO | smallint(2) |  |  | Considerar o mês do afastamento 36 no cálculo de médias e adicionais de 13º salário, mesmo que não tenha direito ao avo do mês. (0=Não/1=Sim) |
| EFETUAR_LANCAMENTO_RUBRICAS_POR_SERVICO | smallint(2) |  |  | Efetuar lançamento de rubricas por serviço. (0=Não/1=Sim) |
| CALCULA_CARNE_LEAO | smallint(2) |  |  | Calcula Carnê-Leão. (0=Não/1=Sim) |
| CALCULAR_ADIANTAMENTO_13_SALARIO_FOLHA_MENSAL | smallint(2) |  |  | Calcular adiantamento de 13º salário na folha mensal. (0=Não/1=Sim) |
| UNIDADE_CALCULO_MENSALISTAS | smallint(2) |  |  | Unidade do cálculo para mensalistas. (1=Horas/2=Dias) |
| UNIDADE_CALCULO_SEMANALISTAS | smallint(2) |  |  | Unidade do cálculo para semanalistas. (1=Horas/2=Dias) |
| UNIDADE_CALCULO_TAREFEIROS | smallint(2) |  |  | Unidade do cálculo para tarefeiros. (1=Horas/2=Dias) |
| UNIDADE_CALCULO_DIARISTAS | smallint(2) |  |  | Unidade do cálculo para diaristas. (1=Horas/2=Dias) |
| UNIDADE_CALCULO_COMISSIONADOS | smallint(2) |  |  | Unidade do cálculo para comissionados. (1=Horas/2=Dias) |
| PAGAR_LIC_REMUNERADA_DIAS_GOZO_EXCEDE_DIAS_DIREITO_PERDA_FALTAS | smallint(2) |  |  | Pagar dias de gozo excedentes aos dias de direito como licença remunerada quando há perda de dias por faltas. (0=Não/1=Sim) |
| CALCULA_ARREDONDAMENTO_PARTICIPACAO_LUCROS | smallint(2) |  |  | Calcula arredondamento. (0=Não/1=Sim) |
| VALOR_ARREDONDAMENTO_PARTICIPACAO_LUCROS | numeric(5) |  | S | Valor de arredondamento. |
| FORMA_DESCONTO_ARREDONDAMENTO_PARTICIPACAO_LUCROS | smallint(2) |  | S | Forma de desconto. (0=Não descontar/1=Na folha mensal da competência de cálculo/2=Na próxima folha de participação de lucros calculada) |
| CTA_DATA_LANC_PARTICIPACAO_LUCROS | smallint(2) |  | S | Data do lançamento para folha de participação de lucros. (1=Final do mês/2=Data de pagamento) |
| CALC_LIC_REMUN_APRENDIZ_MENOR_18_ANOS_FORA_PER_FERIAS_ESCOLARES | smallint(2) |  |  | Calcular licença remunerada para empregado menor de 18 anos quando as férias coletivas não coincidirem com as férias escolares. (0=Não/1=Sim) |
| CONSIDERAR_JANEIRO_PERIODO_FERIAS_ESCOLARES | smallint(2) |  |  | Considerar janeiro como período de férias escolares. (0=Não/1=Sim) |
| CONSIDERAR_FEVEREIRO_PERIODO_FERIAS_ESCOLARES | smallint(2) |  |  | Considerar fevereiro como período de férias escolares. (0=Não/1=Sim) |
| CONSIDERAR_MARCO_PERIODO_FERIAS_ESCOLARES | smallint(2) |  |  | Considerar março como período de férias escolares. (0=Não/1=Sim) |
| CONSIDERAR_ABRIL_PERIODO_FERIAS_ESCOLARES | smallint(2) |  |  | Considerar abril como período de férias escolares. (0=Não/1=Sim) |
| CONSIDERAR_MAIO_PERIODO_FERIAS_ESCOLARES | smallint(2) |  |  | Considerar maio como período de férias escolares. (0=Não/1=Sim) |
| CONSIDERAR_JUNHO_PERIODO_FERIAS_ESCOLARES | smallint(2) |  |  | Considerar junho como período de férias escolares. (0=Não/1=Sim) |
| CONSIDERAR_JULHO_PERIODO_FERIAS_ESCOLARES | smallint(2) |  |  | Considerar julho como período de férias escolares. (0=Não/1=Sim) |
| CONSIDERAR_AGOSTO_PERIODO_FERIAS_ESCOLARES | smallint(2) |  |  | Considerar agosto como período de férias escolares. (0=Não/1=Sim) |
| CONSIDERAR_SETEMBRO_PERIODO_FERIAS_ESCOLARES | smallint(2) |  |  | Considerar setembro como período de férias escolares. (0=Não/1=Sim) |
| CONSIDERAR_OUTUBRO_PERIODO_FERIAS_ESCOLARES | smallint(2) |  |  | Considerar outubro como período de férias escolares. (0=Não/1=Sim) |
| CONSIDERAR_NOVEMBRO_PERIODO_FERIAS_ESCOLARES | smallint(2) |  |  | Considerar novembro como período de férias escolares. (0=Não/1=Sim) |
| CONSIDERAR_DEZEMBRO_PERIODO_FERIAS_ESCOLARES | smallint(2) |  |  | Considerar dezembro como período de férias escolares. (0=Não/1=Sim) |
| SOMAR_ENCARGOS_FOLHA_COMPLEMENTAR_NA_FOLHA_MENSAL | smallint(2) |  |  | Somar encargos da folha complementar na folha mensal quando forem inferiores ao mínimo de recolhimento. (0=Não/1=Sim) |
| CALCULAR_DIARIAS | smallint(2) |  |  | Calcular diárias. (0=Não/1=Sim) |
| TIPO_CONSIDERACAO_REMUNERACAO_DIARIAS | smallint(2) |  | S | Considerar como remuneração para diárias. (1=Salário contratual/2=Salário e adicionais) |
| CONSIDERAR_MEDIA_PRIMEIRO_AFAST_PARA_MESMA_DOENCA_ACIDENTE | smallint(2) |  |  | Considerar para um novo afastamento mesma doença/acidente, as médias utilizadas para o primeiro afastamento. (0=Não/1=Sim) |
| EXTENDE_LIMITE_GOZO_FERIAS_AFASTAMENTO_41 | smallint(2) |  |  | Extende limite de gozo de férias para o afastamento 41. |
| CONSIDERAR_GARANTIA_MINIMA_ADIANTAMENTO_COMISSIONADO | smallint(2) |  |  | Considerar para empregado comissionado o valor da garantia mínima do cálculo do adiantamento. (0=Não/1=Sim) |
| CALCULAR_MEDIA_13_COMISSAO_TROCA_CATEG_COMISSIONADO_MENSALISTA | smallint(2) |  |  | Não calcular médias de 13º salário sobre comissões do período que o empregado era comissionado quando alterada a categoria para mensalista. (0=Não/1=Sim) |
| CALC_MEDIA_FERIAS_COMISSAO_TROCA_CATEG_COMISSIONADO_MENSALISTA | smallint(2) |  |  | Não calcular médias de férias sobre comissões do período que o empregado era comissionado quando alterada a categoria para mensalista. (0=Não/1=Sim) |
| GERAR_LICENCA_REMUNERADA_CALCULO_FERIAS | smallint(2) |  |  | Gerar o valor da licença remunerada no cálculo das férias. (0=Não/1=Sim) |
| CALCULAR_PIS_COMPETENCIA_PAGAMENTO_FERIAS | smallint(2) |  |  | ** SEM USO ** |
| TIPO_RATEIO | smallint(2) |  |  | Tipo de rateio. (1=Conforme o total de dias em cada serviço/2=Conforme período em cada serviço) |
| CALCULAR_SALARIO_FAMILIA_DURANTE_AFAST_AUSENCIA_JUSTIFICADA | smallint(2) |  |  | Calcular salário família durante o afastamento por ausência justificada. (0=Não/1=Sim) |
| EXTENDE_LIMITE_GOZO_FERIAS_AFASTAMENTO_34 | smallint(2) |  |  | Extende o limite de gozo de férias para o afastamento 34. (0=Não/1=Sim) |
| CALCULAR_DIFERENCA_RUBRICAS_SALARIO_PERIODO_AFASTAMENTO_DOENCA | smallint(2) |  |  | Calcular a diferença de rubricas com base de cálculo salário quando houver alteração salarial retroativa a período em que o empregado esteve afastado por doença. (0=Não/1=Sim) |
| CALCULAR_INSS_EMPRESA_13_RESCISAO_SEM_PROPORCIONALIDADE | smallint(2) |  |  | **SEM USO** |
| CALCULAR_FERIAS_SALARIO_MEDIO_QUANDO_HOUVER_REDUCAO_SALARIAL | smallint(2) |  |  | Calcular as férias com valor do salário médio do período aquisitivo quando houver redução de salário. (0=Não/1=Sim) |
| DESCONTAR_VAL_13_ADIANTAMENTO_QUANDO_EXISTIR_ALTERACAO_SALARIAL | smallint(2) |  |  | Descontar do cálculo de 13º adiantamento o valor de 13º já adiantado em competências anteriores se possuir alteração salarial. (0=Não/1=Sim) |
| CALCULAR_DIFERENCA_SALARIO_FAMILIA | smallint(2) |  |  | Calcular diferença de salário família. (0=Não/1=Sim) |
| PERMITE_IMPORTAR_NOTA_FISCAL_CPF_AQUISICAO_PRODUCAO_RURAL_PJ | smallint(2) |  |  | Permite importar notas fiscais com CPF na Aquisição de Produção Rural PJ. (0=Não/1=Sim) |
| PERMITE_IMP_NOTA_FISCAL_CPF_COMERCIALIZACAO_PRODUCAO_RURAL_PJ | smallint(2) |  |  | Permite importar notas fiscais com CPF na Comercialização de Produção Rural PJ. (0=Não/1=Sim) |
| PERMITIR_CALCULAR_VARIOS_ADIANTAMENTOS_COMPETENCIA | smallint(2) |  |  | Permitir calcular várias folhas de adiantamento na mesma competência. (0=Não/1=Sim) |
| LIMITAR_PERCENTUAL_ADIANTAMENTO_MENSAL_COMPETENCIA | smallint(2) |  |  | Limitar o percentual de adiantamento pago na competência. (0=Não/1=Sim) |
| LIMITE_PERCENTUAL_ADIANTAMENTO_MENSAL | numeric(8) |  | S | Limite de percentual pago nas folhas de adiantamento na competência. |
| CONSIDERAR_DIAS_FERIAS_CALCULAR_CONTRIBUICAO_SINDICAL | smallint(2) |  |  | Calcular a contribuição sindical nas férias, de acordo com a quantidade de dias de férias na competência de desconto. (0=Não/1=Sim) |
| QUANTIDADE_MINIMA_DIAS_FERIAS_CALCULAR_CONTRIBUICAO_SINDICAL | smallint(2) |  | S | Quantidade mínima de dias de férias na competência para calcular o desconto da contribuição sindical. |
| DESCONTAR_DSR_FERIADO | smallint(2) |  |  | Descontar o DSR quando recair em feriado. (1=Não/0=Sim) |
| OPTANTE_REGISTRO_ELETRONICO_EMPREGADOS | smallint(2) |  |  | Optante pelo registro eletrônico de empregados. (0=Não/1=Sim) |
| POSSUI_ACORDO_INTERNACIONAL_ISENCAO_MULTA | smallint(2) |  |  | Possui acordo internacional para isenção de multa. (0=Não/1=Sim) |
| CONSIDERAR_AVISO_PREVIO_INDENIZADO_CALCULO_SALARIO_FAMILIA | smallint(2) |  |  | Considerar o valor de aviso prévio indenizado para o cálculo do salário família. (0=Não/1=Sim) |
| PAGAR_PRIMEIROS_90_DIAS_AFASTAMENTO_SERVICO_MILITAR | smallint(2) |  |  | Pagar os primeiros 90 dias de afastamento por serviço militar. (0=Não/1=Sim) |
| GERAR_DATA_TRANSFERENCIA_SAIDA_CAGED | smallint(2) |  |  | Gerar a data da rescisão pelos motivos 6 e 27 como data de transferência de saída para o CAGED. (0=Não/1=Sim) |
| DESCONTAR_FALTA_DSR_CONFORME_FOLGA_JORNADA | smallint(2) |  |  | Descontar as faltas de DSR conforme o dia de folga da jornada do empregado. (0=Não/1=Sim) |
| CALCULAR_IRRF_RPA_MICROEMPREENDEDOR_INDIVIDUAL | smallint(2) |  |  | Calcular IRRF no RPA para microempreendedor individual. (0=Não/1=Sim) |
| CALCULAR_PERIODO_COMPLETO_FERIAS_DOBRO_APOS_LIMITE_GOZO | smallint(2) |  |  | Calcular o período completo de férias em dobro quando ultrapassar a data do limite para gozo. (0=Não/1=Sim) |
| EXTENDE_LIMITE_GOZO_FERIAS_AFASTAMENTO_50 | smallint(2) |  |  | Extende limite de gozo de férias para o afastamento 50. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_DOENCA_PROFISSIONAL_EM_MESES | smallint(2) |  |  | Considerar afastamento por doença profissional em meses. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTOS_50_CALCULO_DIAS_DIREITO_13_SALARIO | smallint(2) |  |  | Considerar afastamento por doença profissional em meses. (0=Não/1=Sim) |
| CALC_CONTRIBUICAO_SIND_REMUNERACAO_MES_ANTERIOR_COMISSIONADO | smallint(2) |  |  | Calcular contribuição sindical com base na remuneração do mês anterior para comissionado. (0=Não/1=Sim) |
| PERMITE_LANCAR_AFAST_DOENCA_ACIDENTE_TRAB_15_DIAS_QUALQ_DATA | smallint(2) |  |  | Permitir utilizar os motivos de afastamento 3, 6, 17 e 18 em qualquer data. (0=Não/1=Sim) |
| DEMONSTRAR_MENSAGEM_AVISO_FERIAS_MENORES_18_MAIORES_50_ANOS | smallint(2) |  |  | Demonstrar mensagem de aviso ao calcular férias com abono pecuniário para menores de 18 e maiores de 50 anos. (0=Não/1=Sim) |
| EXTENDE_LIMITE_GOZO_FERIAS_AFASTAMENTO_18_45 | smallint(2) |  |  | Extende limite de gozo de férias para os afastamentos 18 e 45. (0=Não/1=Sim) |
| PERMITIR_INFORMAR_DATA_LANCAMENTO_FALTA_PARCIAL | smallint(2) |  |  | Permitir informar datas nos lançamentos de faltas parciais. (0=Não/1=Sim) |
| CALCULAR_RATEIO_ENCARGOS_PROPORCIONAL_VALOR_SERVICO | smallint(2) |  |  | Realizar o rateio dos encargos proporcionalmente ao valor de cada serviço. (0=Não/1=Sim) |
| CALC_INSS_EMPRESA_13_SALARIO_RESCISAO_CONFORME_ULTIMO_SERVICO | smallint(2) |  |  | **SEM USO** |
| DESCONTAR_FALTAS_NOTURNAS_FERIAS | smallint(2) |  |  | Descontar faltas noturnas. (0=Não/1=Sim) |
| CONSIDERAR_VALOR_DSR_APRENDIZ_DIMINUIR_HORAS_TRABALHADAS | smallint(2) |  |  | Considerar o valor de DSR aprendiz para diminuir das horas trabalhadas. (0=Não/1=Sim) |
| GERAR_VALORES_AVISO_PREVIO_INDENIZADO_SEFIP | smallint(2) |  |  | Gerar os valores de aviso prévio indenizado na SEFIP da competência da rescisão. (0=Não/1=Sim) |
| CONSIDERAR_MES_AFASTAMENTO_DIVISOR_CALCULO_MEDIAS | smallint(2) |  |  | Considerar o mês do afastamento como divisor no cálculo de médias mesmo que não tenha direito ao avo no mês. (0=Não/1=Sim) |
| CONSIDERAR_MES_AFAST_DIVISOR_CALCULO_MEDIAS_LISTA_AFASTAMENTOS | integer(4) |  |  | Lista de afastamentos para considerar como divisor no cálculo de médias mesmo quando não há direito ao avo. |
| CALC_MULTA_PEDIDO_DEMISSAO_PER_ESTABILIDADE_ACIDENTE_TRABALHO | smallint(2) |  |  | Calcular multa estabilidade para colaboradores que pediram demissão em período de estabilidade por acidente de trabalho. (0=Não/1=Sim) |
| INTEGRAR_IRRF_FERIAS_DATA_PAGAMENTO_FERIAS | smallint(2) |  |  | Integrar IRRF Férias na data do pagamento das férias. (0=Não/1=Sim) |
| GERAR_LANCAMENTO_CONTABIL_AJUSTE_SEFIP_PAGAMENTO_ENCARGOS | smallint(2) |  |  | Gerar o valor do ajuste SEFIP no momento do pagamento dos encargos de INSS, FGTS e GRRF. (0=Não/1=Sim) |
| CALCULAR_PROPORCIONALIDADE_30_DIAS_RESCISAO | smallint(2) |  |  | Calcular proporcionalidade na rescisão sempre 30 dias. (0=Não/1=Sim) |
| LIMITAR_DILATACAO_LIMITE_GOZO_FERIAS_12_MESES_POST_RET_AFAST | smallint(2) |  |  | Limitar a dilatação do limite de gozo para 12 meses posteriores ao retorno do afastamento. (0=Não/1=Sim) |
| CALCULAR_FERIAS_PERIODO_GOZO_INFERIOR_10_DIAS | smallint(2) |  |  | Calcular férias com dias de gozo inferior a 10 dias. (0=Não/1=Sim) |
| CALC_ENCARGOS_INSS_INTEG_MESES_INICIO_RET_LIC_MAT_CONTRIBUINTES | smallint(2) |  |  | Calcular os encargos de INSS integralmente nos meses de início e retorno da licença maternidade. (0=Não/1=Sim) |
| UTILIZAR_QUANTIDADE_DIAS_UTEIS_DIVISOR_HORAS_MES_DSR_HORISTA | smallint(2) |  |  | Utilizar para o cálculo de DSR horista a quantidade de dias úteis do mês como divisor do total de horas mês. (0=Não/1=Sim) |
| CALC_PERC_INSS_EMP_13_SAL_PROPORC_AVO_DES_SERV_NAO_ENQUADRA_DES | smallint(2) |  |  | **SEM USO** |
| DESCONTAR_FALTAS_SUSPENSAO | smallint(2) |  |  | Descontar faltas por suspensão. (0=Não/1=Sim) |
| CONSIDERAR_BASE_MULTIPLOS_VINCULOS_CALCULO_INSS_FERIAS | smallint(2) |  |  | Calcular o INSS das férias utilizando os valores de Outras Bases de INSS. (0=Não/1=Sim) |
| INF_DATA_SOLIC_ABONO_PECUN_AVISO_FER_15_DIA_ANTE_VENC_PER_AQUIS | smallint(2) |  |  | Informar data da solicitação do abono pecuniário 15 dias antes do fim do período aquisitivo. (0=Não/1=Sim) |
| CONSIDERA_SOMENTE_QUANT_DIAS_TRAB_CONTAGEM_AVO_13_SAL_RET_AFAST | smallint(2) |  |  | Considerar para o avo de 13º salário na competência de retorno do afastamento somente a quantidade de dias trabalhados no mês. (0=Não/1=Sim) |
| CALCULAR_ENCARGOS_MULTA_ESTABILIDADE | smallint(2) |  |  | Calcular encargos sobre multa estabilidade. (0=Não/1=Sim) |
| CONSIDERAR_PERIODO_SINDICATO_PAGAMENTO_ALTERACAO_RETROATIVA_CCT | smallint(2) |  |  | Considerar o período vinculado a cada sindicato para o cálculo de alteração salarial conforme Convenção Coletiva de Trabalho. (0=Não/1=Sim) |
| CALCULAR_ENCARGOS_HORAS_REPOUSO_INDENIZADO_RESCISAO | smallint(2) |  |  | Calcular encargos sobre as horas de repouso indenizado na rescisão. (0=Não/1=Sim) |
| CONSIDERAR_5_MESES_ESTABILIDADE_LICENCA_MATERNIDADE | smallint(2) |  |  | Considerar 5 meses de estabilidade para empregados afastados por licença remunerada. (0=Não/1=Sim) |
| CONSIDERAR_DIAS_MES_CONTAGEM_AVOS_FERIAS | smallint(2) |  |  | Considerar os dias para contagem dos avos de férias conforme os dias do mês. (0=Não/1=Sim) |
| CALCULO_PROPORCIONAL_FERIAS_SEMPRE_30_DIAS | smallint(2) |  |  | Cálculo proporcionalidade nas férias sempre 30 dias. (0=Não/1=Sim) |
| CALCULAR_INSS_EMP_13_SAL_PROPORC_MESES_DES_EMP_NAO_ENQUADRA_DES | smallint(2) |  |  | Calcular INSS Empresa sobre 13º salário proporcionalmente aos meses com desoneracação e sem desoneração quando a empresa não for mais enquadrado na desonaração. (0=Não/1=Sim) |
| CONSIDERAR_DIAS_MES_CALCULO_COMPETENCIA_INICIO_ESTAGIO | smallint(2) |  |  | Considerar os dias do mês para cálculo da competência de início do estágio. (0=Não/1=Sim) |
| CALCULAR_SAL_FAMILIA_EPR_DOMESTICO_DURANTE_PERIODO_LICENCA_MAT | smallint(2) |  |  | Calcular salário família para empregados domésticos durante o período de licença maternidade. (0=Não/1=Sim) |
| CALCULAR_ADIANTAMENTO_COMPETENCIA_FERIAS | smallint(2) |  |  | Calcular adiantamento na competência de férias. (0=Não/1=Sim) |
| CALCULAR_ADIANTAMENTO_PROPORC_DIAS_TRABALHADOS_COMP_FERIAS | smallint(2) |  |  | Calcular adiantamento proporcional aos dias trabalhados na competência de férias. (0=Não/1=Sim) |
| CALC_ADIANTAMENTO_PROPORC_COMP_FERIAS_SOMENTE_TRAB_DATA_PAGTO | smallint(2) |  |  | Calcular adiantamento proporcional na competência de férias somente se estiver trabalhando na data do pagamento. (0=Não/1=Sim) |
| CALC_ADIANTAMENTO_PROPORC_COMP_FERIAS_MINIMO_DIAS_TRABALHADOS | smallint(2) |  |  | Calcular adiantamento proporcional na competência de férias dependendo da quantidade de dias trabalhados. (0=Não/1=Sim) |
| CALC_ADIANTAMENTO_PROPO_COMP_FERIAS_MINIMO_DIAS_TRABALHADOS_QTD | smallint(2) |  | S | Quantidade mínima de dias trabalhados na competência de férias para pagamento do adiantamento. |
| CALCULAR_ADIANTAMENTO_COMPETENCIA_LICENCA_MATERNIDADE | smallint(2) |  |  | Calcular adiantamento na competência de licença maternidade. (0=Não/1=Sim) |
| CALC_ADIANTAMENTO_PROPORC_DIAS_TRABALHADOS_COMP_LICENCA_MAT | smallint(2) |  |  | Calcular adiantamento proporcional aos dias trabalhados na competência de licença maternidade. (0=Não/1=Sim) |
| CALC_ADIANTAMENTO_PROPORC_COMP_LIC_MAT_SOMENTE_TRAB_DATA_PAGTO | smallint(2) |  |  | Calcular adiantamento proporcional na competência de licença maternidade somente se estiver trabalhando na data do pagamento. (0=Não/1=Sim) |
| CALC_ADIANTAMENTO_PROPORC_COMP_LIC_MAT_MINIMO_DIAS_TRABALHADOS | smallint(2) |  |  | Calcular adiantamento proporcional na competência de licença maternidade dependendo da quantidade de dias trabalhados. (0=Não/1=Sim) |
| CALC_ADIANTAMENTO_PROPORC_COMP_LIC_MAT_MIN_DIAS_TRABALHADOS_QTD | smallint(2) |  | S | Quantidade mínima de dias trabalhados na competência de licença maternidade para pagamento do adiantamento. |
| CALCULAR_ADIANTAMENTO_COMPETENCIA_OUTROS_AFASTAMENTOS | smallint(2) |  |  | Calcular adiantamento na competência de outros afastamentos. (0=Não/1=Sim) |
| CALC_ADIANTAMENTO_PROPORC_DIAS_TRABALHADOS_COMP_OUTROS_AFAST | smallint(2) |  |  | Calcular adiantamento proporcional aos dias trabalhados na competência de outros afastamentos. (0=Não/1=Sim) |
| CALC_ADIANTAME_PROPORC_COMP_OUTRO_AFAST_SOMENTE_TRAB_DATA_PAGTO | smallint(2) |  |  | Calcular adiantamento proporcional na competência de outros afastamentos somente se estiver trabalhando na data do pagamento. (0=Não/1=Sim) |
| CALC_ADIANTAMENTO_PROPORC_COMP_OUTRO_AFAST_MIN_DIAS_TRABALHADOS | smallint(2) |  |  | Calcular adiantamento proporcional na competência de outros afastamentos dependendo da quantidade de dias trabalhados. (0=Não/1=Sim) |
| CALC_ADIANTAMENTO_PROP_COMP_OUTRO_AFAST_MIN_DIAS_TRABALHADO_QTD | smallint(2) |  | S | Quantidade mínima de dias trabalhados na competência de outros afastamentos para pagamento do adiantamento. |
| CALCULAR_ADIANTAMENTO_COMPETENCIA_ADMISSAO | smallint(2) |  |  | Calcular adiantamento na competência de admissão. (0=Não/1=Sim) |
| CALC_ADIANTAMENTO_PROPORC_DIAS_TRABALHADOS_COMP_ADMISSAO | smallint(2) |  |  | Calcular adiantamento proporcional aos dias trabalhados na competência de admissão. (0=Não/1=Sim) |
| CALC_ADIANTAMENTO_PROPORC_COMP_ADMISSAO_SOMENTE_TRAB_DATA_PAGTO | smallint(2) |  |  | Calcular adiantamento proporcional na competência de admissão somente se estiver trabalhando na data do pagamento. (0=Não/1=Sim) |
| CALC_ADIANTAMENTO_PROPORC_COMP_ADMISSAO_MINIMO_DIAS_TRABALHADOS | smallint(2) |  |  | Calcular adiantamento proporcional na competência de admissão dependendo da quantidade de dias trabalhados. (0=Não/1=Sim) |
| CALC_ADIANTAMENTO_PROPORC_COMP_ADMISSAO_MINIMO_DIAS_TRAB_QTDE | smallint(2) |  | S | Quantidade mínima de dias trabalhados na competência de admissão para pagamento do adiantamento. |
| CONSIDERAR_AFASTAMENTO_54_55_56_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  |  | Considerar os dias afastados pelos afastamentos 54, 55 e 56 para dilatar o período de contrato de experiência. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_54_55_56_CALCULO_DIAS_DIREITO_13_SALARIO | smallint(2) |  |  | Considerar os dias afastados pelos afastamentos 54, 55 e 56 para o cálculo dos dias de direito de 13º salário. (0=Não/1=Sim) |
| CALC_INSS_EMP_13_PROPORC_PER_SIMPLES_NACIONAL_ANO_CALENDARIO | smallint(2) |  |  | Calcular contribuição previdenciária patronal sobre o 13º proporcional ao período em que a empresa era Simples Nacional no ano calendário. (0=Não/1=Sim) |
| ALTERAR_FORMA_PAGTO_LIC_MAT_EMP_MEI_TROCA_CLASS_TRIB_PER_AFAST | smallint(2) |  |  | Alterar a forma de pagamento da licença maternidade para empresa MEI que realiza troca de classificação tributária/regime durante o período do afastamento. (0=Não/1=Sim) |
| CONSIDERAR_SOMENTE_DIAS_UTEIS_AFASTAMENTO_LICENCA_PATERNIDADE | smallint(2) |  |  | Considerar somente os dias úteis para o afastamento de licença paternidade. (0=Não/1=Sim) |
| MASCARA_CONTABIL | varchar(35) |  | S | Máscara contábil. |
| CALC_ENCARGO_INSS_INTEGRAL_COMP_INICIO_FIM_AFAST_CONTRIBUINTES | smallint(2) |  |  | Calcular encargos de INSS integralmente nos meses de início e retorno do afastamento para contribuintes. (0=Não/1=Sim) |
| LISTA_AFAST_CALC_ENCARGO_INSS_INTEG_COMP_INI_FIM_AFAST_CONTRIB | smallint(2) |  | S | Lista de afastamentos da opção = Calcular encargos de INSS integralmente nos meses de início e retorno do afastamento para contribuintes |
| PRODUTOR_RURAL | smallint(2) |  |  | Produtor rural. (0=Não/1=Sim) |
| CALC_CONTRIB_SINDICAL_REMUNERACAO_MES_ANTERIOR_AULISTA_VARIAVEL | smallint(2) |  |  | Calcular contribuição sindical com base na remuneração do mês anterior para professor aulista variável. (0=Não/1=Sim) |
| CONSIDERAR_DIAS_AFASTADOS_INFERIORES_15_DIAS_COMP_OUTROS_AFAST | smallint(2) |  |  | Considerar os dias afastados como trabalhados quando inferior a 15 dias. (0=Não/1=Sim) |
| CONSIDERAR_DSR_DURANTE_PER_AFAST_DOENCA_DIREITOS_INTEGRAIS | smallint(2) |  |  | Considerar os DSRs durante o período afastado por doença com direitos integrais. (0=Não/1=Sim) |
| PERMITIR_INFORMAR_TIPO_CENTRO_CUSTOS | smallint(2) |  |  | Permitir informar o tipo dos Centros de Custos. (0=Não/1=Sim) |
| CALCULAR_UM_SEXTO_SOBRE_BASE_DSR_HORISTA_VARIAVEL | smallint(2) |  |  | Calcular 1/6 sobre a base para DSR do horista variável. (0=Não/1=Sim) |
| CALCULAR_DIFERENCA_CONTRIBUICAO_SINDICAL_ANTECIPACAO_SALARIAL | smallint(2) |  |  | Calcular diferença de contribuição sindical devido antecipação salarial. (0=Não/1=Sim) |
| UTILIZAR_FALTAS_PARCIAIS_DESCONTO_DIAS_FERIAS | smallint(2) |  |  | Utilizar faltas parciais para o desconto de dias de férias. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_41_CALCULO_DIAS_DIREITO_13_SALARIO | smallint(2) |  |  | Considerar o afastamento 41 para o cálculo dos dias de direito de 13º salário. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_41_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  | S | Considerar os dias afastados pelo afastamento 41 para dilatar o contrato de experiência. (0=Não/1=Sim) |
| CONS_MEDIAS_FERIAS_EPR_COMISSIONADO_CALCULO_CONTRIB_SINDICAL | smallint(2) |  |  | Calcular a contribuição sindical sobre as médias de férias do empregado comissionado. (0=Não/1=Sim) |
| CALCULAR_FOLHA_ADIANTAMENTO_APRENDIZ | smallint(2) |  |  | Calcular a folha de adiantamento para aprendiz. (0=Não/1=Sim) |
| CONS_DIAS_AFASTADOS_LICENCA_MAT_PERIODO_TRAB_CALC_ADIANTAMENTO | smallint(2) |  |  | Considerar os dias afastados por maternidade como trabalhados no cálculo proporcional. (0=Não/1=Sim) |
| CTA_DATA_LANCTO_RPA | smallint(2) |  | S | Data do lançamento na contabilidade. (1=Data do pagamento do RPA/2=Data do pagamento da folha mensal/3=Final do mês) |
| SENHA_CONSULTA_FAP | varchar(30) |  | S | Senha para consulta do FAP. |
| CALC_ADIANTAMENTO_PROPORC_CONS_LICENCA_REMUNERADA_DIAS_TRAB | smallint(2) |  |  | Considerar os dias de licença remunerada como dias trabalhados no cálculo proporcional do adiantamento. (0=Não/1=Sim) |
| DISCRIMINAR_HORAS_COMPENSACAO_SABADO_JORNADA_DIARIA | smallint(2) |  |  | Discriminar as horas referentes a compensação do sábado na jornada diária. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_10_17_44_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  |  | Considerar os dias afastados pelos afastamentos 10, 17 e 44 para dilatar o contrato de experiência. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_3_10_42_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  |  | Considerar os dias afastados pelos afastamentos 03, 10 e 42 para dilatar o contrato de experiência. (0=Não/1=Sim) |
| CALCULAR_CONTRIBUICAO_SINDICAL_HORISTA_BASE_30_DIAS | smallint(2) |  |  | Calcular a contribuição sindical para empregados com categoria horista com base em 30 dias. (0=Não/1=Sim) |
| CALCULAR_IRRF_CONTRIBUINTE_AUTONOMO_CONDOMINIO_EDIFICIO | smallint(2) |  |  | Calcular IRRF para contribuinte autônomo de condomínio edifício. (0=Não/1=Sim) |
| CONS_DIAS_AFAST_PERIODO_AQUISITIVO_DILATAR_PERIODO_CONCESSIVO | smallint(2) |  |  | Considerar os dias afastados no período aquisitivo para dilatar o período concessivo. (0=Não/1=Sim) |
| PAGAR_FERIAS_INDENI_RESCISAO_PER_AQUISITIVO_INCOMPLETO_QUITADO | smallint(2) |  |  | Pagar férias indenizadas na rescisão quando o período aquisitivo incompleto já foi gozado. (0=Não/1=Sim) |
| GERA_DATA_PAGTO_RESCISAO_MOT_43_DEC_DIA_UTIL_APOS_DATA_DEMISSAO | smallint(2) |  |  | Gerar a data de pagamento da rescisão pelo motivo 43 no décimo dia útil contado a partir da data de demissão. (0=Não/1=Sim) |
| PRORROGAR_DATA_PAGAMENTO_RESCISAO_SABADO_DOMINGO_FERIADO | smallint(2) |  |  | Prorrogar a data de pagamento da rescisão para o próximo dia útil quando essa recair em sábado, domingo ou feriado. (0=Não/1=Sim) |
| CALC_INSS_EMP_13_SAL_PROPORC_DATA_TRANSF_EMP_ENQUADRA_DESONERAC | smallint(2) |  |  | Calcular o INSS Empresa correspondente a 13º salário proporcional a data de transferência quando a empresa for enquadrada na desoneração. (0=Não/1=Sim) |
| ENTIDADE_SEM_FINS_LUCRATIVOS | smallint(2) |  |  | Entidade sem fins lucrativos. (0=Não/1=Sim) |
| EMPRESA_TRABALHO_TEMPORARIO | smallint(2) |  |  | Empresa de trabalho temporário. (0=Não/1=Sim) |
| NUMERO_REGISTRO_MINISTERIO_TRABALHO | varchar(30) |  | S | Número de registro no Ministério do Trabalho. |
| CONTRATACAO_PESSOA_COM_DEFICIENCIA | smallint(2) |  |  | Contratação de pessoa com deficiência. (1=Dispensado de acordo com a lei/2=Dispensado, mesmo que parcialmente/3=Com a exigibilidade suspensa/4=Obrigado) |
| I_PROCESSO_PESSOA_DEFICIENCIA | integer(4) |  | S | Código do processo judicial para contratação de pessoa com deficiência. |
| LIMITAR_QUANTIDADE_ESTAGIARIOS_SUPERVISOR | smallint(2) |  |  | Limitar a quantidade de estagiários vinculados ao mesmo supervisor. (0=Não/1=Sim) |
| QUANTIDADE_ESTAGIARIOS_SUPERVISOR | smallint(2) |  | S | Quantidade máxima de estagiários vinculados ao mesmo supervisor. |
| CONSIDERAR_DIAS_AFASTADOS_DILATAR_PERIODO_AQUISITIVO_APRENDIZ | smallint(2) |  |  | Considerar os dias afastados para dilatar o período aquisitivo do aprendiz. (0=Não/1=Sim) |
| AFASTAMENTOS_DILATAR_PERIODO_AQUISITIVO_APRENDIZ | smallint(2) |  | S | Soma binária dos afastamentos considerados para dilatar o período aquisitivo do aprendiz. |
| ALIQUOTA_INSS_AUTONOMO_COOPERADO_CONF_ATO_DECLARAT_RFB_N1_2017 | smallint(2) |  |  | Alíquota INSS Autonomo Cooperado conforme Ato Declaratório RFB nº 1 de 2017. (0=Não/1=Sim) |
| CONS_AVISO_PREVIO_INDENI_AVOS_INDENI_13_FERIAS_LEI_12506_2011 | smallint(2) |  |  | Considerar os dias de aviso prévio acrescidos pela Lei 12.506/2011 para projeção do aviso prévio na contagem de avos indenizados de 13º e Férias. |
| CALCULAR_FOLHA_PLR_EMPREGADO_DEMITIDO | smallint(2) |  |  | Calcular a folha de Participação de Lucros quando o colaborador estiver demitido. (0=Não/1=Sim) |
| UTILIZAR_CPF_RESPONSAVEL_LEGAL_EMPRESA_CARNE_LEAO_EMPRESA_CEI | smallint(2) |  |  | Utilizar o CPF do responsável legal da empresa para o Carnê-Leão quando o tipo de inscrição for CEI. (0=Não/1=Sim) |
| CALCULAR_UM_SEXTO_SOBRE_BASE_DSR_DIARISTA_VARIAVEL | smallint(2) |  |  | Calcular 1/6 sobre a base para DSR do diarista variável. (0=Não/1=Sim) |
| DILATAR_LIM_GOZO_FERIAS_AFAST_DATA_RET_PER_AQUISITIVO_INI_AFAST | smallint(2) |  |  | Dilatar o limite de gozo do afastamento quando a data de retorno do afastamento recair no mesmo período aquisitivo/concessivo do início do afastamento. (0=Não/1=Sim) |
| CALCULAR_MULTA_ESTABILIDADE_ART_479_480_PROPORCIONAL_DIAS_MES | smallint(2) |  |  | Calcular multa estabilidade Art. 479 e 480 proporcionalmente aos dias de cada mês. (0=Não/1=Sim) |
| CALC_ANTECIPACAO_FOLHA_ADIANTAMENTO_EPR_ADIANTAMENTO_LANCADO | smallint(2) |  |  | Calcular antecipação salarial na folha de adiantamento para quem tem adiantamento lançado. (0=Não/1=Sim) |
| SOMAR_ENCARGO_INSS_CCT_MENSAL_VAL_RECOLHER_INF_MIN_RECOLHIMENTO | smallint(2) |  |  | Somar os encargos de INSS CCT na folha mensal do mês do aumento quando valor a recolher for inferior ao mínimo para recolhimento. (0=Não/1=Sim) |
| ENVIAR_DADOS_ESOCIAL | smallint(2) |  |  | Enviar dados para o eSocial. (0=Não/1=Sim) |
| WEB_SERVICE_ESOCIAL | smallint(2) |  |  | Web service de envio para o eSocial. (1=Produção restrita/2=Oficial) |
| TIPO_AMBIENTE_ESOCIAL | smallint(2) |  |  | Tipo de ambiente de envio para o eSocial. (1=Produção/2=Pré-produção - dados reais/3=Pré-produção - dados fictícios/6=Homologação/7=Validação/8=Testes/9=Desenvolvimento) |
| ORIGEM_CERTIFICADO_DIGITAL | smallint(2) |  |  | Origem do Certificado. (1=Empresa/2=Contador) |
| TIPO_CENTRALIZACAO_ESOCIAL | smallint(2) |  |  | Tipo de centralização para o eSocial. (1=Centralizada/2=Centralizadora) |
| EMPRESA_CENTRALIZADORA_ESOCIAL | integer(4) |  | S | Código da empresa centralizadora para o eSocial. |
| POSSUI_EMPRESA_CENTRALIZADORA_ESOCIAL_OUTRO_BANCO_DADOS | smallint(2) |  |  | Possui a empresa centralizadora do eSocial em outro banco de dados. (0=Não/1=Sim) |
| COMPETENCIA_INICIO_ESOCIAL | date(4) |  | S | Competência inicial para gerar o eSocial |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| UTILIZA_REGRA_11_2017_PERIODO_AQUISITIVO_EMPREGADO_REGIME_TEMPO_PARCIAL | smallint(2) |  |  | Utiliza a regra de 11/2017 para periodos aquisitivos do empregados com regime tempo parcial. (0=Não/1=Sim) |
| CADASTRAMENTO_INICIAL_ENVIADO_ESOCIAL | smallint(2) |  |  | Cadastramento inicial enviado ao eSocial. (0=Não/1=Sim) |
| TIPO_INSCRICAO_TRANSMISSOR_ESOCIAL | integer(4) |  | S | Tipo de inscrição do transmissor do esocial. |
| INSCRICAO_TRANSMISSOR_ESOCIAL | varchar(14) |  | S | Inscrição do transmissor do esocial. |
| CALCULAR_INSS_EMPRESA_CONTRIBUINTES_CATEGORIA_SEFIP_17_18_24_25 | smallint(2) |  |  | Calcular INSS Empresa para as categorias SEFIP 17, 18, 24 e 25. (0=Não/1=Sim) |
| CONS_SOMENTE_GARANTIA_MIN_ADIANTAMENTO_COMISSIONADO_COM_SALARIO | smallint(2) |  |  | Considerar para empregado comissionado com salário apenas o valor pago de garantia mínima. (0=Não/1=Sim) |
| CALCULAR_INDENIZACAO_ADICIONAL_RESCISAO_TRABALHADOR_TEMPORARIO | smallint(2) |  |  | Calcular indenização adicional na rescisão do trabalhador temporário. (0=Não/1=Sim) |
| CADASTRAMENTO_INICIAL_EVENTOS_NAO_PERIODICOS_ENVIADO_ESOCIAL | smallint(2) |  |  | Cadastramento inicial dos eventos não periódicos enviado para o eSocial. (0=Não/1=Sim) |
| CADASTRAMENTO_INICIAL_RUBRICAS_ENVIADO_ESOCIAL | smallint(2) |  |  | Cadastramento inicial das rubricas enviado para o eSocial. (0=Não/1=Sim) |
| CALCULAR_UM_SEXTO_SOBRE_DSR_CELETISTA_INTERMITENTE | smallint(2) |  |  | Calcular para DSR o valor de 1/6 sobre a base quando empregado com vínculo celetista intermitente. (0=Não/1=Sim) |
| COMPETENCIA_INICIO_ESOCIAL_NAO_PERIODICOS | date(4) |  | S | Competência de início de envio dos eventos não períodicos para o eSocial. |
| COMPETENCIA_INICIO_ESOCIAL_PERIODICOS | date(4) |  | S | Competência de início de envio dos eventos períodicos para o eSocial. |
| EFETUAR_CALCULO_PREVIDENCIARIO_CONFORME_DCFTWEB | smallint(2) |  |  | Efetuar cálculo previdenciário conforme DCTFWeb. (0=Não/1=Sim) |
| COMPETENCIA_INICIO_CALCULO_PREVIDENCIARIO_CONFORME_DCFTWEB | date(4) |  | S | Competência início do cálculo previdenciário conforme DCTFWeb. |
| I_CONTADOR_TRANSMISSAO_ESOCIAL | integer(4) |  | S | Código do contador que irá transmitir os dados pro eSocial. |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| FASEAMENTO_ENVIO_EVENTOS_ESOCIAL | integer(4) |  | S | Tipo de faseamento de envio ao eSocial, 1=1º grupo - Faturamento no ano de 2016 acima de R$ 78.000.000,00/2=2º grupo - Faturamento no ano de 2016 até R$ 78.000.000,00 não optante pelo Simples Nacional/3=3º grupo - Simples Nacional; Empregador PF; Produtor |
| ENVIOU_ESOCIAL_OUTRO_BANCO | smallint(2) |  |  | Empresa enviou eSocial em outro banco de dados. (0=Não/1=Sim) |
| COMPETENCIA_INICIO_UTILIZACAO_ESOCIAL_BANCO_DOMINIO | date(4) |  | S | Competência início da utilização do eSocial no banco da Domínio. |
| CONCLUIU_CONVERSAO_DADOS_ESOCIAL | smallint(2) |  |  | Concluiu a conversão dos dados do eSocial. (0=Não/1=Sim) |
| CALCULAR_FUNRURAL_SOBRE_FOLHA_PAGAMENTO | smallint(2) |  |  | Calcular FUNRURAL sobre a de folha pagamento. (0=Não/1=Sim) |
| COMPETENCIA_INICIO_ESOCIAL_SST_GRUPO_1 | date(4) |  | S | **SEM USO** |
| COMPETENCIA_INICIO_ESOCIAL_SST_GRUPO_2 | date(4) |  | S | **SEM USO** |
| DETERMINAR_COMPETENCIA_FIM_ESOCIAL_SST | smallint(2) |  |  | Determinar a competência fim do envio dos eventos de SST para o eSocial. (0=Não/1=Sim) |
| COMPETENCIA_FIM_ESOCIAL_SST | date(4) |  | S | Competência fim do envio dos eventos de SST para o eSocial. |
| CADASTRAMENTO_INICIAL_EVENTOS_SST_ENVIADO_ESOCIAL | integer(4) |  |  | Cadastramento inicial dos eventos SST foi enviado ao eSocial. |
| UTILIZA_MODULO_WEB_SIMPLIFICADO_ME_EPP_ESOCIAL | smallint(2) |  |  | Utiliza módulo Web Simplificado ME e EPP. (0=Não/1=Sim) |
| COMPETENCIA_INICIO_ESOCIAL_SST | date(4) |  | S | Competência de início do envio dos eventos de SST para o eSocial. |
| CALC_INSS_MULTIPLOS_VINCULOS_CONFORME_ESOCIAL_ANTERIOR_02_2020 | smallint(2) |  |  | Calcular INSS para colaboradores com múltiplos vínculos conforme eSocial em competências anteriores à 02/2020 |
| CALCULAR_HORA_NOTURNA_DE_ACORDO_COM_HORARIO_DO_EMPREGADO | integer(4) |  |  | Calcular hora noturna de acordo com o horário do empregado. (0=Não/1=Sim) |
| DATA_INICIO_CALCULAR_HORA_NOTURNA_DE_ACORDO_COM_HORARIO_DO_EPR | date(4) |  | S | Data início para calcular hora noturna de acordo com o horário do empregado. |
| CAL_HORA_DIURNA_COM_ADICIONAL_NOTURNO_HORARIO_INTEGRAL_NOTURNO | integer(4) |  |  | Calcular Hora Diurna com adicional noturno quando o empregado possui horário integralmente noturno e esse se estende ao horário diurno, conforme Súmula n° 60 TST. |
| INICIO_HORA_NOTURNA | time(8) |  | S | Início da hora noturna. |
| FIM_HORA_NOTURNA | time(8) |  | S | Fim da hora noturna. |
| CONSIDERAR_REDUCAO_ALIQUOTAS_TERCEIROS_SISTEMA_S_CRIADAS_MP_932 | smallint(2) |  |  | Considerar a redução das alíquotas de terceiros do sistema S criada na MP 932. (0=Não/1=Sim) |
| PERMITIR_PROPORCIONALIZAR_CARGA_H_CONFORME_ALT_CAD_EMPREGADO | smallint(2) |  |  | Permitir proporcionalizar a carga horária conforme alterações do cadastro do empregado. (0=Não/1=Sim) |
| COMP_INICIO_PROPORCIONALIZAR_CARGA_H_CONFORME_ALT_CAD_EMPREGADO | date(4) |  | S | Competência início para proporcionalizar a carga horária conforme alterações do cadastro do empregado. |
| EFETUAR_CALCULO_HORAS_NORMAIS_AFAST_COM_BASE_SAL_CADA_DIA_COMP | smallint(2) |  |  | Efetuar o cálculo das horas normais e dos afastamentos com base no salário de cada dia da competência. (0=Não/1=Sim) |
| CALC_AVISO_RESC_POR_ACORDO_ENTRE_PARTES_COM_DIAS_PELA_METADE | smallint(2) |  |  | Calcular o aviso prévio na rescisão por acordo entre as partes considerando os dias pela metade. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_59_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  |  | Considerar os dias afastados pelo afastamento 59 para dilatar o período de contrato de experiência. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_60_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  |  | Considerar os dias afastados pelo afastamento 60 para dilatar o período de contrato de experiência. (0=Não/1=Sim) |
| EXTENDE_LIMITE_GOZO_FERIAS_AFASTAMENTO_59 | smallint(2) |  |  | Extende limite de gozo de férias para o afastamento 59. (0=Não/1=Sim) |
| EXTENDE_LIMITE_GOZO_FERIAS_AFASTAMENTO_60 | smallint(2) |  |  | Extende limite de gozo de férias para o afastamento 60. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_59_CALCULO_DIAS_DIREITO_13_SALARIO | smallint(2) |  |  | Considerar afastamento 59 para o cálculo dos dias de direito do 13º salário. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_60_CALCULO_DIAS_DIREITO_13_SALARIO | smallint(2) |  |  | Considerar afastamento 60 para o cálculo dos dias de direito do 13º salário. (0=Não/1=Sim) |
| CONSIDERAR_MES_AFASTADO_AFASTAMENTO_59_PERIODO_MEDIA_13_SALARIO | smallint(2) |  |  | Considerar o mês dos afastamento 59 no cálculo de médias e adicionais de 13º salário, mesmo que não tenha direito ao avo do mês. (0=Não/1=Sim) |
| CONSIDERAR_MES_AFASTADO_AFASTAMENTO_60_PERIODO_MEDIA_13_SALARIO | smallint(2) |  |  | Considerar o mês dos afastamento 60 no cálculo de médias e adicionais de 13º salário, mesmo que não tenha direito ao avo do mês. (0=Não/1=Sim) |
| CONSIDERAR_ADICIONAIS_CALCULO_GARANTIA_PROVISORIA_MP_936 | smallint(2) |  |  | Considerar os adicionais para o cálculo da Indenização de Garantia Provisória - MP 936/2020. (0=Não/1=Sim) |
| CONSIDERAR_ADICIONAIS_CALCULO_AJUDA_COMPENSATORIA_30_MP_936 | smallint(2) |  |  | Considerar os adicionais para o cálculo da ajuda compensatória 30% - MP 936/2020. (0=Não/1=Sim) |
| CALC_SAL_FAMILIA_EMPREGADOS_ANTES_REDUCAO_SALARIAL_SEM_DIREITO | smallint(2) |  |  | Calcular salário família para empregados que antes do processo de redução salarial não possuiam o direito. (0=Não/1=Sim) |
| CALCULAR_INDENIZACAO_GARANTIA_PROVISORIA_RESCISAO_MOTIVOS_10_23 | smallint(2) |  |  | Calcular indenização de garantia provisoria na rescisão pelos motivos 10 e 23. (0=Não/1=Sim) |
| POSTERGAR_DIAS_RESTANTES_ESTAB_GARANTIA_MPE_COVID_19 | smallint(2) |  |  | Postergar os dias restantes de estabilidade por garantia provisória quando houver Medida de Proteção do Emprego - Covid-19 cadastrada no período. (0=Não/1=Sim) |
| CONSIDERAR_COMPENSACAO_VALORES_PREVIDENCIARIOS | smallint(2) |  |  | Compensar valores previdenciários(0=Não/1=Sim)". |
| COMPETENCIA_CONSIDERAR_COMPENSACAO_VALORES_PREVIDENCIARIOS | date(4) |  | S | Competência fim compensação de valores previdenciários". |
| CALC_RUBRICAS_INSALUBRIDADE_SALARIO_MINIMO_OU_PISO_MPE_COVID_19 | smallint(2) |  |  | Calcular as rubricas com classificação Insalubridade e base de cálculo Salário Mínimo, Salário Mínimo Estadual ou Piso Estadual para a redução salarial de Medida de Proteção do Emprego - Covid-19. (0=Não/1=Sim) |
| CALCULAR_FORMA_REDUZIDA_GRATIFICACAO_COMPETENCIA_REDUCAO | smallint(2) |  |  | Calcular de forma reduzida a gratificação lançada na competência com Redução. (0=Não/1=Sim) |
| CALC_ANTECIPACAO_SAL_DE_FORMA_REDUZIDA_NA_COMP_COM_REDUCAO | smallint(2) |  |  | Calcular a antecipação salarial de forma reduzida na competência com Redução. (0=Não/1=Sim) |
| CONSIDERAR_ANTECIPACAO_SALARIAL_PRO_CALCULO_AJUDA_COMPENSATORIA | smallint(2) |  |  | Considerar a antecipação salarial para o cálculo da ajuda compensatória. (0=Não/1=Sim) |
| CALC_REMUNERACAO_INTEGRALMENTE_MESES_AFASTAMENTOS_CONTRIB | smallint(2) |  |  | Calcular remuneração integralmente nos meses de início e retorno do afastamento para contribuintes(0=Não/1=Sim)". |
| LISTA_AFASTAMENTOS_CALCULAR_REMUNERACAO_INTEGRALMENTE_CONTRIB | smallint(2) |  | S | Lista afastamentos calcular remuneração integralmente para contribuintes |
| DILATAR_PERIODO_AQUISITIVO_FERIAS_AFASTAMENTO_59_60 | smallint(2) |  |  | Dilatar o período aquisitivo de ferias para o afastamento 59 e 60. (0=Não/1=Sim) |
| CALC_AFAST_COM_PAGTO_PELA_EMPRESA_EMPREGADOS_INTERMITENTES | smallint(2) |  |  | Calcular os afastamentos auxílio doença, doença profissional e licença maternidade com pagamento pela empresa para empregados com contrato intermitente. (0=Não/1=Sim) |
| COMP_CALC_AFAST_COM_PAGTO_PELA_EMPRESA_EMPREGADOS_INTERMITENTES | date(4) |  | S | Competência calcular os afastamentos auxílio doença, doença profissional e licença maternidade com pagamento pela empresa para empregados com contrato intermitente. |
| CALCULAR_SALARIO_FAMILIA_INTERMITENTE_COMPETENCIA_SEM_CALCULO | smallint(2) |  |  | Calcular salário família para empregado intermitente quando na competência não possuir cálculo. (0=Não/1=Sim) |
| CALC_SAL_FAMILIA_EMPREGADO_INTEGRALMENTE_AFASTADO_SUSPENSAO | smallint(2) |  |  | Calcular Salário Família quando o empregado estiver integralmente afastado por suspensão. (0=Não/1=Sim) |
| CALCULAR_DIARIAS_TRIBUTAVEIS | smallint(2) |  |  | Calcular diárias tributáveis. (0=Não/1=Sim) |
| COMPETENCIA_CALCULAR_DIARIAS_TRIBUTAVEIS | date(4) |  | S | Competência calcular diárias tributáveis. |
| CONSIDERAR_DIAS_GARANTIA_PROVISORIA_CALCULO_AVO_FERIAS_13 | smallint(2) |  |  | Considerar os dias de indenização de garantia provisória para o cálculo dos avos de férias e 13º salário indenizados. (0=Não/1=Sim) |
| ENTIDADE_EDUCATIVA_PRATICA_DESPORTIVA_APRENDIZ | smallint(2) |  |  | Entidade Educativa/Prática Desportiva (Aprendiz). (0=Não/1=Sim) |
| GERAR_ESOCIAL_DOMESTICO | smallint(2) |  |  | Gerar eSocial doméstico |
| TIPO_ACESSO_ESOCIAL_DOMESTICO | smallint(2) |  |  | Tipo de acesso eSocial doméstico. (1=Código/2=Certificado digital da própria empresa/3=Certificado digital por procuração/4=Conta gov.br) |
| CODIGO_ACESSO_ESOCIAL_DOMESTICO | varchar(12) |  | S | Código de acesso eSocial doméstico |
| SENHA_ACESSO_ESOCIAL_DOMESTICO | varchar(30) |  | S | Senha de acesso eSocial doméstico |
| CONSIDERAR_SALARIO_REDUZIDO_COMPETENCIA_CALCULO_13 | smallint(2) |  |  | Considerar o salário reduzido da competência para o cálculo do 13º salário |
| UTILIZAR_RESCISAO_RUBRICAS_DESCONTO_DIF_13_INCIDENCIA_ENCARGOS | smallint(2) |  |  | Utilizar na rescisão as rubricas de desconto diferença 13° com incidência de encargos |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| DESCONSIDERAR_MES_DIVISOR_MEDIAS_REDUCAO_13 | smallint(2) |  |  | Desconsiderar o mês como divisor para o cálculo de médias de 13º, se o empregado ficou X dias ou mais com redução |
| DESCONSIDERAR_MES_DIVISOR_MEDIAS_REDUCAO_13_DIAS | smallint(2) |  |  | Desconsiderar o mês como divisor para o cálculo de médias de 13º, se o empregado ficou X dias ou mais com redução |
| CONSIDERAR_AFASTAMENTO_47_CALCULO_DIAS_DIREITO_13_SALARIO | smallint(2) |  |  | CONSIDERAR AFASTAMENTO 47 PARA O CÁLCULO DOS DIAS DE DIREITO DO 13º SALÁRIO. (0=NÃO/1=SIM) |
| CONSIDERAR_AFASTAMENTO_36_CALCULO_DIAS_DIREITO_13_SALARIO | smallint(2) |  |  | CONSIDERAR AFASTAMENTO 36 PARA O CÁLCULO DOS DIAS DE DIREITO DO 13º SALÁRIO. (0=NÃO/1=SIM) |
| LIMITAR_PAGAMENTO_CONTRIB_TERCEIRO_20_SALARIO_MINIMO | smallint(2) |  |  | Limitar o pagamento da contribuição de terceiros a 20 salários mínimos. (0=Não/1=Valor à recolher/2=Base de cálculo) |
| COMPETENCIA_LIMITE_PAGAMENTO_CONTRIB_TERCEIRO_20_SALARIO_MINIMO | date(4) |  | S | Competência para limitar o pagamento da contribuição de terceiros a 20 salarios. |
| HABILITAR_IMPORTACAO_DADOS_ESOCIAL | smallint(2) |  |  | Habilitar importação de dados do eSocial |
| CONSIDERAR_ULTIMO_DIA_MES_PARA_LANCAMENTO_COMO_FINAL_DO_MES_OU_PROVISOES | smallint(2) |  |  | Considerar o último dia do mês, independente se cair em dia não útil, para data de lançamento como Final do Mês e para provisões |
| UTILIZA_FORMA_UNIFICADA_ESOCIAL | smallint(2) |  | S | Utiliza forma unificada a orgãos públicos. (0=Não/1=Sim) |
| CNPJ_ENTE_FEDERATIVO_RESPONSAVEL | varchar(14) |  | S | CNPJ do Ente Federativo Responsável a orgãos públicos. |
| NUMERO_PROCESSO_DEFICIENTE | varchar(20) |  | S | Numero do processo para contratação de deficiente. |
| CADASTRAMENTO_INICIAL_EVENTOS_TREICAP | integer(4) |  |  | Cadastramento inicial dos eventos TreiCap se foi enviado ao eSocial. |
| CADASTRAMENTO_INICIAL_EVENTOS_TREICAP_DATA | date(4) |  | S | Competência dos envios TreiCap ao eSocial". |
| ENVIAR_EVENTO_S2210_PELO_MODULO_FOLHA | smallint(2) |  |  | Enviar o evento S-2210 pelo modulo folha. (0=Não/1=Sim) |
| ENVIAR_EVENTO_S2220_PELO_MODULO_FOLHA | smallint(2) |  |  | Enviar o evento S-2220 pelo modulo folha. (0=Não/1=Sim) |
| ENVIAR_EVENTO_S2240_PELO_MODULO_FOLHA | smallint(2) |  |  | Enviar o evento S-2240 pelo modulo folha. (0=Não/1=Sim) |
| VINCULAR_OUTRO_RESPONSAVEL_PARA_ENVIO_EVENTO_SST_ESOCIAL | smallint(2) |  |  | Vincular outro responsável para enviar eventos SST para o eSocial. (0=Não/1=Sim) |
| ORIGEM_CERTIFICADO_ENVIO_EVENTO_SST_ESOCIAL | smallint(2) |  |  | Origem do certificado para o envio dos eventos SST para enviar eventos SST para o eSocial. (1=Empresa/2=Responsavel) |
| I_RESPONSAVEL_ENVIO_SST_ESOCIAL | integer(4) |  | S | Código do responsável pelo envio dos eventos SST para o eSocial |
| ENVIAR_EVENTO_S2210_PELO_RESPONSAVEL_SST | smallint(2) |  |  | Enviar o evento S-2210 pelo responsavel SST (0=Não/1=Sim) |
| ENVIAR_EVENTO_S2220_PELO_RESPONSAVEL_SST | smallint(2) |  |  | Enviar o evento S-2220 pelo responsavel SST (0=Não/1=Sim) |
| ENVIAR_EVENTO_S2240_PELO_RESPONSAVEL_SST | smallint(2) |  |  | Enviar o evento S-2240 pelo responsavel SST (0=Não/1=Sim) |
| ALTERAR_INSCRICAO_EMPRESA | char(1) |  | S | 0-Nao / 1-Sim - Houve alteracao, aguardando atualizacao pelo Folha |
| ADIANTAMENTO_PROPORCIONAL_OUTROS_AFASTAMENTOS_DIAS_TRAB | tinyint(1) |  | S | Parâmetro adiantamento proporcional outros afastamentos dias trabalhados |
| CALC_INSS_8_TRAB_RURAL_CONTRATO_PRAZO_DETERMINADO | smallint(2) |  | S | Parametro calcular INSS 8% para trab. rural com contrato de prazo determinado |
| COMP_INICIO_CALC_INSS_8_TRAB_RURAL_CONTRATO_PRAZO_DETERMINADO | date(4) |  | S | Parametro competencia inicio calculo INSS 8% para trab. rural com contrato de prazo determinado |
| CONSIDERAR_DIAS_CALCULADOS_MES_PROVISAO | smallint(2) |  | S | configuracao do relatorio de provisao de ferias calculadas no mes 0 nao considerar/1 considerar integralmente/ 2 considerar proporcional |
| AGENTE_PUBLICO | smallint(2) |  |  | Agente publico. (0=Não/1=Sim) |
| CALC_SALARIO_PROP_DIAS_MES_COMP_FER | smallint(2) |  |  | CALCULAR SALÁRIO PROPORCIONAL AO NÚMERO DE DIAS DE CADA MÊS NA COMPETÊNCIA DE CÁLCULO DAS FÉRIAS. |
| CALCULA_ARREDONDAMENTO_RESILICAO_PROFESSOR | smallint(2) |  |  | Calcula arredondamento: (0=Não/1=Sim) |
| VALOR_ARREDONDAMENTO_RESILICAO_PROFESSOR | numeric(5) |  | S | Valor de arredondamento |
| FORMA_DESCONTO_ARREDONDAMENTO_RESILICAO_PROFESSOR | smallint(2) |  | S | Forma de Desconto: (0=Não descontar/1=Na próxima folha mensal calculada) |
| CTA_DATA_LANCTO_RESILICAO_PROFESSOR | smallint(2) |  | S | Data do lançamento na contabilidade. (1=Final do mês/2=Data do pagamento) |
| EXTENDE_LIMITE_GOZO_FERIAS_AFASTAMENTO_17 | smallint(2) |  |  | Extende limite de gozo de férias para o afastamento 35 |
| GERAR_INTEGRACAO_CONTABIL_COLABORADOR | smallint(2) |  |  | Gerar integração contábil por colaborador (0=Não/1=Sim) |
| GERAR_INTEGRACAO_CONTABIL_COLABORADOR_FOLHA_MENSAL | smallint(2) |  |  | Gerar integração contábil por colaborador - Folha Mensal (0=Não/1=Sim) |
| GERAR_INTEGRACAO_CONTABIL_COLABORADOR_FERIAS | smallint(2) |  |  | Gerar integração contábil por colaborador - Férias (0=Não/1=Sim) |
| GERAR_INTEGRACAO_CONTABIL_COLABORADOR_RESCISAO | smallint(2) |  |  | Gerar integração contábil por colaborador - Rescisão (0=Não/1=Sim) |
| GERAR_INTEGRACAO_CONTABIL_COLABORADOR_PROVISAO_FERIAS | smallint(2) |  |  | Gerar integração contábil por colaborador - Provisão de Férias (0=Não/1=Sim) |
| GERAR_INTEGRACAO_CONTABIL_COLABORADOR_PROVISAO_13 | smallint(2) |  |  | Gerar integração contábil por colaborador - Provisão de 13º (0=Não/1=Sim) |
| BANKING_LI_ACEITO | char(1) |  |  | Indica se foi marcado o li e aceito do banking |
| CONSIDERAR_BASE_FGTS_SOBRE_INDENIZADO_SEPARADO_DEMAIS_BASE_FTGS | smallint(2) |  |  | Calcular rescisão considerando a base de FGTS sobre o aviso prévio indenizado separado das demais bases de FGTS conforme esocial. (0=Não/1=Sim) |
| COMP_CONSIDERAR_BASE_FGTS_SOBRE_INDENIZADO_SEPARADO_DEMAIS_BASE_FTGS | date(4) |  | S | Competência a considerar a base de FGTS sobre o aviso prévio indenizado separado das demais bases de FGTS no calculo da rescisão. |
| NAO_DEDUZIR_BASE_FGTS_NEGATIVA_DEMAIS_BASE_FGTS | smallint(2) |  |  | Não deduzir a base de cálculo de FGTS negativa de outras bases de FGTS. (0=Não/1=Sim) |
| COMPETENCIA_NAO_DEDUZIR_BASE_FGTS_NEGATIVA_DEMAIS_BASE_FGTS | date(4) |  | S | Competência a não deduzir a base de cálculo de FGTS negativa de outras bases de FGTS. |
| CALC_13_FERIAS_INDENIZADO_AVISO_REAVIDO | smallint(2) |  |  | (0=Não/1=Sim) |
| NAO_CONSIDERAR_FERIAS_13_PAGO_MENSAL_CEL_INT | smallint(2) |  |  | Não considerar os valores de férias e 13 pagos mensalmente para celetista intermitente (0=Não/1=Sim |
| CONSIDERAR_AFASTAMENTO_JUSTIFICADO_CALCULO_AVO_13_DOMESTICO | smallint(2) |  |  | Considerar o afastamento por ausência justificada para cálculo do avo de 13 salário para empregado doméstico (0=Não/1=Sim |
| CONSIDERAR_AVO_13_COMPETENCIA_TROCA_INTERM_OUTRO_VINC | smallint(2) |  |  | Considerar para o avo de 13 salário as competências que possuem cálculo quando teve troca de categoria intermitente para outros vínculos (0=Não/1=Sim |
| AFASTAMENTOS_ADIANTAMENTO_PROPORCIONAL_DIAS_TRABALHADOS | integer(4) |  | S | Afastamentos considerados para adiantamento proporcional dos dias trabalhados. |
| CALCULAR_AVISO_PREVIO_CELETISTA_INTERMITENTE_VERBAS_TRABALHO | smallint(2) |  |  | Calcular o aviso prévio para a categoria Celetista Intermitente considerando as verbas pagas durante o curso do contrato de trabalho (0=Não/1=Sim |
| CALCULAR_SALARIO_FAMILIA_DOMESTICO_RETORNO_AFAST_ACIDENTE_DOENCA | smallint(2) |  |  | Calcular salário família para empregado doméstico na competência que retornar de afastamento por Acidente/Doença igual ou inferior a 15 dias. (0=Não/1=Sim) |
| CALC_13_DESCONTAR_FALTAS_NOTURNAS | smallint(2) |  |  | 13° Salário - Descontar faltas noturnas. (0=Não/1=Sim) |
| ENVIAR_RETIFICACAO_S_1000_CONTRIBUI_PIS | smallint(2) |  |  | Enviar Retificação S-1000 Contribui PIS(0=Não/1=Sim) |
| UTILIZAR_PERCENTUAL_DIFERENCIADO_ESTAGIARIO | smallint(2) |  |  | Utilizar percentual diferenciado para estagiários (0=Não/1=Sim) |
| PERCENTUAL_DIFERENCIADO_ESTAGIARIO | numeric(5) |  | S | Percentual diferenciado para estagiários |
| CONSIDERAR_SALARIO_FAMILIA_RETROATIVO_COMPENSACAO | smallint(2) |  |  | Considerar Salário Família Retroativo para compensação. (0=Não/1=Sim) |
| NAO_ENVIAR_EVENTOS_ESOCIAL | smallint(2) |  |  | Não enviar eventos ao eSocial. (0=Não/1=Sim) |
| NAO_ENVIAR_EVENTOS_ESOCIAL_DATA | date(4) |  | S | Data início para Não enviar eventos ao eSocial. |
| GERAR_DCTFWEB_API_CONTADOR | smallint(2) |  |  | Gerar guia DARF DCTFWeb pela API Integra Contador com certificado digital do contador. (0=Não/1=Sim) |
| ENVIAR_EVENTO_S2221_PELO_MODULO_FOLHA | smallint(2) |  |  | Enviar o evento S-2221 pelo modulo folha. (0=Não/1=Sim) |
| ENVIAR_EVENTO_S2221_PELO_RESPONSAVEL_SST | smallint(2) |  |  | Enviar o evento S-2221 pelo responsavel SST (0=Não/1=Sim) |
| CONSIDERAR_DIAS_AFASTADOS_DILATAR_ACRESCIMO_AVISO_PREVIO | smallint(2) |  |  | Considerar os dias afastados para dilatar a contagem do acréscimo do Aviso Prévio - Lei 12.506/2011 (0=Não/1=Sim). |
| LISTA_AFASTAMENTOS_DILATAR_ACRESCIMO_AVISO_PREVIO | integer(4) |  |  | Lista de afastamentos da opção Considerar os dias afastados para dilatar a contagem do acréscimo do Aviso Prévio - Lei 12.506/2011 |
| DESMARCAR_ENVIAR_DADOS_ESOCIAL_EMPRESA_VALIDADA_INATIVA | smallint(2) |  |  | Indica que o campo ENVIAR_DADOS_ESOCIAL foi desmarcado automaticamente devido a empresa possuir uma inscrição no status inativo, sem a marcação do módulo "Folha" no mesmo tipo de ambiente (0=Não/1=Sim) |
| POSSUI_EMPREGADO_REGIME_PREVIDENCIARIO_RPPS | integer(4) |  | S | Possui empregado com Regime Previdenciário igual a "Regime Próprio de Previdência Social - RPPS" |
| DATA_PERIODICOS_RPPS | date(4) |  | S | data de início do envio do evento S-1202 ao Empregado com Regime Previdenciário igual a "Regime Próprio de Previdência Social - RPPS" |
| CTA_DATA_LANCTO_CONVOCACAO_INTERMITENTE | smallint(2) |  | S | Data do lançamento na contabilidade. (1=Data do pagamento da Convocação Intermitente/2=Data do pagamento da folha mensal/3=Final do mês) |
| ENVIAR_MANUALMENTE_ESOCIAL_NAO_PERIODICOS | smallint(2) |  |  | Enviar automaticamente/0 Não enviar automaticamente/1 |
| DATA_ENVIAR_MANUALMENTE_ESOCIAL_NAO_PERIODICOS | date(4) |  | S | Data para enviar manualmente os eventos não periódicos ao eSocial |
| ENVIAR_MANUALMENTE_ADMISSAO | smallint(2) |  |  | Enviar eventos não periódicos - Admissão S-2190/S-2200/S-2300 |
| ENVIAR_MANUALMENTE_ALT_CONTRATUAL | smallint(2) |  |  | Enviar eventos não periódicos - Alteração contratual S-2206/S-2306 |
| ENVIAR_MANUALMENTE_ALT_CADASTRAL | smallint(2) |  |  | Enviar eventos não periódicos - Alteração cadastral S-2205 |
| ENVIAR_MANUALMENTE_ALT_PENDENTES | smallint(2) |  |  | Enviar os eventos S-2205/S-2206/S-2306 pendentes quando enviado os eventos de remuneração ao eSocial |
| CONFIG_RUBRICAS_DESCONTO_COMPULSORIO | smallint(2) |  | S | 0 - Não / 1 - Sim, Configurar rubricas para serem consideradas como desconto compulsório |
| CALC_INTEGRALMENTE_HORAS_NOTURNAS_EMPREGADO_JORNADA_NOTURNA | smallint(2) |  |  | Calcular integralmente Horas Noturnas para empregado que possui jornada exclusivamente noturna a partir de. (0=Não/1=Sim) |
| COMPETENCIA_CALC_HORAS_NOTURNAS_EMPREGADO | date(4) |  | S | Competência do calculo integral de horas noturnas para empregado com jornada exclusivamente noturna. |
| PAGAR_13_PROPORCIONAL_TROCA_MENSALISTA_HORISTA_VARIAVEL | smallint(2) |  |  | Pagar 13º Salário proporcional na troca mensalista/horista variável. (0=Não/1=Sim) |
| GERA_DADOS_ISENCAO_ENTIDADE_BENEFICIENTE | char(1) |  |  | Entidade Beneficiente - Informações Complementares - Dados da Isenção |
| CONSIDERAR_AFASTAMENTO_90_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  |  | Considerar os dias afastados pelo afastamento 90 para dilatar o período de contrato de experiência. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_91_DILATAR_CONTRATO_EXPERIENCIA | smallint(2) |  |  | Considerar os dias afastados pelo afastamento 91 para dilatar o período de contrato de experiência. (0=Não/1=Sim) |
| EXTENDE_LIMITE_GOZO_FERIAS_AFASTAMENTO_90 | smallint(2) |  |  | Extende limite de gozo de férias para o afastamento 90. (0=Não/1=Sim) |
| EXTENDE_LIMITE_GOZO_FERIAS_AFASTAMENTO_91 | smallint(2) |  |  | Extende limite de gozo de férias para o afastamento 91. (0=Não/1=Sim) |
| CONSIDERAR_MES_AFASTADO_AFASTAMENTO_90_PERIODO_MEDIA_13_SALARIO | smallint(2) |  |  | Considerar o mês dos afastamento 90 no cálculo de médias e adicionais de 13º salário, mesmo que não tenha direito ao avo do mês. (0=Não/1=Sim) |
| CONSIDERAR_MES_AFASTADO_AFASTAMENTO_91_PERIODO_MEDIA_13_SALARIO | smallint(2) |  |  | Considerar o mês dos afastamento 91 no cálculo de médias e adicionais de 13º salário, mesmo que não tenha direito ao avo do mês. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_90_CALCULO_DIAS_DIREITO_13_SALARIO | smallint(2) |  |  | Considerar afastamento 90 para o cálculo dos dias de direito do 13º salário. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_91_CALCULO_DIAS_DIREITO_13_SALARIO | smallint(2) |  |  | Considerar afastamento 91 para o cálculo dos dias de direito do 13º salário. (0=Não/1=Sim) |
| AFASTAMENTOS_PAGAMENTO_EMPRESA_CELETISTA_INTERMITENTE | integer(4) |  | S | Afastamentos que serão pagos pela empresa para empregados celetista intermitente. |
| CALCULAR_SALARIO_FAMILIA_HORISTA_VARIAVEL_SEM_CALCULO | smallint(2) |  |  | Calcular salário família para empregado horista variável quando na competência não possuir cálculo. (0=Não/1=Sim) |
| GERAR_LANCAMENTO_RUBRICA_FOLHA_VIA_API | smallint(2) |  |  | Gerar lançamento de rubricas na folha via API.(0=Não/1=Sim) |
| NAO_APLICAR_REDUCAO_LEI_15270_IRRF_DIF_13_SALARIO | smallint(2) |  |  | Não aplicar as regras de redução da Lei 15.270/2025 para o cálculo de IRRF Diferença 13º salário. (0=Não/1=Sim) |
| TIPO_ACESSO_API_CRED_TRAB | smallint(2) |  | S | Tipo de acesso API Credito do Trabalhador (1=Certificado propria empresa, 2=Certificado procuracao) |
| I_CONTADOR_API_CRED_TRAB | integer(4) |  | S | Contador para consulta API Credito do Trabalhador quando acesso por procuracao |
