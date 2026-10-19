# GEATENDIMENTOLOG — Log do envio de dados do Agente de Comunicação
72.972 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  |  |
| CODIGO_GRUPO | integer(4) |  | S |  |
| CODIGO_TABELA | integer(4) |  | S |  |
| CODIGO_ACAO | integer(4) |  | S |  |
| MENSAGEM_LOG | varchar(5000) |  |  |  |
| DATA_LOG | timestamp(8) |  | S |  |
| TIPO_LOG | integer(4) |  | S |  |
| PID | integer(4) |  | S | PID do processo que inseriu o log |
| THREAD_ID | integer(4) |  | S | ID da Thread que inseriu o log |
| CODIGO_SOLUCAO | integer(4) |  | S | Código da solução no suporte |
