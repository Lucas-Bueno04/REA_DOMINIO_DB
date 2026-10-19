# hntipocontrato — Tipos de Contratos - Cadastro
3 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_tipocontrato | integer(4) | PK |  | Codigo do tipo de contrato |
| tiporeajuste_crt | char(1) |  |  | Tipo de reajuste do contrato (M - Mensal/B - Bimestral/T - Trimestral/Q - Quadrimestral/S - Semestral/A - Anual/D - Data base) |
| periodicidadefat_crt | char(1) |  |  | Periodicidade de faturamento (M - Mensal/B - Bimestral/T - Trimestral/Q - Quadrimestral/S - Semestral/A - Anual) |
| descricao_crt | varchar(50) |  |  | Descricao dos servicos |
| mesbase_crt | tinyint(1) |  | S | Mes base para reajuste do contrato utilizado quando o tipo de reajuste for Data Base |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
