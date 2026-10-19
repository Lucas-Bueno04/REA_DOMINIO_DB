# FOESOCIAL_ARQUIVO_RETORNO_S_5003_BASE_SERVICOS_MATRICULA — Informações sobre FGTS do retorno do eSocial no arquivo S-5003.
22.426 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_DADOS_EVENTOS | integer(4) | PK |  | Código do evento referente a FOESOCIAL_DADOS_EVENTOS |
| I_SERVICOS | integer(4) | PK |  | Código do serviço referente a FOSERVICOS |
| MATRICULA | varchar(30) | PK |  | Matrícula |
| CODCATEG | integer(4) |  |  | Código da categoria |
| CODI_EMP_SERVICO | integer(4) | PK |  | Código da empresa do serviço referente a FOSERVICOS |
| SEQUENCIAL | integer(4) | PK |  | Sequencial para registros repetidos |
