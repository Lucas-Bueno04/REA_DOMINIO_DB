# EFSDOIMP_ES_COMPETE — Saldo dos Impostos - COMPETE - ES
67 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Período |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| VENCIMENTO | date(4) |  |  | Vencimento |
| CODIGO_RECOLHIMENTO | char(6) |  |  | Código recolhimento |
| VALOR_RECOLHER | numeric(13) |  |  | Valor a recolher |
| VALOR_PAGO | numeric(13) |  |  | Valor pago |
| DEDUCAO_CREDITO_ART_534_ZZA | numeric(13) |  |  | Dedução do crédito total - Art. 534-Z-Z-A, §2°, III, a |
| DEDUCAO_CREDITO_ART_530_LRK | numeric(13) |  |  | Dedução do crédito total - Art. 530-L-R-K, §4, III, a |
| OUTROS_DEBITOS_DEVOLUCAO_VENDA_INTERNA | numeric(13) |  |  | Outros Débitos - Devoluções de vendas internas |
| OUTROS_DEBITOS_DEVOLUCAO_VENDA_INTERESTADUAIS | numeric(13) |  |  | Outros Débitos - Devoluções de vendas interestaduais |
| OUTROS_DEBITOS_DEVOLUCAO_COMPRA_INTERNA | numeric(13) |  |  | Outros Débitos - Devoluções de compras internas |
| OUTROS_DEBITOS_DEVOLUCAO_COMPRA_INTERESTADUAIS | numeric(13) |  |  | Outros Débitos - Devoluções de compras interestaduais |
| ESTORNO_CREDITOS_DEVOLUCAO_VENDA_INTERNA | numeric(13) |  |  | Estorno de Créditos - Devoluções de vendas internas |
| ESTORNO_CREDITOS_DEVOLUCAO_VENDA_INTERESTADUAIS | numeric(13) |  |  | Estorno de Créditos - Devoluções de vendas interestaduais |
| ESTORNO_CREDITOS_DEVOLUCAO_COMPRA_INTERNA | numeric(13) |  |  | Estorno de Créditos - Devoluções de compras internas |
| ESTORNO_CREDITOS_DEVOLUCAO_COMPRA_INTERESTADUAIS | numeric(13) |  |  | Estorno de Créditos - Devoluções de compras interestaduais |
| OUTROS_CREDITOS_DEVOLUCAO_VENDA_INTERNA | numeric(13) |  |  | Outros Créditos - Devoluções de vendas internas |
| OUTROS_CREDITOS_DEVOLUCAO_VENDA_INTERESTADUAIS | numeric(13) |  |  | Outros Créditos - Devoluções de vendas interestaduais |
| OUTROS_CREDITOS_DEVOLUCAO_COMPRA_INTERNA | numeric(13) |  |  | Outros Créditos - Devoluções de compras internas |
| OUTROS_CREDITOS_DEVOLUCAO_COMPRA_INTERESTADUAIS | numeric(13) |  |  | Outros Créditos - Devoluções de compras interestaduais |
| ESTORNO_DEBITOS_DEVOLUCAO_VENDA_INTERNA | numeric(13) |  |  | Estorno de Débitos - Devoluções de vendas internas |
| ESTORNO_DEBITOS_DEVOLUCAO_VENDA_INTERESTADUAIS | numeric(13) |  |  | Estorno de Débitos - Devoluções de vendas interestaduais |
| ESTORNO_DEBITOS_DEVOLUCAO_COMPRA_INTERNA | numeric(13) |  |  | Estorno de Débitos - Devoluções de compras internas |
| ESTORNO_DEBITOS_DEVOLUCAO_COMPRA_INTERESTADUAIS | numeric(13) |  |  | Estorno de Débitos - Devoluções de compras interestaduais |
| CREDITO_BASE_REDUZIDA | numeric(13) |  |  | Crédito registrado ou limitado - Base Reduzida - Art. 534-Z-Z-A, §2°, III, b |
| CREDITO_FORA_ESTADO | numeric(13) |  |  | Crédito registrado ou limitado - Fora do Estado - Art. 530-L-R-K, §4°, III, b |
| AJUSTE_RECOLHER_IMPOSTO_OPERACAO_ART_530_LRK | numeric(13) |  |  | Ajsute para recolher o imposto devido nas operações do Art. 530-L-R-K |
| ESTORNO_ADICIONAL_SAIDAS_INTERESTADUAIS | numeric(13) |  |  | Estorno adicional de débito das saídas interestaduais - Art. 530-L-R-K |
| SALDO_CREDOR_APURACAO_OPERACOES_INTERNAS | numeric(13) |  |  | Saldo credor Apuração operações internas |
| SALDO_DEVEDOR_APURACAO_OPERACOES_INTERESTADUAIS | numeric(13) |  |  | Saldo devedor Apuração operações interestaduais |
| SALDO_CREDOR_ANTERIOR_INTERNAS | numeric(13) |  |  | Saldo credor Anterior Internas |
| VENDAS_SEM_BENEFICIO | numeric(13) |  |  | Saídas sem benefício com partic. proporção |
| VENDAS_TOTAIS_TRIBUTADA | numeric(13) |  |  | Total Saídas |
| VENDAS_INTERNAS_BENEFICIADAS | numeric(13) |  |  | Saídas com Redução B.C. - Art. 534-ZZA |
| VENDAS_INTERESTADUAIS_BENEFICIADAS | numeric(13) |  |  | Saídas interestaduais - Art. 530-LRK |
| PROPORCAO_VIB | numeric(13) |  |  | Saídas com Redução B.C. - Art. 534-ZZA / Proporção |
| PROPORCAO_VINTB | numeric(13) |  |  | Saídas interestaduais - Art. 530-LRK / Proporção |
| PROPORCAO_VSB | numeric(13) |  |  | Saídas sem benefício com partic. proporção / Proporção |
| BASE_CALCULO_ENTRADAS_PROPORCAO_SEM_7_PORCENTO_VIB | numeric(13) |  |  | Limite de crédito das entradas proporcionais/Base cálculo ICMS VIB |
| BASE_CALCULO_ENTRADAS_PROPORCAO_COM_7_PORCENTO_VIB | numeric(13) |  |  | Limite de crédito das entradas proporcionais/Limite de 7% VIB |
| BASE_CALCULO_ENTRADAS_PROPORCAO_SEM_7_PORCENTO_VINTB | numeric(13) |  |  | Limite de crédito das entradas proporcionais/Base cálculo ICMS VINTB |
| BASE_CALCULO_ENTRADAS_PROPORCAO_COM_7_PORCENTO_VINTB | numeric(13) |  |  | Limite de crédito das entradas proporcionais/Limite de 7% VINTB |
| BASE_CALCULO_ENTRADAS_PROPORCAO_SEM_7_PORCENTO_VSB | numeric(13) |  |  | Limite de crédito das entradas proporcionais/Base cálculo ICMS VSB |
| VALOR_IMPOSTO_RATEIO_VIB | numeric(13) |  |  | Limite de crédito das entradas proporcionais/Crédito p/Rateio VIB |
| VALOR_IMPOSTO_RATEIO_VINTB | numeric(13) |  |  | Limite de crédito das entradas proporcionais/Crédito p/Rateio VINTB |
| LIMITE_CREDITO_VIB | numeric(13) |  |  | Limite de crédito das entradas proporcionais/Limite de crédito total VIB |
| LIMITE_CREDITO_VINTB | numeric(13) |  |  | Limite de crédito das entradas proporcionais/Limite de crédito total VINTB |
| CREDITO_REGISTRADOS_PROPORCIONAIS_VALOR_ENTRADAS | numeric(13) |  |  | Crédito Total |
| CREDITO_VSB | numeric(13) |  |  | Crédito proporcional VSB |
| SALDO_CREDOR_ANTERIOR_PESSOA_FISICA | numeric(13) |  |  | Saldo credor Anterior Pessoa Física |
| VALOR_SAIDAS_INTERNAS | numeric(13) |  |  | Valor Saídas Internas |
| SALDO_DEVEDOR_APURACAO_OPERACOES_INTERNAS | numeric(13) |  |  | Saldo devedor Apuração operações internas |
| BASE_CALCULO_IND_COM | numeric(13) |  |  | Base Calculo Carga Efetiva Ind Com |
| PERCENTUAL_CARGA_EFETIVA_IND_COM | numeric(13) |  |  | % Carga Efetiva Ind Com |
| VALOR_CARGA_EFETIVA_IND_COM | numeric(13) |  |  | Valor Carga Efetiva Ind Com |
| BASE_CALCULO_CF | numeric(13) |  |  | Base Calculo Carga Efetiva CF |
| PERCENTUAL_CARGA_EFETIVA_CF | numeric(13) |  |  | % Carga Efetiva CF |
| VALOR_CARGA_EFETIVA_CF | numeric(13) |  |  | Valor Carga Efetiva CF |
| ESTORNO_ADICIONAL_SAIDAS_INTERESTADUAIS_NEGATIVO | numeric(13) |  |  | Estorno adicional de débito das saídas interestaduais - Art. 530-L-R-K - Negativo |
| VALOR_CREDITO_ENTRADAS_PESSOA_FISICA | numeric(13) |  |  | Crédito pelas entradas Pessoa Física |
| VALOR_SAIDAS_FORA_REGIME_PESSOA_FISICA | numeric(13) |  |  | Saída fora regime Pessoa Física |
| VALOR_CREDITO_FORA_REGIME_PESSOA_FISICA | numeric(13) |  |  | Crédito fora regime Pessoa Física |
| SALDO_DEVEDOR_PESSOA_FISICA | numeric(13) |  |  | Saldo Devedor Pessoa Física |
| SALDO_CREDOR_PESSOA_FISICA | numeric(13) |  |  | Saldo Credor Pessoa Física |
| VALOR_SAIDAS_INTERESTADUAIS | numeric(13) |  |  | Valor Saídas Interestaduais |
| VALOR_SAIDAS_PESSOA_FISICA | numeric(13) |  |  | Valor Saídas Pessoa Física |
| VALOR_CREDITO_ENTRADAS_INTERESTADUAIS | numeric(13) |  |  | Valor Crédito Entradas Interestaduais |
| DEBITO_ESPECIAL_BARES_RESTAURANTES | numeric(13) |  |  | Débito especial - Benefício Art. 530-LRF RICMS |
| ESTORNO_DEBITO_SAIDAS_BARES_RESTAURANTES | numeric(13) |  |  | Estorno de débito pelas saídas ICMS - Benefício Art. 530-LRF RICMS |
| ESTORNO_ICMS_OPERACOES_BENEFICIADAS_BARES_RESTAURANTES_COMPRA | numeric(13) |  |  | Estorno do ICMS das ope. Beneficiadas - Art. 530-LRF RICMS - Compras |
| ESTORNO_ICMS_OPERACOES_BENEFICIADAS_BARES_RESTAURANTES_DEVOLUCAO | numeric(13) |  |  | Estorno do ICMS das ope. Beneficiadas - Art. 530-LRF RICMS - Devolução |
| DEVOLUCAO_DEBITO_ESPECIAL_BARES_RESTAURANTES | numeric(13) |  |  | Devolução - Débito especial - Benefício Art. 530-LRF RICMS |
| ESTORNO_ICMS_RECOLHER_BARES_RESTAURANTES | numeric(13) |  |  | Estorno do ICMS a recolher das Oper. beneficiadas Art.530-LRF RICMS |
| VALOR_RECOLHER_BARES_RESTAURANTES | numeric(13) |  |  | ICMS COMPETE-ES a recolher - Bares, Restaurantes |
| VALOR_PAGO_BARES_RESTAURANTES | numeric(13) |  |  | Valor pago - Bares, Restaurantes |
| CREDITO_PRESUMIDO_BENEFICIO_ART_530_LRI_RICMS | numeric(13) |  |  | Crédito Presumido - Benefício Art. 530-LRI RICMS |
| ESTORNO_ICMS_OPE_BENEFICIADAS_ART_530_LRI_RICMS | numeric(13) |  |  | Estorno do ICMS das ope. Beneficiadas - Art. 530-LRI RICMS |
| DEBITOS_PELAS_SAIDAS | numeric(13) |  |  | Débito pelas saídas |
| CREDITOS_PELAS_ENTRADAS | numeric(13) |  |  | Crédito pelas entradas |
| ESTORNO_CREDITO_PRESUMIDO_BENEFICIO_ART_530_LRI_RICMS_DEVOLUCAO | numeric(13) |  |  | Estorno Crédito Presumido - Benefício Art. 530-LRI RICMS - Devolução |
| ESTORNO_ICMS_RECOLHER_OPER_BENEFICIADAS_ART_530_LRI_ICMS | numeric(13) |  |  | Estorno do ICMS a recolher das Oper. beneficiadas Art.530-LRI RICMS |
| VALOR_RECOLHER_BENEFICIO_ART_530_LRI_RICMS | numeric(13) |  |  | Valor Recolher - Benefício Art. 530-LRI RICMS - Devolução |
| VALOR_PAGO_BENEFICIO_ART_530_LRI_RICMS | numeric(13) |  |  | Valor Pago - Benefício Art. 530-LRI RICMS - Devolução |
| ADICIONAL_ICMS_VENCIMENTO | date(4) |  | S | Adicional ICMS - Dia vencimento |
| ADICIONAL_CODIGO_RECOLHIMENTO | char(6) |  | S | Adicional ICMS - Código Recolhimento |
| ADICIONAL_ICMS_VALOR_RECOLHER | numeric(13) |  |  | Adicional ICMS - Valor Recolher |
| ADICIONAL_ICMS_VALOR_RECOLHER_BARES_RESTAURANTES | numeric(13) |  |  | Adicional ICMS - Valor Recolher Bares e Restaurantes |
| ADICIONAL_ICMS_VALOR_RECOLHER_BENEFICIO_ART_530_LRI_RICMS | numeric(13) |  |  | Adicional ICMS - Valor Recolher Benef. Art. 530 LRI RICMS |
| ADICIONAL_ICMS_VALOR_PAGO | numeric(13) |  |  | Adicional ICMS - Valor Pago |
| ADICIONAL_ICMS_VALOR_PAGO_BARES_RESTAURANTES | numeric(13) |  |  | Adicional ICMS - Valor Pago Bares e Restaurantes |
| ADICIONAL_ICMS_VALOR_PAGO_BENEFICIO_ART_530_LRI_RICMS | numeric(13) |  |  | Adicional ICMS - Valor Pago Benef. Art. 530 LRI RICMS |
| CREDITO_PRESUMIDO_INTERESTADUAIS_IND_METALMECANICA_BENEFICIO_ART_530_LFII_RICMS | numeric(13) |  |  | Crédito presumido nas saídas interestaduais - Art. 530-LF, II RICMS |
| ESTORNO_DEVOLUCAO_CREDITO_PRESUMIDO_INTERESTADUAIS_IND_METALMECANICA_BENEFICIO_ART_530_LFII_RICMS | numeric(13) |  |  | Estorno devolução créd. presumido - Benefício Art. 530-LF, II RICMS |
| ESTORNO_ICMS_SAIDAS_INTERESTADUAIS_IND_METALMECANICA_BENEFICIO_ART_530_LFII_RICMS | numeric(13) |  |  | Estorno do ICMS saídas interestaduais - Art. 530-LF, § 1º, III RICMS |
| ESTORNO_ICMS_SAIDAS_INTERNAS_IND_METALMECANICA_BENEFICIO_ART_530_LFII_RICMS | numeric(13) |  |  | Estorno do ICMS saídas internas - Art. 530-LF, § 1º, II RICMS |
| SAIDAS_INTERESTADUAIS_IND_METALMECANICA_BENEFICIO_ART_530_LFII_RICMS | numeric(13) |  |  | Saídas interestaduais - Art. 530-LF, § 1º, III RICMS |
| SAIDAS_INTERNAS_IND_METALMECANICA_BENEFICIO_ART_530_LFII_RICMS | numeric(13) |  |  | Saídas internas - Art. 530-LF, § 1º, III RICMS |
| SAIDAS_TRIBUTADAS_IND_METALMECANICA_BENEFICIO_ART_530_LFII_RICMS | numeric(13) |  |  | Saídas tributadas - Art. 530-LF, § 1º, III RICMS |
| CREDITO_PELAS_ENTRADAS_IND_METALMECANICA_BENEFICIO_ART_530_LFII_RICMS | numeric(13) |  |  | Crédito pelas entradas - Art. 530-LF, § 1º, III RICMS |
| BASE_CALCULO_ENTRADAS_IND_METALMECANICA_BENEFICIO_ART_530_LFII_RICMS | numeric(13) |  |  | Base de cálculo dos créditos pelas entradas - Art. 530-LF, § 1º, III RICMS |
| PERCENTUAL_SAIDAS_INTERESTADUAIS_IND_METALMECANICA_BENEFICIO_ART_530_LFII_RICMS | numeric(13) |  |  | Percentual de saídas interestaduais beneficiadas - Art. 530-LF, § 1º, III RICMS |
| PERCENTUAL_SAIDAS_INTERNAS_IND_METALMECANICA_BENEFICIO_ART_530_LFII_RICMS | numeric(13) |  |  | Percentual de saídas internas de produtos beneficiados - Art. 530-LF, § 1º, III RICMS |
| VALOR_RECOLHER_BENEFICIO_ART_530_LFII_RICMS | numeric(13) |  |  | Valor recolher ICMS Beneficio Art. 530-L-F |
| ADICIONAL_ICMS_VALOR_RECOLHER_BENEFICIO_ART_530_LFII_RICMS | numeric(13) |  |  | Acional ICMS Benefaicio Art. 530-L-F |
| VALOR_PAGO_BENEFICIO_ART_530_LFII_RICMS | numeric(13) |  |  | Valor Pago - Beneficio Art 53- LF II |
| ADICIONAL_ICMS_VALOR_PAGO_BENEFICIO_ART_530_LFII_RICMS | numeric(13) |  |  | Adicional ICMS - Valor Pago Benef. Art. 530 LRI RICMS |
