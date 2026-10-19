# GEATENDIMENTOACOES_ONVIO_AVISOS — Avisos gerados pelas ações enviadas ao Onvio.
13.713 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Sequencial autoincremento |
| CODIGO_GRUPO | integer(4) |  |  | Código do grupo |
| CODIGO_TABELA | integer(4) |  |  | Código da tabela |
| CODIGO_ACAO | integer(4) |  | S | Código da ação |
| GUID_CONTABIL | uniqueidentifier(16) |  | S | GUID gerado pelo Contábil para identificação do registro |
| TIPO_AVISO | tinyint(1) |  |  | 1 - Documento já existe, 2 - Documento já visualizado, 3 - Aviso gerado de erro, 4 - Aviso WarningCode, 5 - Avisos Gestta Processos, 6 - Proxy |
| CODI_EMP | integer(4) |  |  | Código da empresa |
| DATA_LOG | timestamp(8) |  | S | Data e hora do aviso |
| MOSTRAR_AVISO | bit(1) |  |  | Indica se o aviso deve ser mostrado |
| MENSAGEM_ERRO | varchar(512) |  | S | Mensagem do aviso |
