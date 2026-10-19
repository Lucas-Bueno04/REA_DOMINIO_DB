# GEATENDIMENTO_SGD_NOTIFICACOES — Notificações de suporte e notícias
2.053 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Codigo auto numeração |
| CODI_EMP | integer(4) |  | S | Codigo da empresa |
| CLASSIFICACAO | integer(4) |  | S | Classificação da notificação 2 - Suporte, 3 - Noticias |
| CLIENTE | integer(4) |  | S | Cliente no SGD |
| DESCRICAO | long varchar(32767) |  | S | Descrição da notificação |
| ENTRADA | timestamp(8) |  | S | Dada da entrada da mensagem no Contabil |
| LINK | long varchar(32767) |  | S | Link para abrir a notificação |
| MENSAGEM | long varchar(32767) |  | S | Mensagem da notificação |
| STATUS | integer(4) |  | S | Status da notificação 1 - Notificado, 2 - Não Lida, 3 - Lida, 4 - Removida |
| ID | integer(4) |  | S | Id da notificação no SGD |
