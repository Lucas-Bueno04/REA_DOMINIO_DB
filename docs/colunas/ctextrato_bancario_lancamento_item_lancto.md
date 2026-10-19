# CTEXTRATO_BANCARIO_LANCAMENTO_ITEM_LANCTO — Lançamento de extrato bancário - lançamentos contábeis
19.292 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_LANCAMENTO | integer(4) | PK |  | Código extrato |
| I_ITEM | integer(4) | PK |  | Sequencial do item |
| NUME_LAN | integer(4) | PK |  | Número do lançamento contábil |
| CODI_LOTE | integer(4) |  |  | Código do lote |
| TIPO | tinyint(1) |  |  | Tipo de lançamento (0=Sistema/ 1=Manual) |
