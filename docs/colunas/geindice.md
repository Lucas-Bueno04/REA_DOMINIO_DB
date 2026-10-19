# GEINDICE — Índices
17 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_INDICE | integer(4) | PK |  | Código |
| DESCRICAO | varchar(40) |  |  | Descrição |
| SIGLA | varchar(8) |  |  | Sigla |
| TIPO | char(1) |  |  | Tipo do índice (O=Outros/ M=Moeda estrangeira) |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
