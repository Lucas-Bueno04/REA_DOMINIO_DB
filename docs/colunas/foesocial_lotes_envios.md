# FOESOCIAL_LOTES_ENVIOS — Registros de envio do lote do e-Social
210.737 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_LOTE | integer(4) | PK |  | Código do lote |
| SEQUENCIAL | smallint(2) | PK |  | Sequencial de envio |
| XML_ENVIO | long varchar(32767) |  | S | XML de envio |
| I_RESPOSTA_ENVIO | integer(4) |  | S | Código de resposta do envio |
| DESCRICAO_RESPOSTA_ENVIO | varchar(1000) |  | S | Descrição da resposta do envio |
| XML_RETORNO_ENVIO | long varchar(32767) |  | S | XML de retorno do envio |
| DATA_HORA_ENVIO | timestamp(8) |  | S | Data e hora de envio |
| NUMERO_PROTOCOLO | varchar(30) |  | S | Número do protocolo |
| I_RESPOSTA_CONSULTA | integer(4) |  | S | Código de resposta da consulta |
| DESCRICAO_RESPOSTA_CONSULTA | varchar(1000) |  | S | Descrição da resposta da consulta |
| HORARIO_CONSULTA | timestamp(8) |  | S | Horário da consulta |
| XML_RETORNO_CONSULTA | long varchar(32767) |  | S | XML de retorno da consulta |
| DATA_CRIACAO_REGISTRO | timestamp(8) |  | S | Data de inserção do registro no banco de dados. |
| DATA_ALTERACAO_REGISTRO | timestamp(8) |  | S | Data da última alteração do registro no banco de dados. |
| DATA_PROCESSAMENTO_REGISTRO | timestamp(8) |  | S | Data de processamento do registro. |
| VERSAO_SISTEMA | varchar(50) |  | S | Versão do sistema no momento da inserção/alteração do registro. |
| XML_ENVIO_OLD | xml(32767) |  | S | **SEM USO** |
| XML_RETORNO_ENVIO_OLD | xml(32767) |  | S | **SEM USO** |
| XML_RETORNO_CONSULTA_OLD | xml(32767) |  | S | **SEM USO** |
