# fofilhos — Empregados - Cadastro - Dependentes
3.828 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_empregados | integer(4) | PK |  | Codigo Empregado |
| i_filhos | integer(4) | PK |  | Codigo do dependente |
| nome | char(60) |  |  | Nome do dependente |
| data_nascto | date(4) |  | S | Data nascimento |
| local_nascto | char(40) |  | S | Local nascimento |
| cartorio_registro | char(40) |  | S | Cartorio registro |
| num_reg_cart | char(10) |  | S | Num. Reg. Cart. |
| filho | char(1) |  |  | Filho |
| idade_fim_fil | integer(4) |  |  | Valido ate (filho) |
| dependente | char(1) |  |  | dependente |
| idade_fim_dep | integer(4) |  | S | Valido ate (dependente) |
| grau_parentesco | integer(4) |  |  | Grau parentesco. |
| nlivro | char(8) |  | S | No. livro |
| nfolha | char(8) |  | S | No. folha |
| data_entrega | date(4) |  | S | Entrega doc. |
| vencto_cart_vacina | date(4) |  | S | Vencto. At. Freq. |
| vencto_atest_freq | date(4) |  | S | Vencto. Cart. Vacina |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| PLANO_SAUDE_OPTANTE | char(1) |  | S | ** SEM USO ** Optande do plano de saúde |
| PLANO_SAUDE_INICIO | date(4) |  | S | ** SEM USO ** Início do plano de saúde |
| PLANO_SAUDE_FIM | date(4) |  | S | ** SEM USO ** Fim do plano de saúde |
| PLANO_SAUDE_FIM_DETERMINADO | char(1) |  | S | ** SEM USO ** Possui data fim do plano de saúde determinado |
| SAL_FAM_FIM | date(4) |  | S | Data fim para dependencia salario familia |
| SAL_FAM_FIM_DETERMINADO | char(1) |  |  | Possui data fim do salario familia determinado |
| DEPEND_IRRF_FIM | date(4) |  | S | Data fim para dependencia do IRRF |
| DEPEND_IRRF_FIM_DETERMINADO | char(1) |  |  | Possui data fim dependencia para o IRRF determinado |
| DECLARACAO_NASCIDO_VIVO | char(11) |  | S | NUmero da declaraCAo de Nascido Vivo |
| MATRICULA_CERTIDAO_NASCIMENTO | char(34) |  | S | NUmero da matricula da certidAo de nascimento |
| CPF | char(11) |  | S | CPF |
| RECEBE_PENSAO_ALIMENTICIA | smallint(2) |  |  | Recebe pensão alimentícia. (0=Não/1=Sim) |
| DETERMINAR_FIM_PENSAO_ALIMENTICIA | smallint(2) |  |  | Determinar fim do recebimento da pensão alimentícia. (0=Não/1=Sim) |
| DATA_FIM_PENSAO_ALIMENTICIA | date(4) |  | S | Data fim do recebimento da pensão alimentícia. |
| GERAR_COMPENSACAO_PER_DCOMP | smallint(2) |  |  | Gerar compensação para o PER/DCOMP. (0=Não/1=Sim) |
| COMPETENCIA_INICIO_COMPENSACAO_PER_DCOMP | date(4) |  | S | Competência de início da compensação para o PER/DCOMP. |
| DETERMINAR_FIM_COMPENSACAO_PER_DCOMP | smallint(2) |  |  | Determinar o fim da compensação para o PER/DCOMP. (0=Não/1=Sim) |
| COMPETENCIA_FIM_COMPENSACAO_PER_DCOMP | date(4) |  | S | Competência de fim da compensação para o PER/DCOMP. |
| POSSUI_DEFICIENCIA_FISICA_MENTAL | smallint(2) |  |  | Possui deficiência física ou mental. (0=Não/1=Sim) |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| GUID_CONTABIL | uniqueidentifier(16) |  |  | Identificador único do registro no banco do Contábil |
| GUID_ONVIO | uniqueidentifier(16) |  | S | Identificador único do registro no banco do Atendimento Onvio |
| ENDPOINT_EXCLUSAO | varchar(1024) |  | S | Endpoint utilizado para a exclusão do registro. |
| ORIGEM | smallint(2) |  |  | Origem do dependente. (1=Normal/2=Transferência) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| CONSIDERAR_ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar dependente ao eSocial. (0=Não/1=Sim) |
| SEXO_DEPENDENTE | char(1) |  |  | Sexo do dependente. (M=Masculino/F=Feminino) |
