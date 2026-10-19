# PMHISTORICO — Históricos
6 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_HISTORICO | integer(4) | PK |  | Código |
| TIPO | tinyint(1) |  |  | Tipo (1=Geral/ 2=Baixa total/ 3=Baixa parcial/ 4=Transferências de contas patrimoniais/ 5=Transferências de centros de custos/ 6=Aquisicao Bem / 7=Transferências de bens entre matriz/filiais) |
| HISTORICO | varchar(512) |  |  | Descrição |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
