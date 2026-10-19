# eftabelamuni_itens — Tabelas Municipais - Cadastro - Itens
630 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_tabela | integer(4) | PK |  | Codigo da Tabela Municipal |
| i_item | char(20) | PK |  | Valor do item |
| descricao | char(60) |  |  | Descricao |
| padrao | char(1) |  |  | Valor padrao (S/N) |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
