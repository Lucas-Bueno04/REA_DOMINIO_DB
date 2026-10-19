# FOEMPREGADOS_TRANSF — TABELA DE TRANSFERÊNCIA DE EMPREGADOS
427 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | CÓDIGO DA EMPRESA |
| I_EMPREGADOS | integer(4) | PK |  | CÓDIGO DO EMPREGADO |
| TRANSF_CODI_EMP | integer(4) | PK |  | CÓDIGO DA EMPRESA DE ORIGEM |
| TRANSF_I_EMPREGADOS | integer(4) | PK |  | CÓDIGO DO EMPREGADO DE ORIGEM |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
