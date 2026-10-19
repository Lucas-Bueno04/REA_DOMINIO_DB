# HRCONTRATO_ALTERACAO — Contratos - Alterações
32 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| i_CONTRATO | integer(4) | PK |  | Código do contrato |
| DATA_ALTERACAO | date(4) | PK |  | Data da alteração |
| I_CAMPO | integer(4) | PK |  | Campo alterado |
| DE | varchar(255) |  |  | Valor anterior a alteracao |
| PARA | varchar(255) |  |  | Valor posterior a aleracao |
