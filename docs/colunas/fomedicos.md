# FOMEDICOS — Tabela de médicos/dentistas
720 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_MEDICOS | integer(4) | PK |  | Código do médico/dentista. |
| NOME | varchar(100) |  |  | Nome do médico/dentista. |
| ORGAO_CLASSE | smallint(2) |  | S | Orgão de classe. (1=CRM/2=CRO/3=RMS) |
| NUMERO_ORGAO_CLASSE | varchar(14) |  | S | Número do orgão de classe. |
| CODIGO_ESTADO | integer(4) |  | S | Código do estado. |
| FORMA_CONTATO | varchar(100) |  | S | Forma de contato. |
| TELEFONE | varchar(15) |  | S | Telefone. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro (0=Sistema/ 1=Imp Tabelas/ 2=Imp Layout/ 3=Imp tabelas concorrentes) |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| CPF | char(11) |  | S | CPF. |
