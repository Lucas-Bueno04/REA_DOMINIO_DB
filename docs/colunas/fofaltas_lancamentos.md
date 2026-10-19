# FOFALTAS_LANCAMENTOS — RELACIONAMENTO ENTRE FALTAS E LANCAMENTOS
14.964 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | CODIGO EMPRESA |
| I_EMPREGADOS | integer(4) | PK |  | EMPREGADO |
| COMPETENCIA | date(4) | PK |  | COMPETENCIA |
| TIPO_PROCES | smallint(2) | PK |  | TIPO DE CALCULO |
| I_EVENTOS | integer(4) | PK |  | EVENTO |
| I_FALTAS | integer(4) | PK |  | SEQUENCIAL DE FALTAS DO EMPREGADO |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| TIPO_LANCAMENTO | smallint(2) | PK |  | Tipo do lançamento: 1=Mensal/2=Fixo |
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
