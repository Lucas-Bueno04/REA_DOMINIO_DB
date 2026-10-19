# FOENCARGOS_PENSAO_ALIMENTICIA — Encargo de pensão alimentícia.
789 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| COMPETENCIA | date(4) | PK |  | Competência. |
| TIPO_PROCESSO | integer(4) | PK |  | Tipo de processo. |
| DATA_PAGAMENTO | date(4) | PK |  | Data de pagamento. |
| RESCISAO | smallint(2) | PK |  | Encargo referente a rescisão (0=Não/1=Sim). |
| VALOR | numeric(13) |  |  | Valor. |
| I_PAGTO | integer(4) |  | S | Código do pagamento. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
