# FOCALCULOS_COMPLEMENTOS — Complementos de cálculo
232 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CALCULOS_COMPLEMENTOS_OLD | integer(4) |  | S | Código - Renomeado |
| CODI_EMP | integer(4) |  |  | Código da empresa |
| COMPETENCIA | date(4) |  |  | Competência do cálculo |
| DATA | date(4) |  |  | Data do complemento |
| ORIGEM | smallint(2) |  |  | Origem do complemento. (1=Lançamento de eventos/2=Alteração salarial/3=Rescisão/4=Alteração salarial CCT) |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro: (0=Sistema, 1=Importação de tabelas, 2=Importação de leiaute, 3=Conversão) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS_COMPLEMENTOS | uniqueidentifier(16) | PK |  | Código |
| I_CALCULOS_COMPLEMENTOS_EXPORTA_IMPORTA | uniqueidentifier(16) |  | S | Código do complemento de cálculo para usar no exporta/importa. |
