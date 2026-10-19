# EFECF_REDUCAO_Z_SITUACAO_TRIBUTARIA_DETALHAMENTO — ECF - Dados da redução Z - Situação tributária - Detalhamento
1.608 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_REDUCAO | integer(4) | PK |  | Código da redução Z |
| I_SITUACAO | integer(4) | PK |  | Sequencial da situação tributária |
| I_DETALHAMENTO | integer(4) | PK |  | Sequencial do detalhamento |
| CODI_ACU | integer(4) |  |  | Acumulador |
| CODI_NAT | integer(4) |  |  | CFOP |
| VERSAO_NAT | smallint(2) |  |  | Versão da CFOP |
| VALOR | numeric(13) |  |  | Valor do detalhamento |
| IMPOSTO | numeric(13) |  |  | Valor do imposto do detalhamento |
| CST | integer(4) |  |  | CST |
