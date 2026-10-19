# rgdadosdw_linhas — Dados do relatorios - Linhas
81 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| tipo | char(128) | PK |  | Tipo de documento |
| codigo | integer(4) | PK |  | Codigo |
| nomedw | char(100) | PK |  | Dataobject ou codigo do relatorio do gerador |
| linha | integer(4) | PK |  | Linha |
| nome | varchar(100) | PK |  | Nome do campo/coluna |
| tipo_dado | tinyint(1) |  |  | Tipo do dado (1=String, 2=Long, 3=Decimal, 4=Date, 5=Time, 6=DateTime) |
| dados | varchar(5000) |  |  | Dados da coluna |
