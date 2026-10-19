# PMCALCULO_CREDITO_ICMS_LANCTO — Cálculo patrimonial - Crédito ICMS - Lançamentos Contábeis
4 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_LANCAMENTO | integer(4) | PK |  | Código |
| COMPETENCIA | date(4) |  |  | Competência |
| EMPRESA_LAN | integer(4) | PK |  | Empresa do lançamento contábil |
| NUME_LAN | integer(4) | PK |  | Número do lançamento contábil |
| FILI_LAN | integer(4) |  |  | Empresa que originou o lançamento contábil |
| CODI_LOTE | integer(4) |  |  | Código do lote |
