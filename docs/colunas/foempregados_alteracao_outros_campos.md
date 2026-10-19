# FOEMPREGADOS_ALTERACAO_OUTROS_CAMPOS — Registros de alteração contratual para envio ao eSocial.
18.081 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| DATA_ALTERACAO | date(4) | PK |  | Data da alteração. |
| I_DEPTO | integer(4) |  | S | Código do departamento |
| I_CCUSTOS | integer(4) |  | S | Código do centro de custos |
| SIMPLES_072007 | smallint(2) |  | S | Optante pelo Simples em 07/2007 |
| I_SINDPISO | integer(4) |  | S | Código do sindicato piso |
| RESIDENCIA_PROPRIA | smallint(2) |  | S | Possui residência própria |
| IMOVEL_ADQUIRIDO_RECURSOS_FGTS | smallint(2) |  | S | Imóvel adquirido com recursos do FGTS |
| DDD_FONE2 | varchar(3) |  | S | DDD do telefone |
| FONE2 | varchar(15) |  | S | Telefone |
| NATURALIZADO | char(1) |  | S | Naturalizado |
| NUMERO_PROCESSO_MTE | varchar(30) |  | S | Número do processo no MTE |
| VALIDADE_CTRAB_ESTR | date(4) |  | S | Validade da carteira de trabalho estrangeira |
| FORMA_CALCULO | smallint(2) |  | S | Forma de pagamento. (1=Por mês/2=Por semana/3=Por convocação) |
| CALCULAR_INSS_PATRONAL | smallint(2) |  | S | Calcular INSS patronal |
| DIRIGENTE_SINDICAL | smallint(2) |  | S | Dirigente sindical |
| CNPJ_EMPRESA_ORIGEM_DIRIGENTE_SINDICAL | varchar(14) |  | S | CNPJ da empresa de origem do dirigente sindical |
| NOME_EMPRESA_ORIGEM_DIRIGENTE_SINDICAL | varchar(100) |  | S | Nome da empresa de origem do dirigente sindical |
| CATEGORIA_ORIGEM_DIRIGENTE_SINDICAL | integer(4) |  | S | Categoria de origem do dirigente sindical |
| DATA_ADMISSAO_EMPRESA_ORIGEM_DIRIGENTE_SINDICAL | date(4) |  | S | Data de admissão na empresa de origem do dirigente sindical |
| MATRICULA_EMPRESA_ORIGEM_DIRIGENTE_SINDICAL | varchar(30) |  | S | Matrícula na empresa de origem do dirigente sindical |
| RESPONSAVEL_REMUNERACAO_DIRIGENTE_SINDICAL | smallint(2) |  | S | Responsável pela remuneração do dirigente sindical |
| TIPO_REMUNERACAO_DIRIGENTE_SINDICAL | smallint(2) |  | S | Tipo de remuneração do dirigente sindical |
| DATA_INICIO_PAGAMENTO_ADICIONAL_DIRIGENTE_SINDICAL | date(4) |  | S | Data de início do pagamento adicional ao dirigente sindical |
| REMUNERACAO_EMPRESA_DIRIGENTE_SINDICAL | numeric(17) |  | S | Remuneração na empresa do dirigente sindical |
| REMUNERACAO_SINDICATO_DIRIGENTE_SINDICAL | numeric(17) |  | S | Remuneração no sindicato do dirigente sindical |
| REMUNERACAO_PERIODO_DESLIGAMENTO_REINTEGRACAO_PAGAS_JUIZO | smallint(2) |  | S | Remuneração no período de desligamento/reintegração pagas por juízo |
| POSSUI_VINC_OUT_EMP | char(1) |  | S | Possui vínculo com outra empresa |
| I_BANCOS | integer(4) |  | S | Código do banco |
| AGENCIA_CONTA_PAGAMENTO | varchar(10) |  | S | Agência para pagamento |
| CONTA_CORR | char(15) |  | S | Conta corrente |
| DIGITO_CONTA_PAGAMENTO | char(3) |  | S | Dígito da conta para pagamento |
| TIPO_CONTA | smallint(2) |  | S | Tipo de conta bancária |
| CARGA_HORARIA_VARIAVEL | smallint(2) |  | S | Carga horária variável |
| I_FILIAIS | integer(4) |  | S | Código da filial |
| I_SINDPISO_EXPERIENCIA | integer(4) |  | S | Código do sindicato piso experiência |
| OCO_SEFIP | integer(4) |  | S | Ocorrência SEFIP |
| TIPO_SERVICO | char(1) |  | S | Tipo de serviço |
| HORAS_COMPENSADAS | numeric(5) |  | S | Horas compensadas |
| HORAS_MES | numeric(5) |  | S | Horas trabalhadas no mês |
| HORAS_DIA | numeric(5) |  | S | Horas trabalhadas por dia |
| DATA_EXPEDICAO_CARTEIRA_TRABALHO | date(4) |  | S | Data de expedição da carteira de trabalho |
| ORGAO_EMISSOR_CNH | varchar(20) |  | S | Órgão emissor da CNH |
| DATA_VALIDADE_RNE | date(4) |  | S | Data de validade do RNE |
| DATA_OPCAO_FGTS | date(4) |  | S | Data de opção pelo FGTS |
| I_COORDENADOR_ESTAGIO | integer(4) |  | S | Código do coordenador de estágio |
| FORMA_PAGAMENTO | varchar(255) |  | S | Forma de pagamento |
| CODIGO_MUNICIPIO_RIC | integer(4) |  | S | Código do município do RIC |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Imp. tabelas/2=Imp. layout/3=Imp. tabelas concorrentes) |
| CODIGO_ESOCIAL | varchar(30) |  | S | Código eSocial. |
| CODIGO_ESOCIAL_EMPREGADO_ORIGEM | varchar(30) |  | S | Código eSocial do empregado origem quando transferência, fusão ou sucessão. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| CODIGO_OPERACAO_PAGAMENTO | smallint(2) |  | S | Código da operação de pagamento 0=Não/1=Sim |
| SINDICALIZADO | smallint(2) |  | S | Funcionário sindicalizado |
| PIS | char(11) |  | S | Número do PIS |
| MUNICIPIO_NASCIMENTO | integer(4) |  | S | Código do município de nascimento |
| UF_NASCIMENTO | char(2) |  | S | UF de nascimento |
| NOME_PAI | varchar(70) |  | S | Nome do pai |
| NOME_MAE | varchar(70) |  | S | Nome da mãe |
| EMAIL_ALTERNATIVO | varchar(60) |  | S | E-mail alternativo |
| NUMERO_RIC | char(15) |  | S | Número do RIC |
| ORGAO_EMISSOR_RIC | char(8) |  | S | Órgão emissor do RIC |
| SIGLA_UF_RIC | char(2) |  | S | UF do RIC |
| DATA_EXPEDICAO_RIC | date(4) |  | S | Data de expedição do RIC |
| IDENTIDADE | char(15) |  | S | Número da identidade (RG) |
| ORGAO_EXPEDICAO_RG | varchar(20) |  | S | Órgão emissor do RG |
| UF_EXP_IDENT | char(2) |  | S | UF do órgão expedidor da identidade |
| DATA_EXPEDICAO_RG | date(4) |  | S | Data de expedição do RG |
| NUMERO_RNE | varchar(15) |  | S | Número do RNE |
| ORGAO_EMISSOR_RNE | char(20) |  | S | Órgão emissor do RNE |
| DATA_EXPEDICAO_RNE | date(4) |  | S | Data de expedição do RNE |
| CART_MOTORISTA | char(15) |  | S | Número da carteira de motorista |
| DATA_EXPEDICAO_CNH | date(4) |  | S | Data de expedição da CNH |
| CODIGO_UF_CARTEIRA_MOTORISTA | integer(4) |  | S | Código UF da carteira de motorista |
| VENC_CART_MOT | date(4) |  | S | Data de vencimento da carteira de motorista |
| DATA_PRIMEIRA_HABILITACAO_CARTEIRA_MOTORISTA | date(4) |  | S | Data da primeira habilitação |
| CATEG_CART_MOT | char(3) |  | S | Categoria da carteira de motorista |
| CARTEIRA_PROFISSIONAL | char(16) |  | S | Número da carteira profissional |
| UF_CARTEIRA_PROFISSIONAL | char(2) |  | S | UF da carteira profissional |
| DATA_NATURALIZACAO | date(4) |  | S | Data de naturalização |
| DATA_CHEGADA_ESTRANGEIRO | date(4) |  | S | Data de chegada ao Brasil (estrangeiro) |
| CASADO_BRASILEIRO | smallint(2) |  | S | Casado com brasileiro(a) |
| FILHOS_BRASILEIRO | smallint(2) |  | S | Possui filhos brasileiros |
| POSSUI_DEFICIENCIA_OUTRAS | smallint(2) |  | S | Possui outras deficiências |
| APOSENTADO | smallint(2) |  | S | Aposentado |
| CATEGORIA_SEFIP_AGENTE_PUBLICO | integer(4) |  | S | Categoria sefip do agente publico. |
| CHAVE_PIX | varchar(70) |  | S | Valor da chave Pix |
| IRRF_TIPO_DEDUCAO | integer(4) |  | S | Tipo de dedução IRRF. |
| INCLUIR_FORMA_PAGAMENTO_ALTERNATIVA | smallint(2) |  | S | Incluir forma de pagamento alternativa 0=Não/1=Sim |
| FORMA_PAGTO_ALTERNATIVA | char(1) |  | S | Forma de pagamento alternativa: (H=Cheque/C=Crédito em conta/D=Dinheiro/P=Pix) |
| I_BANCOS_ALTERNATIVA | integer(4) |  | S | Banco alternativo |
| AGENCIA_CONTA_PAGAMENTO_ALTERNATIVA | varchar(10) |  | S | Agência alternativa |
| CONTA_CORR_ALTERNATIVA | char(15) |  | S | Conta corrente alternativa |
| DIGITO_CONTA_PAGAMENTO_ALTERNATIVA | char(2) |  | S | Digito da Conta corrente alternativa |
| TIPO_CONTA_ALTERNATIVA | smallint(2) |  | S | Tipo de conta alternativa: (1=Não informada/2=Conta corrente/3=Conta salário/4=Conta poupança/5=Conta fácil) |
| CODIGO_OPERACAO_PAGAMENTO_ALTERNATIVA | smallint(2) |  | S | Código da operação de pagamento alternativa 0=Não/1=Sim |
| CHAVE_PIX_ALTERNATIVA | varchar(70) |  | S | Valor da chave Pix alternativa |
| IRRF_EXTERIOR_ISENTO | smallint(2) |  |  | 0 - Não / 1 - Sim, Isenção estabelecida em convênio / 2 - Sim, Isenção prevista em lei interna / 3 - Sim, Alíquota zero prevista em lei interna / 4 - Sim, Pagamento antecipado do imposto / 5 - Sim, Medida judicial / 6 - Sim, Outras hipóteses |
