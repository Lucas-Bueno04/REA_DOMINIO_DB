# GEATENDIMENTO_ONVIO_EMPRESAS_IGNORADAS — Erros de empresas enviadas ao Onvio ignorados.
345 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Sequencial autoincremento |
| CODIGO_ACAO | integer(4) |  |  | Código da ação |
| CODI_EMP | integer(4) |  | S | Código da empresa |
| GUID_CONTABIL | uniqueidentifier(16) |  | S | GUID gerado pelo Contábil para identificação do registro |
| MENSAGEM | varchar(4096) |  | S | Mensagem do erro |
| VERSAO_AGENTE | varchar(8) |  | S | Versão do Agente em que foi gerado o erro |
| DATA_HORA_ERRO | timestamp(8) |  |  | Data e hora do erro |
