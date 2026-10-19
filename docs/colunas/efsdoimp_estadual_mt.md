# EFSDOIMP_ESTADUAL_MT — Saldo dos Impostos - Estadual MT
49 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| DEVOLUCAO_CREDITO_PRESUMIDO_PRODEIC | numeric(13) |  |  | Valor Devolução do Crédito Presumido PRODEIC |
| CREDITO_PRESUMIDO_TRANSPORTE | numeric(13) |  |  | Valor Crédito Presumido Transporte |
| CREDITO_PRESUMIDO_PRODEIC | numeric(13) |  |  | Valor Crédito Presumido PRODEIC |
| CREDITO_PRESUMIDO_ALGODAO | numeric(13) |  |  | VAlor Crédito Presumido Algodão |
| DEVOLUCAO_CREDITO_PRESUMIDO_ALGODAO | numeric(13) |  |  | Valor Devolução do Crédito Presumido Algodão |
| ESTORNO_CREDITO_PRESUMIDO_ALGODAO | numeric(13) |  |  | Valor Estorno Crédito Presumido Algod]ap |
| ESTORNO_CREDITO_PRESUMIDO_TRANSPORTE | numeric(13) |  |  | Valor Estorno Crédito Presumido Transporte |
| ESTORNO_CREDITO_PRESUMIDO_PRODEIC | numeric(13) |  |  | Estorno Crédito Presumido PRODEIC |
| CREDITO_PRESUMIDO_PRODEIC_PARTE_01 | numeric(13) |  |  | Valor Crédito Presumido PRODEIC - Parte 01 |
| CREDITO_PRESUMIDO_PRODEIC_PARTE_02 | numeric(13) |  |  | Valor Crédito Presumido PRODEIC - Parte 02 |
| CREDITO_PRESUMIDO_PRODEIC_PARTE_03 | numeric(13) |  |  | Valor Crédito Presumido PRODEIC - Parte 03 |
| CREDITO_PAGAMENTOS_FATOR_GERADOR | numeric(13) |  |  | Créditos de pagamentos devidos por ocasião do Fato Gerador |
| CREDITO_ICMS_ESTIMATIVA_SIMPLIFICADO | numeric(13) |  |  | Crédito ICMS Estimativa Simplificado |
| AJUSTE_BASE_CALCULO_ICMS_PRODEIC | numeric(13) |  |  | Ajuste referente redução da base de cálculo do ICMS - PRODEIC |
| DEBITO_FECEP_ICMS | numeric(13) |  |  | Valor débito FECEP ICMS |
| CREDITO_OUTORGADO_ESTAB_COMER_VAREJISTA | numeric(13) |  |  | Crédito outorgado estabelecimento comercial varejista - Art. 2º, I, An. XVII, RICMS |
| CREDITO_SOBRE_ESTOQUE_OPERACAO_DE_ENTRADA | numeric(13) |  |  | Crédito sobre estoque operação de entrada - Art.8º, §2º, An.XVII do RICMS |
| CREDITO_SOBRE_ESTOQUE_ICMS_EFETIVAMENTE_PAGO | numeric(13) |  |  | Crédito sobre estoque ICMS efetivamente pago - Art.8º, §3º, An.XVII do RICMS |
| CREDITO_OUTORGADO_ESTAB_COMER_ATAC_SAIDAS_INTERNAS | numeric(13) |  |  | Estab. comercial atacadista - Saídas internas - Art. 2°, II, a, An. XVII, RICMS |
| CREDITO_OUTORGADO_ESTAB_COMER_ATAC_SAIDAS_INTERESTADUAIS | numeric(13) |  |  | Estab. comercial atacadista - Saídas interest. - Art. 2°, II, b, An. XVII, RICMS |
| ESTORNO_CREDITO_OUTORGADO_ESTAB_COMER_ATAC_SAIDAS_INTERNAS | numeric(13) |  |  | Devolução créd. outorgado saídas internas - Art. 2°, II, a, An. XVII, RICMS |
| ESTORNO_CREDITO_OUTORGADO_ESTAB_COMER_ATAC_SAIDAS_INTERESTADUAIS | numeric(13) |  |  | Devolução créd. outorgado saídas interest. - Art. 2°, II, b, An. XVII, RICMS |
| ESTORNO_CREDITO_OUTORGADO_ESTAB_COMER_ATAC_ENTRADAS | numeric(13) |  |  | Estorno créd. excedente 7% nas entradas - Art. 2°, §2º, I, An. XVII, RICMS |
| LIMITE_CREDITO_OUTORGADO | numeric(13) |  |  | Limite do crédito outorgado |
| ESTORNO_DEBITO_REGIME_SIMPLIFICADO_TRIBUTACAO_RESTAURANTES_BARES | numeric(13) |  |  | Estorno de Debito Regime simplificado de tributação - Art. 1o, Anexo XVIII do RICMS |
| CREDITO_OUT_PRODEIC_CREDITO_ESCRITURADO | numeric(13) |  |  | Crédito Out Prodeic - Crédito Escriturado |
| CREDITO_OUT_PRODEIC_TOTAL_SAIDAS | numeric(13) |  |  | Crédito Out Prodeic - Total Saídas |
| CREDITO_OUT_PRODEIC_DEBITOS_OP_INTERNAS | numeric(13) |  |  | Crédito Out Prodeic - Débitos Operações Internas |
| CREDITO_OUT_PRODEIC_DEBITOS_OP_INTERESTADUAIS | numeric(13) |  |  | Crédito Out Prodeic - Débitos Operações Interestaduais |
| CREDITO_OUT_PRODEIC_ESTORNO_CRED_PERIODO_ANTERIOR_INTERNAS | numeric(13) |  |  | Crédito Out Prodeic - Estorno Cédito Período Anterior Operações Internas |
| CREDITO_OUT_PRODEIC_ESTORNO_CRED_PERIODO_ANTERIOR_INTERESTADUAIS | numeric(13) |  |  | Crédito Out Prodeic - Estorno Cédito Período Anterior Operações Interestaduais |
| CREDITO_OUT_PRODEIC_ESTORNO_CRED_PERIODO_SEGUINTE_INTERNAS | numeric(13) |  |  | Crédito Out Prodeic - Estorno Cédito para o Período Seguinte Operações Internas |
| CREDITO_OUT_PRODEIC_ESTORNO_CRED_PERIODO_SEGUINTE_INTERESTADUAIS | numeric(13) |  |  | Crédito Out Prodeic - Estorno Cédito para o Período Seguinte Operações Interestaduais |
| CREDITO_OUT_PRODEIC_PERC_PROPORCAO_OP_INTERNAS | numeric(5) |  |  | Crédito Out Prodeic - Percentual de Proporção para Op. Internas relativo as Saídas |
| CREDITO_OUT_PRODEIC_PERC_PROPORCAO_OP_INTERESTADUAIS | numeric(5) |  |  | Crédito Out Prodeic - Percentual de Proporção para Op. Interestaduais relativo as Saídas |
| CREDITO_OUT_PRODEIC_PERC_PROPORCAO_DEMAIS_PRODUTOS | numeric(5) |  |  | Crédito Out Prodeic - Percentual de Proporção para Demais Produtos relativo as Saídas |
| CREDITO_OUT_PRODEIC_PERC_PROPORCAO_OP_ISENTAS | numeric(5) |  |  | Crédito Out Prodeic - Percentual de Proporção para Op. Isentas relativo as Saídas |
| CREDITO_OUT_PRODEIC_PERC_PROPORCAO_OP_EXPORTACAO | numeric(5) |  |  | Crédito Out Prodeic - Percentual de Proporção para Op. Exportação relativo as Saídas |
| CREDITO_OUT_PRODEIC_CRED_PROPORCIONAL_OP_INTERNAS | numeric(13) |  |  | Crédito Out Prodeic - Crédito Proporcional Op. Internas |
| CREDITO_OUT_PRODEIC_CRED_PROPORCIONAL_OP_INTERESTADUAIS | numeric(13) |  |  | Crédito Out Prodeic - Crédito Proporcional Op. Interestaduais |
| CREDITO_OUT_PRODEIC_CRED_PROPORCIONAL_DEMAIS_PRODUTOS | numeric(13) |  |  | Crédito Out Prodeic - Crédito Proporcional Demais Produtos |
| CREDITO_OUT_PRODEIC_CRED_PROPORCIONAL_OP_ISENTAS | numeric(13) |  |  | Crédito Out Prodeic - Crédito Proporcional Op. Isentas |
| CREDITO_OUT_PRODEIC_CRED_PROPORCIONAL_OP_EXPORTACAO | numeric(13) |  |  | Crédito Out Prodeic - Crédito Proporcional Op. Exportação |
| CREDITO_OUT_PRODEIC_CREDITO_OUTORGADO_OP_INTERNAS | numeric(13) |  |  | Crédito Out Prodeic - Crédito Outorgado nas Op. Internas |
| CREDITO_OUT_PRODEIC_CREDITO_OUTORGADO_OP_INTERESTADUAIS | numeric(13) |  |  | Crédito Out Prodeic - Crédito Outorgado nas Op. Interestaduais |
| CREDITO_OUT_PRODEIC_ESTORNO_CRED_OP_ISENTAS | numeric(13) |  |  | Crédito Out Prodeic - Estorno Crédito Op. Isentas |
| CREDITO_OUT_PRODEIC_ESTORNO_DEBITOS_SALDO_CREDOR | numeric(13) |  |  | Crédito Out Prodeic - Estorno Débitos do Saldo Credor |
| ESTORNO_DEBITO_OPERACOES_CTE_SUBSTITUTO | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto |
| ESTORNO_DEBITO_ICMS_DEVOLUCAO_ENTRADA_SEM_APROVEITAMENTO | numeric(13) |  |  | Estorno de débito de ICMS de devolução, cuja entrada ocorreu sem o aproveitamento |
| ESTORNO_DEBITO_ICMS_DEVOLUCAO_ATIVO_IMOB_USO_CONSUMO | numeric(13) |  |  | Estorno débito ICMS devolução, entrada sem aproveitamento-Ativo Imob/Uso e Consumo |
| CREDITO_AQUISICAO_COMBUSTIVEL_INSUMO | numeric(13) |  |  | Crédito na aquisição de combustíveis para insumo - Conv. ICMS nº 199/22 e 26/23 |
