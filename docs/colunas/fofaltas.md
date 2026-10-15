# FOFALTAS — CADASTRO DE FALTAS DOS EMPREGADOS
15.865 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | CODIGO EMPRESA |
| I_EMPREGADOS | integer(4) | PK |  | CODIGO |
| I_FALTAS | integer(4) | PK |  | SEQUENCIAL DE FALTAS DO EMPREGADO |
| DIA | date(4) |  |  | DIA QUE OCORREU A FALTA |
| ORIGEM | smallint(2) |  |  | Origem lançamento. (1=Lançamento de rubricas/2=Data para férias/3=Advertência e Suspensão) |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| TIPO | smallint(2) |  |  | Tipo de falta. (1=Normal/2=DSR/3=Reembolso/4=Parcial/5=Noturna/6=DSR Noturna/7=Suspensão/8=DSR suspensão) |
| VALOR | numeric(13) |  | S | Quantidade de horas da falta parcial. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
