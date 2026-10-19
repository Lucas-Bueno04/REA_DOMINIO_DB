# FOCALCULOS_DIFERENCA_RAIS — Todos os calculos com diferença de salario por competência.
228.569 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| COMPETENCIA | date(4) | PK |  | Competência do cálculo. |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo - Renomeado |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo. |
