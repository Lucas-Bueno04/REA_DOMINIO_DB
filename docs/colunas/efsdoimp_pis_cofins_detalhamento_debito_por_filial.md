# EFSDOIMP_PIS_COFINS_DETALHAMENTO_DEBITO_POR_FILIAL — Saldo do Impostos - Detalhamentos do PIS/COFINS - Débitos - Por filial
25.497 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| CODIGO_CONTRIBUICAO | integer(4) | PK |  | Código da contribuição |
| ALIQUOTA_PERCENTUAL | numeric(7) | PK |  | Valor da alíquota do imposto |
| ALIQUOTA_VALOR | numeric(13) | PK |  | Alíquota em moeda (quando o cálculo é por unidade de medida) |
| I_SCP | integer(4) | PK |  | Sequencial do SCP |
| I_RECOLHIMENTO | integer(4) | PK |  | Sequencial do Recolhimento |
| FILIAL | integer(4) | PK |  | Filial |
| VALOR_EXCLUSAO_GERAL_COOPERATIVA | numeric(13) |  |  | Valor de Exclusão Especifica das Cooperativas em Geral |
