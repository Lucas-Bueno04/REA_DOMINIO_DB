# HRPARAMETRO_INTERVALO_LOTE — Parametro Honorarios - Intervalo de Lote
3 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritório |
| I_INTERVALO | integer(4) | PK |  | Código |
| INICIAL | numeric(17) |  |  | Inicial |
| FINAL | numeric(17) |  |  | Final |
| ULTIMO_UTILIZADO | numeric(17) |  | S | Último codigo de intervalo utilizado pelo nosso numero |
| INUTILIZAR_INTERVALO | char(1) |  |  | Inutilizar intervalo (S/N) |
| TIPO_INTERVALO | char(1) |  |  | Tipo de invervalo (U=Usuario/S=Sistema) |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| I_SEQUENCIAL_LOTE | integer(4) | PK |  | Sequencial do lote. |
