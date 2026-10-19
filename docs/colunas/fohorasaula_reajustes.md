# fohorasaula_reajustes — Tabela com reajuste de horas aula
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | codigo da empresa |
| i_horasaula | integer(4) | PK |  | codigo das horas aula |
| i_horasaula_reajustes | integer(4) | PK |  | codigo das horas aula reajuste |
| data_reajuste | date(4) |  |  | data do reajuste |
| valor | decimal(13) |  |  | valor do reajuste |
| periodo_inicio | date(4) |  |  | periodo inicial |
| periodo_fim | date(4) |  |  | periodo final |
| forma_alteracao | tinyint(1) |  |  | Forma de alteracao 1=Novo valor 2=Adcionar valor 3=Percentual de almento |
| valor_alteracao | decimal(13) |  |  | Valor da alteracao |
| origem_reg | tinyint(1) |  | S | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| ALTERACAO_RETROATIVA | smallint(2) |  |  | Alteração retroativa. (0=Não/1=Sim) |
| COMPETENCIA_RETROATIVA | date(4) |  | S | Competência retroativa. |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
