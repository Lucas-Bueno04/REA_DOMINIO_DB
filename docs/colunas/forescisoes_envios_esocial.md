# FORESCISOES_ENVIOS_ESOCIAL — Envios das rescisões ao eSocial
5.230 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Código da empresa |
| i_empregados | integer(4) | PK |  | Código do empregado |
| tipo | integer(4) | PK |  | Tipo de rescisão |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo - Renomeado |
| CODI_EMP_DADOS_EVENTOS | integer(4) | PK |  | Código da empresa referente a FOESOCIAL_DADOS_EVENTOS |
| I_DADOS_EVENTOS | integer(4) | PK |  | Código do evento referente a FOESOCIAL_DADOS_EVENTOS |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo. |
