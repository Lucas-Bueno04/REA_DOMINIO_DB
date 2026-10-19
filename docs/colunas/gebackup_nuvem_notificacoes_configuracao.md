# GEBACKUP_NUVEM_NOTIFICACOES_CONFIGURACAO — Tabela de configurações das notificações geradas pelo Backup na Nuvem.
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Chave primária para linha única. |
| BACKUP_SUCESSO | integer(4) |  |  | Gerar notificações ao concluir o processo completo (backup e envio) com sucesso: 1 - Gerar, 2 - Não gerar. |
| BACKUP_ERRO | integer(4) |  |  | Gerar notificações ao ocorrer erro na execução do backup: 1 - Gerar, 2 - Não gerar. |
| ENVIO_ERRO | integer(4) |  |  | Gerar notificações ao ocorrer erro no envio do backup: 1 - Gerar, 2 - Não gerar. |
| EMAILS_DESTINO | varchar(256) |  | S | Emails de destino separados por vírgula para envio das notificações. |
| EMAILS_COPIA | varchar(256) |  | S | Emails com cópia separados por vírgula para envio das notificações. |
