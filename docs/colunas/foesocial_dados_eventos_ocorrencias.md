# FOESOCIAL_DADOS_EVENTOS_OCORRENCIAS — Ocorrências do envio do evento.
82.751 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_DADOS_EVENTOS | integer(4) | PK |  | Código do registro de envio. |
| I_RESPOSTA | integer(4) |  |  | Código da resposta. |
| SEQUENCIAL | smallint(2) | PK |  | Sequencial. |
| DESCRICAO | varchar(1500) |  | S | Descrição da ocorrência. |
| LOCALIZACAO | varchar(128) |  | S | Localização da ocorrência. |
| MOSTRAR_PAINEL_ESOCIAL | smallint(2) |  |  | Indica se o registro vai ser mostrado no painel eSocial. 0=Nao/1=Sim |
