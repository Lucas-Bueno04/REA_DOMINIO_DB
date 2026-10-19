# EFSDOIMP_SUBTRI_POR_UF_PI — Saldo dos Impostos - Substituição Tributária Por PI
65 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| SIGLA_UF | char(2) | PK |  | Sigla da UF |
| ADICIONAL_FECOP | numeric(13) |  |  | Adicional FECOP - ICMS ST - Saídas Internas |
| I_RECOLHIMENTO | integer(4) | PK |  | Recolhimento |
