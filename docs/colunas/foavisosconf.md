# foavisosconf — Avisos de calculo
22 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_avisosconf | integer(4) | PK |  | TIPO DO AVISO: (1-12) |
| ativar | tinyint(1) |  |  | is Status |
| periodo_antes | integer(4) |  |  | No meses antecedencia |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| UNIDADE_PERIODO | integer(4) |  |  | Unidade do Período (1=Dias e 2=Meses). |
| PERIODO_AVISO | smallint(2) |  |  | Período de aviso. (1=Período de antecedência/2=No mês do vencimento/3=Período de antecedência do vencimento do período concessivo) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| DEFINIR_COMPETENCIA_INICIO_AVISO | smallint(2) |  |  | Definir competência início aviso. (0=Não/1=Sim) |
| COMPETENCIA_INICIO_AVISO | date(4) |  | S | Competência início aviso. |
