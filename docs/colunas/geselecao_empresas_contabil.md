# GESELECAO_EMPRESAS_CONTABIL — Filtros de seleção de empresas
149 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_SELECAO | integer(4) | PK |  | Identificador do filtro |
| I_MODULO | integer(4) | PK |  | Identificador do módulo - 0 = Não filtra por módulo |
| NOME | varchar(64) |  |  | Nome do filtro |
| NOME_COMPUTADOR | varchar(64) |  |  | Nome do computador proprietário do filtro |
| EMPRESAS | long varchar(32767) |  | S | Lista de empresas do filtro |
