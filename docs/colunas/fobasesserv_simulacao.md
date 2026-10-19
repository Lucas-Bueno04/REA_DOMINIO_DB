# FOBASESSERV_SIMULACAO — Bases da simulação de rescisão/férias
6.039 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Codigo empresa |
| I_EMPREGADOS | integer(4) | PK |  | Empregado |
| I_DEPTO | integer(4) |  |  | Departamento |
| I_CCUSTOS | integer(4) |  |  | Centro de Custos |
| I_CARGOS | integer(4) |  |  | Cargo |
| COMPETENCIA | date(4) | PK |  | Competencia |
| TIPO_PROCESS | integer(4) | PK |  | TIPO DE CALCULO |
| SITUACAO_MES | integer(4) |  |  | Situação: (0~89) |
| NUM_FILHOS | integer(4) |  |  | No. filhos |
| NUM_DEPENDENTES | integer(4) |  |  | No. Dependentes |
| PROVENTOS | numeric(13) |  |  | Proventos |
| DESCONTOS | numeric(13) |  |  | Descontos |
| SALARIO_BASE | numeric(13) |  | S | ** SEM USO ** SALARIO BASE |
| SALARIO_MATERNIDADE | numeric(13) |  |  | Salario Maternidade |
| SALARIO_MES | numeric(13) |  |  | Salario Mes |
| VALOR_IRRF | numeric(13) |  | S | ** SEM USO ** VALOR IRRF |
| TAXA_IRRF | numeric(5) |  | S | ** SEM USO ** TAXA IRRF |
| VALOR_FGTS | numeric(13) |  | S | ** SEM USO ** VALOR FGTS |
| VALOR_INSS | numeric(13) |  | S | ** SEM USO ** VALOR INSS |
| TAXA_INSS | numeric(5) |  | S | ** SEM USO ** TAXA INSS |
| BASE_INSS | numeric(13) |  | S | ** SEM USO ** BASE INSS |
| EXCEDENTE_INSS | numeric(13) |  | S | ** SEM USO ** EXCEDENTE INSS |
| BASE_IRRF | numeric(13) |  | S | ** SEM USO ** BASE IRRF |
| ABAT_IRRF | numeric(13) |  | S | ** SEM USO ** ABATIMENTO IRRF |
| DED_IRRF | numeric(13) |  | S | ** SEM USO ** DEDUCAO IRRF |
| DESC_DEPEND | numeric(13) |  | S | ** SEM USO ** DESCONTO DEPENDENTE |
| VAL_SAL_FAM | numeric(13) |  |  | Valor Sal. Familia |
| BASE_FGTS | numeric(13) |  | S | ** SEM USO ** BASE FGTS |
| BASE_SINDICATO | numeric(13) |  | S | ** SEM USO ** BASE SINDICATO |
| BASE_HEXTRA | numeric(13) |  | S | ** SEM USO ** BASE HORA EXTRA |
| BASE_PERICULOSIDADE | numeric(13) |  | S | ** SEM USO ** BASE PERICULOSIDADE |
| BASEX1 | numeric(13) |  | S | ** SEM USO ** BASE AUXILIAR 1 |
| BASEX2 | numeric(13) |  | S | ** SEM USO ** BASE AUXILIAR 2 |
| BASEX3 | numeric(13) |  | S | ** SEM USO ** BASE AUXILIAR 3 |
| VAL_INSS_EMPRESA | numeric(13) |  | S | ** SEM USO ** VALOR INSS EMPRESA |
| VAL_INSS_TERCEIRO | numeric(13) |  | S | ** SEM USO ** VALOR INSS TERCEIRO |
| VAL_ACID_TRABALHO | numeric(13) |  | S | ** SEM USO ** VALOR ACIDENTE TRABALHO |
| TEVE_AFAST_MES | char(1) |  | S | ** SEM USO ** TEVE AFASTAMENTO MES |
| NUME_CHEQUE | integer(4) |  | S | No. Cheque |
| I_SERVICOS | integer(4) | PK |  | Servico |
| VARIOS_SERVICOS | char(1) |  | S | ** SEM USO ** VARIOS SERVICOS NO MESMO MES |
| DEDINSSMAT13 | numeric(13) |  |  | Deducao INSS 13 |
| DATA_PAGTO | date(4) |  |  | Data pagamento |
| TEVE_FERIAS | char(1) |  | S | ** SEM USO ** TEVE FERIAS |
| INICIO_FERIAS | date(4) |  | S | ** SEM USO ** INICIO FERIAS |
| FIM_FERIAS | date(4) |  | S | ** SEM USO ** FIM FERIAS |
| BASE_INSS_FER | numeric(13) |  | S | ** SEM USO ** BASE INSS FERIAS |
| VALOR_INSS_FER | numeric(13) |  | S | ** SEM USO ** VALOR INSS FERIAS |
| BASE_FGTS_FER | numeric(13) |  | S | ** SEM USO ** BASE FGTS FERIAS |
| VALOR_FGTS_FER | numeric(13) |  | S | ** SEM USO ** VALOR FGTS FERIAS |
| BASE_PIS | numeric(13) |  | S | ** SEM USO ** BASE PIS |
| VALOR_PIS | numeric(15) |  | S | ** SEM USO ** VALOR PIS |
| BASE_IRRF_FER | numeric(13) |  | S | ** SEM USO ** BASE IRRF FERIAS |
| VALOR_IRRF_FER | numeric(13) |  | S | ** SEM USO ** VALOR IRRF FERIAS |
| BASE_IRRF_13 | numeric(13) |  | S | ** SEM USO ** BASE IRRF 13 |
| ABAT_IRRF_13 | numeric(13) |  | S | ** SEM USO ** ABATIMENTO IRRF 13 |
| TAXA_IRRF_13 | numeric(13) |  | S | ** SEM USO ** TAXA IRRF 13 |
| VALOR_IRRF_13 | numeric(13) |  | S | ** SEM USO ** VALOR IRRF 13 |
| DEDUC_IRRF_13 | numeric(13) |  | S | ** SEM USO ** DEDUCAO IRRF 13 |
| DEPEND_IRRF_13 | numeric(13) |  | S | ** SEM USO ** DEPENDENTE IRRF 13 |
| NODEPEND_IRRF_13 | tinyint(1) |  | S | ** SEM USO ** NO. DEPENDENTE 13 |
| INSS_EMPRESA_FER | numeric(13) |  | S | ** SEM USO ** INSS EMPRESA FERIAS |
| ACID_TRAB_FER | numeric(13) |  | S | ** SEM USO ** ACID. TRAB. FERIAS |
| INSS_TERC_FER | numeric(13) |  | S | ** SEM USO ** INSS TERCEIRO FERIAS |
| VALOR_PIS_FER | numeric(13) |  | S | ** SEM USO ** VALOR PIS FERIAS |
| DESC_LEI_IRRF | numeric(13) |  | S | ** SEM USO ** DESC. LEI IRRF |
| DESC_LEI_IRRF_13 | numeric(13) |  | S | ** SEM USO ** DESC. LEI IRFF 13 |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| RATEIO | integer(4) | PK |  | Rateio |
| DIAS_SERVICO | integer(4) |  |  | Numero de dias que o empregado ficou no servico |
| IMPLANTADO | tinyint(1) |  | S | 1=Dados implantados, 0=Calculado pelo sistema |
| I_FILIAIS | integer(4) |  |  | Filial |
| I_CALCULOS_OLD | integer(4) |  | S | Código sequencial de calculos - Renomeado |
| CATEGORIA | smallint(2) |  |  | Categoria |
| HORAS_DIA | numeric(5) |  |  | Horas dia |
| HORAS_SEMANA | numeric(5) |  |  | Horas semana |
| HORAS_MES | numeric(5) |  |  | Horas mes |
| I_FERIAS_GOZO | integer(4) |  | S | SEQUENCIAL DE PERIODOS DE GOZO |
| COMPETENCIA_CCT | date(4) |  | S | Competência da alteração salarial CCT |
| FOLHA_MES_PAGA | smallint(2) |  | S | Indica no cálculo do 13º salário se a folha do mês já foi paga: 0=Não/1=Sim |
| TIPO_CALCULO_PROP | smallint(2) |  |  | Tipo do cálculo proporcional: 1=Mês comercial/2=Mês civil |
| VINCULO | smallint(2) |  |  | Vínculo empregatício |
| DIF_INSS_13_DESC_MAIOR | numeric(13) |  | S | Diferença de INSS 13º salário descontado a maior |
| PERCENTUAL_ADIANTAMENTO | numeric(5) |  | S | Percentual de adiantamento |
| PERMITE_ALTERAR_DATA_PAGAMENTO | smallint(2) |  |  | Permite alterar a data de pagamento: (0=Não/1=sim) |
| I_CALCULOS_DESCONTO_ARREDONDAMENTO_OLD | integer(4) |  | S | Código do cálculo que descontou o arredondamento - Renomeado |
| GRAVOU_BASES_CALCULO_DIFERENCA | smallint(2) |  |  | Gravou as bases de cálculo das diferenças pagas.(0=Não/1=Sim) |
| I_CALCULOS_COMPLEMENTOS_OLD | integer(4) |  | S | Código do complemento de cálculo - Renomeado |
| I_FUNCAO | integer(4) |  | S | Código da função. |
| CALCULAR_DIFERENCA_13_ADIANTAMENTO | smallint(2) |  | S | Calcular diferença 13º adiantamento. (0=Não/1=Sim) |
| CALCULAR_13_ADIANTAMENTO_FOLHA_MENSAL | smallint(2) |  |  | Calcula o 13º adiantamento folha mensal. (0=Não/1=Sim) |
| CALCULAR_13_ADIANTAMENTO_CONFORME_AVOS_DIREITO | smallint(2) |  |  | Calcula o 13º adiantamento conforme avos direito. (0=Não/1=Sim) |
| BASE_PISO_SALARIAL | numeric(13) |  |  | Base do piso salarial utilizada para o cálculo. |
| QUANTIDADE_FALTAS | smallint(2) |  |  | Quantidade de faltas consideradas no cálculo. |
| TOTAL_RUBRICAS_INFORMATIVAS | numeric(15) |  |  | Soma das rubricas com tipo informativa. |
| TOTAL_RUBRICAS_INFORMATIVAS_DEDUTORAS | numeric(13) |  |  | Soma das rubricas com tipo informativa dedutora. |
| MEDIA_DIFERENCIADA_COMISSOES | smallint(2) |  |  | Considerou médias diferenciadas para comissões. (0=Não/1=Sim) |
| I_PERIODO_GOZO_LICENCA_PREMIO | integer(4) |  | S | Código do período gozo da licença prêmio. |
| SIMULACAO | smallint(2) |  |  | Simulação (0=Não/1=Sim) |
| CALCULAR_ADIANTAMENTO_13_SALARIO_MES_ANTERIOR | smallint(2) |  |  | Calcular adiantamento 13º com base no salário do mês anterior. (0=Não/1=Sim) |
| GRAVOU_VALOR_INTEGRAL_RUBRICAS | smallint(2) |  |  | Gravou o valor integral das rubricas que é considerado para algumas bases de cálculo. (0=Não/1=Sim) |
| SALARIO | numeric(13) |  |  | Salário considerado no cálculo. |
| SALARIO_MENSAL_SINDICATO | numeric(13) |  |  | Salário mensal no sindicato considerado no cálculo do dirigente sindical. |
| SALARIO_SEMANA | numeric(13) |  |  | Salário por semana considerado no cálculo. |
| SALARIO_SEMANA_SINDICATO | numeric(13) |  |  | Salário por semana no sindicato considerado no cálculo do dirigente sindical. |
| SALARIO_DIA | numeric(30) |  |  | Salário por dia considerado no cálculo. |
| SALARIO_DIA_SINDICATO | numeric(30) |  |  | Salário por dia no sindicato considerado no cálculo do dirigente sindical. |
| SALARIO_HORA | numeric(30) |  |  | Salário por hora considerado no cálculo. |
| SALARIO_HORA_SINDICATO | numeric(30) |  |  | Salário por hora considerado no sindicato considerado no cálculo do dirigente sindical. |
| ANTECIPACAO_MES | numeric(13) |  |  | Antecipação mensal considerada no cálculo. |
| ANTECIPACAO_SEMANA | numeric(13) |  |  | Antecipação por semana considerada no cálculo. |
| ANTECIPACAO_DIA | numeric(30) |  |  | Antecipação por dia considerada no cálculo. |
| ANTECIPACAO_HORA | numeric(30) |  |  | Antecipação por hora considerada no cálculo. |
| I_DADOS_EVENTOS_ESOCIAL_S_1200 | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL_S_1200 | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL_S_1200 | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL_S_1200 | smallint(2) |  |  | Enviar para o eSocial o evento S-1200. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL_S_1200 | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL_S_1200 | smallint(2) |  |  | Gerar retificação para o eSocial do evento S-1200. (0=Não/1=Sim) |
| I_DADOS_EVENTOS_ESOCIAL_S_1210 | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL_S_1210 | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL_S_1210 | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL_S_1210 | smallint(2) |  |  | Enviar para o eSocial o evento S-1210. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL_S_1210 | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL_S_1210 | smallint(2) |  |  | Gerar retificação para o eSocial do evento S-1210. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL_S_1200 | smallint(2) |  |  | Marcação do evento S-1200 para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL_S_1210 | smallint(2) |  |  | Marcação do evento S-1210 para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| CALCULAR_ADICIONAL_FERIAS_MP_927 | smallint(2) |  |  | Calcular adicional de 1/3 das férias MP 927 de 2020 (0-Não/1-Sim) |
| I_CALCULOS_PAGAMENTO_ADICIONAL_MP_927_OLD | integer(4) |  | S | Código do cálculo do pagamento do adicional MP 927 - Renomeado |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| LIMITAR_PAGAMENTO_CONTRIB_TERCEIRO_20_SALARIO_MINIMO | smallint(2) |  |  | Limitar o pagamento da contribuição de terceiros a 20 salários mínimos. (0=Não/1=Valor à recolher/2=Base de cálculo) |
| VERSAO_REGRA_LEIAUTE_ESOCIAL | varchar(10) |  | S | Versão das regras do leiaute do eSocial usadas no calculo. |
| NUMERO_RPA | numeric(10) |  | S | RPA RELACIONADO |
| POSSUI_RPA_INDIVIDUALIZADO | integer(4) |  |  | Flag que define se a folha mensal possui calculos destrinchados de RPA. |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código sequencial de calculos |
| I_CALCULOS_PAGAMENTO_ADICIONAL_MP_927 | uniqueidentifier(16) |  | S | Código do cálculo do pagamento do adicional MP 927 |
| I_CALCULOS_DESCONTO_ARREDONDAMENTO | uniqueidentifier(16) |  | S | Código do cálculo que descontou o arredondamento |
| I_CALCULOS_COMPLEMENTOS | uniqueidentifier(16) |  | S | Código do complemento de cálculo |
| DATA_HORA | timestamp(8) |  | S | Data e hora da simulação do cálculo. |
| CONSIDERAR_CONTAGEM_AVOS_13_FERIAS_DATA_EFEITO_REINTEGRACAO | smallint(2) |  |  | Considerar para a contagem de avos de direito de 13º salário e férias a partir da data efeito da reintegração. (0=Não/1=Sim) |
| USUARIO_CALCULO | varchar(128) |  | S | Usuário que efetuou o cálculo |
| DATA_HORA_CALCULO | timestamp(8) |  | S | Data e hora do cálculo |
| POSSUI_DESCONTO_FAIXA_ETARIA | smallint(2) |  |  | Possui desconto por faixa etária (0=Não/1=Sim) |
| I_CONVOCACAO | numeric(10) |  | S | Convocacao Intermitente Relacionada |
| POSSUI_CONVOCACAO_INDIVIDUALIZADA | integer(4) |  |  | Flag que define se a folha mensal possui calculos destrinchados de CONVOCAÇÃO. |
| CALCULAR_13_ADIANTAMENTO_VALOR_INTEGRAL | smallint(2) |  |  | Calcular no 13º adiantamento o valor integral do 13º salário. (0=Não/1=Sim) |
