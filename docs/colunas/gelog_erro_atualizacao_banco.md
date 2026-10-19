# GELOG_ERRO_ATUALIZACAO_BANCO — LOG DE ERRO NA ATUALIZAÇÃO DO BANCO
4 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_NUMERO_ERRO | integer(4) | PK |  |  |
| VERSAO_SISTEMA | varchar(40) |  |  |  |
| ATUALIZACAO | integer(4) |  | S |  |
| VERSAO_BANCO | integer(4) |  |  |  |
| COMANDO | varchar(1024) |  |  |  |
| ERRO_SQL | varchar(1024) |  |  |  |
| DATA_ERRO | timestamp(8) |  |  |  |
