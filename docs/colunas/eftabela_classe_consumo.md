# EFTABELA_CLASSE_CONSUMO — Tabela de Classe de Consumo - SPED e SEF 2012
101 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CLASSE_CONSUMO | integer(4) | PK |  | Código sequencial |
| TIPO | integer(4) |  |  | Tipo (1=SPED / 2=SEF 2012) |
| ESPECIE | char(2) |  |  | Espécie |
| DESCRICAO | varchar(255) |  |  | Descrição |
| CODIGO_SPED | integer(4) |  | S | Código SPED |
| CODIGO_SEF | integer(4) |  | S | Codigo SEF 2012 |
