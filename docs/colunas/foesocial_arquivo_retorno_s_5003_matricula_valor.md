# FOESOCIAL_ARQUIVO_RETORNO_S_5003_MATRICULA_VALOR — Informações sobre FGTS do retorno do eSocial no arquivo S-5003.
19.091 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_DADOS_EVENTOS | integer(4) | PK |  | Código do evento referente a FOESOCIAL_DADOS_EVENTOS |
| MATRICULA | varchar(30) | PK |  | Matrícula |
| CODCATEG | integer(4) | PK |  | Código da categoria |
| TPDPS | integer(4) | PK |  | Tipo de depósito de FGTS |
| DPSFGTS | numeric(30) |  | S | Valor de Depósito de FGTS |
