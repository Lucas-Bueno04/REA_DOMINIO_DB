# FOESOCIAL_ERROS_VALIDACAO_XML — Erros de validação do XML (XSD)
9 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa dos eventos. |
| SEQUENCIAL | integer(4) | PK |  | Sequencial de erros do registro. |
| I_EVENTO_ESOCIAL | integer(4) |  | S | Código do evento do eSocial. |
| CODIGO_ESOCIAL | varchar(30) |  | S | Código eSocial do registro. |
| CODIGO_ERRO | integer(4) |  | S | Código do erro. |
| MENSAGEM_ERRO | varchar(1024) |  | S | Mensagem de erro. |
| TABELA_CHAVE | varchar(128) |  |  | Tabela do registro. |
| CHAVE | varchar(256) |  |  | Chave da tabela do registro. |
| MOSTRAR_PAINEL_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| DATA_CRIACAO_REGISTRO | timestamp(8) |  | S | Data de inserção do registro no banco de dados. |
| DATA_ALTERACAO_REGISTRO | timestamp(8) |  | S | Data da última alteração do registro no banco de dados. |
| VERSAO_SISTEMA | varchar(50) |  | S | Versão do sistema no momento da inserção/alteração do registro. |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | Código do dados eventos eSocial |
| GERAR_REMUNERACAO_13_SALARIO | smallint(2) |  |  | Gerar os dados do evento. |
| REENVIAR | smallint(2) |  |  | Evento marcado para reenviar. (0=Não/1=Sim) |
| GERAR_LIMPEZA_DADOS_ESOCIAL | smallint(2) |  |  | Gerar limpeza de dados no eSocial. |
