# EFSDOIMP_SUBTRI_POR_UF_PR — Saldo dos Impostos - Substituição Tributária Por PR
1.443 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| SIGLA_UF | char(2) | PK |  | Sigla da UF |
| DEBITO_ICMS_SOBRE_ESTOQUE | numeric(13) |  |  | Valor do ICMS sobre estoque - Produtos incluídos SUBTRI |
| DEBITO_FECOP_ICMS_ST | numeric(13) |  |  | Débito referente ao FECOP-PR - ICMS ST |
| DEVOLUCAO_FECOP_ICMS_ST | numeric(13) |  |  | Devolução referente ao FECOP-PR - ICMS ST |
| I_RECOLHIMENTO | integer(4) | PK |  | Recolhimento |
