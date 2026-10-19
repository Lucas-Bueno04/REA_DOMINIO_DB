# FOESOCIAL_LOTES — Lotes para envio do e-Social
210.737 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_LOTE | integer(4) | PK |  | Código do lote |
| STATUS | smallint(2) |  |  | Status do lote.(1=Aguardando envio/2=Enviado/3=Aguardando ajuste/4=Concluído/5=Aguardando senha A3/6=Aguardando Envio Multiplos Vinculos/7=Aguardando fim thread contábil/8=Erro lote/9=Erro preenchimento) |
| I_EVENTO_ESOCIAL | integer(4) |  |  | Código do evento do eSocial que será enviado no lote. |
| VERSAO | varchar(12) |  |  | Versão do XML. |
| LOTE_EXCLUSAO | smallint(2) |  |  | Lote de exclusão da empresa. |
| DATA_CRIACAO_REGISTRO | timestamp(8) |  | S | Data de inserção do registro no banco de dados. |
| DATA_ALTERACAO_REGISTRO | timestamp(8) |  | S | Data da última alteração do registro no banco de dados. |
| DATA_PROCESSAMENTO_REGISTRO | timestamp(8) |  | S | Data de processamento do registro. |
| VERSAO_SISTEMA | varchar(50) |  | S | Versão do sistema no momento da inserção/alteração do registro. |
| POSSUI_EVENTOS_INVALIDADOS | bit(1) |  |  | Indica se o lote possui eventos invalidados. |
| CODI_EMP_FILA_EVENTOS_GERAR | integer(4) |  | S | Código da empresa na fila |
| SEQUENCIAL_FILA_EVENTOS_GERAR | integer(4) |  | S | Sequencial na fila |
