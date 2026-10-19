# FOCALCULOS_EVENTOS_BASES — Contém as bases que não estão vinculadas a eventos para o consulta recibo
11.488 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_EMP_EVE | integer(4) |  |  | Código da empresa dos eventos |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Identificação do cálculo |
| I_EVENTOS | integer(4) | PK |  | Código do evento |
| I_CADBASES | integer(4) | PK |  | Código da base |
| I_EMPRESTIMO | integer(4) | PK |  | Código do empréstimo |
| VALOR | numeric(20) |  | S | Valor do evento |
| BASE | numeric(17) |  | S | Valor da base |
| COMPANY_ID | uniqueidentifier(16) |  |  |  |
