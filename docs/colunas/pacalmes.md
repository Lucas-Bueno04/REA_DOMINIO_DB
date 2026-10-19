# pacalmes — Calculo Mensal do Patrimonio
24 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_bem | numeric(16) | PK |  | Bem |
| data_cal | date(4) | PK |  | Competencia do calculo |
| tipo_cal | tinyint(1) | PK |  | Tipo |
| val_moe | numeric(13) |  |  | Valor em moeda |
| val_ind | numeric(13) |  |  | Valor em indice |
| dep_moe | numeric(13) |  |  | Depreciacao em moeda |
| dep_ind | numeric(13) |  |  | Depreciacao em indice |
| val_moe2 | numeric(13) |  |  | Valor em moeda 2 (para o tipo 10 - correcao da depreciao no mes) |
| val_moe3 | numeric(13) |  |  | Valor em moeda 2 (para o tipo 10 - correcao da depreciao acumulada) |
| codi_ccu | integer(4) |  |  | Centro de custo |
| codi_cta | integer(4) |  |  | Conta patrimonial |
