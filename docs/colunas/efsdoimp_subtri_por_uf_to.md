# EFSDOIMP_SUBTRI_POR_UF_TO — Saldo dos Impostos - Substituição Tributária Por TO
3 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| SIGLA_UF | char(2) | PK |  | Sigla da UF |
| I_RECOLHIMENTO | integer(4) | PK |  | Recolhimento |
| SALDO_INFERIOR_QUANT_MINIMA_RECOLHIMENTO | numeric(13) |  |  | Saldo inferior a quantidade mínima de recolhimento |
| SALDO_ANT_INFERIOR_QUANT_MINIMA_RECOLHIMENTO | numeric(13) |  |  | Saldo de período anterior inferior a quantidade mínima de recolhimento |
