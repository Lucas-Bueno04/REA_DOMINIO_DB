# GEBACKUP_NUVEM_VERSAO — Tabela de controle de versão do Backup na nuvem
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Chave primária para linha única. |
| VERSAO_ATUAL_APLICACAO | varchar(8) |  | S | Versão atual da aplicação do Backup. |
| VERSAO_ATUAL_SERVICO | varchar(8) |  | S | Versão atual do serviço do Backup. |
| VERSAO_DESEJADA | varchar(8) |  | S | Versão desejada do Backup pelo Contábil. |
| NOVA_VERSAO_BAIXADA | integer(4) |  |  | Nova versão baixada disponível para instalação. |
| EXECUTANDO_ATUALIZACAO | integer(4) |  |  |  |
