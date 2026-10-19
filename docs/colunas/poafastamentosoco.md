# poafastamentosoco — Ocorrencia a ser geradas no momento do afastamento
11 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  |  |
| situacao | integer(4) | PK |  | Situação: (0/1/2/3/4/5/6/7/8/9/14/23/31/32) |
| i_ocorrencias | integer(4) |  | S |  |
| descricao | char(25) |  | S |  |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
