# focontrrpaserv — RPA Emitidas - Rateio por serviços
1.994 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Código da empresa |
| i_empregados | integer(4) | PK |  | Código do empregado |
| numero | numeric(10) | PK |  | Número RPA |
| i_servicos | integer(4) | PK |  | Código do serviço |
| valor | numeric(13) |  |  | Valor da RPA referente ao serviço |
| perc_permanencia | numeric(13) |  |  | Percentual do tempo total que o contr. trab. no serviço |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
