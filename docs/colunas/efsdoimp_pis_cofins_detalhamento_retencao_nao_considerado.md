# EFSDOIMP_PIS_COFINS_DETALHAMENTO_RETENCAO_NAO_CONSIDERADO — Saldo do Impostos - Detalhamentos do PIS/COFINS - Retencoes não consideradas
4 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| NATUREZA_RETENCAO | integer(4) | PK |  | Natureza da retencao |
| PERIODO_APURACAO | date(4) | PK |  | Periodo de apuracao da retencao |
| I_SCP | integer(4) | PK |  | Sequencial do SCP |
| I_RECOLHIMENTO | integer(4) | PK |  | Sequencial do Recolhimento |
| VALOR_DISPONIVEL | numeric(13) |  |  | Valor disponivel |
| VALOR_UTILIZADO | numeric(13) |  |  | Valor utilizado |
| VALOR_A_TRANSPORTAR | numeric(13) |  |  | Valor transportar |
