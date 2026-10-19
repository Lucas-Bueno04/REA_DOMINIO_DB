# GEATENDIMENTOACOES_AVISOS — Avisos gerados pelas ações enviadas ao Domínio Atendimento
337 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  |  |
| CODIGO_GRUPO | integer(4) |  |  |  |
| CODIGO_TABELA | integer(4) |  |  |  |
| CODIGO_ACAO | integer(4) |  |  |  |
| CLAUSULA_AVISO | varchar(5000) |  |  |  |
| TIPO_AVISO | integer(4) |  |  |  |
| CODI_EMP | integer(4) |  | S |  |
| DATA_LOG | timestamp(8) |  | S |  |
| MOSTRAR_AVISO | integer(4) |  | S |  |
| MENSAGEM_ERRO | varchar(500) |  |  | Mensagem do aviso quando vindo de erro |
