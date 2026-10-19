# poafastamentos — Afastamentos de empregados do ponto
10 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  |  |
| i_empregados | integer(4) | PK |  |  |
| data | date(4) | PK |  |  |
| tipo | integer(4) |  |  |  |
| descricao | char(25) |  |  |  |
| abrangencia | char(1) |  |  |  |
| hora_ini | integer(4) |  | S |  |
| hora_ini_tol | integer(4) |  | S |  |
| hora_fim | integer(4) |  | S |  |
| hora_fim_tol | integer(4) |  | S |  |
| i_ocorrencias | integer(4) |  | S |  |
| qhoras_gerar | integer(4) |  | S |  |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
