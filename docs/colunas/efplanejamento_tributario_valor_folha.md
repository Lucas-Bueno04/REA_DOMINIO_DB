# EFPLANEJAMENTO_TRIBUTARIO_VALOR_FOLHA — Planejamento Tributário - Valor Folha
24 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| REGIME | char(1) | PK |  | Regime de Planejamento (P - Presumido, R - Real, S - Simples) |
| PERIODO | date(4) | PK |  | Periodo Planejamento |
| VALOR_SALARIO | numeric(13) |  |  | Valor salário |
| VALOR_CONTRIBUINTE | numeric(13) |  |  | Valor Contribuinte |
| VALOR_INSS | numeric(13) |  |  | Valor INSS Empresa/Terceiros |
| VALOR_DEMAIS_TRIBUTOS | numeric(13) |  |  | Valor Demais Tributos |
| VALOR_TOTAL | numeric(13) |  |  | Valor salário + Valor Contribuinte + Valor INSS Empresa/Terceiros + Valor Demais Tributos |
| VALOR_ULTIMO_DOZE_MESES | numeric(13) |  |  | Valor Último Doze Meses |
| AUMENTO | numeric(13) |  |  | Aumento |
| REDUCAO | numeric(13) |  |  | Reducao |
| VALOR_SALARIO_ESTIMATIVA | numeric(13) |  |  | Valor Salário Estimativa |
| VALOR_CONTRIBUINTE_ESTIMATIVA | numeric(13) |  |  | Valor Contribuinte Estimativa |
| VALOR_INSS_ESTIMATIVA | numeric(13) |  |  | Valor INSS Estimativa |
| VALOR_DEMAIS_TRIBUTOS_ESTIMATIVA | numeric(13) |  |  | Valor Demais Tributos Estimativa |
| VALOR_TOTAL_ESTIMATIVA | numeric(13) |  |  | Valor Total Estimativa |
| VALOR_ULTIMO_DOZE_MESES_ESTIMATIVA | numeric(13) |  |  | Valor Último Doze Meses Estimativa |
