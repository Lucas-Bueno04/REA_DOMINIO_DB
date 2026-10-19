# HRTABELA_MENSAGEM_INCONSISTENCIA_IMPORTACAO_REMESSA — Mensagens de inconsistências de arquivos de retorno de boleto bancário
551 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Código da mensagem |
| BANCO | integer(4) | PK |  | Código do banco |
| TIPO_REMESSA | integer(4) | PK |  | Tipo da Remessa: 0 = Ambos/ 1 = CNAB 240/ 2 = CNAB 400 |
| DESCRICAO | varchar(512) |  | S | Descrição da mensagem |
