# FOVARIAVEL_PLANOSAUDE — Lançamentos - Processos - Plano de saúde
17.646 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| COMPETENCIA | date(4) | PK |  | Competência |
| TIPO_PROCES | smallint(2) | PK |  | Tipo de cálculo |
| I_EVENTOS | integer(4) | PK |  | Código do evento |
| I_BENEFICIARIO | integer(4) | PK |  | Sequencial de beneficiário |
| I_FILHOS | integer(4) |  | S | Código do dependente |
| VALOR | numeric(13) |  |  | Valor |
| ORIGEM_REG | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| I_OPERADORAPLANOSAUDE | integer(4) |  |  | Código da operadora de plano de saúde |
| TIPO_LANCAMENTO | smallint(2) | PK |  | Tipo do lançamento: 1=Mensal/2=Fixo |
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
| SEQUENCIAL_LANCAMENTO | integer(4) | PK |  | Sequencial lançamento |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
