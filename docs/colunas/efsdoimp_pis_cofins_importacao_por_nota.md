# EFSDOIMP_PIS_COFINS_IMPORTACAO_POR_NOTA — Saldo dos Impostos - PIS/COFINS Importação - Por Nota - Backup
209 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| CODIGO_NOTA | integer(4) | PK |  | Código da nota |
| EMPRESA_NOTA | integer(4) | PK |  | Empresa da nota |
| VALOR_RECOLHER | numeric(13) |  |  | Saldo a recolher |
| VALOR_CONTABIL | numeric(13) |  |  | Valor contábil |
| BASE_CALCULO | numeric(13) |  |  | Base de cálculo |
| VALOR_IMPOSTO | numeric(13) |  |  | Valor do imposto |
| PARCELA | integer(4) |  |  | Parcela |
| VALOR_PAGO | numeric(13) |  |  | Valor pago |
| DATA_VENCIMENTO | date(4) |  |  | Data do vencimento |
