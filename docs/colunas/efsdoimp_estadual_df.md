# EFSDOIMP_ESTADUAL_DF — Saldo dos Impostos - Estadual DF
28 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| CREDITO_PRESUMIDO_TRANSPORTE | numeric(13) |  |  | Crédito presumido de 20% para  transportadoras - Item 2,  Anexo I do RICMS |
| LEI_5005_TOTAL_VENDAS_INTERNAS | numeric(13) |  |  | Lei 5005 - Total Vendas Internas |
| LEI_5005_TOTAL_VENDAS_INTERESTADUAIS | numeric(13) |  |  | Lei 5005 - Total Vendas Interestaduais |
| LEI_5005_PROPORCAO_VENDAS_INTERNAS | numeric(7) |  |  | Lei 5005 - Proporção Vendas Internas |
| LEI_5005_PROPORCAO_VENDAS_INTERESTADUAIS | numeric(7) |  |  | Lei 5005 - Proporção Vendas Interestaduais |
| LEI_5005_ESTORNO_ENTRADAS | numeric(13) |  |  | Lei 5005 - Estorno Entradas |
| LEI_5005_ESTORNO_DEVOLUCAO_VENDAS | numeric(13) |  |  | Lei 5005 - Estorno Devolução Vendas |
| LEI_5005_BASE_CALCULO_COMPRAS_INTERNAS | numeric(13) |  |  | Lei 5005 - Base Cálculo Compras Internas |
| LEI_5005_BASE_CALCULO_COMPRAS_INTERESTADUAIS | numeric(13) |  |  | Lei 5005 - Base Cálculo Compras Interestaduais |
| LEI_5005_BASE_CALCULO_DEVOLUCAO_VENDAS | numeric(13) |  |  | Lei 5005 - Base Cálculo Devolução Vendas |
| LEI_5005_CREDITO_COMPRAS_INTERNAS | numeric(13) |  |  | Lei 5005 - Crédito Compras Internas |
| LEI_5005_CREDITO_COMPRAS_INTERESTADUAIS | numeric(13) |  |  | Lei 5005 - Crédito Compras Interestaduais |
| LEI_5005_CREDITO_DEVOLUCAO_VENDAS | numeric(13) |  |  | Lei 5005 - Crédito Devolução Vendas |
| LEI_5005_ESTORNO_SAIDAS_ICMS | numeric(13) |  |  | Lei 5005 - Estorno Saídas ICMS |
| LEI_5005_ESTORNO_SAIDAS_FECOP | numeric(13) |  |  | Lei 5005 - Estorno Saídas FECOP |
| LEI_5005_ESTORNO_DEVOLUCAO_COMPRAS | numeric(13) |  |  | Lei 5005 - Estorno Devolução Compras |
| LEI_5005_BASE_CALCULO_VENDAS | numeric(13) |  |  | Lei 5005 - Base Cálculo Vendas |
| LEI_5005_BASE_CALCULO_DEVOLUCAO_COMPRAS_INTERNAS | numeric(13) |  |  | Lei 5005 - Base Cálculo Devolução Compras Internas |
| LEI_5005_BASE_CALCULO_DEVOLUCAO_COMPRAS_INTERESTADUAIS | numeric(13) |  |  | Lei 5005 - Base Cálculo Devolução Compras Interestaduais |
| LEI_5005_DEBITO_VENDAS | numeric(13) |  |  | Lei 5005 - Débito Vendas |
| LEI_5005_DEBITO_DEVOLUCAO_COMPRAS_INTERNAS | numeric(13) |  |  | Lei 5005 - Débito Devolução Compras Internas |
| LEI_5005_DEBITO_DEVOLUCAO_COMPRAS_INTERESTADUAIS | numeric(13) |  |  | Lei 5005 - Débito Devolução Compras Interestaduais |
| LEI_5005_ESTORNO_DEBITO_PARA_AJUSTAR_VALOR_ICMS | numeric(13) |  |  | Lei 5005 - Estorno de débito para ajustar o valor do ICMS próprio a recolher ao valor efetivamente recolhido no mês |
| LEI_5005_OUTROS_DEBITOS_PARA_AJUSTAR_VALOR_ICMS | numeric(13) |  |  | Lei 5005 - Outros débitos para ajustar o valor do ICMS próprio a recolher ao valor efetivamente recolhido no mês |
| LEI_5005_CANC_ESTORNO_DEB_PARA_AJUSTAR_VALOR_ICMS | numeric(13) |  |  | Lei 5005 - Cancelamento do estorno de débito realizado para ajustar o valor do ICMS a recolher ao valor efetivamente recolhido no mês |
| LEI_5005_CANC_OUTROS_DEB_PARA_AJUSTAR_VALOR_ICMS | numeric(13) |  |  | Lei 5005 - Cancelamento do lançamento de outros débitos realizado para ajustar o valor do ICMS a recolher ao valor efetivamente recolhido no mês |
| LEI_5005_BASE_CALCULO_DEVOLUCAO_VENDAS_INTERNAS | numeric(13) |  |  | Lei 5005 - Base Cálculo Devolução Vendas Internas |
| LEI_5005_BASE_CALCULO_DEVOLUCAO_VENDAS_INTERESTADUAIS | numeric(13) |  |  | Lei 5005 - Base Cálculo Devolução Vendas Interestaduais |
| LEI_5005_CREDITO_DEVOLUCAO_VENDAS_INTERNAS | numeric(13) |  |  | Lei 5005 - Crédito Devolução Vendas Internas |
| LEI_5005_CREDITO_DEVOLUCAO_VENDAS_INTERESTADUAIS | numeric(13) |  |  | Lei 5005 - Crédito Devolução Vendas Interestaduais |
| LEI_5005_BASE_CALCULO_VENDAS_INTERNA | numeric(13) |  |  | Lei 5005 - Base de cálculo vendas internas |
| LEI_5005_BASE_CALCULO_VENDAS_INTERESTADUAL | numeric(13) |  |  | Lei 5005 - Base de cálculo vendas interestaduais |
| LEI_5005_DEBITO_VENDAS_INTERNA | numeric(13) |  |  | Lei 5005 - Débito vendas internas |
| LEI_5005_DEBITO_VENDAS_INTERESTADUAL | numeric(13) |  |  | Lei 5005 - Débito vendas interestaduais |
| LEI_5005_TOTAL_VENDAS_INTERNAS_BEBIDAS_ALCOOLICAS | numeric(13) |  |  | Lei 5005 - Total Vendas Internas Bebidas Alcoólicas |
| LEI_5005_TOTAL_VENDAS_INTERESTADUAIS_12 | numeric(13) |  |  | Lei 5005 - Total Vendas Interestaduais Entrada Igual 12% |
| LEI_5005_TOTAL_VENDAS_INTERESTADUAIS_DIFERENTE_12 | numeric(13) |  |  | Lei 5005 - Total Vendas Interestaduais Entrada Diferente 12% |
| LEI_5005_PROPORCAO_VENDAS_INTERNAS_BEBIDAS_ALCOOLICAS | numeric(7) |  |  | Lei 5005 - Proporção Vendas Internas Bebidas Alcoólicas |
| LEI_5005_PROPORCAO_VENDAS_INTERESTADUAIS_12 | numeric(7) |  |  | Lei 5005 - Proporção Vendas Internas Bebidas Entrada Igual 12% |
| LEI_5005_PROPORCAO_VENDAS_INTERESTADUAIS_DIFERENTE_12 | numeric(7) |  |  | Lei 5005 - Proporção Vendas Internas Bebidas Entrada Diferente 12% |
| LEI_5005_BASE_CALCULO_COMPRAS_INTERNAS_BEBIDAS_ALCOOLICAS | numeric(13) |  |  | Lei 5005 - Base Cálculo Compras Internas Bebidas Alcoólicas |
| LEI_5005_BASE_CALCULO_COMPRAS_INTERESTADUAIS_12 | numeric(13) |  |  | Lei 5005 - Base Cálculo Compras Internas Entrada Igual 12% |
| LEI_5005_BASE_CALCULO_COMPRAS_INTERESTADUAIS_DIFERENTE_12 | numeric(13) |  |  | Lei 5005 - Base Cálculo Compras Internas Entrada Diferente 12% |
| LEI_5005_CREDITO_COMPRAS_INTERNAS_BEBIDAS_ALCOOLICAS | numeric(13) |  |  | Lei 5005 - Crédito Compras Internas Bebidas Alcoólicas |
| LEI_5005_CREDITO_COMPRAS_INTERESTADUAIS_12 | numeric(13) |  |  | Lei 5005 - Crédito Compras Internas Entrada Igual 12% |
| LEI_5005_CREDITO_COMPRAS_INTERESTADUAIS_DIFERENTE_12 | numeric(13) |  |  | Lei 5005 - Crédito Compras Internas Entrada Diferente 12% |
| LEI_5005_BASE_CALCULO_VENDAS_INTERNAS_BEBIDAS_ALCOOLICAS | numeric(13) |  |  | Lei 5005 - Base Cálculo Vendas Internas Bebidas Alcoólicas |
| LEI_5005_BASE_CALCULO_VENDAS_INTERESTADUAL_12 | numeric(13) |  |  | Lei 5005 - Base Cálculo Vendas Internas Entrada Igual 12% |
| LEI_5005_BASE_CALCULO_VENDAS_INTERESTADUAL_DIFERENTE_12 | numeric(13) |  |  | Lei 5005 - Base Cálculo Vendas Internas Entrada Diferente 12% |
| LEI_5005_DEBITO_VENDAS_INTERNAS_BEBIDAS_ALCOOLICAS | numeric(13) |  |  | Lei 5005 - Débito Vendas Internas Bebidas Alcoólicas |
| LEI_5005_DEBITO_VENDAS_INTERESTADUAL_12 | numeric(13) |  |  | Lei 5005 - Débito Vendas Internas Bebidas Entrada Igual 12% |
| LEI_5005_DEBITO_VENDAS_INTERESTADUAL_DIFERENTE_12 | numeric(13) |  |  | Lei 5005 - Débito Vendas Internas Bebidas Entrada Diferente 12% |
| LEI_5005_BASE_CALCULO_DEVOLUCAO_COMPRAS_INTERNAS_BEBIDAS_ALCOOLICAS | numeric(13) |  |  | Lei 5005 - Base Cálculo Devolução Compras Internas Bebidas Alcoólicas |
| LEI_5005_BASE_CALCULO_DEVOLUCAO_COMPRAS_INTERESTADUAIS_12 | numeric(13) |  |  | Lei 5005 - Base Cálculo Devolução Compras Internas Entrada Igual 12% |
| LEI_5005_BASE_CALCULO_DEVOLUCAO_COMPRAS_INTERESTADUAIS_DIFERENTE_12 | numeric(13) |  |  | Lei 5005 - Base Cálculo Devolução Compras Internas Entrada Diferente 12% |
| LEI_5005_DEBITO_DEVOLUCAO_COMPRAS_INTERNAS_BEBIDAS_ALCOOLICAS | numeric(13) |  |  | Lei 5005 - Débito Devolução Compras Internas Bebidas Alcoólicas |
| LEI_5005_DEBITO_DEVOLUCAO_COMPRAS_INTERESTADUAIS_12 | numeric(13) |  |  | Lei 5005 - Débito Devolução Compras Internas Entrada Igual 12% |
| LEI_5005_DEBITO_DEVOLUCAO_COMPRAS_INTERESTADUAIS_DIFERENTE_12 | numeric(13) |  |  | Lei 5005 - Débito Devolução Compras Internas Entrada Diferente 12% |
| ICMSA_ICMS_RECOLHIDO_ANTECIPADO | numeric(13) |  |  | Crédito ICMS recolhido antecipado |
| CREDITO_DEVOLUCAO_COMPRA_USO_CONSUMO_OU_IMOBILIZADO | numeric(13) |  |  | Crédito pela devolução de compra uso/consumo ou imobilizado |
| DEBITO_REGIME_ESPECIAL_FRIGORIFICOS_320D | numeric(13) |  |  | Débito Regime Especial - Frigoríficos/Abatedouros Art. 320-D do RICMS |
| ESTORNO_CREDITO_ENTRADAS_REGIME_ESPECIAL_FRIGORIFICOS_320D | numeric(13) |  |  | Est. de créd. pelas entradas Reg. Espec. - Frigoríficos/Abatedouros Art. 320-D do RICMS |
| ESTORNO_DEBITO_SAIDAS_REGIME_ESPECIAL_FRIGORIFICOS_320D | numeric(13) |  |  | Est. de débit. pelas saídas Reg. Espec. - Frigoríficos/Abatedouros Art. 320-D do RICMS |
| LEI_5005_SALDO_CREDOR_OPERACOES_INTERNAS_VI_PERIODO_SEGUINTE | numeric(13) |  |  | Lei 5005 - Saldo Credor Operações Internas VI para o período seguinte |
| LEI_5005_SALDO_CREDOR_OPERACOES_INTERNAS_BEBIDAS_ALCOOLICAS_VI2_PERIODO_SEGUINTE | numeric(13) |  |  | Lei 5005 - Saldo Credor Operações Internas Bebidas Alcoólicas VI2 para o período seguinte |
| LEI_5005_SALDO_CREDOR_OPERACOES_INTERESTADUIAS_VINT3_PERIODO_SEGUINTE | numeric(13) |  |  | Lei 5005 - Saldo Credor Operações Interestaduais VINT3 para o período seguinte |
| LEI_5005_SALDO_CREDOR_OPERACOES_INTERESTADUIAS_VINT4_PERIODO_SEGUINTE | numeric(13) |  |  | Lei 5005 - Saldo Credor Operações Interestaduais VINT4 para o período seguinte |
| LEI_5005_SALDO_CREDOR_OPERACOES_INTERESTADUIAS_VINT5_PERIODO_SEGUINTE | numeric(13) |  |  | Lei 5005 - Saldo Credor Operações Interestaduais VINT5 para o período seguinte |
| RESSARCIMENTO_ICMS_ST_ART_329_330 | numeric(13) |  |  | Restituição do ICMS ST cfe art. 329 e 330 do Decreto 18.955/1997 |
