# CTBAKLANCTOLOTE — Lançamento em lote eliminados
39.403 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_LOTE | integer(4) | PK |  | Codigo |
| TIPO | char(1) |  |  | Tipo (D=Um debito para varios creditos/C=Um credito para varios debitos/X=Um debito para um credito/V=Varios debitos para varios creditos) |
| CODI_PAD | integer(4) |  | S | Lancamento padrao |
