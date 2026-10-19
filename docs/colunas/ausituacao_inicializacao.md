# AUSITUACAO_INICIALIZACAO — Tabela para sinalização da inicialização e parada da Auditoria.
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| SITUACAO | smallint(2) | PK |  | Situação: 0 - Liberado, 1 - Processando inicialização/parada |
| USUARIO | varchar(255) |  | S | Usuario do sistema que iniciou a auditoria |
| CONNECTION_ID | integer(4) |  | S | Connection ID do usuario do sistema que iniciou a auditoria |
