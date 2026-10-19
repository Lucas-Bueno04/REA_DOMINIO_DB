# FOFILHOS_ALTERACAO — Registros de alteração de dependentes.
3.978 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| I_FILHOS | integer(4) | PK |  | Código do dependente. |
| DATA_ALTERACAO | date(4) | PK |  | Data da alteração. |
| GRAU_PARENTESCO | integer(4) |  |  | Grau de parentesco |
| NOME | varchar(60) |  |  | Nome do dependente |
| DATA_NASCTO | date(4) |  | S | Data de nascimento |
| CPF | varchar(11) |  | S | CPF |
| DEPENDENTE | char(1) |  |  | É dependente |
| FILHO | char(1) |  |  | É filho(a) |
| POSSUI_DEFICIENCIA_FISICA_MENTAL | smallint(2) |  |  | Possui deficiência física ou mental |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Imp. tabelas/2=Imp. layout/3=Imp. tabelas concorrentes) |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| CONSIDERAR_ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar dependente ao eSocial. (0=Não/1=Sim) |
| SEXO_DEPENDENTE | char(1) |  |  | Sexo do dependente. (M=Masculino/F=Feminino) |
