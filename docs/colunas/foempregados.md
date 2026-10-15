# foempregados — Empregados - Cadastro
10.974 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo Empresa |
| i_empregados | integer(4) | PK |  | Codigo |
| i_filiais | integer(4) |  |  | Codigo Filial |
| i_horaemp | integer(4) |  | S | **SEM USO** Horário |
| nome | char(70) |  |  | Nome |
| paga_contr_sind | char(1) |  |  | Pagou contr. sindical? |
| opta_fgts | char(1) |  |  | Optante do FGTS |
| categoria | smallint(2) |  |  | Categoria |
| horas_mes | numeric(5) |  |  | Horas mes |
| horas_semana | numeric(5) |  |  | Horas semana |
| horas_dia | numeric(5) |  |  | Horas dia |
| admissao | date(4) |  |  | Admissao |
| salario | numeric(17) |  |  | Salario |
| endereco | varchar(100) |  | S | Endereco |
| complemento | char(30) |  | S | Complemento |
| cep | char(8) |  | S | CEP |
| cidade | char(25) |  | S | Cidade |
| fone | char(15) |  | S | Telefone |
| estado | char(2) |  | S | Sigla UF |
| data_nascimento | date(4) |  |  | Data nascimento |
| venc_ferias | date(4) |  |  | vencimento das ferias |
| i_ccustos | integer(4) |  |  | Centro de Custos |
| forma_pagto | char(1) |  |  | Forma pagamento |
| sexo | char(1) |  |  | Sexo |
| local_nascimento | char(40) |  | S | Local |
| uf_nascimento | char(2) |  | S | UF |
| estado_civil | char(1) |  | S | Estado civil: S=Solteiro/C=Casado/V=Viúvo/D=Divorciado/O=Concubinato/J=Separado judicialmente/U=União estável) |
| nacionalidade | integer(4) |  |  | Nacionalidade |
| ano_chegada | integer(4) |  | S | **SEM USO** Ano de chegada |
| identidade | char(15) |  | S | Identidade |
| naturalizado | char(1) |  | S | Naturalizado |
| pis | char(11) |  | S | PIS |
| cpf | char(11) |  | S | CPF |
| cart_prof | varchar(11) |  | S | CTPS |
| serie_cart_prof | char(5) |  | S | Serie CTPS |
| opcao_fgts | date(4) |  | S | Data opcao FGTS |
| conta_fgts | numeric(12) |  | S | Conta FGTS |
| num_cart_ponto | char(12) |  | S | Cartao ponto |
| venc_exame_medico | date(4) |  | S | Vencto. exame Med. |
| vinculo | smallint(2) |  |  | Vinculo empregaticio |
| i_bancos | integer(4) |  | S | Banco |
| conta_corr | char(15) |  | S | Conta corrente |
| i_cargos | integer(4) |  | S | Cargo |
| data_base | date(4) |  | S | Data Vantagem |
| cart_motorista | char(15) |  | S | Cart. motorista |
| categ_cart_mot | char(3) |  | S | Categoria |
| venc_cart_mot | date(4) |  | S | Vencto. |
| data_transf | date(4) |  | S | Data transferencia |
| sai_rais | char(1) |  |  | Sai da RAIS |
| grau_instrucao | smallint(2) |  |  | Grau instrucao |
| i_depto | integer(4) |  |  | Departamento |
| emprego_ant | smallint(2) |  |  | Tipo de admissão (1=Admissão/2=Admissão por sucessão, incorporação ou fusão/3=Transferência com ônus/4=Transferência sem ônus/5=Reintegração/6=Mudança de CPF) |
| nome_pai | varchar(70) |  | S | Nome do pai |
| nome_mae | varchar(70) |  | S | Nome da mae |
| uf_cart_prof | char(2) |  | S | UF |
| i_sindicatos | integer(4) |  | S | Código da convenção coletiva |
| org_exp_ident | varchar(10) |  | S | Orgao expedicao |
| uf_exp_ident | char(2) |  | S | UF |
| dt_exp_ident | date(4) |  | S | Data |
| dt_exp_cprof | date(4) |  | S | Data de expedicao |
| tipo_visto_estrangeiro | smallint(2) |  | S | Tipo de visto de estrangeiro. |
| validade_id_estr | date(4) |  | S | Data de validade da identidade |
| validade_ctrab_estr | date(4) |  | S | Data de validade da carteira de trabalho |
| grupo_sanguineo | char(2) |  | S | Grupo sang. |
| rh_sanguineo | char(1) |  | S | RH |
| nome_conjuge | char(40) |  | S | Nome do conjuge |
| ultimo_exame_medico | date(4) |  | S | Ult. exame Medico |
| i_conselhos | integer(4) |  | S | Conselhos |
| num_reg_cons_reg | char(8) |  | S | No. registro cons. regional |
| regiao_reg_cons_regional | char(8) |  | S | Regiao do conselho |
| i_estabilidade | integer(4) |  | S | Estabilidade |
| inicio_estabilidade | date(4) |  | S | Inicio estabilidade |
| fim_estabilidade | date(4) |  | S | Fim estabilidade |
| i_localtrab | integer(4) |  | S | Local trabalho |
| titulo_eleit | char(15) |  | S | Titulo eleitoral |
| zona_eleit | char(3) |  | S | Zona eleitoral |
| secao_eleit | char(4) |  | S | Secao |
| dcad_pis | date(4) |  | S | Data de cad. PIS |
| i_servicos | integer(4) |  | S | Servico |
| ini_praz_det | date(4) |  | S | Inicio prazo determinado |
| fim_praz_det | date(4) |  | S | Fim prazo determinado |
| possui_vinc_out_emp | char(1) |  |  | Multiplos vinculos |
| empresa_outro_vinc | integer(4) |  | S | Vinculo outra empresa (sem uso) |
| codigo_vinc_outra_emp | integer(4) |  | S | Cod. vinculo outra empresa (sem uso) |
| ult_cont_sind | date(4) |  | S | Data da ultima contribuicao sindical |
| oco_sefip | integer(4) |  |  | Ocorrencia SEFIP |
| cor | smallint(2) |  |  | Raca/Cor |
| cart_reservista | char(12) |  | S | Cart. reserv. |
| cate_reservista | char(5) |  | S | Cat. |
| i_niveis | integer(4) |  | S | Codigo Nivel |
| i_clasniveis | char(1) |  | S | Classe Nivel |
| i_refeniveis | integer(4) |  | S | Referencia Nivel |
| matricula | char(20) |  | S | Matricula |
| deficiente_fisico | tinyint(1) |  |  | Deficiente fisico |
| matric_inss | char(11) |  | S | Matricula INSS |
| tipo_contrib | char(1) |  |  | Tipo contribuinte (E=Empregador/F=Facultativo/A=Autônomo/R=Produtor Rural/M=Microempreendedor/S=Segurado Especial/I=Autônomo Microempreendedor) |
| contrib_indiv | char(1) |  |  | Contribuinte individual |
| inicio_contribuicao | date(4) |  | S | Inicio contribuicao |
| classe_atual | integer(4) |  | S | Classe de contribuicao |
| data_classe | date(4) |  | S | Inicio de contribuicao na classe |
| troca_aut_clas | tinyint(1) |  |  | Troca automatica de classe |
| evento_prolabore | integer(4) |  | S | Evento |
| gps_trimestral | tinyint(1) |  |  | GPS Trimestral |
| gps_deducao | tinyint(1) |  |  | Deducao na GPS |
| i_contribuintes | integer(4) |  | S | Codigo |
| tipo_epr | tinyint(1) |  |  | tipo |
| usa_sist | smallint(2) |  |  | sistemas |
| tempermuta | tinyint(1) |  |  | Permura de turma |
| i_turmas | integer(4) |  | S | Turma |
| relogio1 | integer(4) |  | S | Codigo relogio1 |
| relogio2 | integer(4) |  | S | Codigo relogio2 |
| relogio3 | integer(4) |  | S | Codigo relogio3 |
| relogio4 | integer(4) |  | S | Codigo relogio4 |
| relogio5 | integer(4) |  | S | Codigo relogio5 |
| aco_nao_aut | char(1) |  | S | bater em um relógio não autorizado |
| codigo_exportacao | integer(4) |  | S | Codigo exportacao para folha |
| transf_codi_emp | integer(4) |  | S | Codigo |
| transf_i_empregados | integer(4) |  | S | Empregado |
| regime_trabalho | integer(4) |  | S | ** Sem uso ** Regime trabalho |
| pis_domi_banc | char(40) |  | S | Domicilio bancario |
| pis_num_banco | integer(4) |  | S | Numero banco |
| pis_agencia | integer(4) |  | S | Agencia PIS |
| pis_agencia_dv | char(3) |  | S | PIS Digito |
| pis_end_banco | char(40) |  | S | Endereco banco |
| autoriza_tf | char(1) |  | S | Autorizacao |
| tipo_valor_tf | tinyint(1) |  | S | Tipo do valor informado |
| valor_tf | numeric(13) |  | S | Valor Ticket Farma |
| data_emissao_tf | date(4) |  | S | Data emissao Ticket farma |
| matricula_tf | numeric(12) |  | S | Matricula |
| bairro | varchar(90) |  | S | Bairro |
| sindicalizado | tinyint(1) |  | S | Sindicalizado |
| numero_end | integer(4) |  | S | No. |
| imprime_recibo | tinyint(1) |  | S | Emitir Recibo |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes, 4-Importação eSocial |
| fone2 | char(15) |  | S | Telefone 2 |
| tipo_servico | char(1) |  | S | Tipo de serviço para dedução do IRRF |
| contr_exper | tinyint(1) |  | S | Contrato de Experiência : 0=Não Possui (default) / 1=Possui |
| pro_praz_det | date(4) |  | S | Prorrogação do prazo determinado |
| contr_sobre_sal_min | tinyint(1) |  |  | Calcular contribuição fixa sobre 1 salário mínimo: (0=Não/1=Sim) |
| contr_sobre_sal_min_data | date(4) |  | S | Início do cálculo da contribuição fixa sobre 1 salário mínimo |
| simples_072007 | tinyint(1) |  |  | Atividade para o simples nacional |
| DATA_CALC_AFASTAMENTOS | date(4) |  | S | DATA PARA CALCULAR OS AFASTAMENTOS POR COMPETENCIA |
| I_AFASTAMENTOS | integer(4) |  |  | CODIGO DO AFASTAMENTO DA ULTIMA SITUACAO DO EMPREGADO |
| ALVARA_JUDICIAL | smallint(2) |  |  | ALVARA JUDICIAL USADO NA RAIS PARA CELETISTAS MENORES DE 16 ANOS (0=NAO, 1=SIM, 2=NAO INFORMADO) |
| I_OPERADORAPLANOSAUDE | integer(4) |  | S | ** SEM USO ** Código da operadora de plano de saúde |
| PLANO_SAUDE_OPTANTES | smallint(2) |  | S | ** SEM USO ** Optante plano de saúde: 0=Não optante/1=Somente titular/2=Titular e dependentes 3 Somente dependentes |
| OPCAO_PLANO_SAUDE | smallint(2) |  |  | Optante plano de saúde: 0=Não/1=Sim |
| TIPO_CLA_ASSEC_DIR_REC_RES_ANT | smallint(2) |  | S | Cláusula assecuratória de direito recíproco de rescisão antecipada (1=Contrato de trabalho regido pelo art. 479/480 CLT ou sem cláusula assecuratória/2=Contrato de trabalho regido pelo art. 481 CLT) |
| TIPO_CONTA | smallint(2) |  | S | Tipo de Conta: (1=Não informada/2=Conta corrente/3=Conta salário/4=Conta poupança/5=Conta fácil) |
| DATA_REINTEGRACAO | date(4) |  | S | Data de reintegração |
| TIPO_INSCRICAO_FILIAL_ORIGEM | smallint(2) |  | S | Tipo de inscrição da filial de origem: (1=CNPJ/2=CPF/3=CEI/6=CAEPF/7=CNO) |
| INSCRICAO_FILIAL_ORIGEM | char(14) |  | S | Inscrição da filial de origem |
| MATRICULA_ORIGEM | char(30) |  | S | Matrícula na empresa origem |
| NOME_EMPRESA_ORIGEM | char(40) |  | S | Nome da empresa de origem |
| EMAIL | char(60) |  | S | E-mail |
| NUMERO_PROCESSO_MTE | char(30) |  | S | Número processo MTE |
| DATA_CHEGADA | date(4) |  | S | Data da chegada |
| DATA_NATURALIZACAO | date(4) |  | S | Data da naturalização |
| CASADO_BRASILEIRO | smallint(2) |  | S | Casado com brasileiro: (0=Não/1=Sim) |
| FILHOS_BRASILEIRO | smallint(2) |  | S | Filhos com brasileiro: (0=Não/1=Sim) |
| NIF | char(30) |  | S | Número de identificação fiscal (NIF) |
| NUMERO_RIC | char(15) |  | S | Número RIC |
| ORGAO_EMISSOR_RIC | char(8) |  | S | Orgão emissor RIC |
| LOCAL_RIC | char(40) |  | S | Local RIC |
| DATA_EXPEDICAO_RIC | date(4) |  | S | Data expedição RIC |
| DATA_VALIDADE_RIC | date(4) |  | S | Data validade RIC |
| DIGITO_CONTA_PAGAMENTO | char(2) |  | S | Dígito da conta de pagamento |
| RESIDENTE_EXTERIOR | smallint(2) |  |  | Residente ou domiciliado no exterior: (0=Não/1=Sim) |
| TIPO_ENDERECO | smallint(2) |  | S | Tipo de endereço. |
| MUNICIPIO_ENDERECO | integer(4) |  | S | Código do município do endereço |
| MUNICIPIO_NASCIMENTO | integer(4) |  | S | Código do município do local de nascimento |
| PAIS_ENDERECO | integer(4) |  | S | Código do país do endereço |
| PAIS_NASCIMENTO | integer(4) |  | S | Código do país de nascimento |
| BENEFICIADO_PAT | smallint(2) |  |  | Beneficiado pelo PAT: (0=Não/1=Sim) |
| CONTR_SOBRE_SAL_MIN_TIPO | smallint(2) |  | S | Tipo de cálculo da contribuição fixa sobre 1 salário mínimo: (1=Alíquota 11%/2=Alíquota 5%) |
| GPS_CONJUNTA_NOVEMBRO_13_INTEGRAL | smallint(2) |  |  | Recolher a competência de novembro e 13º integral em uma única GPS.(0-Não/1-Sim) |
| GPS_CONJUNTA_NOVEMBRO_13_INTEGRAL_INICIO | date(4) |  | S | Início do recolhimento da competência de novembro e 13º integral em uma única GPS. |
| BENEFICIADO_PAT_SERVICO_PROPRIO | smallint(2) |  |  | Beneficiado pelo PAT por serviço próprio. (0=Não/1=Sim) |
| BENEFICIADO_PAT_ADMINISTRACAO_COZINHAS | smallint(2) |  |  | Beneficiado pelo PAT por administração de cozinhas. (0=Não/1=Sim) |
| BENEFICIADO_PAT_REFEICAO_CONVENIO | smallint(2) |  |  | Beneficiado pelo PAT por convênio de refeição. (0=Não/1=Sim) |
| BENEFICIADO_PAT_REFEICOES_TRANSPORTADAS | smallint(2) |  |  | Beneficiado pelo PAT por transporte de refeição. (0=Não/1=Sim) |
| BENEFICIADO_PAT_CESTA_ALIMENTOS | smallint(2) |  |  | Beneficiado pelo PAT por cesta de alimentos. (0=Não/1=Sim) |
| BENEFICIADO_PAT_ALIMENTACAO_CONVENIO | smallint(2) |  |  | Beneficiado pelo PAT por convênio de alimentação. (0=Não/1=Sim) |
| ATIVIDADE_CONTA_PROPRIA_RURAL | smallint(2) |  | S | Atividade por conta própria - Rural: (0=Não/1=Sim) |
| NUMERO_PASSAPORTE | varchar(20) |  | S | Número do passaporte. |
| EMISSOR_PASSAPORTE | smallint(2) |  | S | Emissor do passaporte. |
| UF_PASSAPORTE | char(2) |  | S | UF do passaporte. |
| DATA_EMISSAO_PASSAPORTE | date(4) |  | S | Data de emissão do passaporte. |
| DATA_VALIDADE_PASSAPORTE | date(4) |  | S | Data de validade do passaporte. |
| PAIS_PASSAPORTE | integer(4) |  | S | Código do país do passaporte. |
| TIPO_INDICATIVO_ADMISSAO | smallint(2) |  |  | Tipo de indicativo da admissão. (1=1º emprego/2=Normal/3=Decorrente de ação fiscal/4=Decorrente de decisão judicial/5=Decorrente de Anistia Legal) |
| NOME_MUNICIPIO_RESIDENTE_EXTERIOR | varchar(255) |  | S | Nome do município para residente no exterior. |
| PAIS_NACIONALIDADE | integer(4) |  | S | Código do país da nacionalidade. |
| DATA_EXPEDICAO_CNH | date(4) |  | S | Data de expedição da carteira de motorista. |
| ORGAO_EMISSOR_CNH | varchar(20) |  | S | Orgão emissor da carteira de motorista. |
| CODIGO_POSTAL | varchar(10) |  | S | Código postal. |
| RESIDENCIA_PROPRIA | smallint(2) |  |  | Possui residência própria. (0=Não/1=Sim) |
| IMOVEL_ADQUIRIDO_RECURSOS_FGTS | smallint(2) |  |  | Adquiriu imóvel com recursos do FGTS. (0=Não/1=Sim) |
| EMAIL_ALTERNATIVO | varchar(60) |  | S | E-mail alternativo. |
| TIPO_PROCESSO_ALVARA | smallint(2) |  | S | Tipo de processo do alvará. (1=Judicial/2=Administrativo) |
| AUTORIA_ALVARA | smallint(2) |  | S | Autoria do alvará. (1=Própria/2=Outra entidade) |
| NUMERO_ALVARA | varchar(20) |  | S | Número do alvará. |
| INDICATIVO_DECISAO_ALVARA | smallint(2) |  | S | Indicativo de decisão do alvará. (1=Definitiva (Transitada em Julgado)/2=Decisão não Transitada em Julgado com Efeito Suspensivo/3=Liminar em Mandado de Segurança/4=Liminar ou tutela antecipada, em outras espécies de ação judicial/5=Contestação Administrativa/6=Outros) |
| DATA_DECISAO_ALVARA | date(4) |  | S | Data de decisão do alvará. |
| MONTANTE_INTEGRAL_DEPOSITADO_ALVARA | smallint(2) |  | S | Montante integral do alvará depositado. (0=Não/1=Sim) |
| INICIO_VIGENCIA_ALVARA | date(4) |  | S | Inicío da vigência do alvará. |
| FIM_VIGENCIA_ALVARA | date(4) |  | S | Fim da vigência do alvará. |
| IDENTIFICACAO_ALVARA | varchar(2) |  | S | Identificação do alvará. |
| CODIGO_MUNICIPIO_ALVARA | integer(4) |  | S | Código do município do alvará. |
| POSSUI_DEFICIENCIA | smallint(2) |  | S | Possui deficiência. (0=Não/1=Sim) |
| POSSUI_DEFICIENCIA_MOTORA | smallint(2) |  | S | Possui deficiência motora. (0=Não/1=Sim) |
| POSSUI_DEFICIENCIA_VISUAL | smallint(2) |  | S | Possui deficiência visual. (0=Não/1=Sim) |
| POSSUI_DEFICIENCIA_AUDITIVA | smallint(2) |  | S | Possui deficiência auditiva. (0=Não/1=Sim) |
| POSSUI_DEFICIENCIA_OUTRAS | smallint(2) |  | S | Possui outras deficiências. (0=Não/1=Sim) |
| POSSUI_DEFICIENCIA_REABILITADO | smallint(2) |  | S | Possui deficiência reabilitado. (0=Não/1=Sim) |
| OBSERVACAO_DEFICIENCIA | varchar(255) |  | S | Observação sobre a deficiência. |
| I_FUNCAO | integer(4) |  | S | Código da função. |
| NUMERO_RNE | varchar(15) |  | S | Número do registro nacional de estrangeiros. |
| DATA_EXPEDICAO_RNE | date(4) |  | S | Data de expedição do registro nacional de estrangeiros. |
| ORGAO_EMISSOR_RNE | varchar(20) |  | S | Orgão emissor do registro nacional de estrangeiros. |
| ENDERECO_COMERCIAL | smallint(2) |  |  | Endereço comercial. (0=Não/1=Sim) |
| I_PROCESSO | integer(4) |  | S | Código do processo. |
| CODIGO_SCE_DOMINIO_ATENDIMENTO | integer(4) |  | S | Código da solicitação de cadastro de empregado do Domínio Atendimento. |
| I_INSTITUICAO_ENSINO | integer(4) |  | S | Código da instituição de ensino do estagiário. |
| I_AGENTES_INTEGRACAO | integer(4) |  | S | Código do agente de integração do estagiário. |
| I_COORDENADOR_ESTAGIO | integer(4) |  | S | Código do coordenador de estágio do estagiário. |
| AREA_ATUACAO_ESTAGIARIO | char(100) |  | S | Área de atuação do estagiário. |
| NATUREZA_ESTAGIO | smallint(2) |  | S | Natureza do estágio. (0=Não obrigatório/1=Obrigatório) |
| NIVEL_ESTAGIO | smallint(2) |  | S | Nível do estágio. (1=Fundamental/2=Médio/3=Formação profissional/4=Superior/5=Especial/6=Mãe social (Lei 7644, de 1987)) |
| APOLICE_SEGURO_ESTAGIARIO | varchar(30) |  | S | Apólice de seguro do estagiário. |
| POSSUI_DEFICIENCIA_MENTAL | smallint(2) |  | S | Possui deficiência mental. (0=Não/1=Sim) |
| I_JORNADA | integer(4) |  | S | Código da jornada. |
| SITUACAO_QUALIFICACAO_CADASTRAL_INSS_RECEITA_FEDERAL | smallint(2) |  |  | Situação da qualificação cadastral para o INSS e a Receita Federal. (0=Não qualificado/1=Qualificado) |
| CAIXA_POSTAL | varchar(10) |  | S | Caixa postal. |
| CEP_CAIXA_POSTAL | varchar(8) |  | S | CEP da caixa postal. |
| MOTIVO_CONTRATACAO_TRABALHO_TEMPORARIO | smallint(2) |  | S | ** SEM USO ** |
| NOME_TRABALHADOR_SUBSTITUIDO_TRABALHO_TEMPORARIO | varchar(100) |  | S | ** SEM USO ** |
| CPF_TRABALHADOR_SUBSTITUIDO_TRABALHO_TEMPORARIO | varchar(11) |  | S | ** SEM USO ** |
| MATRICULA_TRABALHADOR_SUBSTITUIDO_TRABALHO_TEMPORARIO | varchar(30) |  | S | ** SEM USO ** |
| TIPO_HORARIO | smallint(2) |  | S | Tipo de horário. (1=Submetidos a Horário de Trabalho (Cap. II da CLT)/2=Atividade Externa especificada no Inciso I do Art. 62 da CLT/3=Funções especificadas no Inciso II do Art. 62 da CLT/4=Horário de Motorista inciso V do Art 2 Lei 12619/2012/5=Horário de Motorista Art 235 C  - Lei 12619/2012/6=Teletrabalho, previsto no Inciso III do Art. 62 da CLT/7=Funções especificadas no § 3º do Art. 443 da CLT/8=Registro de ponto por exceção, prev. no § 4° Art. 74 CLT) |
| CODIGO_ESOCIAL | varchar(30) |  | S | Código no eSocial. |
| I_REMUNERACAO_VARIAVEL | integer(4) |  | S | Código da remuneração variável. |
| I_PROCESSO_REINTEGRACAO | integer(4) |  | S | Coluna sem uso - retirada na SAI 50872 |
| POSSUI_REDUCAO_ALIQUOTA_INSS | smallint(2) |  |  | Possui redução na alíquota de INSS. (0=Não/1=Sim) |
| POSSUI_REDUCAO_ALIQUOTA_INSS_COMPETENCIA | date(4) |  | S | Competência da redução na alíquota de INSS. |
| QUANTIDADE_DIAS_CONTRATO_EXPERIENCIA | integer(4) |  | S | Quantidade de dias do contrato de experiência. |
| QUANTIDADE_DIAS_PRORROGACAO_CONTRATO_EXPERIENCIA | integer(4) |  | S | Quantidade de dias da prorrogação do contrato de experiência. |
| RECEBIA_SEGURO_DESEMPREGO | smallint(2) |  |  | Recebia seguro desemprego. (0=Nenhum requerimento encontrado/1=Notificado - Parcela a Emitir/2=Notificado - Parcela Emitida/3=Notificado - Seguro Completo/4=Notificado - Mais de XX anos da Data de Demissão/Suspensão/5=Notificado - A restituir parcela ou parcelas/6=Notificado - Parcela não recebida/7=Notificado - Reemprego/8=Notificado - Não tem 36 Contribuições/ Postagens >120 dias/9=Notificado - Não possui 06 salários consecutivos/10=Notificado - Divergência nome/ nome da mão/ CPF / sexo / data de nascimen |
| NATUREZA_TRABALHO_AUTONOMO | smallint(2) |  | S | Natureza trabalho autônomo. (1=Rural/2=Urbano) |
| DDD_FONE | varchar(3) |  | S | DDD do telefone 1. |
| DDD_FONE2 | varchar(3) |  | S | DDD do contato 1. |
| DDD_CELULAR | varchar(3) |  | S | DDD do celular. |
| CELULAR | varchar(11) |  | S | Número do celular. |
| DDD_CONTATO_2 | varchar(3) |  | S | DDD do contato 2. |
| CONTATO_2 | varchar(11) |  | S | Número do contato 2. |
| INSCRICAO_MUNICIPAL_AUTONOMO | varchar(20) |  | S | Inscrição municipal de autônomo. |
| REGIME_CASAMENTO | smallint(2) |  | S | Regime de casamento. (0=Nenhum/1=Comunhão parcial de bens/2=Comunhão total de bens/3=Separação total de bens) |
| DIRIGENTE_SINDICAL | smallint(2) |  |  | Dirigente sindical. (0=Não /1=Sim) |
| CNPJ_EMPRESA_ORIGEM_DIRIGENTE_SINDICAL | varchar(14) |  | S | CNPJ da empresa origem do dirigente sindical. |
| NOME_EMPRESA_ORIGEM_DIRIGENTE_SINDICAL | varchar(100) |  | S | Nome da empresa origem do dirigente sindical. |
| CATEGORIA_ORIGEM_DIRIGENTE_SINDICAL | integer(4) |  | S | Categoria origem do dirigente sindical. |
| DATA_ADMISSAO_EMPRESA_ORIGEM_DIRIGENTE_SINDICAL | date(4) |  | S | Data de admissão na empresa origem do dirigente sindical. |
| MATRICULA_EMPRESA_ORIGEM_DIRIGENTE_SINDICAL | varchar(30) |  | S | Matrícula na empresa origem do dirigente sindical. |
| RESPONSAVEL_REMUNERACAO_DIRIGENTE_SINDICAL | smallint(2) |  | S | Responsável pela remuneração do dirigente sindical. (1=Sindicao/2=Sindicato e Empresa origem) |
| TIPO_REMUNERACAO_DIRIGENTE_SINDICAL | smallint(2) |  | S | Tipo de remuneração do dirigente sindical. (1=Igual ao valor da empresa origem/2=Superior ao valor da empresa origem) |
| DATA_INICIO_PAGAMENTO_ADICIONAL_DIRIGENTE_SINDICAL | date(4) |  | S | Data de início do pagamento do adicional para o dirigente sindical. |
| REMUNERACAO_SINDICATO_DIRIGENTE_SINDICAL | numeric(17) |  | S | Remuneração do sindicato do dirigente sindical. |
| REMUNERACAO_EMPRESA_DIRIGENTE_SINDICAL | numeric(17) |  | S | Remuneração da empresa do dirigente sindical. |
| ORGAO_EXPEDICAO_RG | smallint(2) |  |  | Orgão de expedição da RG. |
| FORMA_CALCULO | smallint(2) |  | S | Forma de pagamento. (1=Por mês/2=Por semana/3=Por convocação) |
| USA_SALARIO_MINIMO_ESTADUAL | smallint(2) |  |  | Usa salário mínimo estadual. (0=Não/1=Sim) |
| I_TABCALC_SALARIO_MINIMO_ESTADUAL | integer(4) |  | S | Código sequencial da tabela de salário mínimo estadual. |
| I_CATEGORIA_SALARIO_MINIMO_ESTADUAL | integer(4) |  | S | Código da categoria da tabela de salário mínimo estadual. |
| EMPRESA_ORIGEM_DESONERADA | smallint(2) |  |  | Empresa origem desonerada. (0=Não/1=Sim) |
| REMUNERACAO_PERIODO_DESLIGAMENTO_REINTEGRACAO_PAGAS_JUIZO | smallint(2) |  |  | Remunerações e respectivas contribuições referentes ao período entre o desligamento e a reintegração pagas em juízo. (0=Não/1=Sim) |
| CODIGO_MUNICIPIO_RIC | integer(4) |  | S | Código do município do RIC. |
| CODIGO_UF_CARTEIRA_MOTORISTA | integer(4) |  | S | UF da carteira de motorista. |
| DATA_PRIMEIRA_HABILITACAO_CARTEIRA_MOTORISTA | date(4) |  | S | Data da primeira habilitação. |
| BRASILEIRO_NASCIDO_EXTERIOR | smallint(2) |  |  | Brasileiro nascido no exterior. (0=Não/1=Sim) |
| CALCULAR_INSS_PATRONAL | smallint(2) |  |  | Calcular INSS Patronal. (0=Não/1=Sim) |
| CARGA_HORARIA_VARIAVEL | smallint(2) |  |  | Carga horária variável. (0=Não/1=Sim) |
| DATA_OPERACAO_CONECTIVIDADE_SOCIAL | date(4) |  | S | Data da operação para conectividade social. |
| CHAVE_IDENTIFICACAO_CONECTIVIDADE_SOCIAL | varchar(40) |  | S | Chave de identificação para conectividade social. |
| DATA_REAL_DN_AFASTAMENTO_DA | decimal(13) |  | S | Data real do ultimo afastamento sincronizado com o D.A. |
| CALCULAR_ADIANTAMENTO_SALARIAL | smallint(2) |  |  | Calcular adiantamento salarial. (0=NÃ£o/1=Sim) |
| CALCULO_ADIANTAMENTO_SALARIAL_PERCENTUAL | numeric(5) |  | S | Percentual para o cálculo do adiantamento salarial. |
| TIPO_INSCRICAO_EMPRESA_ORIGEM_DIRIGENTE_SINDICAL | smallint(2) |  |  | Tipo de inscrição da empresa origem do dirigente sindical. (1=CNPJ/3=CEI) |
| UF_BASE_CONTA_FGTS | integer(4) |  | S | Base da conta do FGTS. |
| HORAS_COMPENSADAS | numeric(5) |  | S | Horas compensadas no sábado. |
| NUMERO_LIVRO_REGISTRO | varchar(6) |  | S | Número do livro de registro. |
| NUMERO_FOLHA_LIVRO_REGISTRO | varchar(6) |  | S | Número da folha do livro de registro. |
| NOME_SOCIAL | varchar(70) |  | S | Nome social. |
| APOSENTADO | smallint(2) |  |  | Aposentado. (0=Não/1=Sim) |
| POSSUI_DEFICIENCIA_INTELECTUAL | smallint(2) |  |  | Possui deficiência intelectual. (0=Não/1=Sim) |
| COTA_DIFICIENTE | smallint(2) |  |  | Cota de deficiente. (0=Não/1=Sim) |
| I_SUPERVISOR_ESTAGIO | integer(4) |  | S | Supervisor de estágio. |
| MOTIVO_PRORROGACAO_CONTRATO_EXPERIENCIA | varchar(50) |  | S | Motivo da prorrogação do contrato de experiência. |
| DESCONTAR_ESTOURO_RESCISAO_EMPRESA_ORIGEM | smallint(2) |  |  | Descontar o estouro de rescisão da empresa origem na empresa destino. (0=Não/1=Sim) |
| DESCONTAR_CONTRIBUICAO_SINDICAL_A_PARTIR_11_2017 | smallint(2) |  |  | Descontar contribuição sindical a partir de 11/2017. (0=Não/1=Sim) |
| COMP_INICIO_DESCONTO_CONTRIBUICAO_SINDICAL_A_PARTIR_11_2017 | date(4) |  | S | Competência de início do desconto da contribuição sindical a partir de 11/2017. |
| PAGA_CONTR_SIND_11_2017 | char(1) |  |  | Pagou contr. sindical após 11/2017? |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| CODI_EMP_ESOCIAL_S_2205 | integer(4) |  | S | **SEM USO** |
| I_EMPREGADOS_ESOCIAL_S_2205 | integer(4) |  | S | **SEM USO** |
| I_DADOS_EVENTOS_ESOCIAL_S_2205 | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL_S_2205 | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL_S_2205 | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL_S_2205 | smallint(2) |  |  | Enviar para o eSocial o evento S-2205. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL_S_2205 | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL_S_2205 | smallint(2) |  |  | Gerar retificação do evento S-2205 para o eSocial. (0=Não/1=Sim) |
| I_DADOS_EVENTOS_ESOCIAL_S_2206 | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL_S_2206 | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL_S_2206 | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL_S_2206 | smallint(2) |  |  | Enviar para o eSocial o evento S-2206. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL_S_2206 | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL_S_2206 | smallint(2) |  |  | Gerar retificação do evento S-2206 para o eSocial. (0=Não/1=Sim) |
| EXCLUIR_EVENTO_S_2205_RETIFICACAO | smallint(2) |  |  | Indica se o empregado possui algum evento S-2205 sendo excluído do eSocial referente a uma retificação que excluiu a alteração. |
| EXCLUIR_EVENTO_S_2206_RETIFICACAO | smallint(2) |  |  | Indica se o empregado possui algum evento S-2206/S-2306 sendo excluído do eSocial referente a uma retificação que excluiu a alteração. |
| LEI_ANISTIA_ADMISSAO | varchar(13) |  | S | Lei de Anistia/Ano. |
| DATA_EFEITO_REINTEGRACAO | date(4) |  | S | Data de efeito da reintegração. |
| NUMERO_PROCESSO_REINTEGRACAO | varchar(20) |  | S | Número do processo de reintegração |
| CODI_EMP_REINTEGRACAO | integer(4) |  | S | Código da empresa do empregado para reintegração. |
| I_EMPREGADOS_REINTEGRACAO | integer(4) |  | S | Código do empregado para reintegração. |
| ENVIAR_S_2200_REINTEGRACAO | smallint(2) |  |  | Enviar para o eSocial o evento S-2200 na reintegração. (0=Não/1=Sim) |
| DESLIGAMENTO_REALIZADO_MESMO_BANCO_REINTEGRACAO | smallint(2) |  |  | Desligamento de empregado reintegrado efetuado no mesmo banco. (0=Não/1=Sim) |
| DESLIGAMENTO_ENVIADO_ESOCIAL_REINTEGRACAO | smallint(2) |  |  | Desligamento de empregado reintegrado enviado ao eSocial. (0=Não/1=Sim) |
| DATA_DESLIGAMETO_REINTEGRACAO | date(4) |  | S | Data de desligamento de empregado reintegrado. |
| ENVIAR_REGISTRO_APOS_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Reenviar automaticamente o registro após a exclusão do mesmo no eSocial. (0=Não/1=Sim) |
| TRANSFERIDO_COM_EMPREGADO_ORIGEM_VALIDADO_NO_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| ENVIAR_CADASTRO_EMPREGADO_EVENTO_S_1200_ESOCIAL | smallint(2) |  |  | Enviar o cadastro do empregado para o eSocial através do evento S-1200. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL_S_2205 | smallint(2) |  |  | Marcação do evento S-2205 para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL_S_2206 | smallint(2) |  |  | Marcação do evento S-2206 para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| CATEGORIA_ESOCIAL | integer(4) |  | S | Código da categoria eSocial. |
| NUMERO_RECIBO_VALIDACAO_UTILITARIO_CONVERSAO_OUTRO_BANCO | varchar(50) |  | S | Número do recibo quando validado pelo utilitário de conversão de outros bancos. |
| GUID_CONTABIL | uniqueidentifier(16) |  |  | Identificador único do registro no banco do Contábil |
| GUID_ONVIO | uniqueidentifier(16) |  | S | Identificador único do registro no banco do Atendimento Onvio |
| ENDPOINT_EXCLUSAO | varchar(1024) |  | S | Endpoint utilizado para a exclusão do registro. |
| GUID_SCE_ONVIO | uniqueidentifier(16) |  | S | Identificador único do registro da SCE no banco de Atendimento Onvio |
| INDICATIVO_OBJETO_DETERMINANTE_CONTRATACAO_PRAZO_DETERMINADO | smallint(2) |  |  | Indicativo do objeto determinante da contratação por prazo determinado - Contrato experiência |
| DESCRICAO_INDICATIVO_OBJETO_DETERMINANTE_CONTRATACAO_PRAZO_DETERMINADO | varchar(255) |  | S | Descrição do Indicativo do objeto determinante da contratação por prazo determinado - Contrato experiência |
| UTILIZA_PORTAL_EMPREGADO | integer(4) |  |  | Indica se o empregado utiliza o Portal do Empregado. (0=Não/1=Sim) |
| EMAIL_PORTAL_EMPREGADO | varchar(60) |  | S | E-mail do empregado enviado para o Portal do Empregado. |
| EMAIL_PORTAL_EMPREGADO_ATIVO | varchar(60) |  | S | E-mail ativado do empregado enviado para o Portal do Empregado. |
| SITUACAO_PORTAL_EMPREGADO | integer(4) |  |  | Indica a situação do empregado ao Portal do Empregado. (0=Não enviado para o portal/1=Ativo/2=Aguardando confirmação) |
| CORE_ONVIO_ID | uniqueidentifier(16) |  | S | GUID do contato no Core quando o mesmo for diferente do GUID do empregado no Portal do Cliente |
| CNPJ_EMPRESA_CEDENTE_CELETISTA_CEDIDO | varchar(14) |  | S | CNPJ da empresa cedente - Celetista Trabalhador Cedido. |
| NOME_EMPRESA_CEDENTE_CELETISTA_CEDIDO | varchar(100) |  | S | Nome da empresa cedente - Celetista Trabalhador Cedido. |
| CATEGORIA_ORIGEM_CELETISTA_CEDIDO | integer(4) |  | S | Categoria de origem - Celetista Trabalhador Cedido. |
| ADMISSAO_EMPRESA_CEDENTE_CELETISTA_CEDIDO | date(4) |  | S | Data admissão na empresa cedente - Celetista Trabalhador Cedido. |
| MATRICULA_EMPRESA_ORIGEM_CELETISTA_CEDIDO | varchar(30) |  | S | Matrícula na empresa origem - Celetista Trabalhador Cedido. |
| REGIME_TRABALHISTA_EMPRESA_CEDENTE_CELETISTA_CEDIDO | smallint(2) |  |  | Regime trabalhista na empresa cedente - Celetista Trabalhador Cedido. (1=CLT/2=Estatutário) |
| REGIME_PREVIDENCIARIO_EMPRESA_CEDENTE_CELETISTA_CEDIDO | smallint(2) |  |  | Regime previdenciário na empresa cedente - Celetista Trabalhador Cedido. (1=Regime Geral da Previdência Social/2=Regime Próprio de Previdência Social/3=Regime de Previdência Social no Exterior) |
| RESPONSAVEL_REMUNERACAO_CELETISTA_CEDIDO | smallint(2) |  |  | Responsável pela remuneração - Celetista Trabalhador Cedido. (1=Cedente/2=Cessionário/3=Cedente e Cessionário) |
| REMUNERACAO_CELETISTA_CEDIDO | numeric(8) |  |  | Remuneração - Celetista Trabalhador Cedido. |
| EMISSOR_CARTAO_VALE_TRANSPORTE | varchar(2) |  |  | Emissor do cartão vale transporte |
| NUMERO_MATRICULA_USUARIO_VALE_TRANSPORTE | varchar(17) |  | S | Número de inscrição do usuario do vale transporte |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| EMPRESA_DESTINO_EM_OUTRO_BANCO_DADOS | integer(4) |  | S | Empresa destino em outro banco de dados (0=Não/1=Sim) |
| TIPO_INSCRICAO_EMPRESA_DESTINO_OUTRO_BANCO_DADOS | integer(4) |  | S | Tipo inscrição empresa destino em outro banco de dados (1=CNPJ/2=CPF) |
| INSCRICAO_EMPRESA_DESTINO_OUTRO_BANCO_DADOS | varchar(14) |  | S | Inscrição empresa destino em outro banco de dados |
| ID_ESOCIAL_VALIDACAO_AUTOMATICA | varchar(70) |  | S | ID do evento importado do eSocial |
| CODIGO_OPERACAO_PAGAMENTO | smallint(2) |  | S | Código da operação de pagamento 0=Não/1=Sim |
| TEMPO_RESIDENCIA | smallint(2) |  |  | Tempo de residência no Brasil. |
| REGIME_TRABALHISTA_EMPRESA_ORIGEM | smallint(2) |  |  | Regime trabalhista na empresa origem. |
| REGIME_PREVIDENCIARIO_EMPRESA_ORIGEM | smallint(2) |  |  | Regime previdenciário na empresa origem. |
| NUMERO_PROCESSO | varchar(20) |  | S | Numero do processo - menor de 16 anos. |
| PAIS_EXIGE_NIF | tinyint(1) |  | S | País exige NIF - Número de Identificação Fiscal |
| DISPENSADO_NIF | tinyint(1) |  | S | Dispensado NIF - Número de Identificação Fiscal |
| CPF_RESPONSAVEL_LEGAL_EMPRESA_ORIGEM_DIRIGENTE_SINDICAL | varchar(11) |  | S | CPF do responsÃ¡vel legal na empresa origem dirigente sindical |
| CATEGORIA_ESOCIAL_AGENTE_PUBLICO | integer(4) |  | S | Categoria esocial do agente publico. |
| CATEGORIA_SEFIP_AGENTE_PUBLICO | integer(4) |  | S | Categoria sefip do agente publico. |
| REGIME_TRABALHISTA_AGENTE_PUBLICO | integer(4) |  | S | Regime trabalhista do agente publico. (1=CLT/2=Estatutário - legislações específicas) |
| REGIME_PREVIDENCIARIO_AGENTE_PUBLICO | integer(4) |  | S | Regime previdenciário do agente publico (1=Regime Geral de Previdência Social - RGPS/2=Regime Próprio de Previdência Social - RPPS) |
| TIPO_PROVIMENTO_AGENTE_PUBLICO | integer(4) |  | S | Regime provimento do agente publico. |
| CHAVE_PIX | varchar(70) |  | S | Valor da chave Pix |
| ENVIAR_ESOCIAL_PERIODO_ANTERIOR_INICIO_BANCO_CONTABIL | smallint(2) |  | S | Enviar evento eSocial anterior ao início da utilização do banco de dados (0=Não/1=Sim) |
| CATEGORIA_ESOCIAL_ESTAGIARIO | integer(4) |  | S | Categoria eSocial do estagiário |
| MUDANCA_CPF_DATA | date(4) |  | S | Mudança de CPF - Data da mudança. |
| MUDANCA_CPF_MATRICULA_ESOCIAL_ANTERIOR | char(30) |  | S | Mudança de CPF - Matrícula eSocial anterior. |
| MUDANCA_CPF_CPF_ANTERIOR | char(11) |  | S | Mudança de CPF - CPF anterior. |
| DATA_HORA_ULTIMA_CONSULTA_PORTAL_EMPREGADO | timestamp(8) |  | S | Data hora de ultima consulta portal empregado |
| CONTRATO_DATA_FIM_VIGENCIA_FUTURA | smallint(2) |  |  | Empregado possui contrato de trabalho com data fim futura |
| CATEGORIA_ESOCIAL_EMPREGADO | integer(4) |  | S | Categoria eSocial do Empregado. |
| IRRF_TIPO_DEDUCAO | smallint(2) |  |  | Tipo de dedução IRRF (1=Deduções Legais/2=Dedução Simplificada Mensal/3=Dedução Favorável ao colaborador) |
| CHAVE_PIX_ALTERNATIVA | varchar(70) |  | S | Valor da chave Pix alternativa |
| INCLUIR_FORMA_PAGAMENTO_ALTERNATIVA | smallint(2) |  | S | Incluir forma de pagamento alternativa 0=Não/1=Sim |
| FORMA_PAGTO_ALTERNATIVA | char(1) |  | S | Forma de pagamento alternativa: (H=Cheque/C=Crédito em conta/D=Dinheiro/P=Pix) |
| I_BANCOS_ALTERNATIVA | integer(4) |  | S | Banco alternativo |
| CONTA_CORR_ALTERNATIVA | char(15) |  | S | Conta corrente alternativa |
| DIGITO_CONTA_PAGAMENTO_ALTERNATIVA | char(2) |  | S | Digito da Conta corrente alternativa |
| TIPO_CONTA_ALTERNATIVA | smallint(2) |  | S | Tipo de conta alternativa: (1=Não informada/2=Conta corrente/3=Conta salário/4=Conta poupança/5=Conta fácil) |
| CODIGO_OPERACAO_PAGAMENTO_ALTERNATIVA | smallint(2) |  | S | Código da operação de pagamento alternativa 0=Não/1=Sim |
| MODALIDADE_CONTRATACAO | integer(4) |  | S | Modalidade da Contratação. |
| CNPJ_ENTIDADE_QUALIFICADORA | varchar(14) |  | S | CNPJ da Entidade Qualificadora. |
| CNPJ_ESTABELECIMENTO_ATIVIDADE_PRATICA | varchar(14) |  | S | CNPJ do Estabelecimento da atividade pratica. |
| ENVIAR_CADASTRO_EMPREGADO_ATRAVES_EVENTO_2500 | smallint(2) |  |  | Enviar cadastro do empregado ao eSocial através do evento S-2500 em decorrência de reconhecimento de vínculo em Reclamatória. |
| CODIGO_MOTIVO_DESLIGAMENTO_ESOCIAL | integer(4) |  | S | Código de motivo do desligamento eSocial. |
| DATA_PROJETADA_TERMINO_AVISO_PREVIO_INDENIZADO | date(4) |  | S | Data projetada para o término do aviso prévio indenizado. |
| INDICATIVO_PENSAO_ALIMENTICIA_PARA_FINS_RETENCAO_FGTS | integer(4) |  | S | Indicativo de pensão alimentícia para fins de retenção de FGTS. |
| PERCENTUAL_PENSAO_ALIMENTICIA | numeric(5) |  | S | Percentual pensão alimentícia. |
| VALOR_PENSAO_ALIMENTICIA | numeric(14) |  | S | Valor pensão alimentícia. |
| ESTABELECIMENTO_CONTRATACAO_INDIRETA | varchar(50) |  | S | Estabelecimento de Contratação Indireta |
| CONSIDERAR_CONTAGEM_AVOS_13_FERIAS_DATA_EFEITO_REINTEGRACAO | smallint(2) |  |  | Considerar para a contagem de avos de direito de 13º salário e férias a partir da data efeito da reintegração. (0=Não/1=Sim) |
| TIPO_PLANO_SEGREGACAO_MASSA_AGENTE_PUBLICO | smallint(2) |  | S | Agente Público - Tipo de plano de segregação da massa. (1=Sem segregação da massa/2=Fundo em capitalização/3=Fundo em repartição/4=Mantido pelo Tesouro) |
| SERVIDOR_SUJEITO_TETO_RGPS_AGENTE_PUBLICO | smallint(2) |  |  | Agente Público - Servidor sujeito ao teto do RGPS pela instituição do regime de previdência complementar. (0=Não/1=Sim) |
| IRRF_EXTERIOR_ISENTO | smallint(2) |  |  | 0 - Não / 1 - Sim, Isenção estabelecida em convênio / 2 - Sim, Isenção prevista em lei interna / 3 - Sim, Alíquota zero prevista em lei interna / 4 - Sim, Pagamento antecipado do imposto / 5 - Sim, Medida judicial / 6 - Sim, Outras hipóteses |
| ENVIAR_ESOCIAL_MANUALMENTE | integer(4) |  |  | Enviar eSocial Manualmente |
| BANKING_EMPLOYEE_ID | uniqueidentifier(16) |  | S | Identificador único do registro na Fintech |
| LAST_SYNC_AT | timestamp(8) |  | S | Data e hora da ultima sincronizacao com a Fintech |
| I_SINDICATOS_CADASTRO | integer(4) |  | S | Código do cadastro do sindicato |
