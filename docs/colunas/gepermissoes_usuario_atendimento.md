# GEPERMISSOES_USUARIO_ATENDIMENTO — Permissões do usuário no Domínio Atendimento
78 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO_USUARIO | integer(4) | PK |  |  |
| GERENCIAR_ESTRUTURA_PASTA | integer(4) |  |  |  |
| PERMITE_PUBLICAR_RELATORIO | integer(4) |  |  |  |
| NOTIFICAR_NFE | integer(4) |  |  |  |
| USUARIO | varchar(40) | PK |  |  |
| ATIVO | tinyint(1) |  |  | Situação do usuário no Atendimento. 1 - Ativo, 0 - Inativo |
