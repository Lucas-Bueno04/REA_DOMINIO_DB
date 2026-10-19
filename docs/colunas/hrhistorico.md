# HRHISTORICO — Historicos financeiros
11 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_HISTORICO | integer(4) | PK |  | Codigo |
| TIPO | tinyint(1) |  |  | Tipo 1 Geral 2 Lancto de contas a pagar 3 Pagamento 4 Recebimento 5 Adiantamentos 6 Pagto de impostos 7 Pagto de funcionarios 8 Movto de conta Entrada 9 Movto de conta Saida 10 Movto Transf 11 Renegocicao |
| HISTORICO | varchar(512) |  |  | Descricao |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
