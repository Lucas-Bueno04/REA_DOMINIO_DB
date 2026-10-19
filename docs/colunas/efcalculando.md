# efcalculando — Usuarios calculando apuracao
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| usuario | char(30) | PK |  | Usuario |
| connection_id | integer(4) | PK |  | Identificador da conexao |
| LOGIN_TIME | varchar(32) |  | S | Propriedade LoginTime do connection ID |
| INICIO_APURACAO | timestamp(8) |  |  | Inicio da Apuração |
