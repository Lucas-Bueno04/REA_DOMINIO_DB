# focadbases — Cadastro - Bases de calculo
270 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_cadbases | integer(4) | PK |  | Codigo do cadastro da base |
| descricao | char(64) |  |  | Descricao |
| tipo_base | integer(4) |  |  | Tipo da base |
| frm_script | varchar(8000) |  |  | Formula da base |
| frm_fil1 | varchar(8000) |  | S | Compilacao.1 |
| frm_fil2 | varchar(8000) |  | S | Compilacao.2 |
| frm_fil3 | varchar(8000) |  | S | Compilacao.3 |
| frm_fil4 | varchar(8000) |  | S | Compilacao.4 |
| ordem | tinyint(1) |  | S | Ordem das bases |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
