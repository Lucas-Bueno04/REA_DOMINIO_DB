# FOTROCAS_SINDPISO — TROCAS DOS PISOS DOS SINDICATOS
14.289 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | CÓDIGO DA EMPRESA |
| I_EMPREGADOS | integer(4) | PK |  | CÓDIGO DO EMPREGADO |
| DATA_TROCA | date(4) | PK |  | DATA DA TROCA |
| I_SINDICATOS | integer(4) |  | S | CÓDIGO DO SINDICATO |
| I_SINDPISO | integer(4) |  | S | CÓDIGO DO PISO DO SINDICATO |
| DATA_GRAVACAO | timestamp(8) |  |  | DATA E HORA DA GRAVAÇÃO |
| USUARIO | char(15) |  |  | USIÁRIO |
| PERIODO_CTRL | integer(4) |  |  | PERIODO DE CONTROLE |
| PERIODO_INICIO | date(4) |  |  | PERIODO INICIAL |
| PERIODO_FIM | date(4) |  |  | PERIODO FINAL |
| ORIGEM_REG | tinyint(1) |  | S | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| TIPO_PISO_SALARIAL | smallint(2) | PK |  | Tipo de piso salarial. (1=Normal/2=Período do contrato de experiência) |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
