# FOAMBIENTES_TRABALHO — Ambiente de trabalho.
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_AMBIENTE_TRABALHO | integer(4) | PK |  | Código do ambiente de trabalho. |
| NOME | varchar(100) |  |  | Nome do ambiente de trabalho. |
| DATA_INICIO | date(4) |  |  | Data início. |
| SITUACAO | smallint(2) |  |  | Situação (0=Inativo/1=Ativo). |
| DATA_INATIVACAO | date(4) |  | S | Data de inativação. |
| CODIGO_ESOCIAL | varchar(30) |  | S | Código no eSocial. |
| LOCAL | smallint(2) |  |  | LOCAL. (1=ESTABELECIMENTO DO PRÓPRIO EMPREGADOR/2=ESTABELECIMENTO DE TERCEIROS) |
| I_SERVICOS | integer(4) |  | S | Código do serviço. |
| TIPO_INSCRICAO | smallint(2) |  | S | Tipo de inscrição (1=CNPJ/2=CPF/3=CEI/6=CAEPF/7=CNO). |
| INSCRICAO | varchar(14) |  | S | Inscrição. |
| DESCRICAO | varchar(8000) |  |  | Descrição do ambiente de trabalho. |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
