# GEGESTTA_ATIVIDADE — Conclusão de atividades no módulo Processos
47.858 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  |  |
| ATIVIDADE | integer(4) |  |  |  |
| EMPRESA | uniqueidentifier(16) |  |  |  |
| COMPETENCIA | long varchar(32767) |  |  |  |
| DATAHORACONCLUSAO | long varchar(32767) |  | S |  |
| PROCESSADO | integer(4) |  |  | -1 ERRO , 0 NÃO PROCESSADO, 1 PROCESSADO |
| ESCRITORIO | long varchar(32767) |  | S |  |
| USUARIO | long varchar(32767) |  | S |  |
| TIPO_PROCESSAMENTO | integer(4) |  | S | 1 - CONTABIL, 2 - AGENTE |
| GUID_DOCUMENTO_GESTTA | uniqueidentifier(16) |  | S | Guid do documento enviado para o gestta na tabela GEATENDIMENTO_PUBLICAR_DOCUMENTOS |
| GUID_DOCUMENTO_PORTAL_CLIENTE | uniqueidentifier(16) |  | S | Guid do documento enviado para o portal do cliente na tabela GEATENDIMENTO_PUBLICAR_DOCUMENTOS, este documento é responsavel pela criação do envio do documento para o gestta |
| DATAHORAINSERT | timestamp(8) |  | S |  |
