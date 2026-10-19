# HRCONTA_CORRENTE_ESCRITORIO_IMPOSTOS — Tabela de detalhamento de imposto/encargo para cada movimentacao financeira
634 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_MOVIMENTO_ESCRITORIO | integer(4) | PK |  | Código movimentacao financeira |
| I_SEQUENCIAL | integer(4) | PK |  | Sequencial |
| CODI_IMP | integer(4) |  |  | Imposto |
| VALOR | numeric(13) |  |  | Valor do imposto |
