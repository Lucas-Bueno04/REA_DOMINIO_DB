# GEVERSAO_AGENTE — Versão do Agente de Comunicação
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  |  |
| VERSAO_DESEJADA | varchar(20) |  | S |  |
| VERSAO_ATUAL | varchar(20) |  | S |  |
| VERSAO_ATUAL_SERVICO | varchar(20) |  | S |  |
| EXISTE_VERSAO_NOVA_BAIXADA | integer(4) |  |  | Coluna que indica se foi baixada uma nova versão do site |
| VERSAO_DESEJADA_ESOCIAL | integer(4) |  | S | Versão desejada do Agente E-Social Certificados A3 |
| DATA_HORA_INICIO_DOWNLOAD | timestamp(8) |  | S | Data e hora do início do download |
