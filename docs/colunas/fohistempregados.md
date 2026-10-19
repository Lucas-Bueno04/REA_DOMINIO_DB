# fohistempregados — Empregados - Cadastro - Historico
75 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_empregados | integer(4) | PK |  | Codigo empregado |
| sequencia_emp | integer(4) | PK |  | Sequencial |
| data_historico | date(4) |  |  | Data |
| tipo_historico | integer(4) |  |  | Tipo historico |
| codigo_tabela | integer(4) |  | S | Codigo |
| descricao | varchar(400) |  | S | Descricao |
| data_gravacao | date(4) |  |  | Data Cad. |
| hora_gravacao | time(8) |  |  | Hora Cad. |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
