# fobasesserv — Bases - Calculo
415.218 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_empregados | integer(4) | PK |  | Empregado |
| i_depto | integer(4) |  |  | Departamento |
| i_ccustos | integer(4) |  |  | Centro de Custos |
| i_cargos | integer(4) |  | S | Cargo |
| competencia | date(4) | PK |  | Competencia |
| tipo_process | integer(4) | PK |  | TIPO DE CALCULO |
| situacao_mes | integer(4) |  |  | Situação do mês (0~89) |
| num_filhos | integer(4) |  |  | No. filhos |
| num_dependentes | integer(4) |  |  | No. Dependentes |
| proventos | numeric(13) |  |  | Proventos |
| descontos | numeric(13) |  |  | Descontos |
| salario_base | numeric(13) |  | S | ** SEM USO ** SALARIO BASE |
| salario_maternidade | numeric(13) |  |  | Salario Maternidade |
| salario_mes | numeric(13) |  |  | Salario Mes |
| valor_irrf | numeric(13) |  | S | ** SEM USO ** VALOR IRRF |
| taxa_irrf | numeric(5) |  | S | ** SEM USO ** TAXA IRRF |
| valor_fgts | numeric(13) |  | S | ** SEM USO ** VALOR FGTS |
| valor_inss | numeric(13) |  | S | ** SEM USO ** VALOR INSS |
| taxa_inss | numeric(5) |  | S | ** SEM USO ** TAXA INSS |
| base_inss | numeric(13) |  | S | ** SEM USO ** BASE INSS |
| excedente_inss | numeric(13) |  | S | ** SEM USO ** EXCEDENTE INSS |
| base_irrf | numeric(13) |  | S | ** SEM USO ** BASE IRRF |
| abat_irrf | numeric(13) |  | S | ** SEM USO ** ABATIMENTO IRRF |
| ded_irrf | numeric(13) |  | S | ** SEM USO ** DEDUCAO IRRF |
| desc_depend | numeric(13) |  | S | ** SEM USO ** DESCONTO DEPENDENTE |
| val_sal_fam | numeric(13) |  |  | Valor Sal. Familia |
| base_fgts | numeric(13) |  | S | ** SEM USO ** BASE FGTS |
| base_sindicato | numeric(13) |  | S | ** SEM USO ** BASE SINDICATO |
| base_hextra | numeric(13) |  | S | ** SEM USO ** BASE HORA EXTRA |
| base_periculosidade | numeric(13) |  | S | ** SEM USO ** BASE PERICULOSIDADE |
| basex1 | numeric(13) |  | S | ** SEM USO ** BASE AUXILIAR 1 |
| basex2 | numeric(13) |  | S | ** SEM USO ** BASE AUXILIAR 2 |
| basex3 | numeric(13) |  | S | ** SEM USO ** BASE AUXILIAR 3 |
| val_inss_empresa | numeric(13) |  | S | ** SEM USO ** VALOR INSS EMPRESA |
| val_inss_terceiro | numeric(13) |  | S | ** SEM USO ** VALOR INSS TERCEIRO |
| val_acid_trabalho | numeric(13) |  | S | ** SEM USO ** VALOR ACIDENTE TRABALHO |
| teve_afast_mes | char(1) |  | S | ** SEM USO ** TEVE AFASTAMENTO MES |
| nume_cheque | integer(4) |  | S | No. Cheque |
| i_servicos | integer(4) | PK |  | Servico |
| varios_servicos | char(1) |  | S | ** SEM USO ** VARIOS SERVICOS NO MESMO MES |
| dedinssmat13 | numeric(13) |  |  | Deducao INSS 13 |
| data_pagto | date(4) |  |  | Data pagamento |
| teve_ferias | char(1) |  | S | ** SEM USO ** TEVE FERIAS |
| inicio_ferias | date(4) |  | S | ** SEM USO ** INICIO FERIAS |
| fim_ferias | date(4) |  | S | ** SEM USO ** FIM FERIAS |
| base_inss_fer | numeric(13) |  | S | ** SEM USO ** BASE INSS FERIAS |
| valor_inss_fer | numeric(13) |  | S | ** SEM USO ** VALOR INSS FERIAS |
| base_fgts_fer | numeric(13) |  | S | ** SEM USO ** BASE FGTS FERIAS |
| valor_fgts_fer | numeric(13) |  | S | ** SEM USO ** VALOR FGTS FERIAS |
| base_pis | numeric(13) |  | S | ** SEM USO ** BASE PIS |
| valor_pis | numeric(15) |  | S | ** SEM USO ** VALOR PIS |
| base_irrf_fer | numeric(13) |  | S | ** SEM USO ** BASE IRRF FERIAS |
| valor_irrf_fer | numeric(13) |  | S | ** SEM USO ** VALOR IRRF FERIAS |
| base_irrf_13 | numeric(13) |  | S | ** SEM USO ** BASE IRRF 13 |
| abat_irrf_13 | numeric(13) |  | S | ** SEM USO ** ABATIMENTO IRRF 13 |
| taxa_irrf_13 | numeric(13) |  | S | ** SEM USO ** TAXA IRRF 13 |
| valor_irrf_13 | numeric(13) |  | S | ** SEM USO ** VALOR IRRF 13 |
| deduc_irrf_13 | numeric(13) |  | S | ** SEM USO ** DEDUCAO IRRF 13 |
| depend_irrf_13 | numeric(13) |  | S | ** SEM USO ** DEPENDENTE IRRF 13 |
| nodepend_irrf_13 | tinyint(1) |  | S | ** SEM USO ** NO. DEPENDENTE 13 |
| inss_empresa_fer | numeric(13) |  | S | ** SEM USO ** INSS EMPRESA FERIAS |
| acid_trab_fer | numeric(13) |  | S | ** SEM USO ** ACID. TRAB. FERIAS |
| inss_terc_fer | numeric(13) |  | S | ** SEM USO ** INSS TERCEIRO FERIAS |
| valor_pis_fer | numeric(13) |  | S | ** SEM USO ** VALOR PIS FERIAS |
| desc_lei_irrf | numeric(13) |  | S | ** SEM USO ** DESC. LEI IRRF |
| desc_lei_irrf_13 | numeric(13) |  | S | ** SEM USO ** DESC. LEI IRFF 13 |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| rateio | integer(4) | PK |  | Rateio |
| dias_servico | integer(4) |  |  | Numero de dias que o empregado ficou no servico |
| implantado | tinyint(1) |  | S | 1=Dados implantados, 0=Calculado pelo sistema |
| i_filiais | integer(4) |  |  | Código da filial |
| I_CALCULOS_OLD | integer(4) |  | S | Código sequencial de calculos - Renomeado |
| categoria | smallint(2) |  |  | Categoria |
| horas_dia | numeric(5) |  |  | Horas dia |
| horas_semana | numeric(5) |  |  | Horas semana |
| horas_mes | numeric(5) |  |  | Horas mes |
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
| SIMULACAO | smallint(2) |  |  | Simulação de cálculo. (0=Não/1=Sim) |
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
| I_CALCULOS_COMPLEMENTOS | uniqueidentifier(16) |  | S | Código do complemento de cálculo |
| I_CALCULOS_DESCONTO_ARREDONDAMENTO | uniqueidentifier(16) |  | S | Código do cálculo que descontou o arredondamento |
| I_CALCULOS_PAGAMENTO_ADICIONAL_MP_927 | uniqueidentifier(16) |  | S | Código do cálculo do pagamento do adicional MP 927 |
| DATA_HORA | timestamp(8) |  | S | Data e hora da gravação do cálculo. |
| CONSIDERAR_CONTAGEM_AVOS_13_FERIAS_DATA_EFEITO_REINTEGRACAO | smallint(2) |  |  | Considerar para a contagem de avos de direito de 13º salário e férias a partir da data efeito da reintegração. (0=Não/1=Sim) |
| USUARIO_CALCULO | varchar(128) |  | S | Usuário que efetuou o cálculo |
| DATA_HORA_CALCULO | timestamp(8) |  | S | Data e hora do cálculo |
| POSSUI_DESCONTO_FAIXA_ETARIA | smallint(2) |  |  | Possui desconto por faixa etária (0=Não/1=Sim) |
| I_CONVOCACAO | numeric(10) |  | S | Convocacao Intermitente Relacionada |
| POSSUI_CONVOCACAO_INDIVIDUALIZADA | integer(4) |  |  | Flag que define se a folha mensal possui calculos destrinchados de CONVOCAÇÃO. |
| CALCULAR_13_ADIANTAMENTO_VALOR_INTEGRAL | smallint(2) |  |  | Calcular no 13º adiantamento o valor integral do 13º salário. (0=Não/1=Sim) |
