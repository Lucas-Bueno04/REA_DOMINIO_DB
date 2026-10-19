# GEBACKUP_NUVEM_ESTACAO_VINCULADA — Tabela de controle da estação vinculada e da situacao do Backup na nuvem.
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Chave primária para linha única. |
| NOME_ESTACAO | varchar(64) |  |  | Nome da estação vinculada ao Backup na Nuvem. |
| MODO_INICIALIZACAO | integer(4) |  |  | Modo de inicialização do processo: 1 - Automática, 0 - Manual. |
| SITUACAO_PROCESSO | integer(4) |  |  | Situacao do processo: 1 - Iniciado, 0 - Parado. |
| DATA_HORA_ALIVE | timestamp(8) |  | S | Data hora da última atualização do serviço iniciado. |
