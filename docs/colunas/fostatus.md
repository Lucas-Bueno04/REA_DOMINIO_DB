# FOSTATUS — INDICA A SITUACAO DO SISTEMA PARA DETERMINADOS PROCESSOS
4 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_STATUS | char(10) | PK |  | NOME DO STATUS |
| VALOR | char(30) |  |  | VALOR DO STATUS |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
