# FOFERIAS_GOZO_VANTAGENS_SIMULACAO — Simulação das vantagens do gozo de férias
243 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | CODIGO EMPRESA |
| I_EMPREGADOS | integer(4) | PK |  | CODIGO |
| I_FERIAS_GOZO | integer(4) | PK |  | SEQUENCIAL DE PERIODOS DE GOZO |
| I_EVENTOS | integer(4) | PK |  | CODIGO DO EVENTO |
| VALOR_INF | numeric(13) |  |  | VALOR INFORMADO |
| VALOR_CALC | numeric(13) |  |  | VALOR CALCULADO |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
