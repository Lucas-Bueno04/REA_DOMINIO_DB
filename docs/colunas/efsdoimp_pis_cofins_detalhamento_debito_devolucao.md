# EFSDOIMP_PIS_COFINS_DETALHAMENTO_DEBITO_DEVOLUCAO — Saldo do Impostos - Detalhamentos do PIS/COFINS - Déditos - Devoluçoes
1.786 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| CODIGO_CONTRIBUICAO | integer(4) | PK |  | Código da contribuição |
| ALIQUOTA_PERCENTUAL | numeric(7) | PK |  | Valor da alíquota do imposto |
| BASE_CALCULO | numeric(13) |  |  | Valor base de cálculo |
| ALIQUOTA_VALOR | numeric(13) | PK |  | Alíquota em moeda (quando o cálculo é por unidade de medida) |
| QUANTIDADE_BASE_CALCULO | numeric(13) |  |  | Quantidade - base de cálculo (quando o cálculo é por unidade de medida) |
| PERIODO_APURACAO | date(4) | PK |  | Período em que o dédito foi apurado |
| CODI_ENT | integer(4) | PK |  | Código da nota de entrada |
| FILIAL | integer(4) | PK |  | Filial |
| VALOR | numeric(13) |  |  | Valor do imposto |
| VALOR_DISPONIVEL_ANTERIOR | numeric(13) |  |  | Valor disponível em período anterior |
| VALOR_DISPONIVEL | numeric(13) |  |  | Valor disponível no período |
| VALOR_UTILIZADO | numeric(13) |  |  | Valor utilizado no período |
| VALOR_A_TRANSPORTAR | numeric(13) |  |  | Valor a transportar para o período seguinte |
| I_SCP | integer(4) | PK |  | Sequencial do SCP |
| I_RECOLHIMENTO | integer(4) | PK |  | Sequencial do Recolhimento |
| CODI_SAI | integer(4) | PK |  | Código da nota de saída |
