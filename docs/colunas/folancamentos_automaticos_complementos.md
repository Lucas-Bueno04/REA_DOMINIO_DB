# FOLANCAMENTOS_AUTOMATICOS_COMPLEMENTOS — Lançamentos automáticos de eventos para complementos de cálculos
115 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_LANCTOSAUTO | integer(4) | PK |  | Código do lançamento automático |
| I_CALCULOS_COMPLEMENTOS_OLD | integer(4) |  | S | Código do complemento de cálculo - Renomeado |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro: (0=Sistema, 1=Importação de tabelas, 2=Importação de leiaute, 3=Conversão) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS_COMPLEMENTOS | uniqueidentifier(16) | PK |  | Código do complemento de cálculo |
