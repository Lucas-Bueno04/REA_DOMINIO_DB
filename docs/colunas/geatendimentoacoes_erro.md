# GEATENDIMENTOACOES_ERRO — Erros gerados ao tentar enviar alguma ação ao Onvio ou ao Domínio Atendimento
1.402 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  |  |
| CODIGO_GRUPO | integer(4) |  |  |  |
| CODIGO_TABELA | integer(4) |  |  |  |
| CODIGO_ACAO | integer(4) |  |  |  |
| CLAUSULA_ERRO | varchar(5000) |  |  |  |
| CODI_EMP | integer(4) |  | S |  |
| MENSAGEM | varchar(5000) |  | S |  |
| VERSAO_AGENTE | varchar(20) |  | S |  |
| DATA_HORA_ERRO | timestamp(8) |  |  | Coluna que indica a data e hora em que o erro ocorreu |
