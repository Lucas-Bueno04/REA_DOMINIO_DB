# GECONTROLE_IMPOSTO_RETIDO — Controle do recolhimento do imposto retido - IRRF
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  |  |
| MENSAGEM_IMPOSTO_RETIDO | varchar(2) |  | S | 0 = NÃ£o deve mostrar mensagem na abertura 1 = Deve mostrar mensagem na abertura -1 = Erro na requisiÃ§Ã£o |
| DATA_HORA_ULTIMA_CONSULTA | timestamp(8) |  | S | Data e hora da Ãºltima consulta feita |
