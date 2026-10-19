# GEBACKUP_NUVEM_DADOS_ENVIO — Tabela com os dados à serem enviados para o servidor.
87.159 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| SEQUENCIAL | bigint(8) | PK |  | Sequencial auto-incremento. |
| TIPO_DADO | integer(4) |  |  | Tipo do dado a ser enviado. |
| ACAO | integer(4) |  |  | 1 - Inclusão, 2 - Exclusão |
| VALOR_CHAVE_PRIMARIA | bigint(8) |  |  | Valor da chave primária do dado a ser enviado. |
| VALOR_CHAVE_PRIMARIA_GUID | uniqueidentifier(16) |  | S | Valor da chave UniqueIdentifier primária do dado a ser enviado. |
| SITUACAO | integer(4) |  |  | Situação do dado a ser enviado: 1 - Enviado, 0 - Não enviado |
| DATA_INSERCAO | timestamp(8) |  |  | Data e hora em que o dado de envio foi para a fila. |
| DATA_ENVIO | timestamp(8) |  | S | Data e hora em que o dado de envio foi enviado com sucesso. |
| ENVIAR_ANTES | integer(4) |  |  | Coluna indicando que a ação deve ser enviada antes das outras. |
