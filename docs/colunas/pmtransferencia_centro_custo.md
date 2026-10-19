# PMTRANSFERENCIA_CENTRO_CUSTO — Transferência de Centros de Custos
4.353 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_TRANSFERENCIA | integer(4) | PK |  | Código |
| I_BEM | numeric(16) |  |  | Bem |
| DATA_TRANSFERENCIA | date(4) |  |  | Data da transferência |
| I_CENTRO_CUSTO | integer(4) |  |  | Centro de custo |
| I_HISTORICO | integer(4) |  | S | Código do histórico |
| HISTORICO | varchar(512) |  |  | Histórico |
| ORIGEM_TRANSFERENCIA | char(1) |  |  | Origem da transferência (B=Bem/ T=Transferência) |
| VALOR_DEPRECIACAO_FISCAL_ACUMULADA_BEM | numeric(13) |  |  | Depreciação fiscal acumulada |
| VALOR_DEPRECIACAO_SOCIETARIA_ACUMULADA_BEM | numeric(13) |  |  | Depreciação societária acumulada |
| I_TRANSFERENCIA_VINCULO | integer(4) |  | S | Código da transferência do bem Principal quando é realizada uma transferencia por vinculo. |
