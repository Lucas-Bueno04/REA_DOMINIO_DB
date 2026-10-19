# gedicas — Dicas
88 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_sistemas | integer(4) | PK |  | Codigo do sistema |
| i_dicas | integer(4) | PK |  | Numero da dica |
| descricao | varchar(5120) |  |  | Descrição da dica |
| uf | char(2) |  |  | Estado a que a dica pertence XX=Todos os estados |
| modulo | integer(4) |  |  | Modulo da dica. 0=Todos os modulos. |
