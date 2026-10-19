# GERAEXECUTAR_EMPRESAS_OPCOES_CONTABILIDADE — Informações da contabilidade por empresa utilizados na rotina automatica
6 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_EXECUTARRA | integer(4) | PK |  | Código da execução |
| I_SISTEMA | smallint(2) | PK |  | Código do sistema |
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| PROCESSO | integer(4) | PK |  | Processo da contabilidade (1-Importação Extrato/2-Conciliação Bancaria) |
| OPCAO_CAMPO | varchar(128) | PK |  | Campo da opção da contabilidade |
| OPCAO_VALOR | varchar(512) |  | S | Valor da opção da contabilidade |
