# FOREQUERIMENTO_SEGURO_DESEMPREGO_SALARIOS — Últimos salários para o requerimento de Seguro Desemprego
1.636 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| MESES_TRABALHADOS | smallint(2) |  |  | Quantidade de meses trabalhados. |
| VALOR_ANTEPENULTIMO_SALARIO | numeric(13) |  |  | Valor do antepenúltimo salário. |
| VALOR_PENULTIMO_SALARIO | numeric(13) |  |  | Valor do penúltimo salário. |
| VALOR_ULTIMO_SALARIO | numeric(13) |  |  | Valor do último salário. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro (0=Sistema/1=Importação de tabelas/2=Importação de layout) |
