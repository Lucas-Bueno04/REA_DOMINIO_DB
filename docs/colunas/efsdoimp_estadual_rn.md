# EFSDOIMP_ESTADUAL_RN — Saldo dos Impostos - Estadual RN
23 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| CREDITO_CONFORME_ALIQUOTA_SN | numeric(13) |  |  | Crédito de ICMS conforme alíquota do Simples Nacional - Art. 23, LC 123/06 |
| CREDITO_AQUISICAO_INDUSTRIA_SN | numeric(13) |  |  | Crédito Presumido na aquisição de Indústrias Simples Nacional - Art. 112, XXIII, RICMS |
| DEVOLUCAO_CONFORME_ALIQUOTA_SN | numeric(13) |  |  | Devolução Crédito de ICMS conforme alíquota do Simples Nacional - Art. 23, LC 123/06 |
| DEVOLUCAO_AQUISICAO_INDUSTRIA_SN | numeric(13) |  |  | Devolução Crédito Presumido na aquisição de Indústrias Simples Nacional - Art. 112, XXIII, RICMS |
| DEVOLUCAO_MERCADORIA_ADQUIRIDA_SN | numeric(13) |  |  | Devolução de mercadoria adquirida de Simples Nacional |
| ESTORNO_DEBITO_DEVOLUCAO_SIMPLES_NACIONAL | numeric(13) |  |  | Estorno de Débito Devolução Simples Nacional |
| ESTORNO_ICMS_ST_TRANSPORTE | numeric(13) |  |  | Estorno ICMS ST Transportes |
| CREDITO_PRESUMIDO_20_TRANSPORTADORAS_ICMS | numeric(13) |  |  | Crédito presumido de 20 para transportadoras |
| REGIME_ATACADISTA_SAIDAS_INTERESTADUAIS_ART_16B_I_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Saídas interestaduais, Art. 16-B, I - Base de cálculo |
| REGIME_ATACADISTA_SAIDAS_INTERESTADUAIS_ART_16B_I_VALOR | numeric(13) |  |  | Regime Atacadista - Saídas interestaduais, Art. 16-B, I - Valor |
| REGIME_ATACADISTA_SAIDAS_INTERNAS_ALIQUOTA_18_ART_16B_III_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Saídas internas à alíquota de 18%, Art. 16-B, III - Base de cálculo |
| REGIME_ATACADISTA_SAIDAS_INTERNAS_ALIQUOTA_18_ART_16B_III_VALOR | numeric(13) |  |  | Regime Atacadista - Saídas internas à alíquota de 18%, Art. 16-B, III - Valor |
| REGIME_ATACADISTA_SAIDAS_INTERNAS_ALIQUOTA_25_OU_27_ART_16B_IV_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Saídas internas à alíquota de 25% ou 27%, Art. 16-B, IV - Base de cálculo |
| REGIME_ATACADISTA_SAIDAS_INTERNAS_ALIQUOTA_25_OU_27_ART_16B_IV_VALOR | numeric(13) |  |  | Regime Atacadista - Saídas internas à alíquota de 25% ou 27%, Art. 16-B, IV - Valor |
| REGIME_ATACADISTA_ADICIONAL_PF_ART_16C_I_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Adicional PF, Art. 16-C, I - Base de cálculo |
| REGIME_ATACADISTA_ADICIONAL_PF_ART_16C_I_VALOR | numeric(13) |  |  | Regime Atacadista - Adicional PF, Art. 16-C, I - Valor |
| REGIME_ATACADISTA_ADICIONAL_PF_ART_16C_II_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Adicional PF, Art. 16-C, II - Base de cálculo |
| REGIME_ATACADISTA_ADICIONAL_PF_ART_16C_II_VALOR | numeric(13) |  |  | Regime Atacadista - Adicional PF, Art. 16-C, II - Valor |
| REGIME_ATACADISTA_ADICIONAL_EXCEDENTE_20_PF_ART_16C_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Adicional excedente 20% PF, Art. 16-C, § Único - Base de cálculo |
| REGIME_ATACADISTA_ADICIONAL_EXCEDENTE_20_PF_ART_16C_VALOR | numeric(13) |  |  | Regime Atacadista - Adicional excedente 20% PF, Art. 16-C, § Único - Valor |
| REGIME_ATACADISTA_ADICIONAL_SAIDA_TRANSFERENCIA_18_ART_16D_I_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Adicional saída em transferência 18%, Art. 16-D, I - Base de cálculo |
| REGIME_ATACADISTA_ADICIONAL_SAIDA_TRANSFERENCIA_18_ART_16D_I_VALOR | numeric(13) |  |  | Regime Atacadista - Adicional saída em transferência 18%, Art. 16-D, I - Valor |
| REGIME_ATACADISTA_ADICIONAL_SAIDA_TRANSFERENCIA_25_OU_27_ART_16D_II_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Adicional saída em transferência 25% ou 27%, Art. 16-D, II - Base de cálculo |
| REGIME_ATACADISTA_ADICIONAL_SAIDA_TRANSFERENCIA_25_OU_27_ART_16D_II_VALOR | numeric(13) |  |  | Regime Atacadista - Adicional saída em transferência 25% ou 27%, Art. 16-D, II - Valor |
| REGIME_ATACADISTA_ADICIONAL_EXCEDENTE_20_SAIDA_TRANSFERENCIA_ART_16D_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Adicional excedente 20% saída transferência, Art. 16-D, § Único - Base de cálculo |
| REGIME_ATACADISTA_ADICIONAL_EXCEDENTE_20_SAIDA_TRANSFERENCIA_ART_16D_VALOR | numeric(13) |  |  | Regime Atacadista - Adicional excedente 20% saída transferência, Art. 16-D, § Único - Valor |
| REGIME_ATACADISTA_CREDITO_AQUISICOES_FORNECEDOR_ATACADISTA_18_ART_16B_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Crédito aquisições de fornecedor atacadista(18%), Art. 16-B, §3º - Base de cálculo |
| REGIME_ATACADISTA_CREDITO_AQUISICOES_FORNECEDOR_ATACADISTA_18_ART_16B_VALOR | numeric(13) |  |  | Regime Atacadista - Crédito aquisições de fornecedor atacadista(18%), Art. 16-B, §3º - Valor |
| REGIME_ATACADISTA_CREDITO_AQUISICOES_FORNECEDOR_ATACADISTA_25_OU_27_ART_16B_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Crédito aquisições fornec. atacadista(25% ou 27%),Art. 16-B, §3 - Base de cálculo |
| REGIME_ATACADISTA_CREDITO_AQUISICOES_FORNECEDOR_ATACADISTA_25_OU_27_ART_16B_VALOR | numeric(13) |  |  | Regime Atacadista - Crédito aquisições fornec. atacadista(25% ou 27%),Art. 16-B, §3 - Valor |
| REGIME_ATACADISTA_CREDITO_AQUISIC_PRODUTOS_INDUSTRIA_LOCAL_ART_16B_I_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Crédito aquisiç. produtos da indústria local, Art. 16-B, §16º, I - Base de cálculo |
| REGIME_ATACADISTA_CREDITO_AQUISIC_PRODUTOS_INDUSTRIA_LOCAL_ART_16B_I_VALOR | numeric(13) |  |  | Regime Atacadista - Crédito aquisiç. produtos da indústria local, Art. 16-B, §16º, I - Valor |
| REGIME_ATACADISTA_CREDITO_AQUISIC_PRODUTOS_INDUSTRIA_LOCAL_ART_16B_II_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Crédito aquisiç. produtos da indústria local, Art. 16-B, §16º, II - Base de cálculo |
| REGIME_ATACADISTA_CREDITO_AQUISIC_PRODUTOS_INDUSTRIA_LOCAL_ART_16B_II_VALOR | numeric(13) |  |  | Regime Atacadista - Crédito aquisiç. produtos da indústria local, Art. 16-B, §16º, II - Valor |
| REGIME_ATACADISTA_CREDITO_AQUISIC_PRODUTOS_CESTA_BASICA_ART_16B_I_BASE_CALULO | numeric(13) |  |  | Regime Atacadista - Crédito aquisiç. produtos da Cesta Básica, Art. 16-B, §16º, I - Base de cálculo |
| REGIME_ATACADISTA_CREDITO_AQUISIC_PRODUTOS_CESTA_BASICA_ART_16B_I_VALOR | numeric(13) |  |  | Regime Atacadista - Crédito aquisiç. produtos da Cesta Básica, Art. 16-B, §16º, I - Valor |
| REGIME_ATACADISTA_ESTORNO_CREDITO_RESULTANTE_SISTEMATICA_NORMAL_APURACAO_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Estorno de crédito resultante da sistemática normal de apuração - Base de cálculo |
| REGIME_ATACADISTA_ESTORNO_CREDITO_RESULTANTE_SISTEMATICA_NORMAL_APURACAO_VALOR | numeric(13) |  |  | Regime Atacadista - Estorno de crédito resultante da sistemática normal de apuração - Valor |
| REGIME_ATACADISTA_ESTORNO_DEBITO_RESULTANTE_SISTEMATICA_NORMAL_APURACAO_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Estorno de débito resultante da sistemática normal de apuração - Base de cálculo |
| REGIME_ATACADISTA_ESTORNO_DEBITO_RESULTANTE_SISTEMATICA_NORMAL_APURACAO_VALOR | numeric(13) |  |  | Regime Atacadista - Estorno de débito resultante da sistemática normal de apuração - Valor |
| REGIME_ATACADISTA_AJUSTE_CARGA_SAIDA_CESTA_BASICA_PRODUTOS_INDUSTRIA_RN_18_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Ajuste na carga saída Cesta Básica e Produtos Indústria RN - 18% - Base de cálculo |
| REGIME_ATACADISTA_AJUSTE_CARGA_SAIDA_CESTA_BASICA_PRODUTOS_INDUSTRIA_RN_18_VALOR | numeric(13) |  |  | Regime Atacadista - Ajuste na carga saída Cesta Básica e Produtos Indústria RN - 18% - Valor |
| REGIME_ATACADISTA_AJUSTE_CARGA_SAIDA_PRODUTOS_INDUSTRIA_RN_25_OU_27_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Ajuste na carga saída Produtos Indústria RN - 25 ou 27% - Base de cálculo |
| REGIME_ATACADISTA_AJUSTE_CARGA_SAIDA_PRODUTOS_INDUSTRIA_RN_25_OU_27_VALOR | numeric(13) |  |  | Regime Atacadista - Ajuste na carga saída Produtos Indústria RN - 25 ou 27% - Valor |
| CREDITO_SOBRE_ESTOQUE_OPERACAO_DE_ENTRADA | numeric(13) |  |  | Regime Atacadista - Crédito 2% sobre os estoques - Art. 16-J, Dec. 22.199/2011 |
| TRANSFERENCIA_CREDITO_ICMS_ACUMULADO | numeric(13) |  |  | Transferência de crédito de ICMS acumulado |
| REGIME_ATACADISTA_CREDITO_AQUISICOES_FORNECEDOR_ATACADISTA_7OUMAIOR_16B_INTERESTADUAL_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Considerar no cálculo as entradas interestaduais - Art. 16-B 7% ou maior Base calculo |
| REGIME_ATACADISTA_CREDITO_AQUISICOES_FORNECEDOR_ATACADISTA_7OUMAIOR_16B_INTERESTADUAL_VALOR | numeric(13) |  |  | Regime Atacadista - Considerar no cálculo as entradas interestaduais - Art. 16-B 7% ou maior Valor |
| REGIME_ATACADISTA_CREDITO_AQUISICOES_FORNECEDOR_ATACADISTA_7OUMENOR_16B_INTERESTADUAL_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Considerar no cálculo as entradas interestaduais - Art. 16-B 7% ou menor Base calculo |
| REGIME_ATACADISTA_CREDITO_AQUISICOES_FORNECEDOR_ATACADISTA_7OUMENOR_16B_INTERESTADUAL_VALOR | numeric(13) |  |  | Regime Atacadista - Considerar no cálculo as entradas interestaduais - Art. 16-B 7% ou menor Valor |
| SALDO_ICMS_VENDAS_COM_CARTAO_SEM_DOCUMENTO | numeric(13) |  |  | ICMS a recolher nas vendas efetuadas com cartão de crédito sem documento fiscal |
| REGIME_ATACADISTA_SAIDAS_INTERNAS_ALIQUOTA_20_ART_16B_III_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Saídas internas à alíquota de 20%, Art. 16-B, III - Base de cálculo |
| REGIME_ATACADISTA_SAIDAS_INTERNAS_ALIQUOTA_20_ART_16B_III_VALOR | numeric(13) |  |  | Regime Atacadista - Saídas internas à alíquota de 20%, Art. 16-B, III - Valor |
| REGIME_ATACADISTA_ADICIONAL_SAIDA_TRANSFERENCIA_20_ART_16D_I_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Adicional saída em transferência 20%, Art. 16-D, I - Base de cálculo |
| REGIME_ATACADISTA_ADICIONAL_SAIDA_TRANSFERENCIA_20_ART_16D_I_VALOR | numeric(13) |  |  | Regime Atacadista - Adicional saída em transferência 20%, Art. 16-D, I - Valor |
| REGIME_ATACADISTA_CREDITO_AQUISICOES_FORNECEDOR_ATACADISTA_20_ART_16B_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Crédito aquisições de fornecedor atacadista(20%), Art. 16-B, §3º - Base de cálculo |
| REGIME_ATACADISTA_CREDITO_AQUISICOES_FORNECEDOR_ATACADISTA_20_ART_16B_VALOR | numeric(13) |  |  | Regime Atacadista - Crédito aquisições de fornecedor atacadista(20%), Art. 16-B, §3º - Valor |
| REGIME_ATACADISTA_SAIDAS_INTERNAS_ALIQUOTA_20_ART_16R_IIB_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Saídas internas à alíquota de até 20%, Art. 16-R, II, b - Base de cálculo |
| REGIME_ATACADISTA_SAIDAS_INTERNAS_ALIQUOTA_20_ART_16R_IIB_VALOR | numeric(13) |  |  | Regime Atacadista - Saídas internas à alíquota de até 20%, Art. 16-R, II, b - Valor |
| REGIME_ATACADISTA_SAIDAS_INTERNAS_ALIQUOTA_20_ART_16R_IB_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Saídas internas à alíquota de até 20%, Art. 16-R, I, b - Base de cálculo |
| REGIME_ATACADISTA_SAIDAS_INTERNAS_ALIQUOTA_20_ART_16R_IB_VALOR | numeric(13) |  |  | Regime Atacadista - Saídas internas à alíquota de até 20%, Art. 16-R, I, b - Valor |
| REGIME_ATACADISTA_SAIDAS_INTERNAS_ALIQUOTA_25_OU_27_ART_16R_IIC_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Saídas internas à alíquota de 25% ou 27%, Art. 16-R, II, c - Base de cálculo |
| REGIME_ATACADISTA_SAIDAS_INTERNAS_ALIQUOTA_25_OU_27_ART_16R_IIC_VALOR | numeric(13) |  |  | Regime Atacadista - Saídas internas à alíquota de 25% ou 27%, Art. 16-R, II, c - Valor |
| REGIME_ATACADISTA_SAIDAS_INTERNAS_ALIQUOTA_25_OU_27_ART_16R_IC_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Saídas internas à alíquota de 25% ou 27%, Art. 16-R, I, c - Base de cálculo |
| REGIME_ATACADISTA_SAIDAS_INTERNAS_ALIQUOTA_25_OU_27_ART_16R_IC_VALOR | numeric(13) |  |  | Regime Atacadista - Saídas internas à alíquota de 25% ou 27%, Art. 16-R, I, c - Valor |
| REGIME_ATACADISTA_SAIDAS_INTERNAS_ALIQUOTA_20_ADICIONAL_PF_ART_16R_IIA_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Adicional PF, Art. 16-R, § 1º, II, a - Base de cálculo |
| REGIME_ATACADISTA_SAIDAS_INTERNAS_ALIQUOTA_20_ADICIONAL_PF_ART_16R_IIA_VALOR | numeric(13) |  |  | Regime Atacadista - Adicional PF, Art. 16-R, § 1º, II, a - Valor |
| REGIME_ATACADISTA_SAIDAS_INTERNAS_ALIQUOTA_20_ADICIONAL_PF_ART_16R_IA_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Adicional PF, Art. 16-R, § 1º, I, a - Base de cálculo |
| REGIME_ATACADISTA_SAIDAS_INTERNAS_ALIQUOTA_20_ADICIONAL_PF_ART_16R_IA_VALOR | numeric(13) |  |  | Regime Atacadista - Adicional PF, Art. 16-R, § 1º, I, a - Valor |
| REGIME_ATACADISTA_SAIDAS_INTERNAS_ALIQUOTA_25_OU_27_ADICIONAL_PF_ART_16R_IIB_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Adicional PF, Art. 16-R, § 1º, II, b - Base de cálculo |
| REGIME_ATACADISTA_SAIDAS_INTERNAS_ALIQUOTA_25_OU_27_ADICIONAL_PF_ART_16R_IIB_VALOR | numeric(13) |  |  | Regime Atacadista - Adicional PF, Art. 16-R, § 1º, II, b - Valor |
| REGIME_ATACADISTA_SAIDAS_INTERNAS_ALIQUOTA_25_OU_27_ADICIONAL_PF_ART_16R_IB_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Adicional PF, Art. 16-R, § 1º, I, b - Base de cálculo |
| REGIME_ATACADISTA_SAIDAS_INTERNAS_ALIQUOTA_25_OU_27_ADICIONAL_PF_ART_16R_IB_VALOR | numeric(13) |  |  | Regime Atacadista - Adicional PF, Art. 16-R, § 1º, I, b - Valor |
| REGIME_ATACADISTA_SAIDAS_INTERNAS_ALIQUOTA_20_ART_16B_III_CESTA_BASICA_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Saídas internas à alíquota de até 20%, Art. 16-B, III, E - Cesta Básica - Base de cálculo |
| REGIME_ATACADISTA_SAIDAS_INTERNAS_ALIQUOTA_20_ART_16B_III_CESTA_BASICA_VALOR | numeric(13) |  |  | Regime Atacadista - Saídas internas à alíquota de até 20%, Art. 16-B, III, E - Cesta Básica - Valor |
| REGIME_ATACADISTA_CREDITO_AQUISICOES_FORNECEDOR_ATACADISTA_20_ART_16B_CESTA_BASICA_BASE_CALCULO | numeric(13) |  |  | Regime Atacadista - Crédito aquisições de fornecedor atacadista(20%), Art. 16-B, §3º - Produto Cesta Básica - Base de cálculo |
| REGIME_ATACADISTA_CREDITO_AQUISICOES_FORNECEDOR_ATACADISTA_20_ART_16B_CESTA_BASICA_VALOR | numeric(13) |  |  | Regime Atacadista - Crédito aquisições de fornecedor atacadista(20%), Art. 16-B, §3º - Produto Cesta Básica - Valor |
