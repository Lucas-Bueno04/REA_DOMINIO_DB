# PMCOMPLEMENTO_HISTORICO_CONTABIL — Complemento de Históricos Contábeis
156 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_TIPO | tinyint(1) | PK |  | TIPO (1=DEPRECIAÇÃO FISCAL/ 2=DEPRECIAÇÃO SOCIETÁRIA/ 3=BAIXA/ 4=TRANSFERÊNCIA DE CONTA PATRIMONIAL/ 5= AQUISIÇÃO DE BENS) |
| HISTORICO | varchar(500) |  |  | Descrição |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
