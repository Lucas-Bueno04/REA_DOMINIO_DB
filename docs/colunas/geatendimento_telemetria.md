# GEATENDIMENTO_TELEMETRIA — Dados de integração para telemetria
407 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Código único na tabela |
| STATUS | char(1) |  |  | Situação N - Não enviado / E - Enviado / R - Erro |
| SERVICO | varchar(100) |  | S | Nome do serviço para telemetria |
| CODIGO_STATUS | varchar(10) |  | S | Statuscode de retorno da requisição |
| MENSAGEM | varchar(255) |  | S | Mensagem de retorno da requisição |
| DATA_HORA_INSERCAO | timestamp(8) |  |  | Data e hora de inserção do registro no banco |
| DADOS | long varchar(32767) |  |  | Informação que será enviada |
| SOURCE | varchar(100) |  | S | Nome do source para a telemetria |
