# GECONSULTA_WEB_SERVICE_PORTAL_FEDERAL_CATALOGO — Consulta NF-e Webservice Portal Federal - Catálogo
1.612 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CATALOGO | integer(4) | PK |  | Código sequencial |
| CHAVE_NOTA_OLD | varchar(44) |  |  | SEM USO |
| CNPJ_EMITENTE | varchar(14) |  |  | CNPJ emitente |
| CNPJ_DESTINATARIO | varchar(14) |  |  | CNPJ destinatário |
| DATA_EMISSAO | date(4) |  |  | Data emissão |
| DATA_HORA_RECEBIMENTO | timestamp(8) |  |  | Data/hora recebimento |
| SITUACAO_MANIFESTACAO | integer(4) |  |  | Situação manifestação |
| SITUACAO_NOTA | integer(4) |  |  | Situação nota |
| CSTAT_MANIFESTO | integer(4) |  | S | cStat manifesto |
| XMOTIVO_MANIFESTO | varchar(256) |  | S | xMotivo manifesto |
| REALIZAR_DOWNLOAD | char(1) |  |  | Realizar download |
| CSTAT_DOWNLOAD | integer(4) |  | S | cStat download |
| XMOTIVO_DOWNLOAD | varchar(256) |  | S | xMotivo download |
| DATA_DOWNLOAD | date(4) |  | S | Data download |
| XML_NOTA | long binary(32767) |  | S | XML nota |
| ENVIOU_BOXE | char(1) |  |  | Enviou BOX-e |
| DATA_ENVIO | date(4) |  | S | Data envio ao BOX-e |
| QUANTIDADE_TENTATIVAS_MANIFESTACAO | integer(4) |  |  | Quantidade de tentativas da manifestação |
| TIPO_NOTA | integer(4) |  |  | 1 - Entrada / 2 - Saída / 4 - Serviço |
| NSU_NOTA | numeric(15) |  | S | NSU da nota |
| MODELO_NOTA | integer(4) |  | S | 1 - NF-e / 2 - CT-e / 3 - NFS-e |
| QUANTIDADE_TENTATIVAS_BOXE | integer(4) |  | S | Quantidade de tentativas de envios ao box-e |
| PROTOCOLO_BOXE | varchar(30) |  | S | Protocolo |
| MOTIVO_BOXE | varchar(1024) |  | S | Motivo |
| CHAVE_NOTA | varchar(50) |  |  | Chave nota |
