# HRCLASSIFICACAO_TRIBUTARIA_IBS_CBS — Classificações Tributárias IBS e CBS
69 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | varchar(6) | PK |  | Código da classificação tributária |
| DESCRICAO | varchar(1200) |  |  | Descrição da classificação tributária |
| CST | varchar(6) |  |  | Código de situação tributária vinculado |
| CST_DESCRICAO | varchar(150) |  |  | Descrição do CST |
| REDUCAO_IBS | numeric(5) |  |  | Percentual de redução IBS |
| REDUCAO_CBS | numeric(5) |  |  | Percentual de redução CBS |
