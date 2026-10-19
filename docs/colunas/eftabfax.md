# eftabfax — Incentivos - Cadastro - Faixas
460 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_tab | integer(4) | PK |  | Codigo da tabela |
| vigi_tab | date(4) | PK |  | Vigencia |
| sequ_fax | smallint(2) | PK |  | Faixa |
| inic_fax | numeric(10) |  |  | Faixa inicial |
| fina_fax | numeric(10) |  |  | Faixa final |
| tax1_fax | numeric(8) |  |  | Taxa 1 |
| tax2_fax | numeric(8) |  |  | Taxa 2 |
| tax3_fax | numeric(8) |  |  | Taxa 3 |
| tax4_fax | numeric(8) |  |  | Taxa 4 |
| tipo_fax | char(1) |  | S | Tipo (V - Valor/P - Percentual) |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
