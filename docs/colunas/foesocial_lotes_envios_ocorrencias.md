# FOESOCIAL_LOTES_ENVIOS_OCORRENCIAS — Ocorrências do lote de envio
3.582 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_LOTE | integer(4) | PK |  | Código do lote |
| SEQUENCIAL | smallint(2) | PK |  | Sequencial de envio |
| TIPO | smallint(2) | PK |  | Tipo de ocorrência. (1=Envio/2=Consulta) |
| SEQUENCIAL_OCORRENCIAS | integer(4) | PK |  | Sequencial de ocorrência. |
| I_RESPOSTA | integer(4) |  |  | Código de resposta |
| DESCRICAO_RESPOSTA | varchar(1000) |  | S | Descrição da resposta |
| LOCALIZACAO | varchar(128) |  | S | Localização da ocorrência |
