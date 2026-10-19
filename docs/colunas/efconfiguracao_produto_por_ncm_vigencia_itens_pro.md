# EFCONFIGURACAO_PRODUTO_POR_NCM_VIGENCIA_ITENS_PRO — Configuração de Impostos para Produtos - Definição de Impostos
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da Empresa |
| I_CONFIGURACAO_NCM | integer(4) | PK |  | Código da Configuração de Produto por NCM |
| DATA_VIGENCIA | date(4) | PK |  | Vigência |
| I_SEQUENCIAL | integer(4) | PK |  | Sequencial |
| TIPO_CONTRIBUICAO | char(1) |  |  | Tipo de contribuição (N-Não cumulativo/C-Cumulativo/T-Subt. Tributária/S-Sem incidência) |
| PIS_INCIDENCIA_CUMULATIVA_ART_6 | char(1) |  |  | PIS com incidência cumulativa, conforme lei 12.693/12, Art. 6 (S/N) |
| COFINS_INCIDENCIA_CUMULATIVA_ART_10 | char(1) |  |  | COFINS com incidência cumulativa, conforme lei 10.833/03, Art. 10 (S/N) |
| CODIGO_CST_ENTRADA | integer(4) |  | S | CST - Entradas |
| VINCULO_CREDITO | integer(4) |  | S | Vínculo do crédito |
| BASE_CREDITO | integer(4) |  | S | Base do crédito |
| APROVEITAR_CREDITO_PROPORCIONAL | char(1) |  |  | Aproveitar crédito proporcional apenas referente a receita não cumulativa (S/N) |
| EXCLUIR_BASE_FRETE_SEGURO_OPER_IMPORTACAO | char(1) |  |  | Excluir da BC os valores frete, seguros e desp. acessórias na importação (S/N) |
| CREDITO_UNIDADE_MEDIDA | char(1) |  |  | Crédito por unidade de medida (S/N) - Entradas |
| UNIDADE_DIFERENTE_CREDITO | char(1) |  |  | Unidade tributada diferente da inventariada (S/N) - Entradas |
| UNIDADE_TRIBUTAVEL_CREDITO | char(6) |  | S | Unidade Tributável - Entradas |
| CODIGO_UNIDADE_CREDITO | integer(4) |  | S | Código da unidade Tributável - Entradas |
| FATOR_CONVERSAO_CREDITO | numeric(15) |  |  | Fator de conversao - Entradas |
| VALOR_PIS_CREDITO | numeric(13) |  |  | Valor de PIS - Entradas |
| VALOR_COFINS_CREDITO | numeric(13) |  |  | Valor de COFINS - Entradas |
| CREDITO_ALIQUOTA_DIFERENCIADA | char(1) |  |  | Crédito por alíquota diferenciada (S/N) - Entradas |
| ALIQUOTA_PIS_CREDITO | numeric(7) |  |  | Alíquota do PIS - Entradas |
| ALIQUOTA_COFINS_CREDITO | numeric(7) |  |  | Alíquota do COFINS - Entradas |
| CODIGO_CST_SAIDA | integer(4) |  | S | CST - Saídas |
| NATUREZA_RECEITA | integer(4) |  | S | Natureza da receita |
| CODIGO_RECOLHIMENTO_PIS | char(6) |  | S | Código de recolhimento PIS |
| CODIGO_RECOLHIMENTO_COFINS | char(6) |  | S | Código de recolhimento COFINS |
| DEBITO_UNIDADE_MEDIDA | char(1) |  |  | Débito por unidade de medida (S/N) - Saídas |
| UNIDADE_DIFERENTE_DEBITO | char(1) |  |  | Unidade tributada diferente da inventariada (S/N) - Saídas |
| UNIDADE_TRIBUTAVEL_DEBITO | char(6) |  | S | Unidade Tributável - Saídas |
| CODIGO_UNIDADE_DEBITO | integer(4) |  | S | Código da unidade Tributável - Saídas |
| FATOR_CONVERSAO_DEBITO | numeric(15) |  |  | Fator de conversao - Saídas |
| VALOR_PIS_DEBITO | numeric(13) |  |  | Valor de PIS - Saídas |
| VALOR_COFINS_DEBITO | numeric(13) |  |  | Valor de COFINS - Saídas |
| DEBITO_ALIQUOTA_DIFERENCIADA | char(1) |  |  | Débito por alíquota diferenciada (S/N) - Saídas |
| ALIQUOTA_PIS_DEBITO | numeric(7) |  |  | Alíquota do PIS - Saídas |
| ALIQUOTA_COFINS_DEBITO | numeric(7) |  |  | Alíquota do COFINS - Saídas |
| PRODUTO_COM_MARCA_COMERCIAL | char(1) |  |  | Produto com marca comercial - REFRI (Bebidas Frias)(S/N) |
| TABELA_SPED | integer(4) |  | S | Tabela SPED |
| MARCA_GRUPO_SPED | integer(4) |  | S | Marca grupo SPED |
| CST_ICMS_ENTRADA | integer(4) |  | S | CST ICMS - Entrada |
| CST_ICMS_SAIDA | integer(4) |  | S | CST ICMS - Saída |
| I_TABELA_ICMS | integer(4) |  | S | Sequencial da Tabela Alíquota do ICMS |
| ALIQUOTA_ICMS | numeric(5) |  |  | Alíquota do ICMS |
| CST_IPI_ENTRADA | integer(4) |  | S | CST IPI - Entrada |
| CST_IPI_SAIDA | integer(4) |  | S | CST IPI - Saída |
| PERIODICIDADE_IPI | char(1) |  |  | Periodicidade do IPI (M/Q/D/T/S/E/N/R/V) |
| ALIQUOTA_IPI | numeric(5) |  |  | Alíquota do IPI |
| CALCULA_IPI_UNIDADE_MEDIDA | char(1) |  |  | Calcula IPI por Unidade de Medida (S/N) |
| UNIDADE_TRIBUTADA_DIFERENTE_INVENTARIADA_IPI | char(1) |  |  | Unidade Tributada Diferente da Inventariada do IPI (S/N) |
| UNIDADE_TRIBUTAVEL_IPI | char(6) |  | S | Unidade Tributável - Saídas |
| CODIGO_UNIDADE_TRIBUTAVEL_IPI | integer(4) |  | S | Código da Unidade Tributável - Saídas |
| FATOR_CONVERSAO_IPI | numeric(15) |  |  | Fator de Conversão - Saídas |
| CLASSE_ENQUADRAMENTO_IPI | integer(4) |  | S | Classe do Enquadramento do IPI |
| VALOR_POR_UNIDADE_IPI | numeric(13) |  |  | Valor por Unidade do IPI |
| PRODUTO_SUJEITO_TRIBUTACAO_MONOFASICA_PISCOFINS | char(1) |  |  | Produto sujeito a tributação de PIS e COFINS  (S/N) |
| PRODUTO_SUJEITO_TRIBUTACAO_MONOFASICA_PISCOFINS_TIPO | integer(4) |  |  | Produto sujeito a tributação de PIS e COFINS - Tipo (1/2) |
| PRODUTO_POSSUI_PERC_RED_BC_PIS_COFINS_SAIDA | char(1) |  |  | Produto possui percentual de redução na base de cálculo (S/N) |
| PERCENTUAL_REDUCAO_BASE_CALCULO_PIS_COFINS_SAIDA | numeric(5) |  |  | Percentual do produto possui percentual de redução na base de cálculo |
| I_RECOLHIMENTO_IPI | integer(4) |  | S | Código de recolhimento de IPI |
| CODIGO_CST_NATUREZA_RECEITA | integer(4) |  | S | Código da CST para relacionamento da natureza da receita |
| DADOS_PISCOFINS_OK | char(1) |  |  | Dados referentes ao PIS e COFINS OK (S/N) |
| BEBIDAS_FRIAS_ALIQ_VAREJISTA_CONSUMIDOR_FINAL | char(1) |  |  | Bebidas frias - Alíquota para varejista ou consumidor final |
| ALIQUOTA_PIS_BEBIDAS_FRIAS | numeric(7) |  |  | Alíquota PIS - Bebidas frias |
| ALIQUOTA_COFINS_BEBIDAS_FRIAS | numeric(7) |  |  | Alíquota COFINS - Bebidas frias |
| GO_PRODUTO_SUJEITO_FUNDEPEC | char(1) |  |  | GO - Produto Sujeito a FUNDEPEC (S/N) |
| I_FUNDEPEC | integer(4) |  | S | GO - Produto Sujeito a FUNDEPEC - Tipo do Produto |
| MS_GERAR_CREDITO_PRESUMIDO | char(1) |  |  | MS - Produto sujeito ao crédito presumido (S/N) |
| MS_TIPO_CREDITO_PRESUMIDO | integer(4) |  |  | MS - Produto sujeito ao crédito presumido - Tipo |
| PB_GERAR_CREDITO_PRESUMIDO | char(1) |  |  | PB - Produto sujeito ao crédito presumido (S/N) |
| PB_GERAR_CREDITO_PRESUMIDO_TIPO | integer(4) |  |  | PB - Produto sujeito ao crédito presumido - Tipo |
| GO_PRODUTO_EXCLUIDO_BENEFICIO_COMEXPRODUZIR | char(1) |  |  | GO - Produto excluído do benefício do COMEXPRODUZIR (S/N) |
| I_PRODEPE_APURACAO | integer(4) |  | S | PE - Calcular PRODEPE - Código da apuração |
| PE_CALCULAR_PRODEPE | char(1) |  |  | PE - Calcular PRODEPE (S/N) |
| PE_PRODUTO_SUJEITO_AO_CREDITO_PRESUMIDO | char(1) |  |  | PE - Produto sujeito ao crédito presumido (S/N) |
| PE_PRODUTO_SUJEITO_AO_CREDITO_PRESUMIDO_TIPO | integer(4) |  |  | PE - Produto sujeito ao crédito presumido - Tipo |
| PR_CALCULAR_ESTORNO_CREDITO_ICMS_ART_71 | char(1) |  |  | PR - Calcular o estorno de crédito conforme Art. 71 RICMS (S/N) |
| RJ_CALC_ESTORNO_CREDITO_ICMS_PROP_ISENTA_NAO_TRIB | char(1) |  |  | RJ - Calcular o estorno de crédito proporcional as saídas isentas/não tributadas |
| BASE_CALCULO_ST | char(1) |  |  | Base Cálculo ST (M/P) |
| PERCENTUAL_REDUCAO_BC_ST | numeric(7) |  |  | Percentual da Redução BC ST |
| PERCENTUAL_MARGEM_DE_VALOR_ADIC_ST | numeric(5) |  |  | Percentual margem do valor adic. ST |
| VALOR_UNITARIO_ST | numeric(13) |  |  | Valor unitário |
| PRODUTO_INCLUIDO_ST | char(1) |  |  | Produto incluído ST (S/N) |
| DATA_INICIO_ST | date(4) |  | S | Data início ST |
| DATA_LEVANTAMENTO_ST | date(4) |  | S | Data levantamento ST |
| GRUPO_ST | integer(4) |  | S | Grupo ST |
| CODIGO_TIPO_MERCADORIA_ST | integer(4) |  | S | Código tipo mercadoria ST |
| RS_CREDITO_ARROZ_PDI | char(1) |  |  | RS - Gera crédito presumido nas saídas interestaduais de arroz beneficiado |
| RS_CREDITO_ARROZ_PDI_TIPO | integer(4) |  | S | RS - Tipo do produto (1 - Arroz em casca / 2 - Arroz beneficiado) |
| RS_CREDITO_ARROZ_PDI_UNIDADE | char(1) |  |  | RS - Unidade inventariada diferente da unidade de cálculo (kg) |
| RS_CREDITO_ARROZ_PDI_UNIDADE_CALCULO | integer(4) |  | S | RS - Unidade de cálculo |
| RS_CREDITO_ARROZ_PDI_FATOR_CONVERSAO | numeric(13) |  |  | RS - Fator de conversão |
| RS_GERAR_CREDITO_PRESUMIDO | char(1) |  |  | RS - Gerar Crédito Presumido (S/N) |
| RS_TIPO_CREDITO_PRESUMIDO | integer(4) |  | S | RS - Tipo de Crédito Presumido |
| RS_TIPO_CREDITO_PRESUMIDO_PRODUTO | integer(4) |  | S | RS - Tipo do Produto do Crédito Presumido |
| CREDITO_PRESUMIDO_ALCOOL_12859 | char(1) |  |  | Produto sujeito ao crédito presumido importador ou produtor de álcool - Lei 12.859/2013 |
| CREDITO_PRESUMIDO_ALCOOL_12859_UNIDADE_DIFERENTE | char(1) |  |  | Unidade inventariada diferente de metros cúbicos |
| CREDITO_PRESUMIDO_ALCOOL_12859_UNIDADE_TRIBUTAVEL | char(6) |  | S | Unidade tributável (metros cúbicos) |
| CREDITO_PRESUMIDO_ALCOOL_12859_CODIGO_UNIDADE | integer(4) |  | S | Código da Unidade tributável (metros cúbicos) |
| CREDITO_PRESUMIDO_ALCOOL_12859_FATOR_CONVERSAO | numeric(15) |  |  | Fator de conversão |
| RJ_CALCULAR_FECP_ICMS_NORMAL | char(1) |  |  | Calcular FECP-ICMS Normal |
| RJ_GERAR_CREDITO_PRESUMIDO | char(1) |  |  | RJ - Gerar Crédito Presumido |
| RJ_TIPO_CREDITO_PRESUMIDO | integer(4) |  | S | RJ - Tipo de Crédito Presumido |
| RJ_PRODUTO_INDUSTRIAL_FLUMINENSE_PDI | char(1) |  |  | RJ - Produto é industrializado no estabelecimento Fluminense - Art. 2º Decreto 42.649/2010 |
| CALCULAR_PISCOFINS_BEBIDAS_FRIAS_DECRETO_8442_2015 | char(1) |  |  | Calcular PIS e COFINS de bebidas frias conforme art. 30, Decreto 8.442/2015 (S/N) |
| CODIGO_RECOLHIMENTO_STAT | char(6) |  | S | Código do Recolhimento - Substituição Tributária |
| I_RECOLHIMENTO_STAT | integer(4) |  | S | Código Sequencial do Recolhimento - Substituição Tributária |
| INFORMAR_SITUACAO_TRIBUTARIA_ECF | char(1) |  |  | Informar a situação tributária guia estoque (ECF) |
| INFORMAR_SITUACAO_TRIBUTARIA_ECF_ALIQUOTA | numeric(5) |  |  | Aliquota ICMS ou ISS |
| INFORMAR_SITUACAO_TRIBUTARIA_ECF_OPERACAO | integer(4) |  |  | Situação tributária ECF (1/2/3/4/5/6/7/8/9/10/11/12/13) |
| CODIGO_RECOLHIMENTO_COFINS_ENTRADA | char(6) |  |  | Código do Recolhimento do COFINS |
| CODIGO_RECOLHIMENTO_PIS_ENTRADA | char(6) |  |  | Código do Recolhimento do PIS |
| I_RECOLHIMENTO_COFINS_ENTRADA | integer(4) |  | S | Código Sequencial do Recolhimento do COFINS |
| I_RECOLHIMENTO_PIS_ENTRADA | integer(4) |  | S | Código Sequencial do Recolhimento do PIS |
| AM_CREDITO_ESTIMULO_ICMS_ART_13_LEI_2826_03 | char(1) |  |  | AM - Calcular incentivo fiscal do Crédito Estímulo do ICMS |
| I_SUB_APURACAO | integer(4) |  | S | AM - Nível do incentivo |
| SP_PRODUTO_SUJEITO_FECOEP | char(1) |  |  | SP - Produto sujeito ao Fundo Estadual de Combate e Erradicação da Pobreza - FECOEP-SP (S/N) |
| TO_PRODUTO_SUJEITO_FECOEP | char(1) |  |  | TO - Produto sujeito ao Fundo Estadual de Combate e Erradicação da Pobreza - FECOEP-TO (S/N) |
| TO_TIPO_COMBUSTIVEL_GIAM_CODIGO | integer(4) |  | S | TO - Tipo de combustível no informativo GIAM - Código |
| PR_PRODUTO_SUJEITO_FECOP | char(1) |  |  | PR - Produto sujeito ao Fundo Estadual de Combate à Pobreza do Paraná - FECOP-PR (S/N) |
| MG_CREDITO_PRESUMIDO_RET | char(1) |  |  | MG - Calcular crédito presumido RET |
| MG_CREDITO_PRESUMIDO_RET_TIPO | char(1) |  |  | MG - Calcular crédito presumido RET - Tipo (I-Inferior/S-Superior/P-Importados/D-Demais) |
| I_SUB_APURACAO_MG | integer(4) |  | S | MG - Sub-apuração |
| MG_GERAR_CREDITO_PRESUMIDO | char(1) |  |  | MG - Gerar Crédito Presumido (S/N) |
| MG_TIPO_CREDITO_PRESUMIDO | integer(4) |  | S | MG - Tipo de Crédito Presumido |
| MG_TIPO_PRODUTO | integer(4) |  | S | MG - Tipo do Produto |
| MG_CALCULAR_FEM_ADICIONAL_ALIQ_IMP_ICMS | char(1) |  |  | MG - FEM - Calcular o adicional na alíquota do imposto ICMS (S/N) |
| ES_PRODUTO_BENEFICIADO_SAIDAS_INTERESTADUAIS | char(1) |  |  | Produto fora do benef. fiscal estab. Comercial Atacadista nas saídas interestaduais - Art. 530-LRK RICMS |
| ES_PRODUTO_BENEFICIADO_SAIDAS_INTERNAS | char(1) |  |  | Produto fora do benef. fiscal estab. Comercial Atacadista nas saídas internas - Art. 534-ZZA RICMS |
| RO_PRODUTO_SUJEITO_AO_CREDITO_PRESUMIDO | char(1) |  |  | RO - Produto sujeito ao crédito presumido |
| RO_PRODUTO_POSSUI_INCENTIVO_CONSIT | char(1) |  |  | RO - Produto possui incentivo tributário CONSIT - Decreto n 12.988/2007, art. 2, I |
| RO_PRODUTO_SUJEITO_AO_CREDITO_PRESUMIDO_TIPO | integer(4) |  | S | RO - Produto sujeito ao crédito presumido - Tipo |
| CE_ALIQUOTA_STAT_31270_2013 | numeric(5) |  |  | CE - Alíquota ST Dec. 31.270/2013 |
| MS_PRODUTO_SUJEITO_FECOMP_MS | char(1) |  |  | MS - Produto sujeito ao Fundo Estadual de Combate e Erradicação da Pobreza - FECOMP-MS |
| RS_PRODUTO_SUJEITO_AMPARA | char(1) |  |  | RS - Produto sujeito ao Fundo de Proteção e Amparo |
| RS_PARTICIPA_BASE_CALCULO_FUNDESA | char(1) |  |  | Produto faz parte da base de cálculo do FUNDESA |
| RS_PARTICIPA_BASE_CALCULO_FUNDESA_INCIDENCIA | integer(4) |  |  | Produto faz parte da base de cálculo do FUNDESA - Incidência |
| RS_PARTICIPA_BASE_CALCULO_FUNDESA_TABELA | integer(4) |  | S | Produto faz parte da base de cálculo do FUNDESA - Tipo do Produto |
| RS_PRODUTO_AGROTOXICO_FITOSSANITARIO | char(1) |  |  | RS - Produto agrotóxico fitossanitário |
| RS_PRODUTO_AGROTOXICO_NOME_INGREDIENTE_ATIVO | char(35) |  |  | RS - Nome ingrediente ativo do produto agrotóxico fitossanitário |
| RS_PRODUTO_AGROTOXICO_FORMULACAO | char(120) |  |  | RS - Formulação do produto agrotóxico fitossanitário |
| RS_PRODUTO_AGROTOXICO_CLASSE | char(65) |  |  | RS - Classe do produto agrotóxico fitossanitário |
| RS_PRODUTO_AGROTOXICO_CONCENTRACAO | char(10) |  |  | RS - Concentração do produto agrotóxico fitossanitário |
| DETALHAR_ANEXO_VA | char(1) |  |  | Detalhamento Anexo VA |
| DETALHAR_ANEXO_VB | char(1) |  |  | Detalhamento Anexo VB |
| ANEXO_VA_PADRAO | integer(4) |  | S | Detalhamento Anexo VA Padrão |
| ANEXO_VB_PADRAO | integer(4) |  | S | Detalhamento Anexo VB Padrão |
| MT_PRODUTO_DESTINADO_CONSTRUCAO_CIVIL | char(1) |  |  | MT - Produto destinado a construção civil - constante em lista publicada pelo CEDEM |
| MT_PRODUTO_DESTINADO_CONSTRUCAO_CIVIL_MARGEM_LUCRO | numeric(5) |  |  | MT - Margem de Lucro |
| MT_PRODUTO_DESTINADO_CONSTRUCAO_CIVIL_ALIQUOTA | numeric(5) |  |  | MT - Aliquota |
| I_RECOLHIMENTO_ICMSA | integer(4) |  | S | MT - Sequencial Recolhimento ICMSA |
| CODIGO_RECOLHIMENTO_ICMSA | char(6) |  | S | MT - Código Recolhimento ICMSA |
| MT_PRODUTO_FETHAB | char(1) |  |  | MT - Produto faz parte da base de cálculo no FETHAB |
| MT_CODIGO_RECOLHIMENTO_FETHAB | char(6) |  | S | MT - Código Recolhimento FETHAB |
| MT_RESPONSAVEL_RECOLHIMENTO | integer(4) |  | S | MT - Responsavel pelo Recolhimento |
| RO_PRODUTO_SUJEITO_FECOEP | char(1) |  |  | RO - Produto sujeito ao Fundo Estadual de Combate e Erradicação da Pobreza de Rondônia - FECOEP-RO |
| BA_GERAR_CREDITO_PRESUMIDO | char(1) |  |  | BA - Produto sujeito ao crédito presumido |
| BA_GERAR_CREDITO_PRESUMIDO_TIPO | integer(4) |  | S | BA - Produto sujeito ao crédito presumido - Itens |
| I_RECOLHIMENTO_RECALI | integer(4) |  | S | MG - Sequencial Recolhimento RECALI |
| CODIGO_RECOLHIMENTO_RECALI | char(6) |  | S | MG - Código Recolhimento RECALI |
| DF_PRODUTO_SUJEITO_DIFERENCIAL_ALIQUOTA_OP_INTERESTADUAL | char(1) |  |  | DF - Produto sujeito ao recolhimento da diferença de alíquotas nas aquisições interestaduais - Lei nº 5.558/2015, Art. 20-A |
| SP_PRODUTO_CREDITO_OUTORGADO_EMPRESAS_TEXTEIS | char(1) |  |  | SP - Produto sujeito ao crédito outorgado de 12% para empresas têxteis - Cap. IV, Anexo III, Art. 41 do RICMS |
| GO_PRODUTO_SUJEITO_DIFERENCIAL_ALIQUOTA | char(1) |  |  | GO - Produto sujeito ao Diferencial de alíquota conf. Art. 3º, I do Decreto nº 9.162/2018 |
| PR_PRODUTO_SAIDA_DIFERENTE_ENTRADA | char(1) |  |  | PR - Produto na saída diferente do produto na entrada |
| CODIGO_PRODUTO_ENTRADA | varchar(14) |  | S | PR - Código do produto na entrada |
| MG_PRODUTO_SUJEITO_ANTECIPACAO_AQUISICAO_INTERESTADUAL | char(1) |  |  | MG - Produto sujeito a antecipação nas aquisições interestaduais |
| ES_PRODUTO_INCLUIDO_MOVIMENTACAO_CAFE_CRU | char(1) |  |  | ES - Produto incluído na movimentação de Café Cru |
| ES_PRODUTO_INCLUIDO_MOVIMENTACAO_CAFE_CRU_LIGA | integer(4) |  | S | ES - Produto incluído na movimentação de Café Cru - Liga (1 - Café Arábica, 2 - Café Conilon) |
| ES_PRODUTO_INCLUIDO_MOVIMENTACAO_CAFE_CRU_ESPECIE | char(3) |  | S | ES - Produto incluído na movimentação de Café Cru - Espécie |
| MA_GERAR_CREDITO_PRESUMIDO | char(1) |  |  | MA - Produto incluído no crédito presumido |
| MA_GERAR_CREDITO_PRESUMIDO_TIPO | integer(4) |  | S | MA - Produto incluído no crédito presumido - Tipo |
| AC_PRODUTO_COM_RESSARCIMENTO_DECRETO_6875_2017 | char(1) |  |  | AC - Produto com ressarcimento conforme seção IV do decreto 6.875/2017 |
| PR_PRODUTO_COM_RESSARCIMENTO_NORMA_FISCAL | char(1) |  |  | Produto com ressarcimento conforme Norma de Procedimento Fiscal 027/2017 |
| ES_CREDITO_PRESUMIDO_VENDA_INTERESTADUAL_NAO_PRESENCIAL_CONSUMIDOR_FINAL_ART_530 | char(1) |  |  | Produto fora do Crédito presumido na venda interestadual não presencial a consumidor final - Art. 530-LRI RICMS |
| RS_PRODUTO_INCLUIDO_CALCULAR_RESSARC_COMP_ICMS_ST | char(1) |  |  | RS - Produto incluído no cálculo do ressarcimento/complemento do ICMS ST conf. Art. 25-A a 25-C, Livro III do RICMS |
| MT_PRODUTO_SUJEITO_FECEP | char(1) |  |  | Produto sujeito ao Fundo Estadual de Combate e Erradicação da Pobreza - FECEP-MT |
| MG_CREDITO_PRESUMIDO_RET_SUB_GRUPO | integer(4) |  |  | SUB-GRUPO (1-IMPORTADOS/2-DEMAIS/3-ELETRÔNICOS/4-FIOS/5-CAFÉ/6-SUCOS/7-CHÁ/8-TOMATE/9-FRUTAS/10-EXTRATOS/11-CEREAIS/12-MEDICAMENTOS) |
| SC_PRODUTO_SUJEITO_FCP_ST | char(1) |  |  | SC - Produto sujeito ao Fundo de Combate à Pobreza nas operações interestaduais - FCP-ST |
| SOMAR_IPI_BASE_CALCULO_PIS_COFINS | char(1) |  |  | Somar o valor de IPI na base de cálculo do PIS e da COFINS |
| MT_PRODUTO_INCLUIDO_CALCULO_FEEF | char(1) |  |  | Produto incluído no cálculo do Fundo Estadual de Combate a Pobreza - FEEF |
| RS_PRODUTO_INCLUIDO_CALCULAR_RESSARC_COMP_ICMS_ST_PERCENTUAL | numeric(5) |  |  | RS - Percentual de base de cálculo, Produto incluído no cálculo do ressarcimento/complemento do ICMS ST conf. Art. 25-A a 25-C, Livro III do RICMS |
| SC_PRODUTO_INCLUIDO_CALCULAR_REST_COMP_RESSARC_ICMS_ST | char(1) |  |  | Produto incluído no cálculo da restituição, complemento e ressarcimento do ICMS ST (DRCST) |
| SC_PRODUTO_INCLUIDO_CALCULAR_REST_COMP_RESSARC_ICMS_ST_PERCENTUAL | numeric(5) |  |  | Percentual base de cálculo ICMS Próprio nas entradas |
| SC_ALIQUOTA_EFETIVA_DRCST | numeric(5) |  |  | SC - Alíquota Efetiva DRCST |
| RS_PRODUTO_INCLUIDO_CALCULAR_RESSARC_COMP_ICMS_ST_CALC_COMBUSTIVEL | char(1) |  |  | Calcular o montante do imposto presumido com base na tabela de PMPF de Combustíveis |
| BEBIDAS_FRIAS_ALIQ_SIMPLES_NACIONAL | char(1) |  |  | Bebidas frias - AlÃ­quota para Simples Nacional |
| ALIQUOTA_PIS_BEBIDAS_FRIAS_SIMPLES_NACIONAL | numeric(7) |  |  | Bebidas frias - AlÃ­quota de PIS |
| ALIQUOTA_COFINS_BEBIDAS_FRIAS_SIMPLES_NACIONAL | numeric(7) |  |  | Bebidas frias - AlÃ­quota de COFINS |
| MS_PRODUTO_SUJEITO_FUNDERSUL | char(1) |  |  | MS - Produto sujeito ao FUNDERSUL |
| I_FUNDERSUL | integer(4) |  | S | MS - Produto sujeito ao FUNDERSUL - Tipo do Produto |
| MS_PRODUTO_SUJEITO_FUNDEMS | char(1) |  |  | MS - Produto sujeito ao FUNDEMS |
| I_FUNDEMS | integer(4) |  | S | MS - Produto sujeito ao FUNDEMS - Tipo do Produto |
| PI_PRODUTO_SUJEITO_FECOP | char(1) |  |  | PI - Produto sejeito FECOP |
| MG_PRODUTO_INCLUIDO_CALC_COMPL_REST_ICMS_ST_CONF_ART31 | char(1) |  |  | MG - Produto incluído no cálculo do complemento/restituição do ICMS ST conforme Art. 31-A a 31-I, Anexo XV do RICMS |
| MG_PRODUTO_INCLUIDO_CALC_COMPL_REST_ICMS_ST_CONF_ART31_PERC | numeric(5) |  |  | MG - Produto incluído no cálculo do complemento/restituição do ICMS ST conforme Art. 31-A a 31-I, Anexo XV do RICMS - Percentual de base de cálculo |
| PR_CREDITO_PRESUMIDO_ENTRADA_LEITE_CRU_PDI | char(1) |  |  | PR - Calcular Crédito Presumido nas entradas de leite cru, proporcional às saídas tributadas - Anexo VII, Item 30 do RICMS |
| PR_CREDITO_PRESUMIDO_ENTRADA_LEITE_CRU_TIPO_PDI | integer(4) |  |  | PR - Calcular Crédito Presumido nas entradas de leite cru, proporcional às saídas tributadas - Anexo VII, Item 30 do RICMS - Tipo |
| CALCULAR_FCP | char(1) |  |  | Calcular Fundo Estadual de Combate à Pobreza - FCP |
| SC_GERAR_CREDITO_PRESUMIDO | char(1) |  |  | SC - Gerar Crédito Presumido |
| SC_TIPO_CREDITO_PRESUMIDO | integer(4) |  | S | SC - Tipo de Crédito Presumido |
| SC_TIPO_PRODUTO | integer(4) |  | S | SC - Tipo do Produto |
| SC_CALCULAR_CREDITO_PRESUMIDO_SAIDA_INTERESTADUAL | char(1) |  |  | SC - Calcular o crédito presumido somente nas saídas interestaduais (S/N) |
| SC_CALCULAR_CREDITO_PRESUMIDO_ART_15_XXVIII_SAIDA_INTERESTADUAL | char(1) |  |  | Calcular o crédito presumido Art. 15, XXVIII nas saídas interestaduais |
| SC_CALCULAR_CREDITO_PRESUMIDO_ART_21_IX_SOBRE_PRECO_FOB | char(1) |  |  | SC - Calcular o crédito presumido Art. 21, IX, sobre o preço FOB |
| SC_CALCULAR_CREDITO_PRESUMIDO_ART_21_IX_SOBRE_PRECO_FOB_TIPO | char(1) |  |  | SC - Calcular o crédito presumido Art. 21, IX, sobre o preço FOB - Tipo |
| SC_CALCULAR_CREDITO_PRESUMIDO_ART_21_IX_SOBRE_PRECO_FOB_PERCENTUAL | numeric(5) |  |  | SC - Calcular o crédito presumido Art. 21, IX, sobre o preço FOB - Percentual |
| SC_CALCULAR_CREDITO_PRESUMIDO_ART_21_IX_SOBRE_PRECO_FOB_PRECO | numeric(13) |  |  | SC - Calcular o crédito presumido Art. 21, IX, sobre o preço FOB - Preço FOB |
| SC_CALCULAR_CREDITO_PRESUMIDO_SOBRE | char(1) |  |  | Calcular o Crédito Presumido sobre |
| SC_CREDITO_PRESUMIDO_ENTRADA_LEITE_PDI | char(1) |  |  | SC - Calcular Crédito Presumido na entrada de leite in natura (S/N) |
| SC_CREDITO_PRESUMIDO_ENTRADA_LEITE_TIPO_PDI | integer(4) |  |  | SC - Calcular Crédito Presumido na entrada de leite in natura - Tipo do Produto (1/2/3) |
| SC_CREDITO_PRESUMIDO_ENTRADA_LEITE_QUEIJO_PRATO_MOZARELA | char(1) |  |  | Considerar as saídas para fora do estado do queijo prato e mozarela no cálculo da proporção das saídas tributadas |
| SC_PRODUTO_AUTORIZADO_MANUTENCAO_CREDITO | char(1) |  | S | Produto não autorizado a manutenção de créditos acumulados |
| SP_PRODUTO_SUJEITO_INSUMO_OPER_FORNECI_ALIMENTACAO | char(1) |  |  | SP - Produto utilizado como insumo nas operações com fornecimento de alimentação - Art. 1º, § 4º do Dec. 51.597/07 |
| BA_CALCULAR_ESTORNO_CREDITO_ICMS_ART_312 | char(1) |  | S | Calcular estorno de crédito nas saídas isentas ou não tributadas - Art. 312, I do RICMS |
| PI_PRODUTO_SUJEITO_ANTECIPACAO_AQUISICAO_INTERESTADUAL | char(1) |  |  | PI - Produto sujeito a antecipação nas aquisições interestaduais |
| PR_PROD_INC_CALC_RECUP_RESSARC_COMPTO_ICMS_ST | char(1) |  |  | PR - Produto incluído no cálculo da recuperação, ressarcimento e complementação do ICMS-ST (ADRC-ST) |
| PR_PROD_INC_CALC_REST_COMP_RESSARC_ICMS_ST_PERCENTUAL | numeric(5) |  |  | PR - Percentual base de cálculo ICMS Próprio |
| PR_PROD_INC_CALC_REST_COMP_RESSARC_ICMS_ST_ALIQUOTA_EFETIVA | numeric(5) |  |  | PR - Alíquota efetiva |
| RO_PRODUTO_COM_RESSARCIMENTO_ART_20_ANEXO_VI | char(1) |  |  | RO - Produto com direito ao ressarcimento conforme o Art. 20 do Anexo VI do RICMS |
| PA_PRODUTO_SUJEITO_ANTECIPACAO_AQUISICAO_INTERESTADUAL | char(1) |  |  | PA - Produto sujeito a antecipação nas aquisições interestaduais |
| ES_PRODUTO_SUJEITO_COMPLEMENTO_ICMS_AQUISICAO_ESTAB_ATACADISTA | char(1) |  |  | ES - Produto sujeito ao complemento de ICMS na aquisição de estab. atacadista - Art. 534-Z-Z-A, § 4º RICMS |
| RN_CALCULAR_REGIME_ESPECIAL_TRIB_CONTRIB_ATACADISTAS | char(1) |  |  | Calcular o regime especial de tributação aos contribuintes atacadistas - Decreto 22.199/11 |
| RN_CALCULAR_REGIME_ESPECIAL_TRIB_CONTRIB_ATACADISTAS_TIPO | char(1) |  |  | Calcular o regime especial de tributação aos contribuintes atacadistas - Decreto 22.199/11 - Tipo |
| PB_PRODUTO_SUJEITO_FEEF | char(1) |  |  | Produto sujeito ao Fundo Estadual de Equilíbrio Fiscal - FEEF |
| DF_PRODUTO_SUJEITO_DIFERENCIAL_ALIQUOTA_OP_INTERESTADUAL_TIPO | integer(4) |  |  | DF - Produto sujeito diferencial aliquota oper interestadual |
| SC_CALCULAR_CREDITO_PRESUMIDO_ENTRADA_LEITE_SOBRE | char(1) |  |  | SC - Calcular o Crédito Presumido sobre |
| SC_CONSIDERAR_SAIDAS_INTERNAS_QUEIJO_PRATO_E_MOZARELA | char(1) |  |  | SC - Considerar as saídas internas do queijo prato e mozarela no cálculo da proporção das saídas tributadas |
| AC_CONSIDERAR_ICMS_DESONERADO_COMO_CREDITO_PRESUMIDO | char(1) |  |  | AC - Considerar o ICMS Desonerado do produto como crédito presumido do Art.45 RICMS |
| MS_PRODUTO_SUJEITO_ICMS_EQ | char(1) |  |  | MS - Produto sujeito ao ICMS Equalização Simples Nacional - Decreto 15.055/2018 |
| BASE_CALCULO_DIFERENCA_ALIQUOTA | char(1) |  |  | Base de cálculo diferença alíquota |
| PERCENTUAL_MARGEM_DE_VALOR_ADIC_DIFERENCA_ALIQUOTA | numeric(5) |  |  | % Margem de valor adic. dif. alíq |
| VALOR_UNITARIO_DIFERENCA_ALIQUOTA | numeric(13) |  |  | Valor unitário diferença alíquota |
| RJ_CALC_ESTORNO_CREDITO_ICMS_PROP_POSSUIR_RED_BC | char(1) |  |  | RJ - Calcular o estorno de crédito proporcional as saídas com redução da base de cálculo (Cesta básica) |
| ES_PRODUTO_SUJEITO_FUNCOP | char(1) |  |  | ES - Produto sujeito ao Fundo Estadual de Combate à Pobreza - FUNCOP-ES |
| RS_PRODUTO_INCLUIDO_CALCULO_REST_ICMS_ST_PAGO_ETAPAS_ANT | char(1) |  |  | RS - Produto incluído no cálculo da restituição do ICMS ST pago nas etapas anteriores |
| PR_PRODUTO_COM_REDUCAO_BASE_CALC_DIFALI | char(1) |  |  | PR - Produto com redução na base de cálculo do DIFALI |
| PR_PRODUTO_COM_REDUCAO_BASE_CALC_DIFALI_PERCENTUAL | numeric(5) |  |  | PR - Produto com redução na base de cálculo do DIFALI - Percentual |
| BA_PRODUTO_SUJEITO_ANTECIPACAO_AQUISICAO_INTERESTADUAIS | char(1) |  |  | BA - Produto sujeito à antecipação nas aquisições interestaduais de mercadorias para comercialização |
| RJ_PRODUTO_SUJEITO_FECP | char(1) |  |  | RJ - Produto sujeito ao FECP-Diferencial de Alíquota |
| PRODUTO_GERA_SUBTRI_CREDITO_ICMS | char(1) |  |  | Gera crédito de Substituição Tributária na apuração do imposto ICMS |
| RN_PRODUTO_SUJEITO_FECOP | char(1) |  |  | Produto sujeito ao Fundo Estadual de Combate a Pobreza - FECOP |
| PRODUTO_GERA_SUBTRI_CREDITO_ICMS_PERCENTUAL_BC | numeric(5) |  |  | Gera crédito de Substituição Tributária na apuração do imposto ICMS - Percentual da Base de cálculo |
| RS_PRODUTO_INCLUIDO_DIFERIMENTO_DECRETO_55_797_2021 | char(1) |  |  | Produto incluído no diferimento de ICMS conforme Decreto 55.797/2021 |
| AP_PRODUTO_SUJEITO_ANTECIPACAO_AQUISICAO_INTERESTADUAIS | char(1) |  |  | AP - Produto sujeito à antecipação nas aquisições interestaduais de mercadorias para comercialização |
| SC_PRODUTO_SUJEITO_CREDITO_AQUISICAO_USO_CONSUMO_ART_29 | char(1) |  |  | SC - Produto sujeito ao crédito de ICMS, ICMS-ST e DIFALI nas aquisições para uso e consumo - Art. 29, § 8º do RICMS |
| PRODUTO_RECEBIDO_BONIF_VINCULADO_OP_VENDA | char(1) |  |  | Produto recebido em bonificação vinculado a operação de venda |
| PRODUTO_SUJEITO_AO_COMPLEMENTO_CALCULO_ALIQUOTA_PORTARIA_CAT_42_18 | char(1) |  |  | Produto sujeito ao complemento de alíquota para cálculo da Portaria CAT nº 42/18 |
| ALIQUOTA_COMPLEMENTO_CALCULO_PORTARIA_CAT_42_18 | numeric(5) |  |  | Alíquota  de complemento para cálculo da Portaria CAT nº 42/18 |
| MG_PRODUTO_CALCULO_RESTITUICAO_ICMS_ST_ART_23 | char(1) |  |  | MG - Produto incluído no cálculo da restituição do ICMS ST conforme Art. 23, Anexo XV do RICMS |
| AL_PRODUTO_SUJEITO_FECOEP | char(1) |  |  | AL - Produto sujeito ao Fundo Estadual de Combate a Pobreza - FECOEP |
| DF_CALCULAR_REGIME_FRIGORIFICOS_ART_320D | char(1) |  |  | DF - Calcular o regime especial de Frigoríficos/Abatedouros - Art. 320-D do RICMS |
| DF_CALCULAR_REGIME_FRIGORIFICOS_ART_320D_TIPO | integer(4) |  |  | DF - Calcular o regime especial de Frigoríficos/Abatedouros - Art. 320-D do RICMS Tipo |
| DF_PRODUTO_SISTEMA_APURACAO_REG_ESP_5005_2021 | char(1) |  |  | DF - Produto incluído na sistemática de apuração do Regime especial Lei nº 5.005/2012 |
| DF_PRODUTO_SISTEMA_APURACAO_REG_ESP_5005_2021_TIPO | integer(4) |  |  | DF - Produto incluído na sistemática de apuração do Regime especial Lei nº 5.005/2012 Tipo(1 - Bebidas alcoólicas/ 2 - Demais produtos) |
| SC_CONSIDERAR_ENTRADAS_CREDITO_TOTAL_SAIDAS_PROPORCAO | char(1) |  |  | SC - Considerar nas entradas para o crédito e no total de saídas para proporção |
| RS_SUJEITO_PAGAMENTO_ICMS_ENTRADA_DIFERIMENTO_ART_37_1_F | char(1) |  |  | RS - Produto sujeito ao pagamento do ICMS na entrada quando decorrente do diferimento-Art.37 §1º,f do RICMS |
| RS_SUJEITO_PAGAMENTO_ICMS_ENTRADA_DIFERIMENTO_ART_37_1_F_PERCENTUAL_DIFERIMENTO | numeric(7) |  |  | RS - Produto sujeito ao pagamento do ICMS na entrada quando decorrente do diferimento-Art.37 §1º,f do RICMS - Percentual diferimento |
| PB_PRODUTO_SUJEITO_FUNCEP | char(1) |  |  | PB - Produto sujeito ao Fundo Estadual de Combate à Pobreza - FUNCEP-PB |
| SC_PRODUTO_SUJEITO_ANTECIPACAO_AQUISICAO_INTERESTADUAIS | char(1) |  |  | SC - Produto sujeito à antecipação nas aquisições interestaduais de mercadorias para comercialização |
| BA_PRODUTO_COM_REDUCAO_BASE_CALC_ICMSA | char(1) |  |  | BA - Produto com redução na base de cálculo do ICMSA |
| BA_PRODUTO_COM_REDUCAO_BASE_CALC_ICMSA_PERCENTUAL | numeric(5) |  |  | BA - Percentual de redução ICMSA |
| ES_BENEFICIO_FISCAL_VENDAS_INTERESTADUAIS_IND_METALMECANICA | char(1) |  |  | ES - Produto com benefício fiscal na venda interest. realizada por indústria metalmecânica - Art. 530-LF RICMS |
| SCANC_CTB_VALOR_PMPF | numeric(6) |  |  | SCANC - Valor do PMPF |
| SCANC_CTB_TEOR_MISTURA | numeric(3) |  |  | SCANC - Teor de mistura |
| GERA_SCANC_PDI | char(1) |  |  | Gera informações para SCANC |
| COD_SCANC_PDI | integer(4) |  | S | Codigo do produto SCANC |
| POSSUE_GASA_PDI | char(1) |  | S | Possui gasolina A (S=Sim/N=Nao) |
| TIPO_SCANC_PDI | char(3) |  | S | Tipo Produto SCANC |
| MT_PRODUTO_INCLUIDO_CALCULO_PRODEIC_INVESTE | char(1) |  |  | MT - Produto incluído no cálculo do Desenvolvimento Industrial e Comercial - PRODEIC Investe |
| MT_CALCULO_PRODEIC_INVESTE_PR_OP_INTERNA | numeric(5) |  |  | MT - Produto incluído no cálculo do Desenvolvimento Industrial e Comercial - PRODEIC Investe - Percentual  Op. Interna |
| MT_CALCULO_PRODEIC_INVESTE_PR_OP_INTERESTADUAL | numeric(5) |  |  | MT - Produto incluído no cálculo do Desenvolvimento Industrial e Comercial - PRODEIC Investe - Percentual Op. Interestadual |
| CE_PRODUTO_SUJEITO_FECOP | char(1) |  |  | CE - Produto sujeito ao Fundo Estadual de Combate à Pobreza - FECOP |
| PA_PRODUTO_COM_REDUCAO_BASE_CALC_ICMSA | char(1) |  |  | PA - Produto com redução na base de cálculo do ICMSA |
| PA_PRODUTO_COM_REDUCAO_BASE_CALC_ICMSA_PERCENTUAL | numeric(5) |  |  | PA - Percentual de redução ICMSA |
| TO_PRODUTO_SUJEITO_ANTECIPACAO_AQUISICOES_INTER_MERCADORIAS_COMERCIALIZACAO | char(1) |  |  | TO - Produto sujeito à antecipação nas aquisições interestaduais de mercadorias para comercialização |
| PI_REGIME_ESPECIAL_TRIBUTACAO_OPERACOES_PRODUTOS_FARMACEUTICOS_ART_791F | char(1) |  |  | PI - Calcular regime especial de tributação nas operações com produtos farmacêuticos - Art. 791-F do RICMS |
| PI_SUJEITO_FUNDO_ESTADUAL_EQUILIBRIO_FISCAL_FUNEF | char(1) |  |  | PI - Produto sujeito ao Fundo Estadual de Equilíbrio Fiscal - FUNEF |
| RS_PRODUTO_SUJEITO_ANTECIPACAO_AQUISICOES_INTER_MERCADORIAS_COMERCIALIZACAO | char(1) |  |  | RS - Produto sujeito à antecipação nas aquisições interestaduais de mercadorias para comercialização |
| MG_CONSIDERAR_PROD_CP_RET_QUANDO_ST_REDUZAO_Z | char(1) |  |  | MG - Considerar o produto para o cálculo do crédito presumido RET quando possuir ST nos lançamentos de Redução Z |
| RS_PRODUTO_COM_ALIQUOTA_EFETIVA_7_PREVISTA_ART_23_II_XXIV_LIV_LV_LXIX | char(1) |  |  | Produto com alíquota efetiva de 7% prevista no Art. 23, II, XXIV, XXX, LIV, LV, LXIX |
| RJ_CREDITO_PRESUMIDO_CESTA_BASICA | char(1) |  |  | RJ - Crédito presumido produto compõe cesta basica |
| PRODUTO_INCLUIDO_REGIME_TRIBUTACAO_MONOFASICA_ICMS | char(1) |  |  | Produto incluído no regime de tributação monofásica do ICMS cfe Convênios ICMS nº 199/2022 e 15/2023 |
| PRODUTO_INCLUIDO_REGIME_TRIBUTACAO_MONOFASICA_ICMS_TIPO_COMBUSTIVEL | integer(4) |  |  | Produto incluído no regime de tributação monofásica do ICMS cfe Convênios ICMS nº 199/2022 e 15/2023 - Tipo combustível |
| PRODUTO_INCLUIDO_REGIME_TRIBUTACAO_MONOFASICA_ICMS_ALIQUOTA_FIXA | numeric(13) |  |  | Produto incluído no regime de tributação monofásica do ICMS cfe Convênios ICMS nº 199/2022 e 15/2023 - Alíquota fixa (ad rem) |
| FATOR_CORRECAO_VOLUME_ICMS_MONOFASICO | numeric(13) |  |  | Fator de correção do volume (FCV) |
| SE_PRODUTO_SUJEITO_FECOEP | char(1) |  |  | SE - Produto sujeito ao Fundo Estadual de Combate e Erradicação da Pobreza - FECOEP |
| RJ_CALC_REG_ESPECIAL_PADARIAS_CONFEITARIAS | char(1) |  |  | RJ - Calcular regime especial padarias e confeitarias (S/N) |
| MT_APLICAR_PC_PRODEIC_ANTES_DEDUZIR_ICMS_DEVOLUCAO | char(1) |  |  | MT - Aplicar o percentual fixado PRODEIC antes de deduzir o ICMS das devoluções de vendas |
| PE_PRODUTO_SUJEITO_ANTECIPACAO_ICMS_ATACADISTA | char(1) |  |  | PE - Produto sujeito a antecipação do ICMS nas empresas atacadistas (S/N) |
| PE_VALOR_PAUTA | numeric(13) |  |  | PE - Valor Pauta |
| RJ_PRODUTO_INCLUIDO_CALCULO_COMPLEMENTO_RESTITUICAO_ICMS_RESOLUCAO_578_2023 | char(1) |  |  | RJ -  Produto incluído no cálculo do complemento/restituição do ICMS ST conforme Resolução Sefaz nº 578/2023 |
| RJ_PRODUTO_INCLUIDO_CALCULO_COMPLEMENTO_RESTITUICAO_ICMS_ST_RESOLUCAO_578_2023_PERCENTUAL_BC | numeric(5) |  |  | RJ -  Produto incluído no cálculo do complemento/restituição do ICMS ST conforme Resolução Sefaz nº 578/2023 - Percentual BC |
| RJ_PRODUTO_SUJEITO_CALCULO_FECP_CONFORME_RESOLUCAO_SEFAZ_578_2023 | char(1) |  |  | RJ -  Produto sujeito ao cálculo do FECP conforme Resolução Sefaz nº 578/2023 |
| GERA_SCANC_MONOFASICO_ICMS_PDI | char(1) |  |  | Gera informações para SCANC do produto sujeito ao regime monofásico do ICMS |
| COD_SCANC_MONOFASICO_ICMS_PDI | integer(4) |  | S | Gera informações para SCANC do produto sujeito ao regime monofásico do ICMS - Codigo do Produto |
| TIPO_SCANC_MONOFASICO_PDI | char(4) |  | S | Tipo Produto SCANC Monofasico |
| PRODUTO_SUJEITO_FUNDEINFRA | char(1) |  |  | Produto sujeito ao Fundo Estadual de Infraestrutura - FUNDEINFRA |
| PRODUTO_SUJEITO_FUNDEINFRA_PRODUTO_BENEFICIADO | integer(4) |  |  | Produto sujeito ao Fundo Estadual de Infraestrutura - FUNDEINFRA - Produto Beneficiado |
| PRODUTO_SUJEITO_FUNDEINFRA_ALIQUOTA | numeric(5) |  |  | Produto sujeito ao Fundo Estadual de Infraestrutura - FUNDEINFRA - Alíquota |
| RS_PROD_SEG_AUTOPECAS_SUJ_ANTECIP_IMP_ENTRADAS | char(1) |  |  | RS - Produto do segmento de autopeças sujeito à antecipação do imposto nas entradas |
| PRODUTO_RECEBIDO_BONIF_RETIRADO_RECEITA_BRUTA_RATEIO_CREDITO | char(1) |  |  | Produto recebido em bonificação não considerado como receita bruta para fins de rateio de créditos |
| CCLASS_TRIB_IBS | varchar(6) |  |  | cClassTrib IBS |
| CCLASS_TRIB_CBS | varchar(6) |  |  | cClassTrib CBS |
| MS_PRODUTO_SUJEITO_FUNDERSUL_RECOLHE_CONTRIB | char(1) |  |  | MS - Produto sujeito FUNDERSUL - Recolhe contribuição Estabelecimentos Frigoríficos |
| MS_PRODUTO_SUJEITO_AO_CREDITO_PRESUMIDO_PORCENTAGEM_INTERNO | numeric(5) |  |  | MS - Produto sujeito ao crédito presumido - % interno |
| MS_PRODUTO_SUJEITO_AO_CREDITO_PRESUMIDO_PORCENTAGEM_INTERESTADUAL | numeric(5) |  |  | MS - Produto sujeito ao crédito presumido - % interestadual |
| RS_PRODUTO_COM_REDUCAO_BASE_CALC_ICMSA | char(1) |  |  | RS - Produto sujeito FUNDERSUL - Recolhe contribuição Estabelecimentos Frigoríficos |
| RS_PRODUTO_COM_REDUCAO_BASE_CALC_ICMSA_PERCENTUAL | numeric(4) |  |  | RS - Produto com redução na base de cálculo do ICMSA - Percentual de redução |
| MG_PRODUTO_REDUCAO_BASE_CALCULO_ICMSA | char(1) |  |  | MG - Produto com redução na base de cálculo do ICMSA |
| MG_PERCENTUAL_REDUCAO_BASE_CALCULO_ICMSA | numeric(4) |  |  | MG - Percentual de redução |
| CODIGO_BENEFICIO_DIRBI | integer(4) |  | S | Informar código do benefício DIRBI - Códigos |
| INFORMAR_CODIGO_BENEFICIO_DIRBI | char(1) |  |  | Informar código do benefício DIRBI - Códigos |
| UTILIZA_CCLASSTRIB_VINCULADO_NCM_NBS_IBS | char(1) |  |  | Utiliza a tabela de cClassTrib por vínculo de NCM/NBS |
| UTILIZA_CCLASSTRIB_VINCULADO_NCM_NBS_CBS | char(1) |  |  | Utiliza a tabela de cClassTrib por vínculo de NCM/NBS |
| PA_PRODUTO_SUJEITO_ANTECIPACAO_PRODUTOS_CESTA_BASICA | char(1) |  |  | Produto sujeito à antecipação nas aquisições interestaduais produtos cesta básica |
| PA_PRODUTO_SUJEITO_CREDITO_PRESUMIDO_SAIDAS_CESTA_BASICA | char(1) |  |  | Produto sujeito ao crédito presumido saídas de produtos cesta básica |
| DF_PRODUTO_INCLUIDO_CALCULO_RESTITUICAO_ICMS_ST_PAGO_ETAPAS_ANTERIORES | char(1) |  |  | DF - Produto incluído no cálculo da restituição do ICMS ST pago nas etapas anteriores |
| CCLASS_TRIB_IS | varchar(6) |  |  | Classificação tributaria do imposto seletivo - IS |
| ALIQUOTA_AD_VALOREM | numeric(5) |  |  | Alíquota Ad valorem do imposto IS |
| ALIQUOTA_AD_REM_FIXA | numeric(13) |  |  | Aliquota Ad rem fixa do imposto IS |
| MA_TIPO_PRODUTO_CRED_PRESUMIDO | integer(4) |  |  | MA - Credito Presumido Atacadista: tipo do produto |
| SP_PRODUTO_CREDITO_OUTORGADO_SAIDAS_INTERNAS_CARNE | char(1) |  |  | SP - Produto sujeito ao crédito outorgado nas saídas internas de carnes - Anexo III, Art. 40 do RICMS |
| PRODUTO_PISCOFINS_SUJEITO_REDUCAO_LINEAR_LC224 | char(1) |  |  | Produto não sujeito à redução linear de isenção e alíquota zero da LC 224/2025 |
| ENVIAR_EVENTO_IBS | char(1) |  |  | Enviar evento para ajuste na apuração assistida de IBS |
| ID_EVENTO_IBS | integer(4) |  | S | Tipo de evento para ajuste na apuração assistida de IBS (Ex: 211150 - Solicitação de apropriação de crédito para bens e serviços que dependem de atividade do adquirente) |
| ENVIAR_EVENTO_CBS | char(1) |  |  | Enviar evento para ajuste na apuração assistida de CBS |
| ID_EVENTO_CBS | integer(4) |  | S | Tipo de evento para ajuste na apuração assistida de CBS (Ex: 211150 - Solicitação de apropriação de crédito para bens e serviços que dependem de atividade do adquirente) |
