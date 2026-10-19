# foempreg_campolivres — Empregados - Cadastro - Campos livres
33 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_empregados | integer(4) | PK |  | Codigo empregado |
| i_nume_campo | integer(4) | PK |  | Numero Campo |
| conteudo | varchar(256) |  |  | Conteudo |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
