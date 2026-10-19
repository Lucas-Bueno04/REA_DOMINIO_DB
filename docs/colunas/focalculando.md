# focalculando — Controle de concorrencia
186 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) |  | S | Codigo da empresa |
| i_empregados | integer(4) |  | S | Codigo do empregado |
| usuario | char(30) |  | S | Usuario |
| connection_id | integer(4) |  | S | Identificacao da conexao |
| TIPO_CALCULO | smallint(2) |  | S | Tipo de calculo. (1=Folha/2=Provisão Férias/3=Provisão 13º/4=Férias) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULANDO | bigint(8) | PK |  | Código sequencial |
| LOGIN_TIME | varchar(32) |  | S | Propriedade LoginTime do connection ID |
