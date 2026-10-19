# ctdocumentos_ole_modelos — Modelos de Documento
13 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_modelo | integer(4) | PK |  | Codigo |
| i_tipo | integer(4) | PK |  | Tipo |
| descricao | char(100) |  |  | Descricao |
| padrao | char(10) |  | S | Codigo padrao |
| ole | long binary(32767) |  | S | Definicao do ole |
| EDITOR | integer(4) |  | S | 1- Office, 2-OpenOffice |
