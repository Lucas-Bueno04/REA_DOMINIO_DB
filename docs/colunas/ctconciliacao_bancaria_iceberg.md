# CTCONCILIACAO_BANCARIA_ICEBERG — Conciliação bancária automática Contabilidade Digital
5 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_CONCILIACAO | integer(4) | PK |  | Código da conciliação |
| I_CONCILIACAO_ITEM | integer(4) | PK |  | Item da conciliação |
| I_EXTRATO_BANCARIO | integer(4) |  | S | Código do extrato bancário |
| NUME_LAN | integer(4) |  | S | Número do lançamento |
| CONCILIADO_DEB | char(1) |  |  | Conciliado débito (S/N) |
| CONCILIADO_CRE | char(1) |  |  | Conciliado crédito (S/N) |
