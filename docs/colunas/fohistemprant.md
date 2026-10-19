# fohistemprant — Empregados - Cadastro - Historico - Mov. Ant
2.098 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_empregados | integer(4) | PK |  | Codigo empregado |
| tipo_his | tinyint(1) | PK |  | Tipo do historico |
| data_his | date(4) | PK |  | Data |
| aquisitivo_fim | date(4) |  | S | Per. Aq. fim |
| ini_gozo | date(4) | PK |  | Inicio gozo |
| fim_gozo | date(4) |  | S | Fim gozo |
| valor | numeric(13) |  | S | valor |
| tabela_troca | integer(4) |  | S | Tabela de troca |
| cod_anterior | integer(4) |  | S | Cod. anterior |
| cod_novo | integer(4) |  | S | Cod. novo |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| DATA_GRAVACAO | timestamp(8) |  |  | Data da gravação |
| I_SINDICATOS | integer(4) |  | S | Código do sindicato |
| DESCRICAO | varchar(100) |  | S | Descrição do histórico. |
| SEQUENCIAL | integer(4) | PK |  | Sequencial do histórico. |
| CODI_EMP_TROCA | integer(4) |  | S | Código da empresa origem da troca |
