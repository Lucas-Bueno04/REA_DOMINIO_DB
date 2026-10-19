# HRCUSTOS_GERAL — Dados gerais referente ao custos
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CHAVE | integer(4) | PK |  | Chave |
| STATUS_LIMPEZA_DADOS | tinyint(1) |  |  | 0 - Não executar limpeza, 1 - Executar limpeza, 2 - Limpeza concluída |
| DATA_ULTIMA_LIMPEZA | date(4) |  | S | Data da última limpeza de dados executada |
