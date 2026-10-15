# efnatureza — Naturezas - Cadastro
1.548 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_nat | integer(4) | PK |  | Codigo |
| nome_nat | varchar(512) |  |  | Nome |
| versao_nat | smallint(2) | PK |  | Versao |
| masc_nat | char(7) |  | S | Mascara |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
