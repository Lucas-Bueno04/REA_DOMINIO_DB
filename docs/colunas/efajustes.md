# efajustes — Ajustes - Cadastro
50.027 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_imp | integer(4) |  |  | Imposto |
| oper_aju | integer(4) |  |  | Operacao |
| codi_aju | integer(4) | PK |  | Codigo |
| nome_aju | char(30) |  |  | Nome |
| cdeb_aju | integer(4) |  | S | Conta debito |
| ccre_aju | integer(4) |  | S | Conta credito |
| chis_aju | integer(4) |  | S | Historico padrao |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
