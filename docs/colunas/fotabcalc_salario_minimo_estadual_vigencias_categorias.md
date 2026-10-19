# FOTABCALC_SALARIO_MINIMO_ESTADUAL_VIGENCIAS_CATEGORIAS — Valores do salário mínimo estadual por categoria na vigência.
6 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_TABCALC_SALARIO_MINIMO_ESTADUAL | integer(4) | PK |  | Código sequencial da tabela de salário mínimo estadual. |
| VIGENCIA | date(4) | PK |  | Competência de início da vigência da tabela. |
| I_CATEGORIA | integer(4) | PK |  | Código da categoria |
| VALOR | numeric(13) |  |  | Valor do salário mínimo. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
