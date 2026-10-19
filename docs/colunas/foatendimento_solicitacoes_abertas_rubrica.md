# FOATENDIMENTO_SOLICITACOES_ABERTAS_RUBRICA — Tabela que indica rubricas com lançamentos no portal do cliente
31 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| RUBRICA | integer(4) | PK |  | Rubrica |
| POSSUI_LANCAMENTO | integer(4) |  |  | Possui Lançamento (0=Não/1=Sim) |
| ORIGEM_ATENDIMENTO | integer(4) |  |  | Flag que indica se o registro vem do DA(1) ou não (0) |
