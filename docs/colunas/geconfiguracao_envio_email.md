# GECONFIGURACAO_ENVIO_EMAIL — Tabela para definição do tipo da configuração do envio de email
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Código para controle de linha única |
| TIPO_CONFIGURACAO | integer(4) |  |  | 1 - Configuração definida pelo Outlook, 2 - Configuração definida pelo Contábil |
| CONFIGURACAO_POR_USUARIO | integer(4) |  |  | 0 - Configuração Geral, 1 - Configuração por usuário |
