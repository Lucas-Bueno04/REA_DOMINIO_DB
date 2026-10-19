# FOTABCALCFAP — Tabela de FAP
481 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_TABCALCFAP | date(4) | PK |  | Competência |
| FATOR | numeric(6) |  |  | Fator |
| POSSUI_PROCESSO_JUDICIAL_ADMINISTRATIVO_MODIFICA_FATOR | smallint(2) |  |  | Possui processo judicial ou administrativo que modifica o fator. (0=Não/1=Sim) |
| I_PROCESSO | integer(4) |  | S | Código do processo administrativo/judicial. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
