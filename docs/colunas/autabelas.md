# autabelas — Tabelas que serao auditadas
895 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| table_id | integer(4) | PK |  | Codigo da tabela no banco |
| tabela | char(128) |  |  | Nome da tabela |
| modulo | char(20) |  |  | Modulo da tabela |
| tabela_pai | char(128) |  |  | Tabela pai |
| descricao | char(50) |  |  | Descricao da tabela |
| seleciona | tinyint(1) |  |  | Selecionada (1 - Sim/0 - Nao) |
| comentario | char(128) |  |  | Comentario |
| INATIVA | char(1) |  |  | Tabela foi inativada na auditoria(S/N) |
