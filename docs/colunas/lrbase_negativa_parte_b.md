# LRBASE_NEGATIVA_PARTE_B — Cadastro de Base Negativa e Parte B
183 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_BASE_NEGATIVA_PARTE_B | integer(4) | PK |  | Código |
| DESCRICAO | varchar(140) |  |  | Descrição |
| CONTA | char(1) |  |  | Conta (B=Base Negativa/ P=Parte B) |
| COMPENSAR | tinyint(1) |  |  | Compensar (1=Prejuízo operacional geral/ 2=Prejuízo não operacional geral/ 3=Prejuízo de atividade rural/ 4=Não compensar) |
| DATA_CADASTRO | date(4) |  |  | Data de cadastro |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| CONSIDERAR_SALDO_DESTA_CONTA_POR_LANCAMENTO | char(1) |  |  | Considerar o saldo desta conta por lançamento |
| IDENTIFICADOR_SPED_ECF | varchar(30) |  |  | Identificador SPED ECF |
| TIPO_CONTA_SPED_ECF | integer(4) |  | S | Codigo padrao rfb parte B |
