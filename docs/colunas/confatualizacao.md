# confatualizacao — Configuracao do gerenciador de atualizacoes
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_confatualizacao | integer(4) | PK |  | i_confatualizacao |
| verificar_versao | tinyint(1) |  |  | Se eh para testar se tem uma versao disponivel no diretorio configurado. |
| caminho | varchar(512) |  | S | Caminho para verificar se tem novas versões disponiveis |
