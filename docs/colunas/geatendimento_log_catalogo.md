# GEATENDIMENTO_LOG_CATALOGO — Log dos Catalogos de NF-e retornados do servidor.
9 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Campo auto numeraÃ§Ã£o identificaÃ§Ã£o do registro |
| DATAGRAVACAO | timestamp(8) |  | S | Data da gravaÃ§Ã£o do registro |
| CATALOGO | xml(32767) |  | S | XML do Catalogo retornado do servidor |
