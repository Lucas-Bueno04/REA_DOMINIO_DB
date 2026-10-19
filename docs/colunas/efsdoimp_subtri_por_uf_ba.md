# EFSDOIMP_SUBTRI_POR_UF_BA — Saldo dos Impostos - Substituição Tributária Por BA
344 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| SIGLA_UF | char(2) | PK |  | Sigla da UF |
| ESTORNO_FUNCEP | numeric(13) |  |  | Estorno FUNCEP |
| I_RECOLHIMENTO | integer(4) | PK |  | Recolhimento |
