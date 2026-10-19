# FOMEDIDAS_PROTECAO_EMPREGO_COVID_19_AFASTAMENTOS — Relacionamento entre medidas de proteção ao empregado devido a COVID-19 e o afastamento
233 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| DATA_INICIO | date(4) | PK |  | Data do início da vigência da medida |
| DATA_REAL_DN | numeric(10) | PK |  | Data do afastamento |
| SEQUENCIAL | integer(4) | PK |  | Sequencial usado para quando houver uma medida cancelada na mesma data de início ao empregado |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
