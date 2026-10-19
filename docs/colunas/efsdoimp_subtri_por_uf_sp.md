# EFSDOIMP_SUBTRI_POR_UF_SP — Saldo dos Impostos - Substituição Tributária Por SP
473.587 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| SIGLA_UF | char(2) | PK |  | Sigla da UF |
| DEBITO_ICMS_SOBRE_ESTOQUE | numeric(13) |  |  | Débito ICMS Sobre Estoque |
| OUTRO_CREDITO_TRANSF_ICMS_ST_FECOEP | numeric(13) |  |  | Transferência do ICMS ST devido ao FECOEP para apuração específica |
| I_RECOLHIMENTO | integer(4) | PK |  | Recolhimento |
| ESTORNO_DEBITO_SUBITEM_1499 | numeric(13) |  |  | Estorno de débitos de ajuste do subitem 1499 |
