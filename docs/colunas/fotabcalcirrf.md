# FOTABCALCIRRF — Tabela de IRRF
70 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_TABCALCIRRF | date(4) | PK |  | Competência |
| DESC_DEPEND | numeric(13) |  |  | Desconto por dependente |
| MINIMO_RETENCAO | numeric(13) |  |  | Mínimo para retenção |
| ORIGEM_SGD | smallint(2) |  |  | Tabela incluída através do processo de atualização automática do SGD. (0=Não/1=Sim) |
| VERSAO_TABELA_SGD | smallint(2) |  | S | Versão da tabela atualizada pelo SGD |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| DEDUCAO_SIMPLIFICADA_MENSAL | decimal(13) |  | S | Dedução Simplificada Mensal. |
