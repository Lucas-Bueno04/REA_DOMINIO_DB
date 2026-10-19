# EFSDOIMP_SUBTRI_POR_UF_ES — Saldo dos Impostos - Substituição Tributária Por ES
61 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| SIGLA_UF | char(2) | PK |  | Sigla da UF |
| I_RECOLHIMENTO | integer(4) | PK |  | Recolhimento |
| ADICIONAL_FUNCOP | numeric(13) |  |  | Adicional FUNCOP - ICMS ST - Saídas Internas |
