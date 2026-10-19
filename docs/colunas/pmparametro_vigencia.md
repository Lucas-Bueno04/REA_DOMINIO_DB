# PMPARAMETRO_VIGENCIA — Parâmetros - Patrimônio - Vigência
824 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| VIGENCIA | date(4) | PK |  | Vigência |
| DESCRICAO | varchar(80) |  |  | Descrição |
| CALCULAR_CREDITO_ICMS | char(1) |  |  | Calcular crédito de ICMS (S/N) |
| GERAR_CREDITO_ICMS_SPED_FISCAL | char(1) |  |  | Gerar informações de crédito de ICMS para o SPED Fiscal (S/N) |
| CALCULAR_CONFORME_PRO_RATA_DIE | char(1) |  |  | Calcular conforme Pro Rata Die (S/N) |
| UTILIZAR_INDEXADOR | char(1) |  |  | Utilizar indexador (S/N) |
| I_INDICE_CREDITO_ICMS | integer(4) |  | S | Código do índice do crédito de ICMS |
| PERIODICIDADE_CREDITO_ICMS | char(1) |  |  | Priodicidade (M=Mensal/ Q=Quinzenal) |
| CALCULAR_DEBITO_ICMS_IMPORTACAO | char(1) |  |  | Calcular débito de ICMS - Importação (S/N) |
| DEBITO_ICMS_CODIGO_AJUSTE | integer(4) |  | S | Calcular débito de ICMS - Importação - Código do ajuste na Escrita Fiscal |
| CALCULAR_CREDITO_PISCOFINS_DEPRECIACAO | char(1) |  |  | Calcular crédito de PIS/COFINS sobre depreciação (S/N) |
| CALCULAR_CREDITO_PISCOFINS_AQUISICAO | char(1) |  |  | Calcular crédito de PIS/COFINS sobre valor de aquisição (S/N) |
| CALCULAR_CREDITO_PISCOFINS_AQUISICAO_MP | char(1) |  |  | Calcular crédito de PIS/COFINS sobre valor de aquisição conforme MP 540/11 (S/N) |
| INTEGRAR_GANHOS_CAPITAL_IRPJ | char(1) |  |  | Integrar o valor dos ganhos de capital para cálculo do IRPJ (S/N) |
| INTEGRAR_GANHOS_CAPITAL_CSLL | char(1) |  |  | Integrar o valor dos ganhos de capital para cálculo da Contribuição Social (S/N) |
| GANHOS_CAPITAL_CODIGO_ACUMULADOR | integer(4) |  | S | Ganho de Capital - Código do acumulador |
| I_INDICE_DEBITO_ICMS_IMPORTACAO | integer(4) |  | S | Índice Débito de ICMS Importação |
| DEDUZIR_VALOR_CREDITO_ICMS_DO_PIS_COFINS | char(1) |  |  | Deduzir o valor total do crÃ©dito de ICMS da base de cÃ¡lculo do crÃ©dito de PIS e COFINS |
| POSSUI_CODIGO_RECOLHIMENTO_PIS_COFINS | char(1) |  |  | Possui mais de um código de recolhimento para os impostos PIS e COFINS |
| INFORMAR_CODIGO_RECOLHIMENTO_PIS_COFINS | char(1) |  |  | Informar código de recolhimento |
| CODIGO_RECOLHIMENTO_PIS | varchar(6) |  | S | Código de recolhimento PIS |
| CODIGO_RECOLHIMENTO_COFINS | varchar(6) |  | S | Código de recolhimento COFINS |
| CONSIDERAR_VALOR_DIAS_ANTERIORES_AQUISICAO_VALOR_NAO_CREDITAVEL | varchar(1) |  |  | Considerar o valor dos dias anteriores a data de aquisição dos bens como valor não creditável |
| REALIZAR_LANCAMENTO_TRANSFERENCIA_PARCELAS_LONGO_PRAZO_ICMS | varchar(1) |  |  | Realizar o lançamento de transferência das parcelas do longo prazo para o curto prazo na integração contábil |
| CONSIDERAR_ICMS_CALCULADO_COMPETENCIA_BAIXA_BENS | char(1) |  |  | Não considerar como calculado o crédito de ICMS na competência da baixa dos bens |
| PERIODO_CURTO_PRAZO | char(1) |  |  | T-Até o término do exercício seguinte a data de aquisição do bem/A-12 meses a partir da data de aquisição do bem |
| CALCULAR_DEBITO_ICMS_DIFERENCIAL_ALIQUOTA | char(1) |  |  | Calcular débito de ICMS - Diferencial de alíquota(S/N) |
| DEBITO_ICMS_CODIGO_AJUSTE_DIFERENCIAL_ALIQUOTA | integer(4) |  | S | Calcular débito de ICMS - Diferencial de alíquota - Código do ajuste na Escrita Fiscal |
| POSTERGAR_PARCELA_ICMS_SEM_SAIDAS_LANCADAS | char(1) |  |  | Postergar parcela mensal do crédito de ICMS |
| CALCULAR_CREDITO_PISCOFINS_AQUISICAO_BAIXA_PARCIAL | char(1) |  |  | Calcular crÃ©dito de PIS/COFINS sobre valor de aquisiÃ§Ã£o com baixa parcial(S/N) |
| DEDUZIR_PARCELA_CREDITO_ICMS_DO_PIS_COFINS | char(1) |  | S | Deduzir parcela do crédito de ICMS da base de cálculo do crédito de PIS e COFINS sobre a depreciação |
| DEDUZIR_PARCELA_ICMS_NAO_RECUPERAVEL_PIS_COFINS | char(1) |  | S | Deduzir parcela do ICMS Não Recuperável da base de cálculo do crédito de PIS e COFINS sobre a depreciação |
