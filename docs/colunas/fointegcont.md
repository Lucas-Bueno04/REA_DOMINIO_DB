# fointegcont — Integracao Contabilidade - Configuracao
112.913 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_separador | integer(4) | PK |  | Separador |
| i_codigo | integer(4) | PK |  | Codigo |
| descricao | char(40) |  |  | Descricao |
| conta_cred | integer(4) |  | S | Conta Credito |
| conta_deb | integer(4) |  | S | Conta Debito |
| i_historico | integer(4) |  |  | Historico |
| comp_hist | varchar(512) |  | S | Descricao Historico |
| tipo | integer(4) | PK |  | Tipo de configuracao |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| deb_juros | integer(4) |  | S | Conta debito juros |
| hist_juros | integer(4) |  | S | Historico juros |
| hist_juros_comp | varchar(512) |  | S | Descricao historico juros |
| deb_multa | integer(4) |  | S | Conta debito multa |
| hist_multa | integer(4) |  | S | Historico multa |
| hist_multa_comp | varchar(512) |  | S | Descricao historico multa |
