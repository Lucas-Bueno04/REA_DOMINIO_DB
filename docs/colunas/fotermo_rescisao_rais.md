# FOTERMO_RESCISAO_RAIS — Valores para compor o campo 23 do termo de rescisão.
361.039 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| COMPETENCIA | date(4) | PK |  | Competência do cálculo. |
| TIPO_PROCESSO | integer(4) | PK |  | Tipo do cálculo. |
| I_SERVICOS | integer(4) | PK |  | Serviço relacionado no cálculo. |
| RATEIO | integer(4) | PK |  | Rateio. |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo - Renomeado |
| VALOR_MES_COMPOE_CAMPO_23_TERMO_RESCISAO | numeric(30) |  | S | Valor que compoe o campo 23 do termo de rescisão. |
| VALOR_MES_COMPOE_CAMPO_23_TERMO_RESCISAO_COMPLEMENTAR | numeric(30) |  | S | Valor que compoe o campo 23 do termo de rescisão para complementar. |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo. |
