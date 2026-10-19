# fodadoutraemp — Outras Bases INSS - Processos
91 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_empregados | integer(4) | PK |  | Empregado |
| competencia | date(4) | PK |  | Competencia |
| base_inss | numeric(13) |  |  | Base INSS |
| valor_inss | numeric(13) |  |  | Valor INSS |
| tipo | tinyint(1) |  | S | Tipo |
| tipo_process | integer(4) | PK |  | Tipo folha |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| SEQUENCIAL | integer(4) | PK |  | SEQUENCIAL |
| COMPETENCIA_INICIO | date(4) |  | S | Competência para o início do lançamento fixo. |
| DETERMINAR_FIM | smallint(2) |  | S | Determinar competência para o fim do lançamento fixo. (0=Não/1=Sim) |
| COMPETENCIA_FIM | date(4) |  | S | Competência para o fim do lançamento fixo. |
| TIPO_INSCRICAO | smallint(2) |  | S | Tipo de inscrição. (1=CNPJ/2=CPF) |
| INSCRICAO | varchar(14) |  | S | Inscrição. |
| NOME_EMPRESA | varchar(40) |  | S | Nome da empresa. |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| CATEGORIA | smallint(2) |  |  | Categoria do colaborador. |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
