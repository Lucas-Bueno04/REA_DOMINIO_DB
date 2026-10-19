# HRADIANTAMENTO_APROVEITAMENTO — Adiantamentos - Aproveitamentos
215 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_ADIANTAMENTO | integer(4) | PK |  | Adiantamento |
| I_FATURAMENTO | integer(4) | PK |  | Faturamento |
| I_PARCELA | integer(4) | PK |  | Parcela |
| I_RECEBIMENTO | integer(4) | PK |  | Recebimento |
| I_EVENTO | integer(4) | PK |  | Evento |
| PAGO_ESCRITORIO | char(1) | PK |  | Pago pelo escritorio S N |
| ORIGEM | char(1) |  |  | Origem C Cadastro de adiantamento F Faturamento |
| VALOR | numeric(13) |  |  | Valor aproveitado |
| USUARIO | varchar(128) |  |  | Usuario que efetuou o aproveitamento |
| DATA_HORA | timestamp(8) |  |  | Data e hora do aproveitamento |
