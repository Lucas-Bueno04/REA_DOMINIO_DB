# efprodutos_saldos — Produtos - Cadastro - Saldos
4.106 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_pdi | char(14) | PK |  | Produto |
| codi_emp | integer(4) | PK |  | Empresa |
| data_sal | date(4) | PK |  | Data do saldo |
| qfin_sal | numeric(13) |  |  | Quantidade final |
| vlfin_sal | numeric(14) |  |  | Valor final |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| vuni_sal | numeric(16) |  |  | Valor unitario |
| ICMS_RECUPERAVEL | numeric(13) |  |  | ICMS Recuperável |
