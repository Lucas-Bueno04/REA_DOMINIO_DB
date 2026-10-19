# folanctomedias — Lancamento de eventos para medias
18.103 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | codigo da empresa |
| i_empregados | integer(4) | PK |  | Codigo do empregado |
| competencia | date(4) | PK |  | Competencia |
| i_eventos | integer(4) | PK |  | Codigo do evento |
| valor | numeric(13) |  |  | Valor |
| origem | tinyint(1) | PK |  | 1=Usuario, 2=Ferias, 3=Afastamentos |
| I_FERIAS_GOZO | integer(4) |  | S | Código do gozo |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
