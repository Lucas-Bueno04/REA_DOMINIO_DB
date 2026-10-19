# EFDARF_IRRF — DARF IRRF Por Nota
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| CODIGO_NOTA | integer(4) | PK |  | Sequencial da nota |
| I_RECOLHIMENTO | integer(4) | PK |  | Sequencial do recolhimento |
| VALOR_IMPOSTO | numeric(13) |  |  | Valor do imposto |
| DEDUCAO | numeric(13) |  |  | Valor da dedução |
| DIFERIDO | numeric(13) |  |  | Valor diferido |
| VALOR_RECOLHER | numeric(13) |  |  | Valor a recolher |
| EMITIDO | char(1) |  |  | Emitido(S/N) |
