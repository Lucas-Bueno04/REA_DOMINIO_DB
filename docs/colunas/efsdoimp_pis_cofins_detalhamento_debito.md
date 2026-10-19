# EFSDOIMP_PIS_COFINS_DETALHAMENTO_DEBITO — Saldo do Impostos - Detalhamentos do PIS/COFINS - Débitos
29.018 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| CODIGO_CONTRIBUICAO | integer(4) | PK |  | Código da contribuição |
| RECEITA_BRUTA | numeric(13) |  |  | Valor da receita bruta |
| BASE_CALCULO | numeric(13) |  |  | Valor da base de cálculo |
| ALIQUOTA_PERCENTUAL | numeric(7) | PK |  | Valor da alíquota do imposto |
| QUANTIDADE_BASE_CALCULO | numeric(13) |  |  | Quantidade - base de cálculo (quando o cálculo é por unidade de medida) |
| ALIQUOTA_VALOR | numeric(13) | PK |  | Alíquota em moeda (quando o cálculo é por unidade de medida) |
| VALOR_APURADO | numeric(13) |  |  | Valor do imposto apurado |
| VALOR_ACRESCIMO | numeric(13) |  |  | Valor dos ajustes de acréscimo |
| VALOR_REDUCAO | numeric(13) |  |  | Valor dos ajustes de redução |
| VALOR_CONTRIBUICAO | numeric(13) |  |  | Valor do imposto a pagar no período |
| VALOR_CONTABIL | numeric(13) |  |  | Valor contábil |
| TIPO_SOCIEDADE_COOPERATIVA | tinyint(1) |  |  | Indicador do Tipo de Sociedade Cooperativa |
| BASE_CALCULO_ANTES_EXCLUSAO_COOPERATIVA | numeric(13) |  |  | Valor da Base de Cálculo da Contribuição antes das Exclusões das Cooperativas |
| VALOR_EXCLUSAO_GERAL_COOPERATIVA | numeric(13) |  |  | Valor de Exclusão Especifica das Cooperativas em Geral |
| VALOR_EXCLUSAO_ESPECIFICA_COOPERATIVA | numeric(13) |  |  | Valor das Exclusões da Base de Cálculo Especifica do Tipo da Sociedade Cooperativa |
| BASE_CALCULO_COOPERATIVA | numeric(13) |  |  | Valor da Base de Cálculo, Após as Exclusões Especificas da Sociedade Cooperativa |
| VALOR_DIFERIDO | numeric(13) |  |  | Valor da contribuição diferida |
| VALOR_DIFERIDO_ANTERIOR | numeric(13) |  |  | Valor da contribuição diferida em períodos anteriores |
| VALOR_DEVOLUCAO | numeric(13) |  |  | Valor da devolução |
| VALOR_REDUCAO_SCP | numeric(13) |  |  | Ajuste de redução - SCP |
| I_SCP | integer(4) | PK |  | Sequencial do SCP |
| I_RECOLHIMENTO | integer(4) | PK |  | Sequencial do Recolhimento |
| VALOR_CREDITO_PRESUMIDO_BEBIDA_FRIA_13097 | numeric(13) |  |  | Crédito Presumido na aquisição de bebidas frias - Art. 31 da Lei 13.097/2015 |
| BASE_DEVOLUCAO_CREDITO_PRESUMIDO_ALCOOL_12859 | numeric(13) |  |  | Base de cálculo da Devolução em período diferente do Crédito presumido importador ou produtor de álcool - Lei 12.859/2013 |
| VALOR_DEVOLUCAO_CREDITO_PRESUMIDO_ALCOOL_12859 | numeric(13) |  |  | Devolução em período diferente do Crédito presumido importador ou produtor de álcool - Lei 12.859/2013 |
| VALOR_PRODUTO | numeric(13) |  |  | Valor Total do Produto |
| BASE_CALCULO_DEVOLUCAO_CFE | numeric(13) |  |  | Base de cálculo da devolução da CFE |
| QUANTIDADE_BASE_CALCULO_DEVOLUCAO_CFE | numeric(13) |  |  | Quantidade - base de cálculo da devolução da CFE (quando o cálculo é por unidade de medida) |
| VALOR_APURADO_DEVOLUCAO_CFE | numeric(13) |  |  | Valor do imposto apurado da devolucao da CFE |
| VALOR_DEVOLUCAO_CUSTO_INCORRIDO | numeric(13) |  |  | Estorno de créditos - Devolução Custo Incorrido |
| VALOR_REDUCAO_RESCISAO_CONTRATO_IMOBILIARIO | numeric(13) |  |  | Valor redução recisão contrato imobiliário |
| VALOR_AJUSTE_ACRESCIMO_BASE_CALCULO | numeric(13) |  |  | Valor ajuste de acrécimo na base de cálculo |
| VALOR_AJUSTE_REDUCAO_BASE_CALCULO | numeric(13) |  |  | Valor ajuste de redução na base de cálculo |
| BASE_CALCULO_DEVOLUCAO | numeric(13) |  |  | Valor Base Calculo Devolução |
| VALOR_FRETE_SEGURO_DESPESAS_ACESSORIAS_SAIDA | numeric(13) |  |  | Valor frete, seguro e despesas acessórias - Saída |
| BASE_CALCULO_DEVOLUCAO_CTE | numeric(13) |  |  | Base de cálculo da devolução de CTE |
| VALOR_PIS_DEVOLUCAO_CTE | numeric(13) |  |  | Valor PIS da devolução de CTE |
| VALOR_COFINS_DEVOLUCAO_CTE | numeric(13) |  |  | Valor COFINS da devolução de CTE |
