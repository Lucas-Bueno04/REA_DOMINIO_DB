# EFSDOIMP_ESTADUAL_RO — Saldo dos Impostos - Estadual RO
88 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| CREDITO_PRESUMIDO_BAR_RESTAURANTE | numeric(13) |  |  | Crédito Presumido Bares e Restaurantes |
| ESTORNO_CREDITO_PRESUMIDO_BAR_RESTAURANTE | numeric(13) |  |  | Estorno de Crédito Presumido Bares e Restaurantes |
| CREDITO_PRESUMIDO_BAR_RESTAURANTE_SAIDA | numeric(13) |  |  | Crédito Presumido Bares e Restaurantes - Origem Saída |
| CREDITO_PRESUMIDO_BAR_RESTAURANTE_REDUCAO_Z | numeric(13) |  |  | Crédito Presumido Bares e Restaurantes - Origem Redução Z |
| CREDITO_PRESUMIDO_TRANSPORTE | numeric(13) |  |  | Crédito Presumido Transportes |
| CREDITO_PRESUMIDO_TRANSPORTE_CT_CONV_106 | numeric(13) |  |  | Crédito Presumido Transportes - Conhecimento de Transporte |
| CREDITO_PRESUMIDO_TRANSPORTE_BP_CONV_106 | numeric(13) |  |  | Crédito Presumido Transportes - Bilhete de Passagem |
| ESTORNO_DEBITO_ICMS_FG | numeric(13) |  |  | Estorno de Débito ICMSFG |
| CREDITO_PRESUMIDO_IND_TORREFADORAS | numeric(13) |  |  | Crédito Presumido Indústrias Torrefadoras |
| DEVOLUCAO_CREDITO_PRESUMIDO_IND_TORREFADORAS | numeric(13) |  |  | Devolução Crédito Presumido Indústrias Torrefadoras |
| CREDITO_PRESUMIDO_IND_TORREFADORAS_SAIDA | numeric(13) |  |  | Crédito Presumido Indústrias Torrefadoras - Origem Saídas |
| CREDITO_PRESUMIDO_IND_TORREFADORAS_REDUCAO_Z | numeric(13) |  |  | Crédito Presumido Indústrias Torrefadoras - Origem Reduções Z |
| CREDITO_ICMS_ANTECIPADO | numeric(13) |  |  | Crédito ICMS Antecipado |
| TRANSFERENCIA_SALDO_CREDOR | numeric(13) |  |  | Transferências de crédito de ICMS - Transferido |
| RECEBIMENTO_SALDO_CREDOR | numeric(13) |  |  | Transferências de crédito de ICMS - Recebido |
| CREDITO_PRESUMIDO_BAR_RESTAURANTE_NFC | numeric(13) |  |  | Crédito Presumido Bares e Restaurantes - Origem Saída |
| CREDITO_PRES_LEITE_ITEM15_TABELA1_ANEXOIV | numeric(13) |  |  | Devolução créd. presum. saídas interest. indust. leite - Item 15, Tabela 1, Anexo IV |
| ESTORNO_CREDITO_PRES_LEITE_ITEM15_TABELA1_ANEXOIV | numeric(13) |  |  | Saídas interestaduais de indust. do leite - Item 15, Tabela 1, Anexo IV |
| CREDITO_PRES_LEITE_ITEM6_TABELA1_ANEXOIV | numeric(13) |  |  | Devolução créd. presum. saídas interest. indust. leite - Item 6, Tabela 1, Anexo IV |
| ESTORNO_CREDITO_PRES_LEITE_ITEM6_TABELA1_ANEXOIV | numeric(13) |  |  | Saídas interestaduais de indust. do leite - Item 6, Tabela 1, Anexo IV |
| CREDITO_CONFORME_ALIQUOTA_SN | numeric(13) |  |  | Crédito de ICMS conf. alíquota do Simples Nacional - Art. 23, LC 123/06 |
| CREDITO_PRESUMIDO_MERCADORIA_IMP_EXT_LEI_1473_2005 | numeric(13) |  |  | Crédito presumido nas saídas interest. de mercadoria importada do exterior - Lei nº. 1.473/2005 |
| DEVOLUCAO_CREDITO_PRESUMIDO_MERCADORIA_IMP_EXT_LEI_1473_2005 | numeric(13) |  |  | Devolução créd. presumido saídas interest. de mercadoria importada - Lei nº. 1.473/2005 |
| ESTORNO_ICMS_DOCUMENTOS_EXTEMPORANEOS | numeric(13) |  |  | Estorno de ICMS dos documentos extemporâneos |
| ICMS_DOCUMENTOS_EXTEMPORANEOS_RECOLHER | numeric(13) |  |  | ICMS dos documentos extemporâneos a recolher |
| VALOR_PAGO_ICMS_DOCUMENTOS_EXTEMPORANEOS | numeric(13) |  |  | ICMS pago dos documentos extemporâneos a recolher |
| DATA_VENCIMENTO_ICMS_DOCUMENTOS_EXTEMPORANEOS | date(4) |  | S | Data de vencimento - ICMS dos documentos extemporâneos a recolher |
| CREDITO_ICMS_PROPRIO_ST_IN_22_2018 | numeric(13) |  |  | Crédito de ICMS Próprio |
| RESSARCIMENTO_ICMS_ST_IN_22_2018 | numeric(13) |  |  | Ressarcimento de ICMS ST |
| CREDITO_PRESUMIDO_CONSIT_PROJETO_IMPLANTACAO | numeric(13) |  |  | Crédito presumido CONSIT, Decreto nº 12.988/2007, art. 2º, II |
| DEVOLUCAO_CREDITO_PRESUMIDO_CONSIT_PROJETO_IMPLANTACAO | numeric(13) |  |  | Devolução do crédito presumido CONSIT, Decreto nº 12.988/2007, art. 2º, II |
| ESTORNO_CREDITO_PRESUMIDO_CONSIT_PROJETO_IMPLANTACAO | numeric(13) |  |  | Estorno de Crédito presumido CONSIT, Decreto nº 12.988/2007, art. 2º, II |
| ESTORNO_DEBITO_ICMS_INCENTIVADO_CONSIT_PROJETO_IMPLANTACAO | numeric(13) |  |  | Estorno de Débito ICMS incentivado CONSIT, Decreto nº 12.988/2007, art. 2º, II |
| CREDITO_PRESUMIDO_SAIDAS_INTERNAS_OVO | numeric(13) |  |  | Crédito presumido saídas internas de ovo - Item 10, Parte 2, Anexo IV |
| DEVOLUCAO_CREDITO_PRESUMIDO_SAIDAS_INTERNAS_OVO | numeric(13) |  |  | Devolução créd. presumido saídas internas de ovo - Item 10, Parte 2, Anexo IV |
| EXCLUSAO_MERCADORIA_SUBTRI_DECRETO_22721_2018 | numeric(13) |  |  | Exclusão de mercadorias da substituição tributária - Dec. nº 22.721/18 |
| ESTORNO_DEBITO_OPERACOES_CTE_SUBSTITUTO | numeric(13) |  |  | Estorno de débito nas operações com CT-e e/ou CT-eOS substituto |
| ESTORNO_CREDITO_PRESUMIDO_CTE_SUBSTITUIDO | numeric(13) |  |  | Estorno de Crédito Presumido CT-e e/ou CT-eOS Substituído - Item 3 - Parte 2 - Anexo IV |
| ESTORNO_DEBITO_REFERENTE_TRANSFERENCIA_CREDITOS_ICMS_ITEM_40_33_2018 | numeric(13) |  |  | Estorno de débito referente transferência de créditos de ICMS - Item 40 da IN 33/2018 |
