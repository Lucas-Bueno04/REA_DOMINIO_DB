# FOSINDPISO — GUARDA OS PISOS REGISTRADOS NOS SINDICATOS
111 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_SINDICATOS | integer(4) | PK |  | CÓDIGO DO SINDICATO |
| I_SINDPISO | integer(4) | PK |  | CÓDIGO DO PISO DO SINDICATO |
| DESCRICAO | char(115) |  |  | NOME PARA O PISO DO SINDICATO |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
