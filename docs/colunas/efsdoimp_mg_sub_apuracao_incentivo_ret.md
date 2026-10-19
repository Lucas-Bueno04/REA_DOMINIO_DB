# EFSDOIMP_MG_SUB_APURACAO_INCENTIVO_RET — Saldo dos Impostos - Sub Apuração MG - Incentivo RET
34 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| I_SUB_APURACAO | integer(4) | PK |  | Sequencial sub apuração |
| I_SUB_APURACAO_CONSULTA_APURACAO | integer(4) | PK |  | Sequencial sub apuração (0-Apuração normal/1-N-sub apuração) |
| I_SEQUENCIAL_INCENTIVO | integer(4) | PK |  | Sequencial incentivo |
| E_PTA_RE | char(15) |  |  | E-PTA-RE nº |
| CREDITO_DEVOLUCAO_MERCADORIA_CRED_PRES_RET | numeric(13) |  |  | Crédito da devolução de merc. com crédito presumido - RET e-PTA |
| CREDITO_VINCULADO_OP_ALCANCADA_CRED_PRES_NORM_RET | numeric(13) |  |  | Crédito vinculado à ope. alcançada pelo crédito presumido - RET e-PTA (Cálculo normal) |
| ESTORNO_DEVOLUCAO_MERCADORIA_ALCANCADA_CRED_PRES_RET | numeric(13) |  |  | Estorno ref. devolução de merc. com crédito presumido - RET e-PTA |
| CREDITO_PRESUMIDO_RET | numeric(13) |  |  | Crédito presumido - RET e-PTA |
