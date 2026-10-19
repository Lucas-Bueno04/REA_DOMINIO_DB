# FOFERIAS_LANCAMENTOS_PLANOSAUDE — Lançamentos de férias - Processos - Plano de saúde
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| I_FERIAS_GOZO | integer(4) | PK |  | Código do gozo |
| I_EVENTOS | integer(4) | PK |  | Código do evento |
| I_BENEFICIARIO | integer(4) | PK |  | Sequencial de beneficiário |
| I_FILHOS | integer(4) |  | S | Cóigo do dependente |
| VALOR | numeric(13) |  |  | Valor |
| ORIGEM_REG | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| I_OPERADORAPLANOSAUDE | integer(4) |  |  | Código da operadora de plano de saúde |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
