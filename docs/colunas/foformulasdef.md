# foformulasdef — Formulas Padrao
71 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_eventos | integer(4) | PK |  | Evento |
| script | char(8000) |  |  | Script da formula |
| fil1 | char(8000) |  |  | Fil1 |
| fil2 | char(8000) |  |  | Fil2 |
| fil3 | char(8000) |  |  | Fil3 |
| fil4 | char(8000) |  |  | Fil4 |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
