# CTEXTRATO_BANCARIO_LANCAMENTO — Lançamento de extrato bancário
208 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_LANCAMENTO | integer(4) | PK |  | Código |
| COMPETENCIA | date(4) |  |  | Competência |
| CODI_CTA | integer(4) |  |  | Conta contábil do banco |
| SALDO_INICIAL | numeric(13) |  |  | Saldo inicial |
| NATUREZA | char(1) |  |  | Natureza do saldo inicial (P=Positivo/ N=Negativo) |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
