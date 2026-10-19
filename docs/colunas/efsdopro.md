# efsdopro — Saldo dos Produtos
8.451.202 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_pdi | char(14) | PK |  | Produto |
| data_pro | date(4) | PK |  | Competencia |
| sfisant_pro | numeric(18) |  |  | Saldo fisico anterior |
| svalant_pro | numeric(15) |  |  | Valor do saldo anterior |
| saifis_pro | numeric(15) |  |  | Saidas fisicas do mes |
| saival_pro | numeric(15) |  |  | Valor das saidas do mes |
| entfis_pro | numeric(15) |  |  | Entrada fisicas do mes |
| entval_pro | numeric(15) |  |  | Valor das entradas do mes |
| sfismes_pro | numeric(18) |  |  | Saldo Fisico no mes |
| svalmes_pro | numeric(15) |  |  | Valor do saldo no mes |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| ESTOQUE_FINAL | numeric(15) |  | S | Estoque final - Portaria Cat nº 17/99 |
| VALOR_UNITARIO | numeric(15) |  | S | Valor unitário - Portaria Cat nº 17/99 |
| SALDO_FINAL | numeric(16) |  | S | Valor final do estoque - Portaria Cat nº 17/99 |
| QUANTIDADE_FINAL_ICMS_ST | numeric(15) |  |  | Quantidade final ICMS ST |
| VALOR_UNITARIO_MEDIO_ICMS_ST | numeric(19) |  |  | Valor unitário médio ICMS ST |
| VALOR_FINAL_ICMS_ST | numeric(13) |  |  | Valor final ICMS ST |
| SALDO_VALIDO | char(1) |  | S |  |
