# PMINFORMACAO_CALCULO_CREDITO_ICMS — Informações para Cálculo do Crédito de ICMS
8 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| COMPETENCIA | date(4) | PK |  | Competência |
| MENSAL_QUINZENAL | tinyint(1) | PK |  | Mansal ou quinzenal (0=Mensal/ 1=Primeira quinzena/ 2=Segunda quinzena) |
| VALOR_TOTAL_SAIDA | numeric(13) |  |  | Total de saídas |
| VALOR_SAIDA_TRIBUTADA | numeric(13) |  |  | Saídas tributadas |
| VALOR_SAIDA_ISENTA | numeric(13) |  |  | Saídas isentas |
| VALOR_COEFICIENTE_CREDITO | numeric(15) |  |  | Coeficiente de crédito |
