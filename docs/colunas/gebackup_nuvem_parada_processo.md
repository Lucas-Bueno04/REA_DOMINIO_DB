# GEBACKUP_NUVEM_PARADA_PROCESSO — Controle de pedido de parada do processo do Backup em Nuvem
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Chave primária para linha única. |
| ACAO_PROCESSO | integer(4) |  | S | Indicação para parar o processo para atualizar o banco. 0 - Sem ação, 1 - Parar processo, 2 - Processo parado, 3 - Iniciar Processo |
