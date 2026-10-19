# focalcmedias_mem_oper — Operacao memoria de calculo
4.364.870 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) |  |  | Empresa |
| i_empregados | integer(4) |  |  | Empregado |
| tipo_media | tinyint(1) |  |  | is Tipo de media |
| data_calculo | date(4) |  |  | Data calculo |
| inicio_aquisitivo | date(4) |  |  | Inicio aquisitivo |
| i_operacao | integer(4) | PK |  | Operacao |
| tipo | tinyint(1) |  |  | Tipo descricao |
| descricao | varchar(160) |  |  | Descricao da operacao |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| CODI_EMP_ORIGEM | integer(4) |  |  | Código da empresa de origem |
| I_EMPREGADOS_ORIGEM | integer(4) |  |  | Código do empregado de origem |
| SIMULACAO | integer(4) |  |  | Código sequencial da simulação |
| I_CALCMEDIAS_MEM_OLD | integer(4) |  | S | Código da memória de cálculo - Renomeado |
| SIMULACAO_MAIS_FAVORAVEL | smallint(2) |  |  | Simulação de média mais favorável por rubrica. |
| VALOR_CONVERSAO_DIAS | numeric(13) |  | S | Valor de conversão de dias |
| I_EVENTOS | integer(4) |  | S | Código do evento |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCMEDIAS_MEM | uniqueidentifier(16) | PK |  | Código da memória de cálculo |
