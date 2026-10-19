# FOVIGENCIAS_SERVICO — Vigências serviço - Cadastro
4.432 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_servicos | integer(4) | PK |  | Codigo |
| VIGENCIA | date(4) | PK |  | Vigência |
| DESCRICAO | char(80) |  |  | Descrição da vigência |
| cgc | char(14) |  |  | CNPJ/CPF/CEI |
| tipo_insc | smallint(2) |  |  | Tipo de inscrição (1=CNPJ/2=CPF/3=CEI/6=CAEPF/7=CNO). |
| codigo_terceiro | numeric(4) |  |  | Codigo terceiro |
| perc_terceiro | numeric(5) |  |  | Terceiro(%) |
| perc_inss_empresa | numeric(5) |  |  | INSS Empresa(%) |
| perc_acid_trabalho | numeric(5) |  |  | Acid. Trabalho(%) |
| codigo_sat | numeric(5) |  |  | Codigo do SAT |
| perc_autonomos | numeric(5) |  |  | Pro-Lab./Aut.(%) |
| codigo_fpas | numeric(3) |  |  | Codigo FPAS |
| codigo_atividade | numeric(7) |  |  | CNAE |
| codigo_gfip | numeric(3) |  |  | Codigo SEFIP |
| codigo_gps | numeric(4) |  |  | Codigo GPS |
| i_bancos | integer(4) |  | S | Banco |
| numero_fgts | numeric(14) |  |  | Numero |
| endereco | char(31) |  | S | Endereco |
| numero | integer(4) |  | S | Numero |
| bairro | char(20) |  | S | Bairro |
| cep | char(8) |  | S | CEP |
| cidade | char(20) |  | S | Cidade |
| estado | char(2) |  | S | UF |
| i_filiais | integer(4) |  |  | Filial |
| sequencia_gps | integer(4) |  |  | Sequencia |
| filantropia | numeric(6) |  | S | Isencao Filantropia(%) |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes, 4-Importação eSocial |
| tipo | integer(4) |  |  | Tipo de serviço. (1=Empresa/2=Obra Própria/3=Cooperativa de trabalho/4=Tomador de serviço/5=Empreitada parcial/6=Empreitada total) |
| codi_mun | integer(4) |  | S | Codigo do municipio |
| codigo_municipio | integer(4) |  | S | Codigo do municipio |
| I_FPAS | integer(4) |  | S | Código Sequencial FPAS |
| CALCULA_INSS_EMPRESA_LEI_12546 | smallint(2) |  | S | Calcular INSS Empresa sobre a receita bruta conforme Lei 12.546/2011: (0=Não/1=Sim) |
| TIPO_SERVICO_TOMADOR | smallint(2) |  | S | Tipo de serviço do tomador. (1=Cessão de Mão de Obra, inclusive contratante de cooperativa de trabalho (PJ)/2=Trabalho temporário - substituição de pessoal/3=Trabalho temporário - serviços extraordinários) |
| TIPO_ENDERECO | smallint(2) |  | S | Tipo de endereço. |
| COMPLEMENTO | varchar(30) |  | S | Complemento do endereço. |
| TIPO_INSCRICAO_CONTRATANTE_EMPREITADA_PARCIAL | smallint(2) |  | S | Tipo de inscrição do contratante da empreitada parcial. (1=CNPJ/2=CPF) |
| INSCRICAO_CONTRATANTE_EMPREITADA_PARCIAL | varchar(14) |  | S | Inscrição do contratante da empreitada parcial. |
| NOME_CONTRATANTE_EMPREITADA_PARCIAL | varchar(100) |  | S | Nome do contratante da empreitada parcial. |
| TIPO_INSCRICAO_PROPRIETARIO_CEI_EMPREITADA_PARCIAL | smallint(2) |  | S | Tipo de inscrição do proprietário do CEI da empreitada parcial. (1=CNPJ/2=CPF) |
| INSCRICAO_PROPRIETARIO_CEI_EMPREITADA_PARCIAL | varchar(14) |  | S | Inscrição do proprietário do CEI da empreitada parcial. |
| NOME_PROPRIETARIO_CEI_EMPREITADA_PARCIAL | varchar(100) |  | S | Nome do proprietário do CEI da empreitada parcial. |
| I_CNAE20 | char(15) |  | S | Código do CNAE 2.0. |
| TIPO_INFORMACAO_ALIQUOTA_ACIDENTE_TRABALHO | smallint(2) |  | S | Tipo de informação da alíquota do acidente de trabalho. (1=Informado/2=Conforme CNAE) |
| I_PROCESSO | integer(4) |  | S | Código do processo administravivo/judicial. |
| I_SCP | integer(4) |  | S | SCP. |
| DDD | varchar(4) |  | S | DDD do telefone. |
| TELEFONE | varchar(14) |  | S | Telefone. |
| COMPETENCIA_FIM_VIGENCIA | date(4) |  | S | Competência fim da vigência. |
| TIPO_LOTACAO_ESOCIAL | smallint(2) |  | S | Tipo de lotação eSocial. |
| I_PROCESSO_TERCEIROS | integer(4) |  | S | Código do processo administrativo/judicial de terceiros. |
| CAEPF | varchar(15) |  | S | Código CAEPF. |
| TIPO_CAEPF | smallint(2) |  | S | Tipo de CAEPF. (1=Contribuinte individual/2=Produtor rural/3=Segurado especial) |
| REGISTRO_PONTO | smallint(2) |  | S | Registro ponto. (0=Não utiliza/1=Manual/2=Mecânico/3=Eletrônico/4=Não eletrônico/5=Eletrônico alternativo/6=Eletrônico outros) |
| CONTRATACAO_APRENDIZ | smallint(2) |  | S | Contratação de aprendiz. (1=Dispensado, de acordo com a lei/2=Dispensado, mesmo que parcialmente, em virtude de processo judicial/3=Obrigado) |
| I_PROCESSO_CONTRATACAO_APRENDIZ | integer(4) |  | S | Código do processo para contratação de aprendiz. |
| REALIZA_CONTRATACAO_APRENDIZ_INTERMEDIO_ENTIDADE_EDUCATIVA_SEM_FINS_LUCRATIVOS | smallint(2) |  |  | Realiza contratação de aprendiz por intermédio de entidade educativa sem fins lucrativos. (0=Não/1=Sim) |
| CODIGO_SUSPENSAO_PROCESSO_RAT | varchar(14) |  | S | Código de suspensão do processo do RAT. |
| SOMA_CODIGOS_SUSPENSAO_TERCEIROS | numeric(5) |  | S | Soma do percentual de códigos de suspensão de terceiros. |
| PERCENTUAL_TERCEIRO_BRUTO | numeric(5) |  | S | Percentual bruto de terceiros. |
| I_DADOS_EVENTOS_ESOCIAL_S_1005 | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL_S_1005 | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL_S_1005 | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL_S_1005 | smallint(2) |  |  | Enviar para o eSocial o evento S-1005. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL_S_1005 | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL_S_1005 | smallint(2) |  |  | Gerar retificação para o eSocial do evento S-1005. (0=Não/1=Sim) |
| I_DADOS_EVENTOS_ESOCIAL_S_1020 | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL_S_1020 | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL_S_1020 | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL_S_1020 | smallint(2) |  |  | Enviar para o eSocial o evento S-1020. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL_S_1020 | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL_S_1020 | smallint(2) |  |  | Gerar retificação para o eSocial do evento S-1020. (0=Não/1=Sim) |
| I_CNAE_ESOCIAL | varchar(15) |  | S | Código do CNAE para ser informado no eSocial. |
| I_TERCEIROS | integer(4) |  | S | Identificador da tabela de terceiros. |
| PROCESSAR_EXCLUSAO_ESOCIAL_S_1005 | smallint(2) |  |  | Marcação do evento S-1005 para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL_S_1020 | smallint(2) |  |  | Marcação do evento S-1020 para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| ORIGEM_ALTERACAO | smallint(2) |  | S | Origem do registro ( 1=Sistema/2=Alteração de Faseamento do eSocial). |
| I_DADOS_EVENTOS_ESOCIAL_S_1080 | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL_S_1080 | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL_S_1080 | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL_S_1080 | smallint(2) |  |  | Enviar para o eSocial o evento S-1080. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL_S_1080 | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL_S_1080 | smallint(2) |  |  | Gerar retificação para o eSocial do evento S-1080. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL_S_1080 | smallint(2) |  |  | Marcação do evento S-1080 para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| EFETUAR_RETENCAO_INSS_NOTAS_FISCAIS_INSCRICAO_OUTROS_CLIENTES | smallint(2) |  |  | Efetuar as retenções de INSS de Notas Fiscais com a inscrição de outros clientes. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| NUMERO_RECIBO_ESOCIAL_VALIDACAO_AUTOMATICA_1005 | varchar(50) |  | S | Numero do recibo importado do eSocial |
| NUMERO_PROCESSO_APRENDIZ | varchar(20) |  | S | Numero do processo - contratação de aprendiz. |
| INEXIGIBILIDADE_RAT | smallint(2) |  |  | Inexigibilidade do RAT |
| CALCULAR_APOIO_FINANCEIRO_FOLHA_COLABORADOR_RS_MTE_991_2024 | smallint(2) |  |  | Calcular o apoio financeiro na folha de pagamento dos colaboradores, portaria MTE nº 991/2024 |
