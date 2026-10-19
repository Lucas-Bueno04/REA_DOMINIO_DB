# GERAEXECUTAR_EMPRESAS_OPCOES_HONORARIOS — Informações do honorarios por empresa utilizados na rotina automatica
40 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_EXECUTARRA | integer(4) | PK |  | Código da execução |
| I_SISTEMA | smallint(2) | PK |  | Código do sistema |
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| OPCAO_ID | varchar(128) | PK |  | ID da opção do honorarios |
| OPCAO_VALOR | long varchar(32767) |  | S | Valor da opção do honorarios |
