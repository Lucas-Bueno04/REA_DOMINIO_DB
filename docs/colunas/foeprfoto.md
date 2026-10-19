# foeprfoto — Empregados - Cadastro - Foto
1.290 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_empregados | integer(4) | PK |  | Codigo empregado |
| imagem | long binary(32767) |  |  | Foto |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| TIPO_BLOB_IMAGEM | smallint(2) |  |  | Tipo de informação binária da imagem (1=OLE/2=Picture) |
