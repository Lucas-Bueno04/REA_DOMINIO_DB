# efsp_produtos — Tabela de Produtos - Combustível / Solvente
40 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codigo_spp | integer(4) | PK |  | Codigo do produtos |
| descricao_spp | varchar(50) |  | S | Descricao do produto |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| uf_spp | char(2) | PK |  | Estado |
