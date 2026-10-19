# GEATENDIMENTO_SGD_NOTIFICACOES_USUARIOS — Notificações de suporte e notícias por usuário
37.928 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Codigo auto numeração |
| CODI_EMP | integer(4) |  | S | Codigo da empresa |
| CODIGO_NOTIFICACAO | integer(4) |  | S | fk de notificações |
| ID | integer(4) |  | S | Id do usuario no SGD |
| NOME_USUARIO | long varchar(32767) |  | S | Nome do usuario |
| EMAIL | long varchar(32767) |  | S | E-mail do usuario no SGD |
| ONVIO_ID | long varchar(32767) |  | S | Id do usuario no onvio |
| STATUS_NOTIFICACAO | integer(4) |  | S | Status da notificação 1 - Notificado, 2 - Não Lida, 3 - Lida, 4 - Removida |
