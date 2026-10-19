# FOBASESSERV_ENVIOS_ESOCIAL — Envios de bases de cálculo para o esocial
349.595 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Código da empresa |
| i_empregados | integer(4) | PK |  | Código do empregado |
| competencia | date(4) | PK |  | Competência |
| tipo_process | integer(4) | PK |  | Tipo da folha |
| i_servicos | integer(4) | PK |  | Código do serviço |
| rateio | integer(4) | PK |  | Rateio |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo - Renomeado |
| CODI_EMP_DADOS_EVENTOS | integer(4) | PK |  | Código da empresa referente a FOESOCIAL_DADOS_EVENTOS |
| I_DADOS_EVENTOS | integer(4) | PK |  | Código do evento referente a FOESOCIAL_DADOS_EVENTOS |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo. |
