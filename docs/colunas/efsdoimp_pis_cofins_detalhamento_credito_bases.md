# EFSDOIMP_PIS_COFINS_DETALHAMENTO_CREDITO_BASES — Saldo do Impostos - Detalhamentos do PIS/COFINS - Créditos - Bases do imposto
1.551 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| CODIGO_CREDITO | integer(4) | PK |  | Código do crédito |
| PERIODO_APURACAO | date(4) | PK |  | Período em que o crédito foi apurado |
| ALIQUOTA_PERCENTUAL | numeric(7) | PK |  | Valor da alíquota do imposto |
| ALIQUOTA_VALOR | numeric(13) | PK |  | Alíquota em moeda (quando o cálculo é por unidade de medida) |
| NATUREZA_BASE_CREDITO | integer(4) | PK |  | Natureza da base de cálculo do crédito |
| CST | integer(4) | PK |  | CST vinculado ao crédito |
| BASE_TOTAL | numeric(13) |  |  | Base de cálculo total |
| BASE_CUMULATIVA | numeric(13) |  |  | Base de cálculo cumulativa |
| BASE_NAO_CUMULATIVA | numeric(13) |  |  | Base de cálculo não cumulativa |
| BASE_VINCULADA | numeric(13) |  |  | Base de cálculo vinculada a receita |
| QUANTIDADE_BASE_CALCULO | numeric(13) |  |  | Base de cálculo total (quando o cálculo é por unidade de medida) |
| QUANTIDADE_BASE_CALCULO_VINCULADO | numeric(13) |  |  | Base de cálculo vinculada (quando o cálculo é por unidade de medida) |
| I_SCP | integer(4) | PK |  | Sequencial do SCP |
| I_RECOLHIMENTO | integer(4) | PK |  | Sequencial do Recolhimento |
