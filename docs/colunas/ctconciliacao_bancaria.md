# CTCONCILIACAO_BANCARIA — Conciliação bancária
9.625 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CONCILIACAO | integer(4) | PK |  | Código |
| I_LANCAMENTO | integer(4) |  | S | Código do lançamento de extrato |
| I_ITEM | integer(4) |  | S | Código do lançamento de extrato - sequencial do item |
| NUME_LAN | integer(4) |  | S | Número do lançamento contábil |
| CONCILIADO_DEB | char(1) |  |  | Conciliado a débito (S/N) |
| CONCILIADO_CRE | char(1) |  |  | Conciliado a crédito (S/N) |
| I_CONCILIACAO_ITEM | integer(4) | PK |  | Sequencial da conciliação |
