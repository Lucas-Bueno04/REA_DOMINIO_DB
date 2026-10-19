# EFSDOIMP_PIS_COFINS_DETALHAMENTO_CREDITO — Saldo do Impostos - Detalhamentos do PIS/COFINS - Créditos
2.209 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| CODIGO_CREDITO | integer(4) | PK |  | Código do crédito |
| PERIODO_APURACAO | date(4) | PK |  | Período em que o crédito foi apurado |
| BASE_CALCULO | numeric(13) |  |  | Valor da base de cálculo |
| ALIQUOTA_PERCENTUAL | numeric(7) | PK |  | Valor da alíquota do imposto |
| QUANTIDADE_BASE_CALCULO | numeric(13) |  |  | Quantidade - base de cálculo (quando o cálculo é por unidade de medida) |
| ALIQUOTA_VALOR | numeric(13) | PK |  | Alíquota em moeda (quando o cálculo é por unidade de medida) |
| VALOR_APURADO | numeric(13) |  |  | Valor do imposto apurado |
| VALOR_ACRESCIMO | numeric(13) |  |  | Valor dos ajustes de acréscimo |
| VALOR_REDUCAO | numeric(13) |  |  | Valor dos ajustes de redução |
| VALOR_DISPONIVEL | numeric(13) |  |  | Valor do crédito disponível |
| VALOR_UTILIZADO | numeric(13) |  |  | Valor do crédito utilizado no período |
| VALOR_A_TRANSPORTAR | numeric(13) |  |  | Valor do crédito a trasportar para o período seguinte |
| VALOR_DEVOLUCAO_VENDA | numeric(13) |  |  | Valor do crédito das devoluções de venda |
| VALOR_DIFERIDO | numeric(13) |  |  | Valor do crédito diferido |
| BASE_CALCULO_RECEITA_CUMULATIVA | numeric(13) |  |  | Valor da base de cálculo - Crédito vinculado Receita Cumulativa |
| QUANTIDADE_BASE_CALCULO_RECEITA_CUMULATIVA | numeric(13) |  |  | Quantidade - base de cálculo (quando o cálculo é por unidade de medida) - Crédito vinculado Receita Cumulativa |
| VALOR_REDUCAO_RECEITA_CUMULATIVA | numeric(13) |  |  | Valor dos ajustes de redução - Crédito vinculado Receita Cumulativa |
| VALOR_RESSARCIMENTO | numeric(13) |  |  | Valor do crédito de ressarcimento - Restituição, Ressarcimento e Compensação |
| VALOR_COMPENSACAO | numeric(13) |  |  | Valor do crédito do compensação - Restituição, Ressarcimento e Compensação |
| VALOR_CREDITO_NORMAL_APURADO | numeric(13) |  |  | Valor total do crédito apurado na Escrituração Fiscal Digital |
| VALOR_CREDITO_EXTEMPORANEO_APURADO | numeric(13) |  |  | Valor de Crédito Extemporâneo Apurado |
| VALOR_REDUCAO_SCP | numeric(13) |  |  | Ajuste de redução - SCP |
| I_SCP | integer(4) | PK |  | Sequencial do SCP |
| VALOR_CREDITO_PRESCRITO | numeric(13) |  |  | Créditos prescritos em decorrência do término do prazo decadencial |
| I_RECOLHIMENTO | integer(4) | PK |  | Sequencial do Recolhimento |
