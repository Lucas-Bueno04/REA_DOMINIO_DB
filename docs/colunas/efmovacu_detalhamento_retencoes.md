# EFMOVACU_DETALHAMENTO_RETENCOES — Detalhamento das retenções dos movimentos de acumuladores
18 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_MAC | integer(4) | PK |  | Código do movimento de acumulador |
| CODI_CLI | integer(4) |  |  | Código do cliente |
| VALOR_RENDIMENTO | numeric(13) |  |  | Valor do rendimento |
| CODIGO_RECOLHIMENTO | char(6) |  |  | Código de recolhimento |
| I_RECOLHIMENTO_COMPENSAR | integer(4) |  | S | Código Sequencial do Recolhimento a Compensar |
| CODIGO_RECOLHIMENTO_COMPENSAR | char(6) |  |  | Código do Recolhimento a Compensar |
