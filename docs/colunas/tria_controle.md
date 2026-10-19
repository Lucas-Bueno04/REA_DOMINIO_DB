# TRIA_CONTROLE — Controle de funcionalidades que utilizam TRIA
9 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Código identificador |
| DESCRICAO | varchar(200) |  |  | Descrição |
| STATUS | smallint(2) |  |  | 0:Desativado, 1:Ativado |
| DATA_HORA_ULTIMA_EXECUCAO | timestamp(8) |  | S | Atualizado via trigger: Data e hora da última execução |
