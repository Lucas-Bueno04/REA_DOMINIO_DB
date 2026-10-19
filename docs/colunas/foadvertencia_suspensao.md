# FOADVERTENCIA_SUSPENSAO — Cadastro de advertências e suspensões de empregados
37 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| DATA | date(4) | PK |  | Data da advertência/suspensão. |
| SEQUENCIAL | smallint(2) | PK |  | Sequencial. |
| REINCIDENCIA | smallint(2) |  |  | Reincidente. (0=Não/1=Sim) |
| SUSPENSAO | smallint(2) |  |  | Suspensão. (0=Não/1=Sim) |
| DATA_INICIO | date(4) |  | S | Data início da advertência/suspensão. |
| QUANTIDADE_DIAS | integer(4) |  | S | Quantidade de dias da advertência/suspensão. |
| DATA_RETORNO | date(4) |  | S | Data de retorno da advertência/suspensão. |
| MOTIVO | varchar(1000) |  |  | Motivo da advertência/suspensão. |
| ORIGEM_REG | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
