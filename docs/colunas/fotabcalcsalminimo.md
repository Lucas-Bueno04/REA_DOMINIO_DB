# FOTABCALCSALMINIMO — Tabela de Salário Mínimo
80 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_TABCALCSALMINIMO | date(4) | PK |  | Competência |
| VALOR | numeric(13) |  |  | Valor |
| ORIGEM_SGD | smallint(2) |  |  | Tabela incluída através do processo de atualização automática do SGD. (0=Não/1=Sim) |
| VERSAO_TABELA_SGD | smallint(2) |  | S | Versão da tabela atualizada pelo SGD |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
