# EFSDOIMP_SUBTRI_POR_UF_DF — Saldo dos Impostos - Substituição Tributária Por DF
28 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| SIGLA_UF | char(2) | PK |  | Sigla da UF |
| DEBITO_ICMS_SOBRE_ESTOQUE | numeric(13) |  |  | Debito ICMS Sobre Estoque |
| REDUCAO_DEBITO_FECOP | numeric(13) |  |  | Redução Debito FECOP |
| I_RECOLHIMENTO | integer(4) | PK |  | Recolhimento |
| FECOP_ST_DEVOLUCAO_VENDAS_INTERNAS | numeric(13) |  |  | FECOP ST sobre devolução de vendas internas |
| REDUCAO_CREDITO_FECOP | numeric(13) |  |  | Redução de créditos - Fundo de combate a pobreza |
