# FOAMBIENTES_TRABALHO_ALTERACAO — Alterações do ambiente de trabalho.
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_AMBIENTE_TRABALHO | integer(4) | PK |  | Código do ambiente de trabalho. |
| VIGENCIA | date(4) | PK |  | Vigência. |
| NOME | varchar(100) |  |  | Nome do ambiente de trabalho. |
| LOCAL | smallint(2) |  |  | Local. (1=Estabelecimento do próprio empregador/2=Estabelecimento de terceiros/3=Prestação de serviços em instalações de terceiros sem relação de cessão de mão de obra) |
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
