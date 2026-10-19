# GELOG_UTILITARIOS — Log dos Utilitários
9.543 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
| OPCAO_MENU | integer(4) |  |  | Utilitário (1=Alterar Notas/2=Limpeza Arquivos) |
| USUARIO | varchar(128) |  |  | Usuário |
| DATA_HORA | timestamp(8) |  |  | Data e hora |
| VERSAO | varchar(10) |  |  | Versão |
| ARQUIVO | integer(4) |  |  | Arquivo de atualização |
| OPCOES_TELA | varchar(2000) |  |  | Opções utilizadas na tela |
