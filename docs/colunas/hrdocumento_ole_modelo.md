# HRDOCUMENTO_OLE_MODELO — Modelos de documentos OLEs
19 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_MODELO | integer(4) | PK |  | Codigo |
| I_TIPO | integer(4) | PK |  | Tipo |
| DESCRICAO | varchar(100) |  |  | Descricao |
| PADRAO | char(10) |  | S | Codigo padrao |
| OLE | long binary(32767) |  | S | Definicao do OLE |
| EDITOR | integer(4) |  | S | 1- Office, 2-OpenOffice |
