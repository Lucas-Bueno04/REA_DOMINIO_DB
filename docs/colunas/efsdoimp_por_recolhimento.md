# EFSDOIMP_POR_RECOLHIMENTO — Saldo dos impostos - detalhamento dos impostos por código de recolhimento
407.907 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=COMPLEMENTAR, 52=13SAL) |
| CODIGO_RECOLHIMENTO | char(6) |  |  | Código de recolhimento |
| PARCELA | integer(4) |  |  | Parcela |
| SALDO_RECOLHER | numeric(13) |  |  | Saldo a recolher |
| VALOR_CONTABIL_ENTRADA | numeric(13) |  |  | Valor contábil entrada |
| BASE_CALCULO_ENTRADA | numeric(13) |  |  | Base de cálculo entrada |
| VALOR_IMPOSTO_ENTRADA | numeric(13) |  |  | Valor do imposto entrada |
| OUTROS_CREDITOS | numeric(13) |  |  | Outros créditos |
| OUTROS_DEBITOS | numeric(13) |  |  | Outros débitos |
| ESTORNO_CREDITOS | numeric(13) |  |  | Estorno de créditos |
| ESTORNO_DEBITOS | numeric(13) |  |  | Estorno de débitos |
| VALOR_PAGO | numeric(13) |  |  | Valor pago |
| DATA_VENCIMENTO | date(4) |  | S | Data do vencimento |
| I_RECOLHIMENTO | integer(4) | PK |  | Sequencial do código de recolhimento |
| VALOR_CONTABIL_SAIDA | numeric(13) |  |  | Valor contábil saída |
| BASE_CALCULO_SAIDA | numeric(13) |  |  | Base de cálculo saída |
| VALOR_IMPOSTO_SAIDA | numeric(13) |  |  | Valor do imposto saída |
| SALDO_CREDOR | numeric(13) |  |  | Saldo credor |
| SALDO_DEVEDOR | numeric(13) |  |  | Saldo devedor |
| SALDO_CREDOR_ANTERIOR | numeric(13) |  |  | Saldo credor anterior |
| CLASSE_VENCIMENTO | integer(4) |  |  | Classe do vencimento |
| OUTRAS_DEDUCOES | numeric(13) |  |  | Outras deduções |
| OUTROS_ACRESCIMOS | numeric(13) |  |  | Outros acréscimos |
| VALOR_ISENTAS_ENTRADA | numeric(13) |  |  | Valor isentas entrada |
| VALOR_OUTRAS_ENTRADA | numeric(13) |  |  | Valor outras entrada |
| VALOR_ISENTAS_SAIDA | numeric(13) |  |  | Valor isentas saída |
| VALOR_OUTRAS_SAIDA | numeric(13) |  |  | Valor outras saída |
| VALOR_REGIME_ESPECIAL | numeric(13) |  |  | Valor regime especial |
| VALOR_CREDITO_PRESUMIDO | numeric(13) |  |  | Valor crédito presumido |
| VALOR_ESTORNO_REGIME_ESPECIAL | numeric(13) |  |  | Valor estorno regime especial |
| VALOR_ESTORNO_CREDITO_PRESUMIDO | numeric(13) |  |  | Valor estorno crédito presumido |
| COMPENSACAO_PAGAMENTO_INDEVIDO_MAIOR | numeric(13) |  |  | Compensação de pagamento indevido ou a maior |
| RESSARCIMENTO_COMPENSACAO_PIS_COFINS | numeric(13) |  |  | Ressarcimento/Compensação de PIS/COFINS |
| VALOR_DIFERIDO | numeric(13) |  |  | Valor Diferido |
| VALOR_DIFERIDO_ANTERIOR | numeric(13) |  |  | Valor Diferido anterior |
| CREDITOS_DEVOLUCAO_ENTRADAS | numeric(13) |  |  | Crédito pelas devoluções de entradas |
| CREDITOS_DEVOLUCAO_SAIDAS | numeric(13) |  |  | Crédito pelas devoluções de saídas |
| OUTRAS_COMPENSACOES | numeric(13) |  |  | Outras compensações |
| RESSARCIMENTO_STAT_SIMPLES_NACIONAL | numeric(13) |  |  | Ressarcimento de 31-STAT para empresa do simples nacional |
| RESSARCIMENTO_STAT_OUTRAS_UF | numeric(13) |  |  | Ressarcimento de 31-STAT para empresas de outras UF |
| FUNRURAL_DEVOLUCAO_COMPRA | numeric(13) |  |  | FUNRURAL Devolução Compra |
| FUNRURAL_DEVOLUCAO_VENDA | numeric(13) |  |  | FUNRURAL Devolução Venda |
| FUNRURAL_DEBITO_ENTRADAS_INSS_RAT | numeric(13) |  |  | FUNRURAL Débito Entradas INSSRAT |
| FUNRURAL_DEBITO_SAIDAS_INSS_RAT | numeric(13) |  |  | FUNRURAL Débito Saídas INSSRAT |
| FUNRURAL_DEBITO_ENTRADAS_OUTRAS_ENTIDADES | numeric(13) |  |  | FUNRURAL Débito Entradas Outras Entidades |
| FUNRURAL_DEBITO_SAIDAS_OUTRAS_ENTIDADES | numeric(13) |  |  | FUNRURAL Débito Saídas Outras Entidades |
| FUNRURAL_SALDO_CREDOR_ANTERIOR_INSS_RAT | numeric(13) |  |  | FUNRURAL Saldo Credor Anterior INSSRAT |
| FUNRURAL_DEVOLUCAO_COMPRA_INSS_RAT | numeric(13) |  |  | FUNRURAL Devolução Compra INSSRAT |
| FUNRURAL_DEVOLUCAO_VENDA_INSS_RAT | numeric(13) |  |  | FUNRURAL Devolução Venda INSSRAT |
| FUNRURAL_SALDO_CREDOR_INSS_RAT | numeric(13) |  |  | FUNRURAL Saldo Credor INSSRAT |
| FUNRURAL_SALDO_CREDOR_ANTERIOR_OUTRAS_ENTIDADES | numeric(13) |  |  | FUNRURAL Saldo Credor Anterior Outras Entidades |
| FUNRURAL_DEVOLUCAO_COMPRA_OUTRAS_ENTIDADES | numeric(13) |  |  | FUNRURAL Devolução Compra Outras Entidades |
| FUNRURAL_DEVOLUCAO_VENDA_OUTRAS_ENTIDADES | numeric(13) |  |  | FUNRURAL Devolução Venda Outras Entidades |
| FUNRURAL_SALDO_CREDOR_OUTRAS_ENTIDADES | numeric(13) |  |  | FUNRURAL Saldo Credor Outras Entidades |
| FUNRURAL_SALDO_DEVEDOR_INSS_RAT | numeric(13) |  |  | FUNRURAL Saldo Devedor INSSRAT |
| FUNRURAL_SALDO_DEVEDOR_OUTRAS_ENTIDADES | numeric(13) |  |  | FUNRURAL Saldo Devedor Outras Entidades |
| FUNRURAL_VALOR_A_RECOLHER_INSS_RAT | numeric(13) |  |  | FUNRURAL Valor a Recolher INSSRAT |
| FUNRURAL_VALOR_A_RECOLHER_OUTRAS_ENTIDADES | numeric(13) |  |  | FUNRURAL Valor a Recolher Outras Entidades |
| FUNRURAL_SALDO_DIFERIDO_INSS_RAT | numeric(13) |  |  | FUNRURAL Saldo Diferido INSSRAT |
| FUNRURAL_SALDO_DIFERIDO_OUTRAS_ENTIDADES | numeric(13) |  |  | FUNRURAL Saldo Diferido Outras Entidades |
| FUNRURAL_SALDO_DIFERIDO_ANTERIOR_INSS_RAT | numeric(13) |  |  | FUNRURAL Saldo Diferido Anterior INSSRAT |
| FUNRURAL_SALDO_DIFERIDO_ANTERIOR_OUTRAS_ENTIDADES | numeric(13) |  |  | FUNRURAL Saldo Diferido Anterior Outras Entidades |
| DEBITOS_COMPENSACOES | numeric(13) |  |  | Débitos Compensações |
| RESSARCIMENTO_CREDITO_IPI_LANCADO | numeric(13) |  |  | Ressarcimento de Crédito IPI Lançado |
| RESSARCIMENTO_COMPENSACAO_PIS_COFINS_DEDUCOES | numeric(13) |  |  | Ressarcimento/Compensação de PIS/COFINS Deduções |
| VALOR_IPI_DEVOLUCAO | numeric(13) |  |  | IPI Devolução |
| BASE_CALCULO | numeric(13) |  |  | Base de cálculo |
| FETHAB_CONTRIBUICAO_FACS | numeric(13) |  |  | Contribuição ao Fundo de Apoio à Cultura da Soja - FACS |
| FETHAB_CONTRIBUICAO_FABOV | numeric(13) |  |  | Contribuição ao Fundo de Apoio à Bovinocultura de Corte - FABOV |
| FETHAB_CONTRIBUICAO_FAMAD | numeric(13) |  |  | Contribuição ao Fundo de Apoio à Madeira - FAMAD |
| FETHAB_CONTRIBUICAO_IMAMT | numeric(13) |  |  | Contribuição ao Instituito Mato-grossense do Algodão - IMAmt |
| FETHAB_ADICIONAL | numeric(13) |  |  | Contribuição adicional ao FETHAB |
| FUNRURAL_DEBITO_ENTRADAS_INSS | numeric(13) |  |  | FUNRURAL Débito Entradas INSS |
| FUNRURAL_DEBITO_ENTRADAS_RAT | numeric(13) |  |  | FUNRURAL Débito Entradas RAT |
| FUNRURAL_DEBITO_SAIDAS_INSS | numeric(13) |  |  | FUNRURAL Débito Saídas INSS |
| FUNRURAL_DEBITO_SAIDAS_RAT | numeric(13) |  |  | FUNRURAL Débito Saídas RAT |
| FUNRURAL_SALDO_CREDOR_ANTERIOR_INSS | numeric(13) |  |  | FUNRURAL Saldo Credor Anterior INSS |
| FUNRURAL_SALDO_CREDOR_ANTERIOR_RAT | numeric(13) |  |  | FUNRURAL Saldo Credor Anterior RAT |
| FUNRURAL_DEVOLUCAO_COMPRA_INSS | numeric(13) |  |  | FUNRURAL Devolução Compra INSS |
| FUNRURAL_DEVOLUCAO_COMPRA_RAT | numeric(13) |  |  | FUNRURAL Devolução Compra RAT |
| FUNRURAL_DEVOLUCAO_VENDA_INSS | numeric(13) |  |  | FUNRURAL Devolução Venda INSS |
| FUNRURAL_DEVOLUCAO_VENDA_RAT | numeric(13) |  |  | FUNRURAL Devolução Venda RAT |
| FUNRURAL_SALDO_CREDOR_INSS | numeric(13) |  |  | FUNRURAL Saldo Credor INSS |
| FUNRURAL_SALDO_CREDOR_RAT | numeric(13) |  |  | FUNRURAL Saldo Credor RAT |
| FUNRURAL_SALDO_DEVEDOR_INSS | numeric(13) |  |  | FUNRURAL Saldo Devedor INSS |
| FUNRURAL_SALDO_DEVEDOR_RAT | numeric(13) |  |  | FUNRURAL Saldo Devedor RAT |
| FUNRURAL_VALOR_A_RECOLHER_INSS | numeric(13) |  |  | FUNRURAL Valor a Recolher INSS |
| FUNRURAL_VALOR_A_RECOLHER_RAT | numeric(13) |  |  | FUNRURAL Valor a Recolher RAT |
| FUNRURAL_SALDO_DIFERIDO_INSS | numeric(13) |  |  | FUNRURAL Saldo Diferido INSS |
| FUNRURAL_SALDO_DIFERIDO_RAT | numeric(13) |  |  | FUNRURAL Saldo Diferido RAT |
| FUNRURAL_SALDO_DIFERIDO_ANTERIOR_INSS | numeric(13) |  |  | FUNRURAL Saldo Diferido Anterior INSS |
| FUNRURAL_SALDO_DIFERIDO_ANTERIOR_RAT | numeric(13) |  |  | FUNRURAL Saldo Diferido Anterior RAT |
| ICMSA_OUTROS_CREDITOS_PAGTOS_MAIOR_DUPLICIDADE_INDEVIDOS | numeric(13) |  |  | ICMSA MG - Outros créditos - Pagamentos feitos a maior, em duplicidade ou indevidos |
| FETHAB_CONTRIBUICAO_IAGRO | numeric(13) |  |  | Contribuição ao Instituto Mato-Grossense do Agronegócio (IAGRO) |
| FUNRURAL_ESTORNO_DEBITO_INSS | numeric(13) |  |  | Valor estorno débito INSS |
| FUNRURAL_ESTORNO_DEBITO_RAT | numeric(13) |  |  | Valor estorno debito RAT |
| FUNRURAL_ESTORNO_DEBITO_OUTRAS_ENTIDADES | numeric(13) |  |  | Valor estorno debito outras entidades |
| FETHAB_CONTRIBUICAO_CIPEM | numeric(13) |  |  | Contribuição ao Centro das Indústrias Prod. e Export. de Madeira do Estado MT (CIPEM) |
| FUNDERSUL_DEBITOS_ENTRADAS | numeric(13) |  |  | FUNDERSUL - Débitos pelas entradas |
| FUNDERSUL_DEBITOS_SAIDAS | numeric(13) |  |  | FUNDERSUL - Débitos pelas saídas |
| FUNDEMS_DEBITOS_ENTRADAS | numeric(13) |  |  | FUNDEMS - Débitos pelas entradas |
| FUNDEMS_DEBITOS_SAIDAS | numeric(13) |  |  | FUNDEMS - Débitos pelas saídas |
| FUNRURAL_DEBITO_ENTRADAS_OUTRAS_ENTIDADES_TRIB_SOBRE_FOLHA_PAGTO | numeric(13) |  |  | FUNRURAL Débitos pelas entradas outras entidades tributação sobre folha pagamento |
| FETHAB_CONTRIBUICAO_IMAFIR | numeric(13) |  |  | Contribuição ao Instituto Mato-grossense do Feijão, Pulses, Grãos Especiais e Irrigação - IMAFIR/MT |
| RECALI_OUTROS_CREDITOS_PAGTOS_MAIOR_DUPLICIDADE_INDEVIDOS | numeric(13) |  |  | RECALI MG - Outros créditos - Pagamentos feitos a maior, em duplicidade ou indevidos |
| FUNRURAL_SOMENTE_FORN_QUE_POSSUI_TRIB_FOLHA_PAGAMENTO | char(1) |  |  | FUNRURAL - Somente Fornecedor que possui tributação na folha de pagamento |
| FECOP_ST_RECUP_RESSARC_ADRC_ST | numeric(13) |  |  | FECOP ST a recuperar/ressarcir conforme NPF 03/2020 - ADRC-ST |
| FECOP_ST_COMP_ADRC_ST | numeric(13) |  |  | FECOP ST a complementar conforme NPF 03/2020 - ADRC-ST |
| VALOR_PAGO_COMPLEMENTO | numeric(13) |  |  | Valor Pago Complemento DRCST |
| RESSARCIMENTO_ICMS_ST_ACOBERTADO_NFE | numeric(13) |  |  | Ressarcimento de ICMS Substituição Tributária acobertado por NF-e |
| FETHAB_CONTRIBUICAO_IMAD | numeric(13) |  |  | Contribuição ao Instituto da Madeira do Estado de Mato Grosso - IMAD/MT |
| FETHAB_CONTRIBUICAO_INPECMT | numeric(13) |  |  | Contribuição ao Instituto da Pecuária de Corte Mato-grossense - INPECMT |
| VALOR_IPI_DEVOLUCAO_DEBITO | numeric(13) |  |  | IPI Devolução Debito |
| IOF_DEBITOS_CONTRATOS_FOMENTO_MERCANTIL | numeric(13) |  |  | IOF - Débitos pelos contratos de fomento mercantil |
| IOF_DEBITOS_CONTRATOS_EMPRESA_SIMPLES_CREDITO | numeric(13) |  |  | IOF - Débitos pelos contratos de empresa simples de crédito |
| FECOEP_DEBITO_SAIDAS | numeric(12) |  |  | FECOEP - Debitos pelas saidas |
| FECOEP_DEBITO_ENTRADAS | numeric(12) |  |  | FECOEP - Debitos pelas entradas |
| FECOEP_CREDITO_ENTRADAS | numeric(12) |  |  | FECOEP - Creditos pelas entradas |
| FECOEP_PAGAMENTO | numeric(12) |  |  | FECOEP - Pagamento |
| ESTORNO_LIMITE_RECOLHIMENTO | numeric(12) |  |  | Estorno - Limite de recolhimento |
| FUNRURAL_TRIBUTOS_FEDERAIS_CAEPF | numeric(13) |  |  | FUNRURAL - Gerar valor nos Tributos Federais com base na inscrição da empresa e cliente |
| FUNDERSUL_DEVOLUCAO_COMPRA_MESMO_PERIODO | numeric(13) |  |  | FUNDERSUL - Devolução de compra mesmo período |
| FUNDERSUL_DEVOLUCAO_COMPRA_PERIODO_ANTERIOR | numeric(13) |  |  | FUNDERSUL - Devolução de compra período anterior |
| FUNDERSUL_DEVOLUCAO_COMPRA | numeric(13) |  |  | FUNDERSUL - Devolução de compra |
| FUNDERSUL_DEVOLUCAO_VENDA_MESMO_PERIODO | numeric(13) |  |  | FUNDERSUL - Devolução de venda mesmo período |
| FUNDERSUL_DEVOLUCAO_VENDA_PERIODO_ANTERIOR | numeric(13) |  |  | FUNDERSUL - Devolução de venda período anterior |
| FUNDERSUL_DEVOLUCAO_VENDA | numeric(13) |  |  | FUNDERSUL - Devolução de venda |
| FUNDEMS_DEVOLUCAO_COMPRA_MESMO_PERIODO | numeric(13) |  |  | FUNDEMS - Devolução de compra mesmo período |
| FUNDEMS_DEVOLUCAO_COMPRA_PERIODO_ANTERIOR | numeric(13) |  |  | FUNDEMS - Devolução de compra período anterior |
| FUNDEMS_DEVOLUCAO_COMPRA | numeric(13) |  |  | FUNDEMS - Devolução de compra |
| FUNDEMS_DEVOLUCAO_VENDA_MESMO_PERIODO | numeric(13) |  |  | FUNDEMS - Devolução de venda mesmo período |
| FUNDEMS_DEVOLUCAO_VENDA_PERIODO_ANTERIOR | numeric(13) |  |  | FUNDEMS - Devolução de venda período anterior |
| FUNDEMS_DEVOLUCAO_VENDA | numeric(13) |  |  | FUNDEMS - Devolução de venda |
