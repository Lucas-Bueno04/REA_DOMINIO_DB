# FORESCISOES_TERMO_SIMULACAO — Simulação do termo rescisão
1.902 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| TIPO | integer(4) | PK |  | Tipo da rescisão |
| AVOS_13 | smallint(2) |  | S | Quantidade de avos de 13º salário pagos |
| AVOS_FERIAS | smallint(2) |  | S | Quantidade de avos de férias pagos |
| ORIGEM_REG | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| VALOR_FERIAS_VENCIDAS | numeric(13) |  | S | Valor das férias vencidas (Valor lançado/alterado) |
| VALOR_FERIAS_DOBRO | numeric(13) |  | S | Valor das férias em dobro (Valor lançado/alterado) |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo - Renomeado |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo |
