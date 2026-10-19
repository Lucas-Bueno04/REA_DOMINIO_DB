# gedicasusuarios — Dicas - Controle de dicas por usuarios
31 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_usuario | char(15) | PK |  | i_usuario |
| i_dicas | integer(4) | PK |  | Numero da dica |
| i_sistemas | integer(4) | PK |  | Codigo do sistema |
| no_exibicoes | integer(4) |  |  | Numero de vezes que a dica foi exibida |
| ultima_exibicao | timestamp(8) |  |  | Ultima vez que a dica foi exibida para o usuario. |
