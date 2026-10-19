# foempregados_vinc — Empregados - Cadastro - Multiplos vinculos
82 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_empregados | integer(4) | PK |  | Codigo empregado |
| codi_emp_vinc | integer(4) | PK |  | Codigo empresa |
| i_empregados_vinc | integer(4) | PK |  | Codigo empregado |
| ORDEM_MENOR | smallint(2) |  |  | Vínculo com ordem de cálculo menor |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
