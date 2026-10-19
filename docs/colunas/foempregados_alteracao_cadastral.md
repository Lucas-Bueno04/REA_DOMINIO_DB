# FOEMPREGADOS_ALTERACAO_CADASTRAL — Registros de alteração contratual para envio ao eSocial.
12.680 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| DATA_ALTERACAO | date(4) | PK |  | Data da alteração. |
| NOME | varchar(70) |  |  | Nome |
| PIS | char(11) |  | S | PIS |
| SEXO | char(1) |  | S | Sexo |
| COR | smallint(2) |  | S | Cor |
| ESTADO_CIVIL | char(1) |  | S | Estado civil |
| GRAU_INSTRUCAO | smallint(2) |  | S | Grau de instrução |
| DATA_NASCIMENTO | date(4) |  | S | Data de nascimento |
| MUNICIPIO_NASCIMENTO | integer(4) |  | S | Município de nascimento |
| PAIS_NASCIMENTO | integer(4) |  | S | Código do país de nascimento |
| UF_NASCIMENTO | char(2) |  | S | **SEM USO** |
| PAIS_NACIONALIDADE | integer(4) |  | S | Código do país da nacionalidade |
| NOME_PAI | varchar(70) |  | S | **SEM USO** |
| NOME_MAE | varchar(70) |  | S | **SEM USO** |
| NOME_SOCIAL | varchar(70) |  | S | Nome no eSocial |
| TIPO_ENDERECO | smallint(2) |  | S | Tipo do endereço |
| ENDERECO | varchar(100) |  | S | Endereço |
| NUMERO_ENDERECO | integer(4) |  | S | Número do endereço |
| BAIRRO | varchar(90) |  | S | Bairro |
| COMPLEMENTO_ENDERECO | varchar(30) |  | S | Complemento |
| CEP_ENDERECO | varchar(8) |  | S | CEP |
| MUNICIPIO_ENDERECO | integer(4) |  | S | Código do município do endereço |
| UF_ENDERECO | char(2) |  | S | UF do endereço |
| PAIS_ENDERECO | integer(4) |  | S | Código do país do endereço |
| CODIGO_POSTAL | varchar(10) |  | S | Código postal |
| DDD_FONE | varchar(3) |  | S | DDD do telefone |
| FONE | varchar(15) |  | S | Número de Telefone |
| DDD_CELULAR | varchar(3) |  | S | DDD do celular |
| CELULAR | varchar(15) |  | S | Número de celular |
| EMAIL_PRINCIPAL | varchar(60) |  | S | E-mail principal |
| EMAIL_ALTERNATIVO | varchar(60) |  | S | **SEM USO** |
| NUMERO_RIC | char(15) |  | S | **SEM USO** |
| ORGAO_EMISSOR_RIC | char(8) |  | S | **SEM USO** |
| SIGLA_UF_RIC | char(2) |  | S | **SEM USO** |
| DATA_EXPEDICAO_RIC | date(4) |  | S | **SEM USO** |
| IDENTIDADE | char(15) |  | S | **SEM USO** |
| ORGAO_EXPEDICAO_RG | smallint(2) |  | S | **SEM USO** |
| ORG_EXPED_IDENT | varchar(10) |  | S | Órgão de expedição |
| UF_EXP_IDENT | char(2) |  | S | **SEM USO** |
| DATA_EXPEDICAO_RG | date(4) |  | S | **SEM USO** |
| NUMERO_RNE | varchar(15) |  | S | **SEM USO** |
| ORGAO_EMISSOR_RNE | varchar(20) |  | S | **SEM USO** |
| DATA_EXPEDICAO_RNE | date(4) |  | S | **SEM USO** |
| CART_MOTORISTA | char(15) |  | S | **SEM USO** |
| DATA_EXPEDICAO_CNH | date(4) |  | S | **SEM USO** |
| CODIGO_UF_CARTEIRA_MOTORISTA | integer(4) |  | S | **SEM USO** |
| VENC_CART_MOT | date(4) |  | S | **SEM USO** |
| DATA_PRIMEIRA_HABILITACAO_CARTEIRA_MOTORISTA | date(4) |  | S | **SEM USO** |
| CATEG_CART_MOT | char(3) |  | S | **SEM USO** |
| DATA_CHEGADA_ESTRANGEIRO | date(4) |  | S | **SEM USO** |
| TIPO_VISTO_ESTRANGEIRO | smallint(2) |  | S | Tipo de visto estrangeiro |
| CASADO_BRASILEIRO | smallint(2) |  | S | **SEM USO** |
| FILHOS_BRASILEIRO | smallint(2) |  | S | **SEM USO** |
| POSSUI_DEFICIENCIA | smallint(2) |  | S | Possui deficiência (0=Não/1=Sim) |
| POSSUI_DEFICIENCIA_MOTORA | smallint(2) |  | S | Possui deficiência motora (0=Não/1=Sim) |
| POSSUI_DEFICIENCIA_VISUAL | smallint(2) |  | S | Possui deficiência visual (0=Não/1=Sim) |
| POSSUI_DEFICIENCIA_AUDITIVA | smallint(2) |  | S | Possui deficiência auditiva(0=Não/1=Sim) |
| POSSUI_DEFICIENCIA_MENTAL | smallint(2) |  | S | Possui deficiência mental(0=Não/1=Sim) |
| POSSUI_DEFICIENCIA_INTELECTUAL | smallint(2) |  | S | Possui deficiência intelectual(0=Não/1=Sim) |
| POSSUI_DEFICIENCIA_OUTRAS | smallint(2) |  | S | **SEM USO** |
| POSSUI_DEFICIENCIA_REABILITADO | smallint(2) |  | S | Possui deficiência reabilitado(0=Não/1=Sim) |
| RESIDENTE_EXTERIOR | smallint(2) |  | S | Residente ou domiciliado no exterior (0=Não/1=Sim) |
| NOME_MUNICIPIO_RESIDENTE_EXTERIOR | varchar(255) |  | S | Nome do municipio para residente no exterior |
| CARTEIRA_PROFISSIONAL | varchar(16) |  | S | **SEM USO** |
| UF_CARTEIRA_PROFISSIONAL | char(2) |  | S | **SEM USO** |
| APOSENTADO | smallint(2) |  | S | **SEM USO** |
| COTA_DEFICIENTE | smallint(2) |  | S | Cota de deficiente (0=Não/1=Sim) |
| OBSERVACAO_DEFICIENCIA | varchar(255) |  | S | Observação da deficiência |
| DATA_NATURALIZACAO | date(4) |  | S | **SEM USO** |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes, 4-Importação eSocial |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| NUMERO_RECIBO_ESOCIAL_VALIDACAO_AUTOMATICA | varchar(50) |  | S | Numero do recibo importado do eSocial |
| ID_ESOCIAL_VALIDACAO_AUTOMATICA | varchar(70) |  | S | ID do evento importado do eSocial |
| TEMPO_RESIDENCIA | smallint(2) |  | S | Tempo de residência no Brasil. |
| ENVIAR_ESOCIAL_PERIODO_ANTERIOR_INICIO_BANCO_CONTABIL | smallint(2) |  | S | Enviar evento eSocial anterior ao início da utilização do banco de dados (0=Não/1=Sim) |
| ENVIAR_ESOCIAL_MANUALMENTE | integer(4) |  |  | Enviar eSocial Manualmente |
