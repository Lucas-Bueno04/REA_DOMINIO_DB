# CTGRUPOSDRA — Estrutura DRA
21.168 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODIGO | integer(4) | PK |  | Codigo |
| SEQUENCIA | integer(4) |  |  | Sequencia dos grupos |
| DESCRICAO | varchar(100) |  |  | Descricao |
| OPERACAO | char(1) |  |  | Operacao (C=Contas/ T=Total) |
| SOMA | char(1) |  | S | Soma (C=Acima/ B=Abaixo/ G=Geral) |
| GRUPOS | integer(4) |  | S | Grupos |
| TIPO | char(1) |  |  | Tipo (T=Saldo total / D=Total débito / C=Total crédito) |
