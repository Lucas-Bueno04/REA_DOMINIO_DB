# EFSDOIMP_PIS_COFINS_DETALHAMENTO_DEBITO_DEVOLUCAO_APROVEITAMENTO — Saldo do Impostos - Detalhamentos do PIS/COFINS - Déditos - Devoluçoes - Aproveitamento
1.352 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| CODIGO_CONTRIBUICAO | integer(4) | PK |  | Código da contribuição |
| ALIQUOTA_PERCENTUAL | numeric(7) | PK |  | Valor da alíquota do imposto |
| ALIQUOTA_VALOR | numeric(13) | PK |  | Alíquota em moeda (quando o cálculo é por unidade de medida) |
| PERIODO_APURACAO | date(4) | PK |  | Período em que o dédito foi apurado |
| CODI_ENT | integer(4) | PK |  | Código da nota de entrada |
| FILIAL | integer(4) | PK |  | Filial |
| CODIGO_CONTRIBUICAO_APROVEITADO | integer(4) | PK |  | Código da contribuição aproveitada |
| ALIQUOTA_PERCENTUAL_APROVEITADO | numeric(7) | PK |  | Valor da alíquota do imposto aproveitado |
| ALIQUOTA_VALOR_APROVEITADO | numeric(13) | PK |  | Alíquota em moeda (quando o cálculo é por unidade de medida) aproveitado |
| VALOR_APROVEITADO | numeric(13) |  |  | Valor aproveitado |
| I_SCP | integer(4) | PK |  | Sequencial do SCP |
| I_RECOLHIMENTO | integer(4) | PK |  | Sequencial do Recolhimento |
| CODI_SAI | integer(4) | PK |  | Código da nota de saída |
