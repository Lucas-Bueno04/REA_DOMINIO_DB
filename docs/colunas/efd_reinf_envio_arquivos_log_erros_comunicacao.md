# EFD_REINF_ENVIO_ARQUIVOS_LOG_ERROS_COMUNICACAO — EFD-Reinf - Envio dos Arquivos - Log dos Erros na Comunicação
1.120 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_FILIAL | integer(4) | PK |  | Código da empresa filial |
| I_ENVIO | integer(4) | PK |  | Código sequencial de envio dos arquivos |
| I_SEQUENCIAL | integer(4) | PK |  | Código sequencial de erros |
| USUARIO | varchar(128) |  |  | Usuário |
| VERSAO_SISTEMA | varchar(40) |  |  | Versão do sistema |
| ATUALIZACAO | integer(4) |  |  | Arquivo de atualização |
| VERSAO_BANCO | integer(4) |  |  | Versão do banco de dados |
| DATA_HORA | timestamp(8) |  |  | data e Hora do erro |
| MENSAGEM_ERRO | varchar(1024) |  |  | Mensagem do erro |
