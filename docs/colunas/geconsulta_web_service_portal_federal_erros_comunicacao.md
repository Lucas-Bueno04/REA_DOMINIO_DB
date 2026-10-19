# GECONSULTA_WEB_SERVICE_PORTAL_FEDERAL_ERROS_COMUNICACAO — Consulta NF-e Webservice Portal Federal - Erros de comunicação
46 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
| CNPJ_DESTINATARIO | varchar(14) |  |  | CNPJ destinatário |
| DATA_ERRO | date(4) |  |  | Data do erro |
| CODIGO_SITUACAO | integer(4) |  |  | Código da situação |
| SITUACAO | varchar(1024) |  |  | Situação |
| DATA_HORA | timestamp(8) |  | S | Data e hora do erro |
