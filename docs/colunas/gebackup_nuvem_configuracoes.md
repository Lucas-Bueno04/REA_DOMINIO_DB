# GEBACKUP_NUVEM_CONFIGURACOES — Tabela de configurações adicionais do Backup na Nuvem.
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Chave primária para linha única. |
| LIMITAR_MEMORIA_VALIDACAO | integer(4) |  |  | Limitar memória utilizada na validação do backup: 1 - Limitar, 0 - Não limitar. |
| MEMORIA_MAXIMA_VALIDACAO | integer(4) |  | S | Quantidade de memória utilizada na validação do backup em MB. |
| LIMITAR_VELOCIDADE_ENVIO | integer(4) |  |  | Limitar velocidade do envio do backup: 1 - Limitar, 2 - Não limitar. |
| VELOCIDADE_MAXIMA_ENVIO | integer(4) |  | S | Velocidade máxima do envio do backup em Kbps. |
| DEFINIR_CAMINHO_TEMPORARIO | integer(4) |  |  | Definir a pasta temporária para salvar o backup: 1 - Definir, 0 - Utilizar temp do Windows. |
| CAMINHO_TEMPORARIO | varchar(256) |  | S | Caminho temporário do backup. |
| SALVAR_COPIA_LOCAL | integer(4) |  |  | Salvar uma copia local do backup: 1 - Salvar, 0 - Não salvar. |
| TIPO_CAMINHO_COPIA_LOCAL | integer(4) |  |  | Tipo do caminho da cópia local do backup: 1 - Pasta local, 2 - Pasta de rede. |
| CAMINHO_COPIA_LOCAL | varchar(256) |  | S | Caminho da cópia local do backup. |
| NOME_USUARIO_CAMINHO_REDE | varchar(256) |  | S | Nome de usuário utilizado para salvar a cópia local em pasta de rede. |
| SENHA_USUARIO_CAMINHO_REDE | varchar(256) |  | S | Senha de usuário utilizado para salvar a cópia local em pasta de rede. |
