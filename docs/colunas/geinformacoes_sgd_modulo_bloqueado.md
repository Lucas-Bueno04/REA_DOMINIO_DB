# GEINFORMACOES_SGD_MODULO_BLOQUEADO — Informações das tentativas de acessos aos modulos bloqueados para serem enviadas para o SGD
170 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_ACESSO | integer(4) | PK |  | Sequencial |
| CODIGO_MODULO | integer(4) |  |  | Código do módulo |
| I_USUARIO | integer(4) |  |  | Código do usuário relacionado com a tabela USCONFUSUARIO |
| TIPO_USUARIO | smallint(2) |  |  | Tipo do usuário relacionado com a tabela USCONFUSUARIO |
| DATA_HORA_TENTATIVA_ACESSO | timestamp(8) |  |  | Data e hora da tentativa de acesso |
