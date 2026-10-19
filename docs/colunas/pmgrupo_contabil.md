# PMGRUPO_CONTABIL — Grupos Contábeis
1.058 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_GRUPO_CONTABIL | integer(4) | PK |  | Código |
| DESCRICAO | varchar(40) |  |  | Descrição |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
