# LRINTEGRACAO_CONTABIL_LANCTO — Integração Contábil Lalur - Lançamentos Contábeis
199 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_LANCAMENTO | integer(4) | PK |  | Sequencial |
| COMPETENCIA | date(4) |  |  | Competência |
| EMPRESA_LAN | integer(4) | PK |  | Empresa do lançamento contábil |
| NUME_LAN | integer(4) | PK |  | Número do lançamento contábil |
| FILI_LAN | integer(4) |  |  | Empresa que originou o lançamento contábil |
| CODI_LOTE | integer(4) |  |  | Código do lote |
| I_SCP | integer(4) |  | S | SCP |
