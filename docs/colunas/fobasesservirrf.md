# fobasesservirrf — Bases de Calculo - Base de IRRF
338.941 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo da empresa |
| i_empregados | integer(4) | PK |  | Código do empregado |
| competencia | date(4) | PK |  | Competência |
| tipo_process | integer(4) | PK |  | Tipo da Folha |
| i_servicos | integer(4) | PK |  | Código do serviço |
| rateio | integer(4) | PK |  | Indica se a linha e resultado de um rateio de calculo |
| I_BASESIRRF_OLD | integer(4) |  | S | Numero sequencia que identifica a base - Renomeado |
| teve_rpa | integer(4) |  |  | teve rpa? (1=sim, 0=nao) |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo - Renomeado |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo |
| I_BASESIRRF | uniqueidentifier(16) | PK |  | Numero sequencia que identifica a base |
