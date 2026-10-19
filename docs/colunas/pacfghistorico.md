# pacfghistorico — Configuracao de historico
4 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| i_tipo | integer(4) | PK |  | Tipo (1=Correcao do periodo/2=Depreciacao do periodo/3=Correcao da depreciacao acumulada/4=Correcao da depreciacao do periodo/5=Baixa) |
| historico | varchar(100) |  |  | Historico |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
