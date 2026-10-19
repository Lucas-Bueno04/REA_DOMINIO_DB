# FOESOCIAL_INGESTAO_CARGA — Controle da carga inicial (dia zero) da ingestão eSocial, por empresa
287 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| SITUACAO | smallint(2) |  |  | Situação (0-Pendente/1-Em andamento/2-Concluída/3-Esgotada) |
| NOITES_TENTADAS | integer(4) |  |  | Quantidade de noites em que a carga da empresa foi tentada |
| DATA_INICIO | timestamp(8) |  | S | Data/Hora de início da carga da empresa |
| DATA_ULTIMA_NOITE | timestamp(8) |  | S | Data/Hora da última noite processada (uma geração por noite) |
| DATA_CONCLUSAO | timestamp(8) |  | S | Data/Hora de conclusão/liberacao da carga |
| MENSAGEM | varchar(2048) |  | S | Mensagem/observação do último ciclo |
| DATA_CRIACAO | timestamp(8) |  | S | Data/Hora de criação do registro |
