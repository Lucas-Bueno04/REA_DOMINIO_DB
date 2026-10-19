# FOFILIAIS_FAP — Informações do FAP para a filial a partir de 01/2016.
2.957 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_FILIAIS | integer(4) | PK |  | Código da filial |
| VIGENCIA | date(4) | PK |  | Vigência |
| FATOR | numeric(6) |  |  | Fator do FAP |
| POSSUI_PROCESSO_JUDICIAL_ADMINISTRATIVO_MODIFICA_FATOR | smallint(2) |  |  | Possui processo judicial administrativo (0=Não/1=Sim) |
| I_PROCESSO | integer(4) |  | S | Código do processo |
| CODIGO_SUSPENSAO_PROCESSO_MODIFICA_FATOR | varchar(14) |  | S | Código de suspensão do processo que modifica o fator. |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
