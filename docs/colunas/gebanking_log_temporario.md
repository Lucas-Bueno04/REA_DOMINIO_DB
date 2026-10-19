# GEBANKING_LOG_TEMPORARIO — Tabela de logs para monitoramento temporário de processos
6 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_LOG | integer(4) | PK |  | Sequencial auto incremental |
| CODI_EMP | integer(4) |  | S | Código da empresa |
| DATA_HORA_LOG | timestamp(8) |  |  | Data da gravação do log |
| TIPO_LOG | varchar(100) |  | S | Tipo de log (Processando, Aviso, Advertência ou Erro) |
| PROCESSO | varchar(2048) |  | S | Título do processo |
| DESCRICAO | varchar(2048) |  | S | Descrição da etapa do processo |
