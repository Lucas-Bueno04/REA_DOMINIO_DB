# FODOMINIO_BENEFICIOS_CONTROLE_IDENTIFICADOR_EMPREGADO — Controle de alterações dos identificadores de empregados para integração com Fintech
16.882 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CONTROLE_IDENTIFICADOR | integer(4) | PK |  | Sequencial do controle |
| DATA_HORA | timestamp(8) |  |  | Data e hora da alteração |
| USUARIO | varchar(128) |  |  | Usuário que realizou a alteração |
| OPERACAO | varchar(20) |  |  | Tipo de operação (Inserção, Atualização) |
| CODI_EMP | integer(4) |  |  | Código da empresa |
| I_EMPREGADOS | integer(4) |  |  | Código do empregado |
| GUID_ONVIO_ANTES | uniqueidentifier(16) |  | S | GUID Onvio anterior |
| GUID_ONVIO_DEPOIS | uniqueidentifier(16) |  | S | GUID Onvio posterior |
| BANKING_EMPLOYEE_ID_ANTES | uniqueidentifier(16) |  | S | Banking Employee ID anterior |
| BANKING_EMPLOYEE_ID_DEPOIS | uniqueidentifier(16) |  | S | Banking Employee ID posterior |
