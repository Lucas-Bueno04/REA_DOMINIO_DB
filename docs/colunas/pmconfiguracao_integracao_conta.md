# PMCONFIGURACAO_INTEGRACAO_CONTA — Configurar Integração por Centro de Custos - Contas
14 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CONFIGURACAO | integer(4) | PK |  | Código |
| I_CENTRO_CUSTO | integer(4) | PK |  | Centro de custo |
| CONTA_CONTABIL_PATRIMONIAL | integer(4) |  |  | Conta patrimonial |
| CONTA_AQUISICAO | integer(4) |  |  | Aquisição - Conta caixa |
| HISTORICO_AQUISICAO | integer(4) |  |  | Aquisição - Histórico |
| CONTA_DEBITO_AVALIACAO | integer(4) |  |  | Avaliação - valor não recuperável - Conta débito |
| CONTA_CREDITO_AVALIACAO | integer(4) |  |  | Avaliação - valor não recuperável - Conta crédito |
| HISTORICO_AVALIACAO | integer(4) |  |  | Avaliação - valor não recuperável - Histórico |
| CONTA_DEPRECIACAO_ACUMULADA | integer(4) |  |  | Depreciação acumulada - Conta contábil |
| HISTORICO_DEPRECIACAO_ACUMULADA | integer(4) |  |  | Depreciação acumulada - Histórico |
| CONTA_DEPRECIACAO_PERIODO | integer(4) |  |  | Depreciação do período - Conta contábil |
| HISTORICO_DEPRECIACAO_PERIODO | integer(4) |  |  | Depreciação do período - Histórico |
| CONTA_BAIXA_CAIXA | integer(4) |  |  | Baixas - Conta caixa |
| CONTA_BAIXA_RECEITA_ALIENACAO | integer(4) |  |  | Baixas - Conta receita da alienação |
| HISTORICO_BAIXA_RECEITA_ALIENACAO | integer(4) |  |  | Baixas - Histórico receita da alienação |
| CONTA_BAIXA_CUSTO_ALIENACAO | integer(4) |  |  | Baixas - Conta custo da alienação |
| HISTORICO_BAIXA_CUSTO_ALIENACAO | integer(4) |  |  | Baixas - Histórico custo da alienação |
| CONTA_CREDITO_ICMS_RECUPERAR | integer(4) |  |  | Provisão do crédito de ICMS - Conta ICMS a recuperar |
| HISTORICO_CREDITO_ICMS_RECUPERAR | integer(4) |  |  | Provisão do crédito de ICMS - Histórico |
| CONTA_CREDITO_ICMS_CUSTO_PERDA | integer(4) |  |  | Estorno do crédito de ICMS - Conta custo ou perda |
| HISTORICO_CREDITO_ICMS_CUSTO_PERDA | integer(4) |  |  | Estorno do crédito de ICMS - Histórico |
| CONTA_PIS_RECUPERAR | integer(4) |  |  | Impostos a recuperar sobre valor de aquisição - PIS a recuperar |
| HISTORICO_PIS_RECUPERAR | integer(4) |  |  | Impostos a recuperar sobre valor de aquisição - Histórico PIS a recuperar |
| CONTA_COFINS_RECUPERAR | integer(4) |  |  | Impostos a recuperar sobre valor de aquisição - COFINS a recuperar |
| HISTORICO_COFINS_RECUPERAR | integer(4) |  |  | Impostos a recuperar sobre valor de aquisição - Histórico COFINS a recuperar |
| CONTA_DEBITO_AVALIACAO_AJUSTE | integer(4) |  |  | Avaliação - Ajuste de avaliação patrimonial - Conta débito |
| CONTA_CREDITO_AVALIACAO_AJUSTE | integer(4) |  |  | Avaliação - Ajuste de avaliação patrimonial - Conta crédito |
| HISTORICO_AVALIACAO_AJUSTE | integer(4) |  |  | Avaliação - Ajuste de avaliação patrimonial - Histórico |
| CONTA_DEBITO_ICMS_RECUPERAR | integer(4) |  |  | Conta débito da provisão do crédito de ICMS a recuperar |
| CONTA_DEBITO_ICMS_CUSTO_PERDA | integer(4) |  |  | Conta débito do estorno do crédito de ICMS |
| CONTA_CREDITO_ICMS_RECUPERAR_LONGO_PRAZO | integer(4) |  |  | Provisão do crédito de ICMS - Conta ICMS a recuperar - Longo Prazo |
| CONTA_DEBITO_ICMS_RECUPERAR_LONGO_PRAZO | integer(4) |  |  | Conta débito da provisão do crédito de ICMS a recuperar - Longo Prazo |
| HISTORICO_PROVISAO_CREDITO_ICMS_RECUPERAR_LONGO_PRAZO | integer(4) |  |  | Provisão do crédito de ICMS - Histórico - Longo Prazo |
| HISTORICO_TRANSFERENCIA_CREDITO_ICMS_RECUPERAR_LONGO_PRAZO | integer(4) |  |  | Transferência do crédito de ICMS - Histórico - Longo Prazo |
| SUBCONTA_DEPRECIACAO_ACUMULADA | integer(4) |  |  | Subconta - Depreciação acumulada |
| SUBCONTA_DEBITO_AVALIACAO_VALOR_JUSTO_GANHO | integer(4) |  |  | Avaliação a valor justo - Ganho - Conta Débito |
| CONTA_CREDITO_AVALIACAO_VALOR_JUSTO_GANHO | integer(4) |  |  | Avaliação a valor justo - Ganho - Conta Crédito |
| HISTORICO_AVALIACAO_VALOR_JUSTO_GANHO | integer(4) |  |  | Histórico - Avaliação a valor justo - Ganho |
| CONTA_DEBITO_AVALIACAO_VALOR_JUSTO_PERDA | integer(4) |  |  | Avaliação a valor justo - Perda - Conta Débito |
| SUBCONTA_CREDITO_AVALIACAO_VALOR_JUSTO_PERDA | integer(4) |  |  | Avaliação a valor justo - Perda - Conta Crédito |
| HISTORICO_AVALIACAO_VALOR_JUSTO_PERDA | integer(4) |  |  | Histórico - Avaliação a valor justo - Perda |
