# EFSDOIMP_ESTADUAL_RJ — Saldo dos Impostos - Estadual RJ
523 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| CODI_IMP | integer(4) | PK |  | Imposto |
| CREDITO_PRESUMIDO_INFORMATICA_IMPORTADOS | numeric(13) |  |  | Crédito presumido saídas internas e interestaduais de produtos importados |
| CREDITO_PRESUMIDO_INFORMATICA_NACIONAIS | numeric(13) |  |  | Crédito presumido saídas interestaduais de produtos nacionais |
| CREDITO_PRESUMIDO_INFORMATICA_FLUMINENSE | numeric(13) |  |  | Crédito presumido saídas de produto industrializado no estabelecimento Fluminense |
| ESTORNO_CREDITO_INFORMATICA_IMPORTADOS | numeric(13) |  |  | Devolução produto informática, eletrônicos e eletrodomésticos Importados |
| ESTORNO_CREDITO_INFORMATICA_NACIONAIS | numeric(13) |  |  | Devolução produto informática, eletrônicos e eletrodomésticos Nacionais |
| ESTORNO_CREDITO_INFORMATICA_FLUMINENSE | numeric(13) |  |  | Devolução produto informática, eletrônicos e eletrodomésticos Fluminense |
| ESTORNO_CREDITO_INFORMATICA_TOTAL | numeric(13) |  |  | Devolução produto informática, eletrônicos e eletrodomésticos |
| CREDITO_PRESUMIDO_EMBARCACOES_NAUTICAS | numeric(13) |  |  | Crédito presumido nas saídas com embarcações náuticas - Dec. 41.681/2009 |
| DEVOLUCAO_CREDITO_PRESUMIDO_EMBARCACOES_NAUTICAS | numeric(13) |  |  | Devolução do créd. presumido nas saídas com embarcações náuticas - Dec. 41.681/2009 |
| DEDUCAO_FECP_EMBARCACOES_NAUTICAS | numeric(13) |  |  | FECP pelas saídas com embarcações náuticas - Dec. 41.681/2009 |
| CREDITO_PRESUMIDO_TRANSPORTE | numeric(13) |  |  | Crédito presumido transporte 20% |
| CREDITO_CONFORME_ALIQUOTA_SN | numeric(13) |  |  | Crédito de ICMS conf. Alíquota do Simples Nacional - Art.23, LC 123/06 |
| DEVOLUCAO_MERCADORIA_ADQUIRIDA_SN | numeric(13) |  |  | Devolução de mercadoria adquirida de Simples Nacional |
| TRANSFERENCIA_SALDO_CREDOR | numeric(13) |  |  | Transferência de saldo credor - Art. 1, Livro III do RICMS |
| RECEBIMENTO_SALDO_CREDOR | numeric(13) |  |  | Recebimento de saldo credor - Art. 1, Livro III do RICMS |
| SAIDAS_ICMS_PROP_ISENTA_NAO_TRIB | numeric(13) |  |  | Estorno Proporcional - Saídas isentas não tributadas |
| SERVICOS_ICMS_PROP_ISENTA_NAO_TRIB | numeric(13) |  |  | Estorno Proporcional - ICMS Serviços isentas não tributadas |
| SAIDAS_TOTAIS_ICMS_PROP_ISENTA_NAO_TRIB | numeric(13) |  |  | Estorno Proporcional - Saídas totais isentas não tributadas |
| PROP_SAIDAS_SERV_ICMS_PROP_ISENTA_NAO_TRIB | numeric(5) |  |  | Estorno Proporcional - Proporção Saídas/Serviços isentas não tributadas |
| TOTAL_CREDITOS_ICMS_PROP_ISENTA_NAO_TRIB | numeric(13) |  |  | Estorno Proporcional - Total Créditos ICMS |
| ESTORNO_CREDITO_ICMS_PROP_ISENTA_NAO_TRIB | numeric(13) |  |  | Estorno Proporcional - Estorno Credito ICMS |
| CREDITO_PRESUMIDO_SAIDAS_PLASTICOS_PROCESSO_FABRIL | numeric(13) |  |  | Crédito Presumido Saídas Plásticos Processo Fabril |
| CREDITO_PRESUMIDO_SAIDAS_PLASTICOS_PROCESSO_FABRIL_DEVOLUCAO | numeric(13) |  |  | Devolução Crédito Presumido Saídas Plásticos Processo Fabril |
| CREDITO_PRESUMIDO_SAIDAS_PLASTICOS_CONSUMIDOR_FINAL | numeric(13) |  |  | Crédito Presumido Saídas Plásticos Consumidor Final |
| CREDITO_PRESUMIDO_SAIDAS_PLASTICOS_CONSUMIDOR_FINAL_DEVOLUCAO | numeric(13) |  |  | Devolução Crédito Presumido Saídas Plásticos Consumidor Final |
| ESTORNO_ICMS_OPER_CRED_PRESUMIDO_DEC_42649_2010 | numeric(13) |  |  | Estorno do ICMS nas operações com crédito presumido conforme Dec. 42.649/2010 |
| CREDITO_ICMS_NAO_APROPRIADO_AQUISICAO_MERC_ICMS_ST | numeric(13) |  |  | Crédito ref. ao ICMS próprio não apropriado na aquisição de merc. sujeita ao ICMS-ST devolvida |
| ESTORNO_CREDITO_PRESUMIDO_TRANSPORTE | numeric(13) |  |  | Estorno de ICMS nas operações com Crédito Presumido Transportes |
| SAIDAS_INTER_RIOLOG_LEI_4173_03_ART_3_I | numeric(13) |  |  | Saídas interestaduais - RIOLOG - Lei 4.173/03, Art.3º, I |
| ENTRADAS_INTER_RIOLOG_LEI_4173_03_ART_3_II | numeric(13) |  |  | Entradas interestaduais - RIOLOG - Lei 4.173/03, Art.3º, II |
| ENTRADAS_POR_TRANSF_RIOLOG_LEI_4173_03_ART_3_III | numeric(13) |  |  | Entradas por transferência - RIOLOG - Lei 4.173/03, Art.3º, III |
| ENTRADAS_INTERNAS_RIOLOG_LEI_4173_03_ART_3_IV | numeric(13) |  |  | Entradas internas - RIOLOG - Lei 4.173/03, Art.3º, IV |
| DEVOLUCAO_CRED_PRES_SAIDAS_INTER_RIOLOG_LEI_4173_03_ART_3_I | numeric(13) |  |  | Devolução créd. pres. saídas interest. - RIOLOG - Lei 4.173/03, Art.3º, I |
| DEVOLUCAO_CRED_PRES_ENTRADAS_INTER_RIOLOG_LEI_4173_03_ART_3_II | numeric(13) |  |  | Devolução créd. pres. entradas interest. - RIOLOG - Lei 4.173/03, Art.3º, II |
| DEVOLUCAO_CRED_PRES_ENTRADAS_POR_TRANSF_RIOLOG_LEI_4173_03_ART_3_III | numeric(13) |  |  | Devolução créd. pres. entradas transfer. - RIOLOG - Lei 4.173/03, Art.3º, III |
| DEVOLUCAO_CRED_PRES_ENTRADAS_INTERNAS_RIOLOG_LEI_4173_03_ART_3_IV | numeric(13) |  |  | Devolução créd. pres. entradas internas - RIOLOG - Lei 4.173/03, Art.3º, IV |
| VALOR_ICMS_MINIMO_RIOLOG | numeric(13) |  |  | ICMS mínimo a recolher conforme Art. 5º da Lei 4.173/2003 - RIOLOG |
| VALOR_PAGO_ICMS_MINIMO_RIOLOG | numeric(13) |  |  | ICMS mínimo pago conforme Art. 5º da Lei 4.173/2003 - RIOLOG |
| DEVOLUCAO_MERCADORIA_ADQUIRIDA_SIMPLES_NACIONAL | numeric(13) |  |  | Devolução de mercadoria adquirida de Simples Nacional |
| OUTROS_CREDITOS_CRED_ICMS_DEV_COMPRA | numeric(13) |  |  | Crédito ICMS - Devolução de compra uso e consumo ou imobilizado |
| OUTROS_CREDITOS_RECUP_DIFALI_DEV_COMPRA | numeric(13) |  |  | Recuperação do Difali - Devolução de compra |
| ESTORNO_CREDITO_ICMS_PROP_POSSUIR_RED_BC | numeric(13) |  |  | Estorno proporcional saída com redução da base de cálculo – Produtos da cesta básica |
| ESTORNO_ICMS_COMPLEMENTAR | numeric(13) |  |  | Estorno do ICMS Complementar |
| ICMS_COMPLEMENTAR_VALOR_RECOLHER | numeric(13) |  |  | ICMS Complementar - valor a recolher |
| ICMS_COMPLEMENTAR_VALOR_PAGO | numeric(13) |  |  | ICMS Complementar - valor pago |
| ICMS_COMPLEMENTAR_DATA_VENCIMENTO | date(4) |  | S | ICMS Complementar - data de vencimento |
| ICMS_COMPLEMENTAR_CODIGO_RECOLHIMENTO | char(6) |  | S | ICMS Complementar - código de recolhimento |
| ESTORNO_ICMS_DOCUMENTOS_EXTEMPORANEOS | numeric(13) |  |  | Estorno ICMS documentos extemporaneo |
| ICMS_DOCUMENTOS_EXTEMPORANEOS_RECOLHER | numeric(13) |  |  | ICMS documentos extemporaneo recolher |
| VALOR_PAGO_ICMS_DOCUMENTOS_EXTEMPORANEOS | numeric(13) |  |  | Valor pago ICMS documento extemporaneo |
| DATA_VENCIMENTO_ICMS_DOCUMENTOS_EXTEMPORANEOS | date(4) |  | S | Data vencimento ICMS documentos extemporaneo |
| CREDITO_PRESUMIDO_FORNECIMENTO_REFEICOES | numeric(13) |  |  | Crédito Presumido Fornecimento de refeições - Lei 9.355/2021 |
| CREDITO_PRESUMIDO_DEMAIS_OPERACOES | numeric(13) |  |  | Crédito Presumido Demais operações - Lei 9.355/2021 |
| DEVOLUCAO_CREDITO_PRESUMIDO_FORNECIMENTO_REFEICOES | numeric(13) |  |  | Devolução Crédito Presumido Fornecimento de refeições - Lei 9.355/2021 |
| DEVOLUCAO_CREDITO_PRESUMIDO_DEMAIS_OPERACOES | numeric(13) |  |  | Devolução Crédito Presumido Demais operações - Lei 9.355/2021 |
| ESTORNO_CREDITO_PRESUMIDO_PELAS_ENTRADAS | numeric(13) |  |  | Estorno do ICMS nas operações com crédito presumido - Lei 9.355/2021 |
| OPERACAO_CREDITO_PRESUMIDO_RIOLOG_LEI_9025_2020_ART_2_I | numeric(13) |  |  | Operações com crédito presumido - RIOLOG Art. 2º, I, Lei 9.025/2020 |
| DEVOLUCAO_CREDITO_PRESUMIDO_RIOLOG_LEI_9025_2020 | numeric(13) |  |  | Devolução de crédito presumido - RIOLOG Lei 9.025/2020 |
| COMPENSACAO_VALOR_MINIMO_ICMS_RIOLOG_LEI_9025_2020_ART_7 | numeric(13) |  |  | Compensação de valor mínimo de ICMS Art. 7º, §1º Lei 9.025/2020 |
| SAIDAS_INTER_RIOLOG_LEI_9025_2020_ART_2_I | numeric(13) |  |  | Saídas interestaduais - RIOLOG, Art. 2º, I, Lei 9.025/2020 |
| VALOR_ICMS_MINIMO_RIOLOG_LEI_9025_2020 | numeric(13) |  |  | ICMS mínimo a recolher conforme Art. 7º da Lei 9.025/2020 - RIOLOG |
| VALOR_PAGO_ICMS_MINIMO_RIOLOG_LEI_9025_2020 | numeric(13) |  |  | ICMS mínimo pago conforme Art. 7º da Lei 9.025/2020 - RIOLOG |
| ESTORNO_CREDITO_PRESUMIDO_RIOLOG_LEI_9025_2020 | numeric(13) |  |  | ICMS estorno de crédito conforme Art. 7º da Lei 9.025/2020 - RIOLOG |
| REGIME_ESPECIAL_PADARIAS_CONFEITARIAS_TITULO_VA_LIVRO_V_RICMS | numeric(13) |  |  | Regime especial padarias e confeitarias - Título V-A, Livro V do RICMS |
| ESTORNO_CREDITO_REGIME_ESPECIAL_PADARIAS_CONFEITARIAS_TITULO_VA_RICMS | numeric(13) |  |  | Estorno de crédito regime especial padarias e confeitarias - Título V-A, Livro V do RICMS |
| ESTORNO_DEBITOS_REGIME_ESPECIAL_PADARIAS_CONFEITARIAS_TITULO_VA_RICMS | numeric(13) |  |  | Estorno de débito regime especial padarias e confeitarias - Título V-A, Livro V do RICMS |
| RESTITUICAO_ICMS_ST_ART_16_578_2023 | numeric(13) |  |  | Restituição de ICMS ST - Art. 16-J da Resolução Sefaz 578/2023 |
| RESTITUICAO_FECP_ART_16_578_2023 | numeric(13) |  |  | Restituição de FECP - Art. 16-J da Resolução Sefaz 578/2023 |
| COMPLEMENTO_ICMS_ST_ART_16_578_2023 | numeric(13) |  |  | Complemento de ICMS ST - Art. 16-I da Resolução Sefaz 578/2023 |
| COMPLEMENTO_FECP_ART_16_578_2023 | numeric(13) |  |  | Complemento de FECP - Art. 16-I da Resolução Sefaz 578/2023 |
| ESTORNO_DEBITO_OPERACOES_CTE_SUBSTITUTO | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto |
| CREDITO_PRESUMIDO_SAIDAS_INTERNAS_ABATEDOR_INDUSTRIAL_FRIGORIFICO_ART_1_LEI_8792_2020 | numeric(13) |  |  | Créd. pres. saídas internas de abatedor e industrial frigorífico - Art. 1º, V, Lei 8.792/20 |
| ESTORNO_ICMS_NAS_OPERACOES_COM_CREDITO_PRESUMIDO_ART_1_LEI_8792_2020 | numeric(13) |  |  | Estorno do ICMS nas operações com crédito presumido - Art. 1º, I, § 3º, Lei 8.792/20 |
| DEVOLUCAO_CREDITO_PRESUMIDO_SAIDAS_INTERNAS_ABATEDOR_INDUSTRIAL_FRIGORIFICO_ART_1_LEI_8792_2020 | numeric(13) |  |  | Dev. créd. pres. saídas internas abatedor e industrial frigorífico - Art. 1º, V, Lei 8.792/20 |
| CREDITO_PRESUMIDO_REG_ESPECIAL_RECUP_INDUSTRIAL | numeric(13) |  |  | Reg. Especial de Recup. Industrial Regionalizada - Crédito presumido conf. Lei 6.979/15 |
| ESTORNO_DEBITO_INDEVIDO_TRANSPORTE_OUTRA_UF | numeric(13) |  |  | Estorno de débito de ICMS lançado indevidamente em transporte iniciado em outra UF |
| ESTORNO_CREDITO_DEVOLUCAO_VENDAS_REG_ESPEC_RECUP_INDUSTRIAL | numeric(13) |  |  | Reg. Especial de Recup. Industrial Regionalizada - Estorno de crédito devoluções de vendas conf. Resolução SEFAZ nº 705/2024 |
| CREDITO_PRESUMIDO_SAIDAS_INTERESTADUAIS_PRODUTOS_FARMACEUTICOS | numeric(13) |  |  | Créd. pres. saídas interestaduais de produtos farmacêuticos - Art. 9º do Dec. 36.450/2004 |
| DEVOLUCAO_CREDITO_PRESUMIDO_SAIDAS_INTERESTADUAIS_PRODUTOS_FARMACEUTICOS | numeric(13) |  |  | Dev. Créd. Pres. saídas interestaduais de produtos farmacêuticos - Art. 9º do Dec. 36.450/2004 |
| ESTORNO_CREDITO_PRESUMIDO_SAIDAS_INTERESTADUAIS_PRODUTOS_FARMACEUTICOS | numeric(13) |  |  | Estorno do ICMS nas operações com crédito presumido - Art. 9º do Dec. 36.450/2004 |
| VALOR_ICMS_MINIMO_ART_10_LEI_6979_2015_REG_ESP_RECUP_IND_REG | numeric(13) |  |  | ICMS mínimo a recolher Art. 10° Lei 6.979/2015 – Reg. Esp. Recup. Ind. Reg. |
| VALOR_PAGO_ICMS_MINIMO_ART_10_LEI_6979_2015_REG_ESP_RECUP_IND_REG | numeric(13) |  |  | ICMS mínimo pago Art. 10° Lei 6.979/2015 – Reg. Esp. Recup. Ind. Reg. |
