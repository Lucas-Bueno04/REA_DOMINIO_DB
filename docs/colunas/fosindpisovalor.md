# FOSINDPISOVALOR — GURDA O VALOS DO PISO DOS SINDICATOS
191 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_SINDICATOS | integer(4) | PK |  | CÓDIGO DO SINDICATO |
| I_SINDPISO | integer(4) | PK |  | CÓDIGO DO PISO DO SINDICATO |
| COMPETENCIA | date(4) | PK |  | COMPETENCIA |
| VALOR | numeric(13) |  |  | VALOR DE ACORDO COM A COMPETENCIA |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| COMPETENCIA_RETROATIVA | date(4) |  | S | Competência retroativa. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
