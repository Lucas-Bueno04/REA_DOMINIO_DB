# efsdoimp_simples_nacional — Saldo dos Impostos - Detalhamento do Simples Nacional
31.723 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_imp | integer(4) | PK |  | Imposto |
| data_sim | date(4) | PK |  | Competencia |
| pdic_sim | integer(4) | PK |  | Periodicidade |
| filial | integer(4) | PK |  | Codigo da filial |
| anexo | tinyint(1) | PK |  | Anexo |
| secao | tinyint(1) | PK |  | Secao |
| tabela | tinyint(1) | PK |  | Tabela |
| incidencia | integer(4) |  |  | Incidencia de impostos |
| faixa | tinyint(1) |  |  | Faixa de enquadramento |
| basen | numeric(13) |  |  | Base de calculo |
| bases | numeric(13) |  |  | Base de calculo excedente do sublimite |
| basee | numeric(13) |  |  | Base de calculo excedente |
| valorn | numeric(13) |  |  | Valor do imposto |
| valors | numeric(13) |  |  | Valor do imposto excedente do sublimite |
| valore | numeric(13) |  |  | Valor do imposto do excedente |
| aliquotan | numeric(23) |  |  | Aliquota do imposto |
| aliquotas | numeric(23) |  |  | Aliquota do imposto excedente do sublimite |
| aliquotae | numeric(23) |  |  | Aliquota do imposto excedente |
| birpj | numeric(13) |  |  | Base do IRPJ |
| beirpj | numeric(13) |  |  | Base do IRPJ excedente |
| virpj | numeric(13) |  |  | Valor do IRPJ |
| veirpj | numeric(13) |  |  | Valor do IRPJ do excedente |
| airpj | numeric(23) |  |  | Aliquota do IRPJ |
| aeirpj | numeric(23) |  |  | Aliquota do IRPJ do excedente |
| bcsll | numeric(13) |  |  | Base da CSLL |
| becsll | numeric(13) |  |  | Base da CSLL excedente |
| vcsll | numeric(13) |  |  | Valor da CSLL |
| vecsll | numeric(13) |  |  | Valor da CSLL do excedente |
| acsll | numeric(23) |  |  | Aliquota da CSLL |
| aecsll | numeric(23) |  |  | Aliquota da CSLL do excedente |
| bpis | numeric(13) |  |  | Base do PIS |
| bepis | numeric(13) |  |  | Base do PIS excedente |
| vpis | numeric(13) |  |  | Valor do PIS |
| vepis | numeric(13) |  |  | Valor do PIS do excedente |
| apis | numeric(23) |  |  | Aliquota do PIS |
| aepis | numeric(23) |  |  | Aliquota do PIS do excedente |
| bcofins | numeric(13) |  |  | Base da COFINS |
| becofins | numeric(13) |  |  | Base da COFINS excedente |
| vcofins | numeric(13) |  |  | Valor do COFINS |
| vecofins | numeric(13) |  |  | Valor da COFINS do excedente |
| acofins | numeric(23) |  |  | Aliquota da COFINS |
| aecofins | numeric(23) |  |  | Aliquota da COFINS do excedente |
| binss | numeric(13) |  |  | Base do INSS |
| beinss | numeric(13) |  |  | Base do INSS excedente |
| vinss | numeric(13) |  |  | Valor do INSS |
| veinss | numeric(13) |  |  | Valor do INSS do excedente |
| ainss | numeric(23) |  |  | Aliquota do INSS |
| aeinss | numeric(23) |  |  | Aliquota do INSS do excedente |
| bipi | numeric(13) |  |  | Base do IPI |
| beipi | numeric(13) |  |  | Base do IPI excedente |
| vipi | numeric(13) |  |  | Valor do IPI |
| veipi | numeric(13) |  |  | Valor do IPI do excedente |
| aipi | numeric(23) |  |  | Aliquota do IPI |
| aeipi | numeric(23) |  |  | Aliquota do IPI do excedente |
| bicms | numeric(13) |  |  | Base do ICMS |
| beicms | numeric(13) |  |  | Base do ICMS excedente |
| vicms | numeric(13) |  |  | Valor do ICMS |
| veicms | numeric(13) |  |  | Valor do ICMS do excedente |
| aicms | numeric(23) |  |  | Aliquota do ICMS |
| aeicms | numeric(23) |  |  | Aliquota do ICMS do excedente |
| biss | numeric(13) |  |  | Base do ISS |
| beiss | numeric(13) |  |  | Base do ISS excedente |
| viss | numeric(13) |  |  | Valor do ISS |
| veiss | numeric(13) |  |  | Valor do ISS do excedente |
| aiss | numeric(23) |  |  | Aliquota do ISS |
| aeiss | numeric(23) |  |  | Aliquota do ISS do excedente |
| vissr | numeric(13) |  |  | Valor do ISS Retido |
| base_negativa | numeric(13) |  |  | Base negativa acumulada |
| arbcicms | numeric(13) | PK |  | Aliquota de reducao da base de calculo do ICMS |
| arbceicms | numeric(13) |  |  | Aliquota de reducao da base de calculo excedente do ICMS |
| arbciss | numeric(13) | PK |  | Aliquota de reducao da base de calculo do ISS |
| arbceiss | numeric(13) |  |  | Aliquota de reducao da base de calculo excedente do ISS |
| iicms | numeric(13) |  |  | Isentas de ICMS |
| iiss | numeric(13) |  |  | Isentas de ISS |
| icms_fixo | numeric(13) |  |  | Valor do ICMS fixo |
| iicms_estoque | numeric(13) |  |  | Valor de estoque deduzido da base do ICMS |
| valor_estoque | numeric(13) |  |  | Valor do estoque |
| estoque_aproveitado_anterior | numeric(13) |  |  | Valor do estoque aproveitado anterior |
| estoque_disponivel | numeric(13) |  |  | Saldo do estoque disponivel para o mes seguinte |
| estoque_aproveitado_total | numeric(13) |  |  | Valor do estoque aproveitado total |
| iss_fixo | numeric(13) |  |  | Valor do ISS fixo |
| SITUACOES | char(16) | PK |  | Situacoes fiscais |
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
| MUNICIPIO | integer(4) | PK |  | Código do município |
| FATOR_FEDERAL | numeric(13) |  |  | Fator de cálculo da base majorada |
| FATOR_ESTADUAL | numeric(13) |  |  | Fator de cálculo da majoração do sublimite |
| RECEITA_EXCEDENTE_ESTADUAL | numeric(13) |  |  | Valor de receita excedente do sublimite |
| VALOR_DEVOLUCAO_VENDA | numeric(13) |  |  | Valor de devoluções de venda |
| ARBCPIS | numeric(13) | PK |  | Alíquota de Redução de Base de Cálculo do PIS |
| ARBCCOFINS | numeric(13) | PK |  | Alíquota de Redução de Base de Cálculo do COFINS |
| ARBCEPIS | numeric(13) |  |  | Alíquota de Redução de Base de Cálculo Excedente do PIS |
| ARBCECOFINS | numeric(13) |  |  | Alíquota de Redução de Base de Cálculo Excedente do COFINS |
| TIPO_RECEITA | integer(4) | PK |  | Tipo Receita (1- Mercado Interno / 2- Exportação) |
| BASE_NEGATIVA_SECUNDARIA | numeric(13) |  |  | Base negativa secundária acumulada (utilizada para apuração por regime de caixa) |
| ANEXO_ORIGEM | integer(4) | PK |  | Anexo Origem |
| SECAO_ORIGEM | integer(4) | PK |  | Seção Origem |
| TABELA_ORIGEM | integer(4) | PK |  | Tabela Origem |
| ALIQUOTA_EFETIVA_CALCULADA | numeric(23) |  |  | Alíquota Efetiva Calculada |
| ALIQUOTA_EFETIVA_ISS_ORIGINAL | numeric(23) |  |  | Alíquota Efetiva ISS Original |
| ALIQUOTA_EFETIVA_IRPJ_ORIGINAL | numeric(23) |  |  | Alíquota Efetiva IRPJ Original |
| ALIQUOTA_EFETIVA_CSLL_ORIGINAL | numeric(23) |  |  | Alíquota Efetiva CSLL Original |
| ALIQUOTA_EFETIVA_COFINS_ORIGINAL | numeric(23) |  |  | Alíquota Efetiva COFINS Original |
| ALIQUOTA_EFETIVA_PIS_ORIGINAL | numeric(23) |  |  | Alíquota Efetiva PIS Original |
| ALIQUOTA_EFETIVA_INSS_ORIGINAL | numeric(23) |  |  | Alíquota Efetiva INSS Original |
| ALIQUOTA_EFETIVA_ICMS_ORIGINAL | numeric(23) |  |  | Alíquota Efetiva ICMS Original |
| ALIQUOTA_EFETIVA_IPI_ORIGINAL | numeric(23) |  |  | Alíquota Efetiva IPI Original |
| ALIQUOTA_EXCEDENTE_ISS | numeric(23) |  |  | Alíquota Excedente ISS |
| PERCENTUAL_DISTRIBUICAO_ISS_NO_IRPJ | numeric(23) |  |  | Percentual de Redistribuição do ISS no IRPJ |
| PERCENTUAL_DISTRIBUICAO_ISS_NO_CSLL | numeric(23) |  |  | Percentual de Redistribuição do ISS no CSLL |
| PERCENTUAL_DISTRIBUICAO_ISS_NO_COFINS | numeric(23) |  |  | Percentual de Redistribuição do ISS no COFINS |
| PERCENTUAL_DISTRIBUICAO_ISS_NO_PIS | numeric(23) |  |  | Percentual de Redistribuição do ISS no PIS |
| PERCENTUAL_DISTRIBUICAO_ISS_NO_INSS | numeric(23) |  |  | Percentual de Redistribuição do ISS no INSS |
| PERCENTUAL_DISTRIBUICAO_ISS_NO_ICMS | numeric(23) |  |  | Percentual de Redistribuição do ISS no ICMS |
| PERCENTUAL_DISTRIBUICAO_ISS_NO_IPI | numeric(23) |  |  | Percentual de Redistribuição do ISS no IPI |
| ALIQUOTA_EFETIVA_DO_CALCULO_DO_ICMS | numeric(23) |  |  | Alíquota Efetiva do Cálculo do ICMS |
| ALIQUOTA_EFETIVA_DO_CALCULO_DO_ISS | numeric(23) |  |  | Alíquota Efetiva do Cálculo do ISS |
| PERCENTUAL_PARCELA_QUE_EXCEDEU_LIMITE_SUBLIMITE | numeric(23) |  |  | Percentual Parcela que Excedeu o limite/sublimite |
| LIMITE_CALCULO_RPA_EXCEDEU | numeric(13) |  |  | Limite/SubLimite para o cálculo da Parcela que excedeu |
| ALIQUOTA_EFETIVA_EXCEDENTE_CALCULADA | numeric(23) |  |  | Alíquota Efetiva Excedente Calculada |
| ALIQUOTA_EFETIVA_ISS_EXCEDENTE_ORIGINAL | numeric(23) |  |  | Alíquota Efetiva ISS Excedente Original |
| ALIQUOTA_EFETIVA_IRPJ_EXCEDENTE_ORIGINAL | numeric(23) |  |  | Alíquota Efetiva IRPJ Excedente Original |
| ALIQUOTA_EFETIVA_CSLL_EXCEDENTE_ORIGINAL | numeric(23) |  |  | Alíquota Efetiva CSLL Excedente Original |
| ALIQUOTA_EFETIVA_COFINS_EXCEDENTE_ORIGINAL | numeric(23) |  |  | Alíquota Efetiva COFINS Excedente Original |
| ALIQUOTA_EFETIVA_PIS_EXCEDENTE_ORIGINAL | numeric(23) |  |  | Alíquota Efetiva PIS Excedente Original |
| ALIQUOTA_EFETIVA_INSS_EXCEDENTE_ORIGINAL | numeric(23) |  |  | Alíquota Efetiva INSS Excedente Original |
| ALIQUOTA_EFETIVA_ICMS_EXCEDENTE_ORIGINAL | numeric(23) |  |  | Alíquota Efetiva ICMS Excedente Original |
| ALIQUOTA_EFETIVA_IPI_EXCEDENTE_ORIGINAL | numeric(23) |  |  | Alíquota Efetiva IPI Excedente Original |
| ALIQUOTA_EXCEDENTE_ISS_EXCEDENTE | numeric(23) |  |  | Alíquota Excedente ISS Excedente |
| PERCENTUAL_DISTRIBUICAO_ISS_NO_IRPJ_EXCEDENTE | numeric(23) |  |  | Percentual de Redistribuição do ISS no IRPJ Excedente |
| PERCENTUAL_DISTRIBUICAO_ISS_NO_CSLL_EXCEDENTE | numeric(23) |  |  | Percentual de Redistribuição do ISS no CSLL Excedente |
| PERCENTUAL_DISTRIBUICAO_ISS_NO_COFINS_EXCEDENTE | numeric(23) |  |  | Percentual de Redistribuição do ISS no COFINS Excedente |
| PERCENTUAL_DISTRIBUICAO_ISS_NO_PIS_EXCEDENTE | numeric(23) |  |  | Percentual de Redistribuição do ISS no PIS Excedente |
| PERCENTUAL_DISTRIBUICAO_ISS_NO_INSS_EXCEDENTE | numeric(23) |  |  | Percentual de Redistribuição do ISS no INSS Excedente |
| PERCENTUAL_DISTRIBUICAO_ISS_NO_ICMS_EXCEDENTE | numeric(23) |  |  | Percentual de Redistribuição do ISS no ICMS Excedente |
| PERCENTUAL_DISTRIBUICAO_ISS_NO_IPI_EXCEDENTE | numeric(23) |  |  | Percentual de Redistribuição do ISS no IPI Excedente |
| ALIQUOTA_EFETIVA_DO_CALCULO_DO_ICMS_EXCEDENTE | numeric(23) |  |  | Alíquota Efetiva do Cálculo do ICMS Excedente |
| ALIQUOTA_EFETIVA_DO_CALCULO_DO_ISS_EXCEDENTE | numeric(23) |  |  | Alíquota Efetiva do Cálculo do ISS Excedente |
| ALIQUOTA_EFETIVA_ICMS_ESTADUAL | numeric(23) |  |  | Alíquota Efetiva do ICMS Estadual |
| ALIQUOTA_EFETIVA_ICMS_ESTADUAL_EXCEDENTE | numeric(23) |  |  | Alíquota Efetiva do ICMS Estadual Excedente |
| ALIQUOTA_EFETIVA_ISS_SEM_REDUCAO | numeric(23) |  |  | Alíquota Efetiva do Cálculo do ISS Sem redução |
| ALIQUOTA_EFETIVA_ISS_EXCEDENTE_SEM_REDUCAO | numeric(23) |  |  | Alíquota Efetiva do Cálculo do ISS Excedente Sem redução |
| DEDUCAO_EMISSORAS_RADIO_TV | char(1) |  |  | Dedução para Emissoras de Rádio e Televisão pela Cessão do Horário Gratuito |
| PERCENTUAL_PARCELA_QUE_EXCEDEU_LIMITE_SUBLIMITE_ICMS_ISS | numeric(23) |  |  | Percentual Parcela que Excedeu o limite/sublimite ICMS/ISS |
| LIMITE_CALCULO_RPA_EXCEDEU_ICMS_ISS | numeric(13) |  |  | Limite/SubLimite para o cálculo da Parcela que excedeu ICMS/ISS |
| VALOR_COFINS_ISS_DISTRIBUICAO | numeric(13) |  |  | Valor do COFINS com o percentual de ISS redistribuido (quando não junto ao valor original) |
| VALOR_CSLL_ISS_DISTRIBUICAO | numeric(13) |  |  | Valor do CSLL com o percentual de ISS redistribuido (quando não junto ao valor original) |
| VALOR_INSS_ISS_DISTRIBUICAO | numeric(13) |  |  | Valor do INSS com o percentual de ISS redistribuido (quando não junto ao valor original) |
| VALOR_IPI_ISS_DISTRIBUICAO | numeric(13) |  |  | Valor do IPI com o percentual de ISS redistribuido (quando não junto ao valor original) |
| VALOR_IRPJ_ISS_DISTRIBUICAO | numeric(13) |  |  | Valor do IRPJ com o percentual de ISS redistribuido (quando não junto ao valor original) |
| VALOR_PIS_ISS_DISTRIBUICAO | numeric(13) |  |  | Valor do PIS com o percentual de ISS redistribuido (quando não junto ao valor original) |
| VALOR_COFINS_EXCEDENTE_ISS_DISTRIBUICAO | numeric(13) |  |  | Valor do COFINS com o percentual de ISS redistribuido (quando não junto ao valor original) |
| VALOR_CSLL_EXCEDENTE_ISS_DISTRIBUICAO | numeric(13) |  |  | Valor do CSLL com o percentual de ISS redistribuido (quando não junto ao valor original) |
| VALOR_INSS_EXCEDENTE_ISS_DISTRIBUICAO | numeric(13) |  |  | Valor do INSS com o percentual de ISS redistribuido (quando não junto ao valor original) |
| VALOR_IPI_EXCEDENTE_ISS_DISTRIBUICAO | numeric(13) |  |  | Valor do IPI com o percentual de ISS redistribuido (quando não junto ao valor original) |
| VALOR_IRPJ_EXCEDENTE_ISS_DISTRIBUICAO | numeric(13) |  |  | Valor do IRPJ com o percentual de ISS redistribuido (quando não junto ao valor original) |
| VALOR_PIS_EXCEDENTE_ISS_DISTRIBUICAO | numeric(13) |  |  | Valor do PIS com o percentual de ISS redistribuido (quando não junto ao valor original) |
| APLICA_REDUCAO_BASE_CALCULO_ICMS | char(1) | PK |  | Aplica redução na base de calculo do ICMS |
| ULTRAPASSOU_SUBLIMITE_EM_MENOS_20_PORCENTO | char(1) |  |  | Ultrapassou sublimite em menos de 20% |
| APLICA_REDUCAO_ISS | char(1) | PK |  | Redução do ISS aplicado na Alíquota ou na Base de Calculo |
| PARCELA_RECEITA_SEM_DEDUCAO_ISS | numeric(13) |  |  | Parcela receita sem dedução do ISS |
| PARCELA_RECEITA_COM_DEDUCAO_ISS | numeric(13) |  |  | Parcela receita com dedução do ISS |
| VALOR_COFINS_SEM_DEDUCAO_ISS | numeric(13) |  |  | Valor do COFINS sem dedução ISS |
| VALOR_CSLL_SEM_DEDUCAO_ISS | numeric(13) |  |  | Valor do CSLL sem dedução ISS |
| VALOR_INSS_SEM_DEDUCAO_ISS | numeric(13) |  |  | Valor do INSS sem dedução ISS |
| VALOR_IPI_SEM_DEDUCAO_ISS | numeric(13) |  |  | Valor do IPI sem dedução ISS |
| VALOR_IRPJ_SEM_DEDUCAO_ISS | numeric(13) |  |  | Valor do IRPJ sem dedução ISS |
| VALOR_PIS_SEM_DEDUCAO_ISS | numeric(13) |  |  | Valor do PIS sem dedução ISS |
| VALOR_COFINS_COM_DEDUCAO_ISS | numeric(13) |  |  | Valor do COFINS com dedução ISS |
| VALOR_CSLL_COM_DEDUCAO_ISS | numeric(13) |  |  | Valor do CSLL com dedução ISS |
| VALOR_INSS_COM_DEDUCAO_ISS | numeric(13) |  |  | Valor do INSS com dedução ISS |
| VALOR_IPI_COM_DEDUCAO_ISS | numeric(13) |  |  | Valor do IPI com dedução ISS |
| VALOR_IRPJ_COM_DEDUCAO_ISS | numeric(13) |  |  | Valor do IRPJ com dedução ISS |
| VALOR_PIS_COM_DEDUCAO_ISS | numeric(13) |  |  | Valor do PIS com dedução ISS |
