# FOESOCIAL_ARQUIVO_RETORNO_S_5003_BASE_SERVICOS_MATRICULA_VALOR — Informações sobre FGTS do retorno do eSocial no arquivo S-5003.
19.091 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_DADOS_EVENTOS | integer(4) | PK |  | Código do evento referente a FOESOCIAL_DADOS_EVENTOS |
| I_SERVICOS | integer(4) | PK |  | Código do serviço referente a FOSERVICOS |
| MATRICULA | varchar(30) | PK |  | Matrícula |
| CODCATEG | integer(4) |  |  | Código da categoria |
| TPVALOR | integer(4) | PK |  | Tipo do valor |
| REMFGTS | numeric(30) |  | S | Valor de remuneração FGTS |
| CODI_EMP_SERVICO | integer(4) | PK |  | Código da empresa do serviço referente a FOSERVICOS |
