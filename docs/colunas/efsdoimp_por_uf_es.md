# EFSDOIMP_POR_UF_ES — Saldo dos Impostos - Por UF - RS
5 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| SIGLA_UF | char(2) | PK |  | Sigla da UF |
| ESTORNO_DEBITOS_LANCADO | numeric(13) |  |  | Estorno Débitos - Lançados |
