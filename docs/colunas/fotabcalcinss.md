# FOTABCALCINSS — Tabela de INSS
80 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_TABCALCINSS | date(4) | PK |  | Competência |
| RAT_15 | numeric(13) |  |  | Acréscimo RAT 15 anos |
| RAT_20 | numeric(13) |  |  | Acréscimo RAT 20 anos |
| RAT_25 | numeric(13) |  |  | Acréscimo RAT 25 anos |
| MINIMO_RECOLHIMENTO | numeric(13) |  |  | Mínimo para recolhimento |
| ORIGEM_SGD | smallint(2) |  |  | Tabela incluída através do processo de atualização automática do SGD. (0=Não/1=Sim) |
| VERSAO_TABELA_SGD | smallint(2) |  | S | Versão da tabela atualizada pelo SGD |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
