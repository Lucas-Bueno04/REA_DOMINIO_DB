# FOAFASTAMENTOS_SOMAR_DIAS — Informações sobre os afastamentos que devem somar para calcular a data folha.
23 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| DATA_REAL_DN | numeric(10) | PK |  | Data numérica do afastamento |
| DATA_REAL_DN_AFASTAMENTO | numeric(10) | PK |  | Data numérica do afastamento |
| I_AFASTAMENTOS | integer(4) |  |  | Código do afastamento |
| DATA_REAL | date(4) |  |  | Data do afastamento |
| DATA_FIM | date(4) |  |  | Data final do afastamento |
| SELECIONADO | integer(4) |  | S | Linha selecionada |
| AFASTAMENTO_DECORRENTE_CONTAMINACAO_CORONAVIRUS | integer(4) |  | S | Afastamento decorrente de contaminação pelo coronavírus (Covid-19) (0 = Não/ 1 = Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
