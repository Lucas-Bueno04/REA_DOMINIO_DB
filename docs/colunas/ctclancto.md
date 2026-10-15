# ctclancto — Lancamento do centro de custo
46.687 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo da empresa |
| nume_ccu | integer(4) | PK |  | Numero do lancamento |
| cdeb_ccu | integer(4) | PK |  | Conta debito do centro de custo |
| ccre_ccu | integer(4) | PK |  | Conta credito do centro de custo |
| codi_cta | integer(4) |  |  | Conta contabil |
| data_ccu | date(4) |  |  | Data do lancamento |
| vlor_ccu | numeric(13) |  |  | Valor do lancamento |
| fili_ccu | integer(4) |  |  | Codigo da filial |
| nume_lan | integer(4) |  | S | Numero Lancto. Contabil |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
