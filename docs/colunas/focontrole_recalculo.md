# FOCONTROLE_RECALCULO — Controle de alteração nos cálculos para recálculo
52.082 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| TIPO_PROCESSO | integer(4) | PK |  | Tipo de cálculo |
| COMPETENCIA | date(4) | PK |  | Competência |
| VERSAO_CALCULO | integer(4) |  |  | Versão do cálculo |
| VERSAO_RECALCULO | integer(4) |  |  | Versão do recálculo |
| STATUS_CALCULO | smallint(2) |  |  | Status do cálculo (1=NOVO/2=MODIFICADO/3=PENDENTE) |
