# laparmto — Parametros - Lalur
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| aliqcs_par | numeric(5) |  | S | Aliquota da CS |
| aplucro_par | tinyint(1) |  | S | Nao usado |
| ctlucro_par | integer(4) |  | S | Conta do Lucro da Contabilidade |
| mes_par | integer(4) |  | S | Mes |
| ano_par | integer(4) |  | S | Ano |
| limt_par | tinyint(1) |  | S | Limite para compensacao de prejuizos anteriores |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| ctpreju_par | integer(4) |  | S | Conta do Prejuizo da Contabilidade |
| CSLL15_PAR | char(1) |  |  | Pessoa juridica sujeita a aliquota da csll de 15% a partir de maio de 2008 |
