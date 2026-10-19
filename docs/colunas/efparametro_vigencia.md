# EFPARAMETRO_VIGENCIA — Paramentros - Cadastro - Escrita Fiscal
6.450 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| VIGENCIA_PAR | date(4) | PK |  | Vigencia |
| DESCRICAO_PAR | char(80) |  |  | Descricao |
| LCTB_PAR | char(1) |  |  | Gera lancamentos contabeis (S/N) |
| REST_PAR | integer(4) |  |  | Regime estadual (1 - Normal/2 - ME/3 - Estimativa/4 - EPP) |
| RFED_PAR | integer(4) |  |  | Regime federal (1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9) |
| FILI_PAR | integer(4) |  |  | Processa as filiais (1 - Nao/2 - Sim) |
| CRIACTAFOR_PAR | char(1) |  | S | Cada fornecedor gera uma conta (S/N) |
| CLASCTAFOR_PAR | char(20) |  | S | Classificacao de fornecedores |
| NIVDIFFOR_PAR | char(1) |  | S | Nivel diferente para cada conta de fornecedor (S/N) |
| CRIACTACLI_PAR | char(1) |  | S | Cada cliente gera uma conta (S/N) |
| CLASCTACLI_PAR | char(20) |  | S | Classificacao de clientes |
| NIVDIFCLI_PAR | char(1) |  | S | Nivel diferente para cada conta de cliente (S/N) |
| RSIMPR_PAR | integer(4) |  | S | Regime de enquadramento no SIMPLES Estadual |
| CTBMAT_PAR | char(1) |  | S | Lancamentos Contabeis (N - Mesma empresa/S - Outra empresa) |
| CODMAT_PAR | integer(4) |  | S | Codigo da Empresa na Contabilidade |
| GEHO_PAR | char(1) |  |  | Gera Honorarios (S/N) |
| DCOF_PAR | char(1) |  | S | Deducao de 1/3 Cofins na C.SOC (S/N) |
| IPIEPP_PAR | char(1) |  | S | Soma IPI para enquadramento EPP (S/N) |
| SUBST_PAR | char(1) |  | S | Substituicao Tributaria (S/N) |
| CRECHE_PAR | char(1) |  | S | SIMPLES: Creche, pre-escola ou estabelecimento de ensino fundamental (S/N) |
| TEMISS_PAR | integer(4) |  | S | Calcular Simples/PR com ISS (1 - Sim/0 - Nao) |
| CALCPIS_PAR | char(1) |  | S | Nao calcular PIS com incidencia cumulativa a partir de 12/2002 (S/N) |
| CALCICMS_PAR | char(1) |  | S | Apuracao do ICMS conforme decreto 42035 de 12/2002 - RS (S/N) |
| DATAICMS_PAR | date(4) |  | S | Data final do calculo do ICMS conforme decreto 42035 que iniciou em 12/2002 - RS |
| CENTRAL_PAR | integer(4) |  | S | Centralizacao do recolhimento |
| SIMPLESISS_PAR | char(1) |  | S | Calcular Simples Federal com ISS (S/N) |
| BENEFICIO_PAR | char(1) |  | S | Beneficiario do PRODEPE/FUNCRESCE - PE (S/N) |
| REGIMEISS_PAR | integer(4) |  | S | Calcular Simples com ISS para (1 - ME e EPP /2 - Somente ME/4 - Somente EPP) |
| IECENTRAL_PAR | char(10) |  | S | Inscricao Estadual Centralizadora - SE |
| CODIGUALFOR_PAR | char(1) |  | S | Codigo do Fornecedor igual a Conta (S/N) |
| CODIGUALCLI_PAR | char(1) |  | S | Codigo do Cliente igual a Conta (S/N) |
| INTEGRAENT_PAR | char(1) |  | S | Integracao das Entradas (A - Analitica com data da nota/U - Analitica com data do ultimo dia do mes/S - Sintetica por mes/D - Sintetico por dia |
| INTEGRASAI_PAR | char(1) |  | S | Integracao das Saidas (A - Analitica com data da nota/U - Analitica com data do ultimo dia do mes/S - Sintetica por mes/D - Sintetico por dia |
| INTEGRASER_PAR | char(1) |  | S | Integracao dos Servicos (A - Analitica com data da nota/U - Analitica com data do ultimo dia do mes/S - Sintetica por mes/D - Sintetico por dia |
| CALCCOFINS_PAR | char(1) |  | S | Nao calcular COFINS com incidencia cumulativa a partir de 02/2004 (S/N) |
| FUNDESE_PAR | char(1) |  | S | Optante do FUNDESE - MG (S/N) |
| SALDOSIMPLES_PAR | char(1) |  | S | Transfere saldo negativo do faturamento para o proximo mes (S/N) |
| RSICMS2003_PAR | char(1) |  | S | Apuracao do ICMS com antecipacao em 12/2003 - RS (S/N) |
| RSDATAICMS2003_PAR | date(4) |  | S | Data  final do calculo do ICMS com antecipacao que iniciou em 12/2003. |
| SIMPLES50_PAR | char(1) |  | S | Calcular Simples com 50% de aumento para prestadoras de servico (S/N) |
| RSSELECIONADO_PAR | char(1) |  | S | Contribuinte Selecionado - RS (S/N) |
| RMUN_PAR | integer(4) |  | S | Regime Municipal (1 - Normal/2 - Simples) |
| ATLSDOANT_PAR | char(1) |  | S | Atualiza saldos do ano anterior - RS (S/N) |
| CRFFATGER_PAR | char(1) |  | S | Fato gerador da CRF(E - emissao/P - pagamento). |
| IRRFFATGER_PAR | char(1) |  | S | Fato gerador do IRRF(E - emissao/P - pagamento). |
| FAIXARMUN_PAR | integer(4) |  | S | Faixa Inicial do Regime Municipal |
| RSICMS2004_PAR | char(1) |  | S | Apuracao do ICMS com antecipacao em 12/2004 - RS (S/N) |
| RSDATAICMS2004_PAR | date(4) |  | S | Data  final do calculo do ICMS com antecipacao que iniciou em 12/2004. |
| AGRUPAFIL_PAR | char(1) |  | S | Agrupar Lancamentos das filiais (S/N) |
| DFTARE_PAR | char(1) |  | S | DF/SE: Optante da TARE (S/N) |
| DFDECRETO_PAR | char(1) |  | S | Optante do Decreto 23806/2003 - DF (S/N) |
| CONSOLIDADA_PAR | integer(4) |  | S | Apuracao consolidada (1 - Nao/2 - Estabelecimento consolidador/3 - Estabelecimento consolidado) |
| TRANSFERECREDITOS_PAR | char(1) |  | S | Efetua transferencia de creditos acumulados |
| FUNDOSOCIAL_PAR | char(1) |  | S | Efetuar Doacao ao FUNDOSOCIAL |
| PRESTSERV_PAR | char(1) |  | S | Empresa exclusivamente prestadora de servico com aliquota base de LP de 16% |
| SIMPLESISS50_PAR | char(1) |  | S | Calcular Simples com 50% de aumento para prestadoras de servico tambem sobre a aliquota do ISS (S/N) |
| DEDUZ_ISENTAS_SIMPLESPR_PAR | char(1) |  |  | Deduz isentas da base do Simples/PR (S/N) |
| SIMPLES_ALIQ_DIFERENCIADA_PAR | char(1) |  |  | Calcular Simples com aliquota diferenciada(S/N) |
| REGIME_RECOLHIMENTO_PAR | char(1) |  | S | Regime de recolhimento (R - Real/P - Presumido) |
| MVA_PAR | numeric(5) |  | S | Margem do valor agregado |
| SEITEC_PAR | char(1) |  | S | Participa de projeto SEITEC (S/N) |
| ANTECIPADO_MERCADO_PAR | char(1) |  | S | Calcular ICMS antecipado minimercado/supermercado(S/N) |
| CTB_CLIFOR_AVISTA_PAR | char(1) |  | S | Gerar lancamento na conta cliente/fornecedor para parcelas pagas a vista |
| CRFOPFATGER_PAR | char(1) |  | S | Fato gerador da CRFOP(E - emissao/P - pagamento) |
| IRRFPFATGER_PAR | char(1) |  | S | Fato gerador do IRRFP(E - emissao/P - pagamento) |
| DEDUZST_PAR | char(1) |  | S | Deduzir o valor de Substituicao Tributaria da Base do IRPJ e CSLL (S/N) |
| REGIME_ESPECIAL_ST_PAR | char(1) |  | S | Regime especial para recolhimento de substiuicao tributaria(S/N) |
| MES_ATLSDOANT_PAR | integer(4) |  | S | Mes de atualizacao do saldo anterior - RS |
| ADICIONAL_ICMS_PAR | char(1) |  | S | Calcula adicional de ICMS (S/N) |
| ADICIONAL_ARTIGO_PAR | integer(4) |  | S | Artigo base para o calculo do adicional |
| SIMPLESN_ANEXO_I_PAR | char(1) |  | S | Simples Nacional - Anexo I(S/N) |
| SIMPLESN_ANEXO_II_PAR | char(1) |  | S | Simples Nacional - Anexo II(S/N) |
| SIMPLESN_ANEXO_III_PAR | char(1) |  | S | Simples Nacional - Anexo III(S/N) |
| SIMPLESN_ANEXO_IV_PAR | char(1) |  | S | Simples Nacional - Anexo IV(S/N) |
| SIMPLESN_ANEXO_V_PAR | char(1) |  | S | Simples Nacional - Anexo V(S/N) |
| SIMPLESN_OPTANTE_PAR | char(1) |  | S | Simples Nacional - optante (S/N) |
| SIMPLESN_ESCRITORIO_CONT_PAR | char(1) |  | S | Simples Nacional - Escritorio de servicos contabeis (S/N) |
| SIMPLESN_FORMA_CALC_PAR | char(1) |  | S | Simples Nacional - Forma de calculo do ISS (N=Normal/S=Simplificado) |
| SIMPLESN_SIMPLES_MUN_PAR | integer(4) |  | S | Simples Nacional - Faixa Simples Municipal |
| SIMPLESN_ULTRAPASSOU_PAR | char(1) |  | S | Simples Nacional - Ultrapassou sub-limite no ano anterior (S/N) |
| SIMPLESN_CODIGO_ACESSO_PAR | char(12) |  | S | Simples Nacional - Codigo de acesso |
| SCPORTE_PAR | integer(4) |  | S | Porte - SC (1=ME/2=EPP/3=Normal) |
| SIMPLESN_ISS_FIXO_PAR | char(1) |  | S | Simples Nacional - Recolhe ISS fixo (S/N) |
| TIPO_CONTRIBUINTE_PAR | integer(4) |  | S | Tipo de contribuinte(0- Outro/1 - Produtor Rural/2 - Servico trib. ICMS/3 - ME/4 - EPP) |
| CREDITO_PRESUMIDO_PAR | char(1) |  | S | Calcula credito presumido de ICMS-Importacao |
| SIMPLESN_ICMS_FIXO_PAR | char(1) |  | S | Simples Nacional - Recolhe ICMS fixo (S/N) |
| ANTECIPACAO_COMBUSTIVEIS_PAR | char(1) |  | S | Efetua calculo de antecipacao de combustiveis liquido e gasosos(S/N) |
| SIMPLESN_ICMS_NORMAL_PAR | char(1) |  | S | Simples Nacional - Calcular ICMS Normal (S/N) |
| SIMPLESN_CREDITO_ENTRADAS_PAR | char(1) |  | S | Simples Nacional - Aproveitar creditos pelas entradas(S/N) |
| PRO_EMPREGO_PAR | char(1) |  | S | Participa do programa Pro-emprego (S/N) |
| DACON_SEPARAR_CREDITOS_PAR | char(1) |  | S | Separar creditos de importacao(S/N) |
| DACON_DETERMINACAO_DE_CREDITOS_PAR | char(1) |  | S | Metodo de determinacao de creditos(I-somente internos/E-interno e exportacao) |
| SIMPLESN_DEDUZ_SUBTRI_PAR | char(1) |  | S | Simples Nacional - Deduzir o valor de ICMS Substituição Tributária(S/N) |
| FOMENTAR_PAR | char(1) |  | S | Empresa Beneficiaria do Programa Fomentar/Produzir/Microproduzir(S/N) |
| DFDECRETO_NUMERO_PAR | integer(4) |  | S | Numero do Decreto/DF |
| SIMPLESN_REGIME_PAR | char(1) |  | S | Regime de apuracao do Simples Nacional(C-competencia/X-Caixa) |
| SIMPLESN_ESCRITORIO_ANEXO_III_PAR | char(1) |  | S | Simples Nacional - Escritorio de servicos contabeis Anexo III(S/N) |
| SIMPLESN_FORMA_CALC_ANEXO_III_PAR | char(1) |  | S | Simples Nacional - Forma de calculo do ISS - Anexo III (N - Normal /S - Simplificado) |
| SIMPLESN_SIMPLES_MUN_ANEXO_III_PAR | integer(4) |  | S | Simples Nacional - Faixa Simples Municipal - Anexo III |
| SIMPLESN_PORTE_PAR | char(1) |  | S | Porte (E - EPP/M - Microempresa/N - Normal) |
| SIMPLESN_TABELA_ICMS_PAR | char(1) |  | S | Simples Nacional - Tabela do ICMS (E - Estadual/F - Federal) |
| POSSUI_ENT_MERC_INTER_PAR | char(1) |  |  | Possui entrada de mercadorias interestadual sujeitas a antecipacao do imposto (S/N) |
| LANCTO_PLANILHA_NOTA_PAR | char(1) |  |  | Lancamento por (P=planilha/N=nota) |
| CENTRALIZA_SEITEC_PAR | char(1) |  | S | Centraliza o incentivo SEITEC(S/N) |
| SIMPLESN_RS_REFEICOES_PAR | char(1) |  | S | Empresa utiliza a reducao do ICMS, conforme Art. 23, VI do Livro I do RICMS/RS - Receitas de Refeicoes (S/N) |
| SIMPLESN_MEI_PAR | char(1) |  | S | Microempreendedor Individual (S/N) |
| SIMPLESN_MEI_ICMS_PAR | char(1) |  | S | Microempreendedor Individual - ICMS (S/N) |
| SIMPLESN_MEI_ISS_PAR | char(1) |  | S | Microempreendedor Individual - ISS (S/N) |
| NAOUSARCRED_PROTEGE_GO_PAR | char(1) |  |  | Nao utilizar como credito o valor do imposto Protege GO (S/N) |
| ISSCFETABMUNICIPAL_PAR | char(1) |  |  | Calcula ISS conforme tabela municipal (S/N) |
| CONSIDERA_CREDOR_ANTERIOR_PAR | char(1) |  |  | Considerar saldo credor de períodos anteriores no cálculo da CSLL e IRPJ-LP(S/N) |
| CONSIDERA_CREDOR_ANTERIOR_ICMS_PAR | char(1) |  |  | Considerar saldo credor de períodos anteriores no cálculo do ICMS(S/N) |
| CREDENCIAL_PAR | char(13) |  | S | Número da credencial |
| CHAVE_ACESSO_PAR | char(20) |  | S | Chave de acesso |
| SENHA_PAR | char(20) |  | S | Senha |
| FEDERAIS_REGIME_PAR | char(1) |  | S | Regime de apuracao dos impostos federais(C-Competência/X-Caixa) |
| SETOR_TEXTIL_PAR | char(1) |  | S | Regime especial de tributação do ICMS - Estabelecimentos Indústriais dos setores têxtil(S/N) |
| CONTROLA_ESTOQUE_SUBTRI_CAT_17_99_PAR | char(1) |  | S | Controlar estoques de mercadorias sujeitas a Substituição Tributária - Portaria CAT 17/99 (S/N) |
| METODO_CALCULO_CONFRONTO_CAT_17_99_PAR | char(1) |  | S | Método de cálculo do valor de confronto |
| LANCAMENTO_AUTOMATICO_CAT_17_99_PAR | char(1) |  | S | Efetuar lançamento de forma automática na apuração do ICMS próprio (S/N) |
| CLIENTE_REDUCAO_Z_PAR | integer(4) |  | S | Código do cliente padrão para o lançamento da redução Z |
| DETALHAR_CUPONS_FISCAIS_PAR | char(1) |  | S | Detalhar cupons fiscais(S/N) |
| CONTA_PADRAO_REDUCAO_Z_PAR | integer(4) |  | S | Conta contábil padrão para lançamentos a prazo de cupons fiscais |
| INTEGRAECF_PAR | char(1) |  | S | Integracao das Reduções Z (A - Analitica com data da nota/U - Analitica com data do ultimo dia do mes/S - Sintetica por mes/D - Sintetico por dia) |
| ACUMULADOR_PADRAO_CUPOM_FISCAL | integer(4) |  | S | Acumulador padrão para o recebimento de parcelas |
| CODIGO_ESCRITORIO | integer(4) |  | S | Empresa do escritorio |
| RJ_BARES_RESTAURANTES_PAR | char(1) |  | S | Regime especial de tributação de ICMS - Bares, Restaurantes e Similares(S/N) |
| SIMPLESN_UTILIZAR_ARBC_MUNICIPAL_PAR | char(1) |  | S | Utilizar a redução da Base de cálculo da tabela alíquota Municipal(S/N) |
| SIMPLESN_POR_EMISSAO_PAR | char(1) |  | S | Calcular o imposto Simples Nacional com Base na data de emissão da nota (S/N) |
| CALCULAR_PISCOFINS_MOVTO_PRODUTO_PAR | char(1) |  |  | Calcular PIS e COFINS conforme a escrituracao digital - EFD PIS/COFINS (S/N) |
| APURACAO_ALIQ_BASICA_PAR | char(1) |  |  | Apuracao com aliquota basica (S/N) |
| APURACAO_ALIQ_DIFERENCIADA_PAR | char(1) |  |  | Apuracao com aliquotas diferenciadas (S/N) |
| APURACAO_ALIQ_UNIDADE_PRODUTO_PAR | char(1) |  |  | Apuracao com aliquota por unidade de medida de produto (S/N) |
| NATUREZA_JURIDICA_PAR | tinyint(1) |  |  | Natureza juridica (0=Sociedade empresaria em geral/ 1=Sociedade cooperativa/ 2=Entidade sujeita ao PIS/Pasep - Folha de Salarios) |
| VALOR_PRESENTE_LANCAMENTO_PAR | char(1) |  |  | Efetuar lancamentos contabeis ao valor presente (S/N) |
| VALOR_PRESENTE_ENT_CONT_JUROS_PAR | char(1) |  |  | Contabilizar os juros do valor presente em contas especificas - Entradas (S/N) |
| VALOR_PRESENTE_ENT_PART_SIMPLES_PAR | char(1) |  |  | Gerar lancamentos de partida simples - Entradas (S/N) |
| VALOR_PRESENTE_SAISER_CONT_JUROS_PAR | char(1) |  |  | Contabilizar os juros do valor presente em contas especificas - Saidas e Servicos (S/N) |
| VALOR_PRESENTE_SAISER_PART_SIMPLES_PAR | char(1) |  |  | Gerar lancamentos de partida simples - Saidas e Servicos (S/N) |
| EMITE_MAPA_RESUMO_ECF_PAR | char(1) |  |  | Emite mapa resumo do ECF (S/N) |
| MG_CREDITO_PRESUMIDO_ST_TRANSPORTE_PAR | char(1) |  |  | Calcular crédito presumido de 20% - ICMS ST Transporte(S/N) |
| CALCULAR_ADICIONAL_IRPJ_MENSALMENTE_PAR | char(1) |  |  | Calcular adicional do IRPJ mensalmente quando o valor acumulado no mês ultrapassar o limite(S/N) |
| SC_CREDITO_PRESUMIDO_TRANSPORTADORA_PAR | char(1) |  |  | Crédito presumido de 20% - ICMS ST Transportadora(S/N) |
| SC_CREDITO_PRESUMIDO_TRANSPORTADORA_TIPO_PAR | char(2) |  |  | Tipo do crédito presumido transportadora (20=Crédito Presumido - 20%/ 40=Crédito Presumido Pró-Cargas - 40%/ 50=Crédito Presumido Pró-Cargas - 50% / 30=Crédito Presumido Pró-Cargas - 30%) |
| INTEGRA_ECF_BILHETE_PAR | char(1) |  |  | Integracao das Reduções Z - Bilhetes de passagem (A - Analitica com data da nota/U - Analitica com data do ultimo dia do mes/S - Sintetica por mes/D - Sintetico por dia |
| INTEGRA_RESUMO_MOVIMENTO_DIARIO_PAR | char(1) |  |  | Integracao dos Resumos movimento diário (A - Analitica com data da nota/U - Analitica com data do ultimo dia do mes/S - Sintetica por mes/D - Sintetico por dia |
| INTEGRA_BILHETE_PASSAGEM_PAR | char(1) |  |  | Integracao dos Bilhetes de passagem (A - Analitica com data da nota/U - Analitica com data do ultimo dia do mes/S - Sintetica por mes/D - Sintetico por dia |
| APURACAO_ATIVIDADE_IMOBILIARIA_PAR | char(1) |  |  | Apuração com atividade imobiliária (S/N) |
| LUCRO_PRESUMIDO_FORMA_CALCULO_PAR | char(1) |  |  | Forma de cáclulo do PIS/COFINS EFD lucro presumido (S - simplificado/C - completo) |
| LUCRO_PRESUMIDO_LANCAMENTO_PAR | char(1) |  |  | Tipo do lançamento para o cáclulo do PIS/COFINS EFD lucro presumido (N - por nota/P - por produto) |
| POSSUI_REGIME_ESPECIAL_OPERACOES_INTERMUN_PAR | char(1) |  |  | Possui regime especial para operações intermunicipais |
| NUMERO_ATO_DECLARATORIO_PAR | varchar(8) |  | S | Nº Ato Declaratório |
| PROBAN_PAR | char(1) |  |  | Regime Especial - Instituições Financeiras (S/N) |
| TIPO_SOCIEDADE_COOPERATIVA_PAR | tinyint(1) |  |  | Tipo de sociedade cooperativa (1=Cooperativa de Produção Agropecuária/ 2=Cooperativa de Consumo/ 3=Cooperativa de Crédito/ 4=Cooperativa de Eletrificação Rural/ 5=Cooperativa de Transporte Rodoviário de Cargas/ 6=Cooperativa de Médicos/ 99=Outras) |
| SC_FUNDOSOCIAL_SUBTRI_PAR | char(1) |  |  | Efetua doação para o Fundosocial - Substituição tributária (S/N) |
| TIPO_CALCULO_ISS | integer(4) |  |  | Tipo de cálculo do ISS |
| CLASSE_PROFISSIONAL_CALCULO_ISS | integer(4) |  | S | Clase profissional de cálculo do ISS |
| SIMPLESN_CALCULAR_ISS_MUNICIPAL | char(1) |  |  | Calcular ISS conforme legislação Municipal |
| SIMPLESN_TIPO_CALCULO_ISS | integer(4) |  |  | Tipo de cálculo do ISS |
| SIMPLESN_FAIXA_ISS | integer(4) |  | S | Faixa do ISS do Simples Municipal |
| SIMPLESN_CLASSE_PROFISSIONAL_CALCULO_ISS | integer(4) |  | S | Clase profissional de cálculo do ISS |
| EXIGIR_AIDF_SAIDAS | char(1) |  |  | Exigir cadastro de AIDF para notas fiscais de energia elétrica, comunicações e telecomunicações |
| CREDITO_PRESUMIDO_TRANSPORTADORA_RJ | char(1) |  |  | Crédito Presumido de 20% para transportadoras - Convênio 106/96 |
| CREDITO_PRESUMIDO_TRANSPORTADORA_SP | char(1) |  |  | Crédito Presumido de 20% para transportadoras - Convênio 106/96 |
| CREDITO_PRESUMIDO_TRANSPORTADORA_MG | char(1) |  |  | Crédito Presumido de 20% para transportadoras - Convênio 106/96 |
| TIPO_ATIVIDADE_SP | integer(4) |  | S | Tipo de atividade (1-Atacadista/2-Varejista) |
| MT_DATA_CADASTRO_SEFAZ | date(4) |  |  | MT - Data do Cadastro no SEFAZ |
| SC_CREDITO_PRESUMIDO_CONFECCAO_ART_15 | char(1) |  |  | Crédito Presumido Confecção Art. 15 |
| PIS_COFINS_POSSUI_RECEITA_DIFERIDA | char(1) |  |  | Possui Receita diferida para as contribuições do PIS e COFINS - Art. 25 da IN 247/2002 |
| CONSIDERAR_JURO_MULTA_RECEITA_CSLL_IRPJ | char(1) |  |  | Considerar juros e multas como receita financeira no calculo dos impostos CSLL e IRPJ-LP |
| RJ_CALCULAR_FECP_ICMS_NORMAL_ALIQUOTA | integer(4) |  |  | Calcular FECP-ICMS Normal com base na alíquota do ICMS (1=Da Nota/2=Do Movimento de Estoque) |
| SC_CONTRIBUI_FUNDOSOCIAL | char(1) |  |  | Contribui ao FUNDOSOCIAL |
| SC_CALCULA_FUNDOSOCIAL_SOBRE | integer(4) |  |  | CALCULAR O FUNDOSOCIAL SOBRE (1/2/3/4) |
| SC_CALCULAR_OPERACAO_IMPOSTOS | integer(4) |  |  | Calcular para operações com os impostos(1 - ICMS/2 - Substituição Tributária/3 - ICMS e Substituição Tributária) |
| OPTANTE_MINHA_CASA_MINHA_VIDA | char(1) |  |  | Optante pelo programa Minha Casa Minha Vida |
| FATO_GERADOR_OPERACOES_SAIDA | char(1) |  |  | Fato gerador dos impostos nas operações de saídas |
| SC_CREDITO_PRESUMIDO_INFORMATICA | char(1) |  |  | Crédito Presumido Ind. Prod. Informática - Anexo 2, Art. 142 RICMS |
| MS_APROVEITAR_SUBTRI_ENTRADA | char(1) |  |  | Aproveitar o valor do imposto Substituição Tributária das entradas |
| MS_APROVEITAR_SUBTRI_ENTRADA_TIPO | tinyint(1) |  |  | Aproveitar o valor do imposto Substituição Tributária das entradas (1-Integralmente / 2-Proporcional ao materia utilizado) |
| MG_POSSUI_ENTRADA_FARINHA_TRIGO_SUB_TRIB_PAR | char(1) |  |  | Possui entradas de farinha de trigo sujeita a antecipação tributária |
| MG_ENTRADA_FARINHA_TRIGO_SUB_TRIB_TIPO_PAR | tinyint(1) |  | S | Entradas de farinha de trigo sujeita a antecipação tributária tipo(1 - Lançamento crédito por nota/2 - Lançamento crédito por mês) |
| DF_CALCULAR_ADICIONAL_FUNDO_POBREZA | char(1) |  |  | Calcular adicional do Fundo de Combate a Pobreza |
| DF_CALCULAR_ADICIONAL_FUNDO_POBREZA_TIPO | integer(4) |  |  | Calcular adicional do Fundo de Combate a Pobreza por (1=Nota / 2=Produto) |
| GERAR_SAIDA_SEM_ICMS_EM | char(1) |  |  | Gerar saída sem ICSM em (I - Isentas/O - Outras) |
| BA_CALCULAR_ICMSA_CONFORME_ART_275 | char(1) |  |  | Calcular o imposto 27-ICMSA conforme Art. 275 RICMS/BA(S/N) |
| PE_INDICADOR_EXIGIBILIDADE | integer(4) |  | S | Indicador de exigibilidade |
| PE_SEF_ESCRITURACAO_CONTABIL | integer(4) |  | S | Perfil e marcadores - Escrituração contábil |
| PE_SEF_GRAFICA | integer(4) |  | S | Perfil e marcadores - Gráficas |
| PE_SEF_UTILIZACAO_DOCUMENTO | integer(4) |  | S | Perfil e marcadores - Utilização de documentos |
| PE_SEF_ESTOQUE_AVULSO | integer(4) |  | S | Perfil e marcadores - Estoque avulso |
| PE_SEF_ESTOQUE_ANUAL | integer(4) |  | S | Perfil e marcadores - Estoque anual |
| FATO_GERADOR_IRPF_APF | char(1) |  |  | Fato gerador do IRRF-APF(E - Emissão/P - Pagamento). |
| SIMPLESN_TRIBUTAR_PARCELA_NAO_RECEBIDA | integer(4) |  |  | Tributar as parcelas não recebidas conforme Art. 19, I da Resolução CGSN 94/2011 |
| CALCULAR_BONUS_ADIMPLENCIA_FISCAL_CSLL | char(1) |  |  | Calcular o bônus adimplência fiscal na CSLL |
| BA_UTILIZAR_ICMSA_CREDITO_ICMS | char(1) |  |  | Utilizar o valor do imposto 27-ICMSA como crédito na apuração do imposto 1-ICMS(S/N) |
| SE_CREDITO_PRESUMIDO_TRANSPORTADORA | char(1) |  |  | Crédito presumido de 20% para transportadoras - Convênio 106/96 |
| DESCONTAR_VALOR_ICMS_CFOP_5929_6929 | char(1) |  |  | Desconsiderar os valores de ICMS das notas com CFOP 5.929/6.929 |
| RS_REGIME_ESPECIAL_PAGAMENTO_ART_53E | char(1) |  |  | Possui regime especial de pagamento conforme Art. 53-E I do livro III do RICMS/RS |
| SPED_FISCAL_PERFIL | char(1) |  |  | SPED - Perfil de apresentacao (A/B/C) |
| DESCONTAR_VALOR_ICMS_IPI_CFOP_MERCANTIL | char(1) |  |  | Desconsiderar os valores de ICMS e IPI das notas com CFOP de consignação mercantil |
| FATO_GERADOR_ISS_RETIDO | char(1) |  |  | Fato gerador do ISS Retido(E - Data de Entrada/P - Data de Pagamento/M - Data de Emissão/S - Mês subsequente a emissão) |
| SC_CREDITO_PRESUMIDO_SAIDA_PEIXE_PAR | char(1) |  |  | Crédito Presumido na Saídas de Peixes, Crustáceos ou Moluscos - An 2, Art 21, Inc VI |
| DEDUZIR_ST_PIS_COFINS_BASE_IRPJ_CSLL | char(1) |  |  | Deduzir o valor do Substituição Tributária do PIS e COFINS da base do IRPJ e CSLL(S/N) |
| APROVEITA_CREDITO_UTILIZAR_SALDO_CREDOR | tinyint(1) |  |  | Utilizar saldo credor (1 - Do período mais recente / 2 - Do período mais antigo) |
| APROVEITA_CREDITO_PRIORIZAR_POR | tinyint(1) |  |  | Priorizar aproveitamento de crédito por (1- Tipo de crédito / 2 - Competência do saldo) |
| MT_CALCULO_IMPOSTO_FETHAB | tinyint(1) |  |  | Cálculo do Imposto FETHAB (1 - Por nota / 2 - Por produto) |
| MG_CREDITO_PRESUMIDO_BARES_RESTAURANTES_SIMILARES | char(1) |  |  | MG - Crédito Presumido Bares, restaurantes e similares |
| EMPRESA_VAREJISTA_COMBUSTIVEL | char(1) |  |  | Empresa do ramo varejista de combustíveis(Postos de combustíveis) (S/N) |
| EMPRESA_VAREJISTA_COMBUSTIVEL_TIPO | tinyint(1) |  |  | Informar movimentação de combustíveis (1 - Pelo lançamentos de notas / 2 - Pelo menu Movimentos/Combustíveis) |
| SC_POSSUI_TTD_409_410_411 | char(1) |  |  | SC - Possui Tratamento Tributário Diferenciado - TTD 409, 410 ou 411 (S/N) |
| SC_CREDITO_PRESUMIDO_ABATEDOR_GADO | char(1) |  |  | SC - Crédito Presumido ao estabelecimento abatedor de gado bovino - An2, Art. 16 |
| SC_CREDITO_PRESUMIDO_SAIDAS_MADEIRA | char(1) |  |  | SC - Crédito Presumido nas saídas de madeira serrada - An2, Art. 15, XLIII |
| RO_POSSUI_INCENTIVO_CONSIT | char(1) |  |  | RO - Possui incentivo tributário CONSIT - Decreto n 12.988/2007 |
| RO_POSSUI_INCENTIVO_CONSIT_PERCENTUAL | numeric(5) |  |  | RO - Percentual do crédito presumido |
| MT_CREDITO_PRESUMIDO_SERVICO_TRANSPORTE | char(1) |  |  | MT - Crédito presumido na prestação de serviço de transporte interestadual - Art. 3, Anexo IX |
| MT_CREDITO_PRESUMIDO_ALGODAO | char(1) |  |  | MT - Crédito presumido na saída interestadual de algodão - Art. 8-A, Anexo IX |
| MT_CREDITO_PRESUMIDO_PRODEIC | char(1) |  |  | MT - Crédito presumido do Programa de Desenvolvimento Industrial e Comercial - PRODEIC |
| SIMPLESN_DEDUZ_SUBTRI_OPCAO_PAR | integer(4) |  | S | Simples Nacional - Deduzir o valor de ICMS Substituição Tributária - Opção |
| FORMA_CALCULO_INSS_RB | tinyint(1) |  | S | Forma de Cálculo (1 - Conforme CNAE principal / 2 - Conforme NCM e serviços) |
| I_CNAE_INSS_RB | char(15) |  | S | CNAE Principal |
| I_ATIVIDADE_INSS_RB | char(8) |  | S | Código de atividade INSS |
| ALIQUOTA_INSS_RB | numeric(7) |  |  | Código de atividade INSS - Alíquota |
| ATIVIDADE_INDUSTRIA_INSS_RB | char(1) |  |  | Atividades - Indústria |
| ATIVIDADE_COMERCIO_INSS_RB | char(1) |  |  | Atividades - Comércio |
| ATIVIDADE_SERVICO_TRANSPORTE_INSS_RB | char(1) |  |  | Atividades - Serviço de Transporte |
| ATIVIDADE_DEMAIS_SERVICOS_INSS_RB | char(1) |  |  | Atividades - Demaos Serviços |
| ALIQUOTA_RECEITAS_NAO_REL_INFERIOR_5_INSS_RB | numeric(5) |  | S | Alíquota para receitas não relacionadas inferior a 5% (1 - 1,00% - Art. 8º da Lei 12.546 / 2 - 2,00% - Art. 7º da Lei 12.546 / 3 - Da atividade com maior receita) |
| FORMA_LANCAMENTO_INSS_RB | integer(4) |  | S | Forma de lançamento (1 - Por nota / 2 - Por produto) |
| PR_REGIME_ESPECIAL_RECOLHIMENTO_ICMS | char(1) |  |  | Regime especial de recolhimento de ICMS - RERI |
| PR_NUMERO_RERI | char(20) |  | S | Número do RERI |
| ES_CREDITO_PRESUMIDO_TRANSPORTADORA | char(1) |  |  | Crédito presumido de 20% para transportadoras - Convênio ICMS 106/96 |
| RS_CREDITO_PRESUMIDO_SAIDAS_ARROZ | char(1) |  |  | RS - Crédito presumido nas saídas interestaduais de arroz beneficiado - Livro I, art. 32, XXXIII |
| CALCULAR_ISS_LIMITADO_RECEITA | char(1) |  |  | Calcular o ISS limitado a 5% da receita - Art. 13°, § 5°, da Lei n° 8.725/2003 |
| SC_CREDITO_PRESUMIDO_MATERIAL_RECICLADO | char(1) |  |  | SC - Crédito Presumido Material Reciclável - An2, Art. 21, XII |
| SC_CREDITO_PRESUMIDO_CONFECCAO_ART_15_TIPO | integer(4) |  |  | SC - Crédito Presumido Confecção Art. 15 - Tipo Calculo |
| MS_CREDITO_PRESUMIDO_TRANSPORTADORA_10696 | char(1) |  |  | MS - Crédito presumido de 20% para transportadoras - Convênio 106/96 |
| MG_CREDITO_PRESUMIDO_TRANSPORTE_RODOVIARIO | char(1) |  |  | MG - Crédito presumido transporte rodoviário de passageiros - Art. 75, XXXI, do RICMS |
| MG_REGIME_ESPECIAL_FISCALIZACAO | char(1) |  |  | MG - Regime Especial de Fiscalização |
| RS_CREDITO_PRESUMIDO_SAIDAS_INFO_ALTO_FALANTES | char(1) |  |  | RS - Crédito presumido nas saídas de prod. de informática/alto-falantes, rec. - Livro I, art. 32, VIII |
| RJ_CREDITO_PRESUMIDO_INFORMATICA_ELETRO | char(1) |  |  | RJ - Crédito Presumido prod. informática, eletroeletrônicos e eletrodomésticos - Dec. 42.649/2010 |
| SIMPLESN_EMITIR_AVISO_RECEITA_BRUTA | char(1) |  |  | Simples Nacional - Emitir aviso quando a receita bruta atingir o limite de enquadramento em até |
| SIMPLESN_EMITIR_AVISO_RECEITA_BRUTA_VALOR | numeric(7) |  |  | Simples Nacional - Emitir aviso quando a receita bruta atingir o limite de enquadramento em até - Valor |
| POSSUI_SCP | char(1) |  |  | Possui Sociedade em Conta de Participação - SCP |
| PE_CREDITO_PRESUMIDO_20_TRANSPORTADORA_ICMS | char(1) |  |  | PE - Crédito presumido de 20% para transportadoras - Convênio ICMS 106/96 |
| CE_CREDITO_PRESUMIDO_20_TRANSPORTADORA_ICMS | char(1) |  |  | CE - Crédito presumido de 20% para transportadoras - Convênio ICMS 106/96 |
| RJ_POLITICA_RECUPERACAO_INDUSTRIAL_REGIONALIZADA | char(1) |  |  | RJ - Regime especial de tributação de ICMS - Política de Recuperação Industrial Regionalizada (S/N) |
| RS_POSSUI_OPERACAO_FARMACIA_BONIFICACAO | char(1) |  |  | RS - Possui operações internas com produtos farmacêuticos recebidos a título de bonificação |
| RS_POSSUI_OPERACAO_FARMACIA_BONIFICACAO_LANC | char(1) |  |  | RS - Possui operações internas com produtos farmacêuticos recebidos a título de bonificação - Lancamento por (P=Planilha / N=Nota) |
| TO_CREDITO_PRESUMIDO_MERCADORIA_ST | char(1) |  |  | TO - Crédito presumido na aquisição de mercadorias sujeita a ST - Lei N° 1.201/2000, Art. 1°, III (S/N) |
| GERAR_LANCAMENTO_CREDITO_PIS_COFINS | char(1) |  |  | Gerar lançamento dos créditos de PIS/COFINS conforme o valor das notas |
| BA_CALCULAR_FUNCEP | char(1) |  |  | BA - Calcular o Fundo de Combate a Erradicação da Pobreza - FUNCEP (S/N) |
| BA_CALCULAR_FUNCEP_TIPO | integer(4) |  |  | BA - Calcular o Fundo de Combate a Erradicação da Pobreza - FUNCEP por: 1-Notas / 2-Produtos |
| ENTIDADE_FINANCEIRA_EQUIPARADA | char(1) |  |  | Entidade Financeira e/ou Equiparada |
| SC_CREDITO_PRESUMIDO_ARROZ_BENEFICIADO | char(1) |  |  | SC - Crédito Presumido nas Saídas de Arroz Beneficiado - An2, Art. 15, XX (S/N) |
| SC_CREDITO_PRESUMIDO_BARES_RESTAURANTES_SIMILARES | char(1) |  |  | SC - Crédito Presumido Bares, Restaurantes e Similares - An2, Art. 21, IV (S/N) |
| EMPRESA_REVENDA_VEICULOS | char(1) |  |  | Empresa com atividade de revenda de veículos (S/N) |
| SC_CREDITO_PRESUMIDO_ENTRADA_LEITE | char(1) |  |  | SC - Crédito Presumido na entrada de leite in natura (S/N) |
| RJ_CREDITO_PRESUMIDO_SAIDAS_EMBARCACOES_NAUTICAS | char(1) |  |  | RJ - Crédito Presumido nas saídas com embarcações náuticas - Dec. 41.681/2009 (S/N) |
| DF_CREDITO_PRESUMIDO_20_TRANSPORTADORA_ICMS | char(1) |  |  | DF - Crédito Presumido de 20% para Transportadoras - Convênio ICMS 106/96 |
| RO_CREDITO_PRESUMIDO_BARES_RESTAURANTES | char(1) |  |  | RO - Crédito presumido de bares e restaurantes - Item 21 Tabela 1 Anexo IV (S/N) |
| BA_GERAR_INFORMATIVO_COMPRA_LEGAL | char(1) |  |  | BA - Gera informativo Compra Legal (S/N) |
| BA_CREDITO_PRESUMIDO_CONFECCAO | char(1) |  |  | BA - Crédito Presumido de Confecção (S/N) |
| BA_CREDITO_PRESUMIDO_CONFECCAO_ALIQUOTA | numeric(7) |  |  | BA - Crédito Presumido de Confecção - Alíquota |
| EFETUA_APURACAO_SIMPLIFICADA_CRED_ACU_ICMS | char(1) |  |  | Efetua apuração simplificada do crédito acumulado do ICMS |
| DIFALI_POR_PRODUTO | char(1) |  |  | Calcular por produto o diferencial de alíquota destinado a uso, consumo ou ativo imobilizado |
| SC_CREDITO_PRESUMIDO_SAIDAS_ERVA_MATE | char(1) |  |  | SC - Crédito Presumido nas saídas de erva-mate (S/N) |
| TO_CREDITO_PRESUMIDO_75_ICMS_APURADO | char(1) |  |  | TO - Crédito presumido de 75% sobre o ICMS apurado (S/N) |
| TO_CREDITO_PRESUMIDO_75_NRO_TARE | varchar(20) |  | S | TO - Crédito presumido de 75% sobre o ICMS apurado - Número TARE |
| TO_CREDITO_PRESUMIDO_75_DATA_VENCIMENTO | date(4) |  | S | TO - Crédito presumido de 75% sobre o ICMS apurado - Data de Vencimento |
| CONSIDERAR_FRETE_SEGURO_DESPESA_TIPO | integer(4) |  |  | Considerar receita de Frete, Seguros e Despesas Acessórias |
| RS_CREDITO_PRESUMIDO_SAIDA_PEIXES | char(1) |  |  | RS - Crédito presumido nas saídas de peixes, crustáceos e moluscos |
| RS_CREDITO_PRESUMIDO_20_TRANSPORTADORA_ICMS | char(1) |  |  | RS - Crédito presumido de 20% para transportadoras - Convênio ICMS 106/96 |
| MG_CREDITO_PRESUMIDO_PRODUTOR_RURAL_PF | char(1) |  |  | MG - Crédito Presumido ao Produtor Rural Pessoa Física (S/N) |
| MG_CALCULAR_FEM | char(1) |  |  | MG - Calcular o Fundo de Erradicação da Miséria - FEM (S/N) |
| MG_CALCULAR_FEM_TIPO | integer(4) |  |  | MG - Calcular o Fundo de Erradicação da Miséria - FEM - Tipo (1-Nota / 2-Produto) |
| RS_CREDITO_PRESUMIDO_FABRIC_PROD_SAUDE_MEDIC | char(1) |  |  | RS - Crédito presumido p/ fabricante de prod. de saúde e medicamentos (S/N) |
| RS_EMPRESA_BENEFICIA_FUNDOPEM | char(1) |  |  | RS - Empresa beneficiária do FUNDOPEM/RS (S/N) |
| SE_POSSUI_INCENTIVO_PSDI | char(1) |  |  | Possui incentivo PSDI - Programa Sergipano de Desenvolvimento Industrial, Lei nº 3.140/91 |
| SC_FORMA_CALCULO_TTD | char(1) |  |  | Possui Tratamento Tributário Diferenciado - TTD 409, 410 ou 411 - Forma de cálculo |
| SC_CREDITO_PRESUMIDO_CONFECCAO_ART_21 | char(1) |  |  | Crédito Presumido Confecção - Anexo 2, Art. 21, IX |
| MG_CREDITO_PRESUMIDO_CARNES | char(1) |  |  | Crédito presumido de peixes, abate ou proces. de aves e de gado - Art. 75, IV do RICMS |
| POSSUI_PRODUTO_TRIBUTACAO_MONOFASICA_PISCOFINS | char(1) |  |  | Possui produto com tributação monofásica de PIS e COFINS |
| BA_CREDITO_PRESUMIDO_IND_VESTUARIO_ART_270 | char(1) |  |  | Crédito Presumido de vestuário, calçados e artefatos de tecidos - Art. 270, V |
| SC_CREDITO_PRESUMIDO_ABATEDORES | char(1) |  |  | Crédito presumido aos estabelecimentos abatedores - An2, Art. 17 (S/N) |
| SC_CREDITO_PRESUMIDO_SAIDA_EMBARCACAO_NAUTICA | char(1) |  |  | SC - Crédito Presumido nas saídas de embarcações náuticas - An2, Art.176 |
| MG_CREDITO_PRESUMIDO_CARGA_TRIBUTARIA | char(1) |  |  | MG - Crédito presumido com carga tributária equivalente a 3% - Art. 75, XIV do RICMS |
| MG_CREDITO_PRESUMIDO_ACUCAR_ALCOOL | char(1) |  |  | MG - Crédito Presumido ao fabricante de álcool ou açúcar - Art.75, XXXII do RICMS |
| RS_CREDITO_PRESUMIDO_CALCADOS | char(1) |  |  | RS - Crédito presumido fabricantes de calçados ou de artefatos de couro - Livro I, art. 32, CXLI |
| MG_CREDITO_PRESUMIDO_DOCES | char(1) |  |  | MG - Crédito presumido de polpas, doces, conservas, molhos e outros - Art.75, XII do RICMS |
| SC_CREDITO_PRESUMIDO_SAIDA_INDUSTRIALIZACAO_LEITE | char(1) |  |  | SC - Crédito Presumido nas saídas de industrialização de leite (S/N) |
| RS_CREDITO_PRESUMIDO_MICROCERVEJARIAS | char(1) |  |  | RS - Crédito presumido microcervejarias (S/N) |
| SOMAR_ICMS_STAT_BASE_PIS_COFINS | char(1) |  |  | Somar o valor do ICMS ST Antecipação Total na base de cálculo do PIS e da COFINS |
| CE_CREDITO_PRESUMIDO_SUINOS | char(1) |  |  | CE - Crédito Presumido nas operações com suínos (S/N) |
| PB_CREDITO_PRESUMIDO_20_TRANSPORTADORA_ICMS | char(1) |  |  | PB - Crédito presumido de 20% para transportadoras - Convênio ICMS |
| SC_APURA_CREDITO_PRESUMIDO_CONFECCAO_ART_21 | char(1) |  |  | SC - Apurar o Crédito Presumido Anexo 2, Art. 21, IX, no estabelecimento centralizador (S/N) |
| SC_APURA_CREDITO_PRESUMIDO_CONFECCAO_ART_21_CODI_EMP | integer(4) |  | S | SC - Empresa - Apurar o Crédito Presumido Anexo 2, Art. 21, IX, no estabelecimento centralizador |
| ISS_RECOLHER_DIFERENCA_FIXO_APURADO | char(1) |  |  | Recolher o valor da diferença entre o ISS fixo e o apurado - Art. 24. VI. a, Dec. 17.419/2011 |
| MS_CREDITO_PRESUMIDO_BARES_RESTAURANTES | char(1) |  |  | MS - Crédito presumido bares, restaurantes e similares (S/N) |
| SC_ANTECIPACAO_SERVICO_TELECOMUNICACAO | char(1) |  |  | SC - Efetuar cálculo de antecipações do ICMS das prestações de serviços de telecomunicações |
| SC_CREDITO_PRESUMIDO_VENDAS_INTEREST_INTERNET | char(1) |  |  | SC - Crédito presumido nas vendas interestaduais a consumidor por meio da internet - An2, Art. 15, XXX |
| PA_CREDITO_PRESUMIDO_20_TRANSPORTADORA_ICMS | char(1) |  |  | PA - Crédito presumido de 20% para transportadoras - Convênio ICMS 106/96 |
| RS_CREDITO_PRESUMIDO_CALCADOS_CXXX | char(1) |  |  | Crédito presumido fabricantes de calçados ou de artefatos de couro - Livro I, art. 32, CXXX |
| MS_POSSUI_BENEFICIO_PROGRAMA_FOMENTO | char(1) |  |  | MS - Possui benefício do Programa de Fomento à Industrialização - Lei Comp. nº 93/2001 |
| MS_POSSUI_BENEFICIO_PROGRAMA_FOMENTO_PERC | numeric(13) |  |  | MS - Percentual - Possui benefício do Programa de Fomento à Industrialização - Lei Comp. nº 93/2001 |
| CE_ATIVIDADE_ENQUADRAMENTO | integer(4) |  |  | CE - Enquadramento - atividade (1-Bares, restaurantes e similares / 2-Comércio varejista) |
| RS_APURACAO_CENTRALIZADA | integer(4) |  |  | RS - Apuração Centralizada - Opções (0/1/2) |
| FATO_GERADOR_IRRF_ENTRADA | char(1) |  |  | Fato Gerador IRRF - Entradas (E/P) |
| FATO_GERADOR_IRRF_SAIDA | char(1) |  |  | Fato Gerador IRRF - Saídas (E/P) |
| RS_CREDITO_PRESUMIDO_ESTAB_RECICLADORES | char(1) |  |  | Crédito presumido aos estabelecimentos recicladores (S/N) |
| RO_CREDITO_PRESUMIDO_20_TRANSPORTADORA_ICMS | char(1) |  |  | RO - Crédito presumido de 20% para transportadoras - Convênio ICMS 106/96 |
| PR_ESTORNAR_CREDITO_ICMS_ART_71 | char(1) |  |  | PR - Estornar crédito de ICMS conforme Art. 71 RICMS (S/N) |
| PR_ESTORNAR_CREDITO_ICMS_ART_71_TIPO_CALCULO | integer(4) |  |  | PR - Estornar crédito de ICMS conforme Art. 71 RICMS - Tipo (0/1) |
| SC_8095_RECOLHER_VALOR_MINIMO_ISS | char(1) |  |  | SC - Recolher o valor mínimo de ISS conforme Lei Complementar (S/N) |
| MS_CREDITO_OUTORGADO_OPERACAO_INTERESTADUAL_MILHO | char(1) |  |  | Crédito outorgado nas operações interestaduais com milho (S/N) |
| RO_CREDITO_PRESUMIDO_INDUSTRIAS_TORREFADORAS | char(1) |  |  | RO - Crédito presumido as indústrias torrefadoras (S/N) |
| GO_CREDITO_COMEXPRODUZIR | char(1) |  |  | GO - Crédito outorgado nas operações interestaduais de comércio exterior - COMEXPRODUZIR (S/N) |
| RJ_ESTORNAR_CREDITO_ICMS_PROP_ISENTA_NAO_TRIB | char(1) |  |  | RJ - Estornar crédito de ICMS proporcional a saída ou prestação de serviço isenta/não tributada |
| SC_CREDITO_PRESUMIDO_CERVEJA_CHOPE_ARTESANAL | char(1) |  |  | SC - Crédito presumido na saída de cerveja e chope artesanais - An2, Art. 15, XXXII |
| PISCOFINS_UTILIZAR_CREDITO_APOS_PRAZO_DECADENCIAL | char(1) |  |  | Utilizar crédito de PIS e COFINS após o término do prazo decadencial |
| PIS_COFINS_METODO_APROPRIACAO_CREDITO | integer(4) |  |  | PIS/COFINS - Créditos - Método Apropriação - Opções (1/2) |
| GO_CREDITO_PRESUMIDO_20_TRANSPORTADORA_ICMS | char(1) |  |  | GO - Crédito presumido de 20% para transportadoras - Convênio ICMS 106/96 |
| SIMPLESN_ANEXO_VI_PAR | char(1) |  |  | Simples Nacional - Anexo VI (S/N) |
| RS_CREDITO_PRESUMIDO_SORO_DE_LEITE_EM_PO | char(1) |  |  | RS - Crédito presumido nas saídas de soro de leite em pó, albuminas e composto lácteo (S/N) |
| PE_CREDITO_PRESUMIDO_PRODEAUTO | char(1) |  |  | PE - Crédito presumido PRODEAUTO (S/N) |
| FATO_GERADOR_CRF_ENTRADA | char(1) |  |  | Fato Gerador CRF - Entradas (E/P) |
| FATO_GERADOR_CRF_SAIDA | char(1) |  |  | Fato Gerador CRF - Saídas (E/P) |
| TO_CREDITO_PRESUMIDO_70_ICMS_APURADO | char(1) |  |  | TO - Crédito presumido de 70% sobre o ICMS apurado (S/N) |
| TO_CREDITO_PRESUMIDO_70_NRO_TARE | varchar(20) |  | S | TO - Crédito presumido de 70% sobre o ICMS apurado - Número do TARE |
| TO_CREDITO_PRESUMIDO_70_DATA_VENCIMENTO | date(4) |  | S | TO - Crédito presumido de 70% sobre o ICMS apurado - Data de Vencimento |
| PR_APROP_CRED_ICMS_INSUMOS_PREST_SERV_TRANSP | char(1) |  |  | PR - Apropriar crédito de ICMS |
| PR_APROP_CRED_ICMS_INSUMOS_PREST_SERV_TRANSP_TIPO | integer(4) |  |  | PR - Apropriar crédito de ICMS - Tipo (0/1) |
| SIMPLESN_POSSUI_DEDUCAO_EMISSORA_RADIO_TV | char(1) |  |  | Possui dedução para emissoras de rádio e televisão pela cessão do horário gratuito |
| MG_4961_CALCULAR_ISS_ISENTO | char(1) |  |  | MG - Patrocínio - Calcular ISS de acordo com faturamento em indice para empresas do Simples. Art. 27 LC 102/2001 |
| MG_4961_CALCULAR_ISS_ISENTO_INDICE | char(8) |  | S | MG - Patrocínio - Índice para Calcular ISS de acordo com faturamento em indice para empresas do Simples. Art. 27 LC 102/2001 |
| RS_COMPENSAR_SALDO_CREDOR_SUBTRI_NO_ICMS | char(1) |  |  | RS - Compensar saldo credor anterior do ICMS Substituição Tributária no ICMS próprio |
| POSSUI_DEDUCAO_IRPJ_RADIO_TV_HORARIO_GRATUITO | char(1) |  |  | Possui dedução do IRPJ para emissoras de rádio e televisão pela cessão do horário gratuito |
| POSSUI_RECEITA_DIFERIDA_IRPJ_CSLL_IN_247_2002 | char(1) |  |  | Possui receita diferida para as contribuições do IRPJ e CSLL - Art. 25 da IN 247/200 |
| RS_CREDITO_PRESUMIDO_SAIDA_QUEIJO | char(1) |  |  | RS - Crédito presumido nas saídas de queijo - Livro I, art. 32, XXVI |
| MS_CREDITO_PRESUMIDO_PRODUTOS_AGRICOLAS | char(1) |  |  | MS - Crédito presumido nas operações interestaduais com produtos agrícolas - Lei nº 2.783/2003 |
| GO_CREDITO_LOGPRODUZIR | char(1) |  |  | GO - Crédito outorgado nas prestações interestaduais de transporte - LOGPRODUZIR |
| PB_CREDITO_PRESUMIDO_CALCADOS | char(1) |  |  | PB - Regime Especial nas saídas de calçados, artigos de couro e similares - Dec. 25.390/04 |
| PB_CREDITO_PRESUMIDO_CALCADOS_ALIQUOTA | numeric(5) |  |  | PB - Regime Especial nas saídas de calçados, artigos de couro e similares - Dec. 25.390/04 - Alíquota |
| AP_CREDITO_PRESUMIDO_20_TRANSPORTADORA_ICMS | char(1) |  |  | AP - Crédito presumido de 20% para transportadoras - Convênio ICMS 106/96 |
| POSSUI_ATIVIDADE_PROPAGANDA_PUBLICIDADE | char(1) |  |  | Empresa com atividade de propaganda e publicidade |
| SC_CREDITO_PRESUMIDO_SAIDAS_VINHO | char(1) |  |  | SC - Crédito Presumido nas saídas de vinho - An2, Art. 21, X |
| SC_CREDITO_PRESUMIDO_SAIDAS_VINHO_TIPO | integer(4) |  |  | SC - Crédito Presumido nas saídas de vinho - An2, Art. 21, X por (1=Nota / 2=Produto) |
| RS_CREDITO_PRESUMIDO_VINHO | char(1) |  |  | RS - Crédito Presumido Vinho |
| REGIME_APURACAO_INSS_RB | integer(4) |  |  | INSS R.B. - Regime de Apuração (1=Competência / 2=Caixa) |
| CALCULAR_ICMS_RECUPERAVEL_INVENTARIO | char(1) |  |  | Calcular o valor do ICMS recuperável para o Livro Registro de Inventário |
| MT_DETALHAR_VALORES_ISENTOS_ICMS | char(1) |  |  | MT - Detalhar valores isentos de ICMS |
| PI_CREDITO_PRESUMIDO_20_TRANSPORTADORAS_ICMS | char(1) |  |  | PI - Crédito presumido de 20% para transportadores - Convênio ICMS 106/96 |
| INTEGRA_CF_E_PAR | char(1) |  |  | Integração do Cupom Fiscal Eletrônico (A/U/S/D) |
| EXCLUIR_IRRF_BASE_CALCULO_CIDE | char(1) |  |  | Excluir da base de cálculo do imposto CIDE o valor do IRRF |
| RS_CREDITO_PRESUMIDO_PROGRAMA_AGREGAR | char(1) |  |  | RS - Crédito presumido estab. abatedores do Programa AGREGAR-RS CARNES - Livro I, art. 32, XI |
| RS_CREDITO_PRESUMIDO_AQUISICAO_INTERNA_LEITE | char(1) |  |  | RS - Crédito presumido nas aquisições internas de leite produzido neste Estado - Livro I, art. 32, CVII |
| RS_CREDITO_PRESUMIDO_SAIDAS_MOVEIS | char(1) |  |  | RS - Crédito presumido nas saídas interestaduais de móveis - Livro I, art. 32, LXI |
| PIS_COFINS_CALCULAR_POR_RECOLHIMENTO | char(1) |  |  | Possui mais de um código de recolhimento para os impostos PIS e COFINS (S/N) |
| PISCOFINS_CREDITO_PRESUMIDO_BEBIDA_FRIA_13097 | char(1) |  |  | Crédito Presumido na aquisição de bebidas frias - Art. 31 da Lei 13.097/2015 |
| SOMAR_SUBTRI_BASE_PIS_COFINS | char(1) |  |  | Somar o valor do ICMS SUBTRI das entradas na base de cálculo do PIS e da COFINS (S/N) |
| PISCOFINS_CREDITO_PRESUMIDO_ALCOOL_12859 | char(1) |  |  | Crédito Presumido importador ou produtor de álcool - Lei 12.859/2013 |
| RJ_CREDITO_PRESUMIDO_SAIDAS_PLASTICOS | char(1) |  |  | RJ - Crédito Presumido nas saídas de produtos plásticos |
| RS_CREDITO_PRESUMIDO_AQUISICAO_INTERNA_LEITE_CVI | char(1) |  |  | RS - Crédito presumido nas aquisições internas de leite |
| RS_CREDITO_PRESUMIDO_AQUISICAO_INTERNA_LEITE_CVI_TIPO | char(2) |  | S | RS - Crédito presumido nas aquisições internas de leite - Tipo |
| SPED_FISCAL_GERAR_CONTROLE_PRODUCAO_ESTOQUE | char(1) |  |  | Gerar o controle da produção e do estoque - Bloco K |
| SPED_FISCAL_GERAR_CONTROLE_PRODUCAO_ESTOQUE_TIPO | char(1) |  |  | Gerar o controle da produção e do estoque - Bloco K - Tipo (C/S/N) |
| TO_CREDITO_PRESUMIDO_LEI_1201_2000 | char(1) |  |  | TO - Crédito presumido - Lei Nº 1.201/2000, Art. 1º, I |
| TO_CREDITO_PRESUMIDO_LEI_1201_2000_TIPO | integer(4) |  | S | TO - Crédito presumido - Lei Nº 1.201/2000, Art. 1º, I - Tipo |
| CONSIDERAR_JURO_MULTA_RECEITA_PIS_COFINS | char(1) |  |  | Considerar juros, multas e outras como receita financeira no cálculo do PIS e COFINS (S/N) |
| PR_CREDITO_PRESUMIDO_20_TRANSPORTADORAS_ICMS | char(1) |  |  | PR - Crédito presumido de 20% para transportadoras - Convênio ICMS 106/96 e 85/03 |
| SP_ESCRITURAR_REMESSA_PARA_VENDA_FORA_ESTAB | char(1) |  |  | Escriturar as notas de remessa e retorno de venda fora do estabelecimento conf. Art. 434 RICMS |
| CALCULAR_TTD_AGRUPADO_POR_ALIQUOTA_EFETIVA | char(1) |  |  | Realizar o cálculo do TTD 409, 410 ou 411 agrupando por tributação efetiva |
| CE_GERAR_VALOR_DIFALI_COMO_OUTROS_DEBITOS_ICMS | char(1) |  |  | Gerar o valor do imposto 8-DIFALI como outros débitos na apuração do imposto 1-ICMS |
| SC_CREDITO_PRESUMIDO_ST_DECRETO_3346_2010 | char(1) |  |  | SC - Crédito Presumido Substituição Tributária - Decreto 3.346/2010 (S/N) |
| SC_CREDITO_PRESUMIDO_ST_DECRETO_3346_2010_TIPO | integer(4) |  |  | SC - Crédito Presumido Substituição Tributária - Decreto 3.346/2010 - Tipo (1-Nota / 2-Produto) |
| CONSIDERAR_DESCONTO_RECEITA_PIS_COFINS | char(1) |  |  | Considerar descontos obtidos como receita financeira no cálculo do PIS e COFINS |
| AM_CREDITO_ESTIMULO_ICMS_ART_13_LEI_2826_03 | char(1) |  |  | AM - Possui incentivo fiscal do Crédito Estímulo do ICMS |
| BA_CREDITO_PRESUMIDO_20_TRANSPORTADORA_ICMS | char(1) |  |  | BA - Crédito Presumido de 20% para transportadora - Convênio ICMS 106/96 |
| PR_CALCULAR_RESSARCIMENTO_ICMS_ST | char(1) |  |  | PR - Calcular ressarcimento de ICMS ST nas vendas interestaduais |
| PR_CALCULAR_RESSARCIMENTO_ICMS_ST_TIPO | char(1) |  |  | PR - Calcular ressarcimento de ICMS ST nas vendas interestaduais - Tipo (M/ P) |
| CONTAB_IMP_FEDERAIS_RETIDOS_PELO_REGIME_COMP | char(1) |  |  | Contabilizar os impostos federais retidos na fonte pelo regime de competência |
| AL_CREDITO_PRESUMIDO_20_TRANSPORTADORAS_ICMS | char(1) |  |  | AL - Crédito presumido de 20% para transportadoras - Convênio ICMS 106/96 |
| RN_CREDITO_PRESUMIDO_20_TRANSPORTADORAS_ICMS | char(1) |  |  | Crédito presumido de 20 para transportadoras |
| CONSIDERAR_SALDO_CREDOR_COSIRF_PERIODOS_ANTERIORES_CSLL_IRPJ | char(1) |  |  | Considerar saldo credor de COSIRF de períodos anteriores no cálculo da CSLL e IRPJ |
| MS_POSSUI_BENEFICIO_PROGRAMA_FOMENTO_OPER_DENTRO_DO_ESTADO | numeric(13) |  |  | FAI Operações dentro do estado |
| MS_POSSUI_BENEFICIO_PROGRAMA_FOMENTO_OPER_INTERESTADUAIS | numeric(13) |  |  | Operações interestaduais |
| CONSIDERAR_JURO_MULTA_RECEITA_PIS_COFINS_CALCULAR | integer(4) |  |  | Considerar mais de um código de recolhimento para os impostos PIS e COFINS - Calcular |
| SIMPLESN_DEDUZIR_PEDAGIO_DA_RECEITA_BRUTA | char(1) |  |  | Deduzir da receita bruta o valor do pedágio nas operações de transporte |
| SEPARAR_CONTABILIZACAO_OUTROS_VALORES | char(1) |  |  | Gerar lançamento de partida simples |
| SEPARAR_CONTABILIZACAO_OUTROS_VALORES_PARTIDA_SIMPLES | char(1) |  |  | Separar contabilização dos valores de frete, pedágio, seguro, despesas acessórias e desconto |
| SIMPLESN_SEM_BENEFICIO_REDUCAO_BASE_CALCULO_ICMS | char(1) |  |  | PR - Empresa inscrita no CADIN, sem benefício da redução da Base de Cálc. do ICMS |
| RS_CREDITO_PRESUMIDO_VINHO_32_CLXVIII | char(1) |  |  | RS - Crédito presumido nas saídas internas de vinho - Livro I, Art. 32, CLXVIII |
| RS_CREDITO_PRESUMIDO_PAPEL_HIGIENICO | char(1) |  |  | RS - Crédito presumido nas aquisições internas de leite - Livro I, art. 32, CVI |
| DEDUZIR_VALOR_PEDAGIO_RECEITA_BRUTA_IMPOSTOS_FEDERAIS | char(1) |  |  | Deduzir o valor do pedágio da receita bruta dos impostos federais |
| MG_CREDITO_PRESUMIDO_RET | char(1) |  |  | MG - Possui crédito presumido concedido por meio de Regime Especial |
| RS_CREDITO_PRESUMIDO_MICROCERVEJARIAS_PERMITE_UTILIZAR_EXCEDENTE_LIMITE | char(1) |  |  | RS - Crédito presumido microcervejarias - Livro I, Art. 32, CXL |
| UTILIZAR_CREDITO_PER_SEM_REC_DESONERADA_INSS_RB | char(1) |  |  | Não utilizar o crédito da devolução quando no período de ocorrência não ter receita desonerada |
| POSSUI_BENEFICIO_FISCAL_ESTABALECIMENTO_COMERCIAL_ATACADISTA | char(1) |  |  | Possui benefício fiscal estabelecimento Comercial Atacadista - Arts. 530-LRK e 534-ZZA RICMS |
| MS_POSSUI_BENEFICIO_PROGRAMA_FOMENTO_TEM_PERCENTUAL_DIFERENCIADO_OPER_INTERESTADUAIS | char(1) |  |  | Percentual diferenciado do benefício para operações interestaduais |
| RO_CREDITO_PRESUMIDO_LEITE_ITEM15_TABELA1_ANEXOIV | char(1) |  |  | RO - Crédito presumido nas saídas interestaduais de indust. do leite - Item 15, Tabela 1, Anexo IV |
| RO_CREDITO_PRESUMIDO_LEITE_ITEM6_TABELA1_ANEXOIV | char(1) |  |  | RO - Crédito presumido nas saídas interestaduais de indust. do leite - Item 6, Tabela 1, Anexo IV |
| RN_GERAR_DES_IF | char(1) |  |  | RN - Gerar DES-IF |
| RN_GERAR_DES_IF_TIPO_INSTITUICAO | char(1) |  | S | RN - DES-IF - Tipo Instituição |
| PR_APROP_CRED_ICMS_INSUMOS_PREST_SERV_TRANSP_CONSOLIDADO | char(1) |  |  | PR - Considerar no cálculo as prestações realizadas por todos os estabelecimentos da empresa |
| MG_CREDITO_PRESUMIDO_ARTEFATOS_JOALHERIA | char(1) |  |  | MG - Crédito presumido artefatos de joalheria com carga tributária de 5% - Art. 75, XXVIII do RICMS |
| CE_CALCULAR_IMPOSTO_ICMS_STAT_COM_CADA_EFETIVA | char(1) |  |  | CE - Calcular o imposto ICMS Antecipação Total-ST com carga efetiva |
| CE_CALCULAR_IMPOSTO_ICMS_STAT_COM_CADA_EFETIVA_TIPO | char(1) |  |  | CE - Calcular o imposto ICMS Antecipação Total-ST com carga efetiva - Tipo |
| RS_CREDITO_PRESUMIDO_PROD_INFO_AUT_ART_32_CLXVII | char(1) |  |  | RS - Crédito presumido nas saídas de produtos de informática e automação - Livro I, art. 32, CLXVII |
| RS_EMP_FABRIC_DISTRIB_PAPEIS_MOEDA_NCM_84729010 | char(1) |  |  | RS - Empresa fabric. de distribuidores automáticos de papéis-moeda classif. no cód. NCM 8472.90.10 |
| SN_EMITIR_AVISO_TROCA_FAIXA | char(1) |  |  | Emitir aviso quando houver troca de faixa de receita bruta |
| SC_CRED_PRES_CONFEC_ART_15_APURAR_ESTAB_CENT | char(1) |  |  | SC - Apurar o crédito presumido confecção Art XXXIX |
| SC_CRED_PRES_CONFEC_ART_15_APURAR_ESTAB_CENT_EMP | integer(4) |  | S | SC - Apurar o crédito presumido confecção Art XXXIX - Empresa |
| DEDUZIR_ICMS_DESONERADO_DA_BASE_CALCULO_PIS_COFINS | char(1) |  |  | Deduzir o valor do ICMS desonerado da base de cálculo dos impostos PIS e COFINS |
| RJ_EFETUAR_COMPARACAO_ENTRE_APURACAO_COM_E_SEM_BENEFICIO_CALCULO_154_FEEF | char(1) |  |  | RJ - Efetuar a comparação entre a apuração com benefício e sem benefício para o cálculo do imposto 154-FEEF |
| GERAR_CONTABILIZACAO_PIS_COFINS_SEPARADAMENTE_POR_FILIAL | char(1) |  |  | Gerar contabilização de PIS/COFINS separadamente por filial |
| DEDUZIR_VALOR_PEDAGIO_RECEITA_BRUTA_IMPOSTOS_FEDERAIS_OPERACAO | char(1) |  |  | Deduzir o valor do pedágio da receita bruta dos impostos federais |
| SP_CALCULAR_RESSARCIMENTO_ICMS_PORTARIA_158_2015 | char(1) |  |  | SP - Calcular o ressarcimento de ICMS conforme Portaria CAT 158/2015 |
| CONSIDERAR_REC_DOC_NAO_FISCAL_P_RATEIO_PROP_CRED | char(1) |  |  | Considerar Receitas de Documento Não Fiscal para rateio proporcional de créditos |
| CONSIDERAR_TOTAL_RETENCOES_BAIXAS_PARCIAIS | char(1) |  |  | Considerar no cálculo do IRPJ e CSLL o total das retenções da baixa de parcelas parciais |
| SC_CALCULAR_RESSARCIMENTO_VENDAS_INTERESTADUAIS_SUBTRI | char(1) |  |  | Calcular ressarcimento nas vendas interestaduais com Substituição Tributária |
| DEDUZIR_VALOR_ICMS_CUSTO_AQUISICAO_VEICULOS_USADOS | char(1) |  |  | Deduzir o valor de ICMS do  custo da aquisição de veículos usados |
| SC_CREDITO_PRESUMIDO_SAIDAS_FEIJAO_ART_21_VIII | char(1) |  |  | SC - Crédito Presumido nas saídas de feijão - An2, Art. 21 |
| SP_CALCULAR_RESSARCIMENTO_ICMS_PORTARIA_158_2015_TIPO | char(1) |  |  | Calcular o ressarcimento de ICMS conforme Portaria CAT 158/2015 - Tipo |
| SC_CREDITO_PRESUMIDO_VENDAS_INTEREST_CONS_FINAL_ART_21_XV | char(1) |  |  | Crédito Presumido nas vendas interest. a consumidor final não contrib. do ICMS - An2, Art.21,XV |
| ES_POSSUI_BENEFICIO_BARES_RESTAURANTES | char(1) |  |  | Possui benefício fiscal Bares, Rest. Refeições coletivas e similares - Art. 530-LRF RICMS |
| ES_POSSUI_BENEFICIO_BARES_RESTAURANTES_TIPO | char(1) |  |  | Possui benefício fiscal Bares, Rest. Refeições coletivas e similares - Art. 530-LRF RICMS - Tipo |
| MASCARA_CONTABIL | char(35) |  | S | Máscara contábil |
| UTILIZA_CREDITO_PISCOFINS_RESCISAO_CONTRATO_IMOB | char(1) |  |  | Utilizar o crédito de PIS e COFINS da rescisão do contrato imobiliário em outras atividades |
| GO_CONTRIBUINTE_INDUSTRIAL_ATACADISTA | char(1) |  |  | GO - Contribuinte Industrial e Atacadista - Estornar crédito conforme IN 1.237/15-GSF |
| MG_CREDITO_PRESUMIDO_CARNES_SOBRE | char(1) |  |  | Crédito presumido de peixes, abate ou proces. de aves e de gado - Art. 75, IV do RICMS |
| DEDUZIR_DEVOLUCAO_CONFORME_PERCENTUAL_BASE_CALCULO | char(1) |  |  | Deduzir a devolução conforme percentual da Base de Cálculo |
| GO_DEDUZIR_CREDITO_OUTORGADO_ICMS_ANTECIPADO | char(1) |  |  | Deduzir o crédito outorgado na apuração do ICMS antecipado conf. Art. 3, II da IN 598/2003 |
| RS_CALCULAR_RESTITUICAO_ICMS_ST_PAGO_ETAPAS_ANTERIORES | char(1) |  |  | Calcular a restituição do ICMS Substituição Tributária pago nas etapas anteriores |
| REDUCAO_Z_GERAR_LANCTOS_CONTABEIS_MEIO_PAGAMENTO_PAR | char(1) |  |  | Gerar os lançamentos contábeis conforme Meio de Pagamento |
| DEDUZIR_ICMS_DA_BASE_CALCULO_PIS_COFINS | char(1) |  |  | Deduzir o valor do ICMS da base de cálculo do PIS e COFINS |
| BA_CREDITO_PRESUMIDO_LEITE_DE_COCO_ART_270 | char(1) |  |  | BA - Crédito presumido aos fabricantes de leite de coco - Art. 270, VI do RICMS |
| CALCULAR_INSS_RB_CONFORME_EFD_REINF | char(1) |  |  | Efetuar o cálculo do INSS Receita Bruta conforme a EFD-Reinf |
| SC_APURA_CREDITO_PRESUMIDO_CONFECCAO_ART_21_CONSOLIDADA | char(1) |  |  | SC - Apuração consolidada conforme Art. 55, § 5º |
| PIS_COFINS_CONSIDERAR_DEV_COMPRA_DEBITO_MESMO_PER | char(1) |  |  | Considerar devoluções de compra como débito no mesmo período |
| SC_CREDITO_PRESUMIDO_CONFECCAO_ART_15_BASE_CALCULO | integer(4) |  |  | SC - Crédito Presumido Confecção Art. 15, XXXIX - Base de cálculo para o crédito presumido |
| SP_CREDITO_OUTORGADO_EMPRESAS_TEXTEIS | char(1) |  |  | SP - Crédito Outorgado de 12% para empresas têxteis - Cap. IV, Anexo III, Art. 41 do RICMS |
| RS_CREDITO_PRESUMIDO_SUCO_UVA_ART_32_XCIV | char(1) |  |  | RS - Crédito presumido nas saídas internas de sucos de uva - Livro I, Art. 32, XCIV |
| DCTF_WEB_EFETUAR_CALCULO_PREVIDENCIARIO | char(1) |  |  | Efetuar cálculo previdenciário conforme DCTFWeb |
| SC_CREDITO_PRESUMIDO_CONFECCAO_ART_21_TIPO | char(1) |  |  | SC - Crédito Presumido Confeccção - Anexo 2, Art. 21, IX - Forma de cálculo |
| DF_DECRETO_CALCULAR_BC_ENTRADAS_PAR | char(1) |  |  | DF - Calcular BC das entradas conforme Ato Declaratório 97/20141 |
| AM_CREDITO_PRESUMIDO_20_TRANSPORTADORAS_ICMS | char(1) |  |  | AM - Crédito presumido de 20% para transportadoras - Convênio ICMS 106/96 |
| ES_POSSUI_MOVIMENTACAO_CAFE_CRU | char(1) |  |  | ES - Possui movimentação de Café Cru |
| MA_CREDITO_PRESUMIDO_INDUSTRIA_LATICINIO | char(1) |  |  | MA - Crédito Presumido Indústria de Laticínio - Anexo 1.5, Art. 5 do RICMS |
| SC_CONTRIBUI_FUNDOSOCIAL_CALCULAR_CARTA_CIRCULAR | char(1) |  |  | SC - Calcular o Fundo Social conforme Carta Circular Nº 11/2018 a partir de 06/2018 |
| AC_CALCULAR_RESSARCIMENTO_DECRETO_6875_2017 | char(1) |  |  | AC - Calcular o ressarcimento conforme seção IV do decreto 6.875/2017 |
| AC_CALCULAR_RESSARCIMENTO_DECRETO_6875_2017_TIPO | char(1) |  |  | AC - Calcular o ressarcimento conforme seção IV do decreto 6.875/2017 - Tipo |
| PR_CALCULAR_RESSARCIMENTO_ICMS_VENDAS_INTERESTADUAIS_TIPO | char(1) |  |  | S-ICMS ST / P-ICMS Próprio / A-ICMS Próprio e ICMS ST(Ambos) |
| MG_POSSUI_INCENTIVO_PONTUALIDADE_ICMS | char(1) |  |  | Possui Incentivo à Pontualidade do ICMS conforme Art. 91-A do RICMS |
| MG_POSSUI_INCENTIVO_PONTUALIDADE_ICMS_PERCENTUAL | numeric(5) |  |  | Possui Incentivo à Pontualidade do ICMS conforme Art. 91-A do RICMS - Percentual |
| SIMPLESN_CONSIDERAR_TODAS_CASAS_DECIMAIS_CALCULO_REDUCAO_ICMS | char(1) |  |  | Considerar todas as cadas decimais no calculo da redução de base de cálculo do ICMS no SN |
| EMPRESA_SALAO_PARCEIRO | char(1) |  |  | Empresa atua como salão-parceiro |
| EMPRESA_SALAO_PARCEIRO_DEDUCAO_TIPO | char(1) |  |  | Lançar dedução do valor repassado ao profissional-parceiro |
| DEDUZIR_ISS_DA_BASE_CALCULO_PIS_COFINS | char(1) |  |  | Deduzir o valor do ISS da base de cálculo do PIS e COFINS |
| RJ_POLITICA_RECUPERACAO_INDUSTRIAL_REGIONALIZADA_TIPO | integer(4) |  |  | RJ - Base de cálculo para o regime especial (1-Valor contábil / 2-Deduzir ICMS-ST / 3-Deduzir ICMS-ST e IPI) |
| MA_CALCULAR_DIFALI_SN | char(1) |  |  | MA - Calcular diferencial de alíquota para Simples Nacional |
| SP_CALCULAR_RESSARCIMENTO_ICMS_PORTARIA_42_2018 | char(1) |  |  | Calcular o ressarcimento ou complemento de ICMS conforme Portaria CAT 42/2018 |
| SC_CONTRIBUI_FUNDOSOCIAL_CALCULAR_CARTA_CIRCULAR_TIPO | integer(4) |  |  | SC - Calcular o Fundo Social conforme Carta Circular - Tipo |
| ES_CREDITO_PRESUMIDO_VENDA_INTERESTADUAL_NAO_PRESENCIAL_CONSUMIDOR_FINAL_ART_530 | char(1) |  |  | Crédito presumido na venda interestadual não presencial a consumidor final - Art. 530-LRI RICMS |
| RS_CALCULAR_RESSARC_COMP_ICMS_ST | char(1) |  |  | RS - Calcular o ressarcimento/complemento do ICMS ST conf. Art. 25-A a 25-C, Livro III do RICMS |
| RS_CALCULAR_RESSARC_COMP_ICMS_ST_EMP_RAMO | char(1) |  |  | RS - Calcular o ressarcimento/complemento do ICMS ST conf. Art. 25-A a 25-C, Livro III do RICMS - Ramo de atividade da empresa |
| EMPRESA_FACTORING | char(1) |  |  | Empresa de factoring (fomento mercantil) |
| ES_UTILIZAR_SALDO_CREDOR_ICMS_PARA_ABATER_DEBITO_NORM_003_2013 | char(1) |  |  | Utilizar o saldo credor do ICMS para abater do débito do DIFALI - Parecer Norm. Nº 003/2013 |
| MT_DEDUZIR_ICMS_ST_PRODUTOS_ICMS_ES | char(1) |  |  | Deduzir o valor do ICMS ST proporcional aos produtos no cálculo do ICMS ES - Carga Média |
| MT_CALCULAR_FEEF_SOBRE_CREDITO_PRESUMIDO_PRODEIC | char(1) |  |  | Calcular o Fundo Estadual de Equilíbrio Fiscal - FEEF sobre o crédito presumido PRODEIC |
| SEPARAR_CONTABILIZACAO_IPI_E_ICMS_ST | char(1) |  |  | Separar contabilização IPI e ICMS ST |
| SEPARAR_CONTABILIZACAO_IPI_E_ICMS_ST_PARTIDA_SIMPLES | char(1) |  |  | Separar contabilização IPI e ICMS ST partida simples |
| FATO_GERADOR_INSS_RET | char(1) |  |  | Fato gerador das retenções - INSS-RET |
| SC_CALCULAR_REST_COMP_RESSARC_ICMS_ST | char(1) |  |  | Calcular a restituição, o complemento e o ressarcimento do ICMS ST (DRCST) |
| SC_CRED_PRES_VENDAS_INT_CONS_FINAL_ART_21_XV_APURAR_ESTAB_CENT | char(1) |  |  | Crédito presumido nas vendas interest. a consumidor final NC do ICMS - An2, Art 21, XV |
| SC_CRED_PRES_VENDAS_INT_CONS_FINAL_ART_21_XV_APURAR_ESTAB_CENT_EMP | integer(4) |  | S | Crédito presumido nas vendas interest. a consumidor final NC do ICMS - An2, Art 21, XV - Empresa |
| RO_CREDITO_PRESUMIDO_MERCADORIA_IMP_EXT_LEI_1473_2005 | char(1) |  |  | Crédito presumido nas saídas interest. de mercadoria importada do exterior - Lei nº. 1.473/2005 |
| SIMPLESN_APLICAR_REDUCAO_BASE_CALCULO_ICMS_SN_QUALQUER_UF_ORIGEM | char(1) |  |  | Aplicar a redução de base de cálculo do ICMS do Simples Nacional para qualquer UF origem |
| FATO_GERADOR_INSS_RET_ENTRADA | char(1) |  |  | INSS-Ret sobre Entradas |
| FATO_GERADOR_INSS_RET_SAIDA | char(1) |  |  | INSS-Ret sobre Saídas/Serviços |
| SC_APLICAR_ALIQUOTA_EFETIVA_SOBRE_BC_QUANDO_REDUCAO | char(1) |  |  | SC - Aplicar a alíquota efetiva sobre a base de cálculo integral do ICMS quando possuir redução |
| CONSIDERAR_SALDO_RETENCOES_PERIODO_ANT_CALCULO_PIS_COFINS | char(1) |  |  | Não considerar saldo de retenções de períodos anteriores no cálculo de PIS e COFINS |
| APLICAR_PERC_PRESUNCAO_CSLL_IRPJ_CALC_RECEITA_FINANCEIRA | char(1) |  |  | Aplicar o percentual de presunção dos impostos CSLL e IRPJ no cálculo da receita financeira |
| RS_EMPRESA_SUBMETIDA_REF | char(1) |  |  | RS - Empresa submetida ao Regime Especial de Fiscalização - REF, conforme Art. 2º da Lei nº 13.711/2011 |
| MA_CREDITO_PRESUMIDO_20_TRANSPORTADORAS_ICMS | char(1) |  |  | MA - Crédito presumido de 20% para transportadoras - Convênio ICMS 106/96 |
| SC_CREDITO_PRESUMIDO_MATERIAL_RECICLADO_TIPO | char(1) |  |  | Crédito Presumido Material Reciclável - An2, Art. 21, XII - Tipo |
| RJ_CREDITO_PRESUMIDO_RIOLOG_LEI_4173_2003 | char(1) |  |  | RJ - Crédito Presumido do Programa RIOLOG - Lei 4.173/2003 |
| MG_CALCULAR_COMPLEMENTO_RESTITUICAO_ICMS_ST_CONFORME_ART31 | char(1) |  |  | MG - Calcular o complemento/restituição do ICMS ST conforme Art. 31-A a 31-I, Anexo XV do RICMS |
| MT_CALCULAR_IMPOSTO_FECEP_MT_ICMS_ES_POR_PRODUTOS | char(1) |  |  | Calcular imposto FECEP MT |
| CALCULAR_ISS_PROF_HAB_SERVICO | char(1) |  |  | Calcular ISS por Profissional habilitado somente nos períodos em que houver prestação de serviço |
| MA_CREDITO_PRESUMIDO_SAIDA_INTERNA_GADO_SUINO | char(1) |  |  | MA - Crédito presumido na saída interna de gado suíno - Anexo 1.5, Art. 4 do RICMS |
| PR_CREDITO_PRESUMIDO_ENTRADA_LEITE_CRU | char(1) |  |  | PR - Crédito Presumido na entrada de leite cru - Anexo VII, Item 30 do RICMS |
| SC_CREDITO_PRESUMIDO_SAIDAS_INTERNAS_BISCOITOS_BOLACHAS | char(1) |  |  | SC - Crédito presumido nas saídas internas de biscoitos e bolachas - An2, Art. 15, IV |
| SP_APROVEITAR_CREDITO_ART_271_COMPRA_SN_CAT_42_2018 | char(1) |  |  | SP - Aproveitar como crédito do Art. 271 o permitido de crédito nas compras do Simples Nacional |
| FATO_GERADOR_OPERACOES_BILHETE_PASSAGEM_ELETRONICO | char(1) |  |  | Fato gerador dos impostos nas operações de saídas/serviços |
| SP_REGIME_ESP_TRIBUTA_ICMS_FORNECI_ALIMENTACAO | char(1) |  |  | SP - Regime especial de tributação do ICMS no fornecimento de alimentação - Dec. 51.597/07 |
| BA_CALCULAR_ESTORNO_CREDITO_ICMS_ART_312 | char(1) |  | S | Calcular o estorno dos créditos de ICMS conforme Art. 312, I do RICMS/BA |
| RJ_APLICAR_RED_BC_ICMS_RECEITA_ACU_ZERADA_SN | char(1) |  |  | RJ - Aplicar redução da B.C do ICMS quando possuir receita acumulada zerada no Simples Nacional |
| RS_EMPRESA_OPTANTE_ROT_ST | char(1) |  |  | RS - Empresa não optante pelo Regime de Substituição Tributária (ROT ST) |
| APLICAR_REDUCAO_ICMS_SN_5147_2007_SERVICOS_INICIADOS_RJ | char(1) |  |  | Aplicar a redução de ICMS no Simples Nacional conf. Lei 5.147/2007 para serviços iniciados no RJ |
| SC_CALCULAR_REST_COMP_RESSARC_ICMS_ST_TIPO_SALDO_ESTOQUE | char(1) |  |  | SC - Tipo de saldo de estoque considerado para o DRCST (M - Saldo do movimento / P - Saldo do produto) |
| SIMPLESN_RECOLHIMENTO_ISS | char(1) |  |  | Simples Nacional ISS - Recolhimento |
| PR_CALC_RECUP_RESSARC_COMPTO_ICMS_ST | char(1) |  |  | PR - Calcular a recuperação, ressarcimento e complementação do ICMS-ST (ADRC-ST) |
| MA_CREDITO_PRESUMIDO_ESTAB_ATACADISTA | char(1) |  |  | MA - Crédito Presumido Estabelecimento Atacadista - Anexo 1.5, Art. 8 do RICMS |
| MT_CREDITO_OUTORGADO_ESTAB_COMER_VAREJISTA | char(1) |  |  | MT - Crédito outorgado estabelecimento comercial varejista - Art. 2º, I, Anexo XVII do RICMS |
| RO_CALCULAR_RESSARCIMENTO_ART_20_ANEXO_VI | char(1) |  |  | RO - Calcular o ressarcimento conforme o Art. 20 do Anexo VI do RICMS |
| RO_CALCULAR_RESSARCIMENTO_ART_20_ANEXO_VI_TIPO | char(1) |  |  | RO - Calcular o ressarcimento conforme o Art. 20 do Anexo VI do RICMS - Tipo |
| SC_CREDITO_PRESUMIDO_TRANSPORTADORA_PAR_APURAR_ESTAB_CENT | char(1) |  |  | Apurar o crédito presumido no estabelecimento centralizador |
| SC_CREDITO_PRESUMIDO_TRANSPORTADORA_PAR_APURAR_ESTAB_CENT_EMP | integer(4) |  | S | Apurar o crédito presumido no estabelecimento centralizador - Empresa |
| RN_REGIME_ESPECIAL_TRIB_ICMS_CONTRIB_ATACADISTAS | char(1) |  |  | Regime especial de tributação do ICMS aos contribuintes atacadistas - Decreto 22.199/11 |
| SEPARAR_CONTAB_VALORES_FUNRURAL_NAS_SAIDAS_CLIENTES_CNPJ | char(1) |  |  | Separar contabilização dos valores de FUNRURAL nas saídas para cliente com inscrição CNPJ |
| DEDUZIR_ICMS_DA_BASE_CALCULO_PIS_COFINS_TIPO | char(1) |  |  | Deduzir o valor do ICMS da base de cálculo do PIS e COFINS |
| CTB_MOSTRAR_RATEIO_CENTRO_DE_CUSTOS | char(1) |  |  | Mostrar rateio de centro de custos na integração contábil |
| GERAR_CONTABILIZACAO_CFE_VALOR_VENDA_TOTAL | char(1) |  |  | Gerar contabilização do Cupom Fiscal Eletrônico pelo valor da venda total |
| PISCOFINS_CREDITO_PRESUMIDO_RECEITA_12865 | char(1) |  |  | Crédito Presumido sobre as receitas - Art. 31 da Lei 12.865/2013 |
| PISCOFINS_CREDITO_PRESUMIDO_RECEITA_12865_DEDUZIR | char(1) |  |  | Deduzir do crédito presumido as aquisições dos produtos utilizados como insumo na produção |
| RS_CALCULAR_RESSARC_COMP_ULT_ENT_PROPOR_SAI | char(1) |  |  | RS - Calcular o ressarcimento/complemento considerando as últimas entradas proporcional as saídas /* NÃO UTILIZADO */ |
| GERAR_DCTF_VALOR_SUSPENSO_PIS_COFINS_ICMS_RECOLHER | char(1) |  |  | Gerar na DCTF o valor suspenso de PIS/COFINS referente ao ICMS a recolher |
| PR_CALC_RECUP_RESSARC_COMPTO_ICMS_ST_TIPO_REAVER_IMP | char(1) |  |  | PR - Forma de reaver o imposto (1-Recuperação em conta gráfica / 2-Ressarcimento para fornecedor) |
| RJ_ESTORNAR_CREDITO_ICMS_PROP_POSSUIR_RED_BC | char(1) |  |  | RJ - Estornar crédito de ICMS proporcional a saída que possuir redução da base de cálculo |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| SC_CALCULAR_REST_COMP_RESSARC_ICMS_ST_APURAR_ESTAB_CENT | char(1) |  |  | Apurar no estabelecimento centralizador |
| SC_CALCULAR_REST_COMP_RESSARC_ICMS_ST_APURAR_ESTAB_CENT_EMP | integer(4) |  | S | Apurar no estabelecimento centralizador - Empresa |
| DEDUZIR_ICMS_BASE_IRPJ_CSLL | char(1) |  |  | Deduzir o valor do ICMS da base do IRPJ e CSLL |
| SC_CREDITO_PRESUMIDO_ABATEDORES_CALCULAR_ENT_PROD_ABAT_TERC | char(1) |  |  | SC - Calcular crédito presumido na entrada de produtos abatido por terceiros |
| MT_CREDITO_OUTORGADO_ESTAB_COMER_ATACADISTA | char(1) |  |  | MT - Crédito outorgado estabelecimento comercial atacadista - Art. 2°, II, Anexo XVII do RICMS |
| SC_CREDITO_PRESUMIDO_MATERIAIS_USO_MEDICINAL | char(1) |  |  | SC - Crédito Presumido materiais para uso medicinal, cirúrgico, dentário ou veterinário - An2, Art. 245 |
| BA_CALCULAR_STAT_MVA_FORNECEDOR_SIMPLES | char(1) |  |  | BA - Calcular o imposto 31-ST/AT pela MVA original quando o fornecedor for do Simples Nacional |
| SC_CONSIDERAR_NOTAS_DE_REMESSAS_PARA_CALCULO | char(1) |  |  | SC - Não considerar as notas de remessas para o cálculo |
| RS_EMPRESA_DIFERIMENTO_DECRETO_55_797_2021 | char(1) |  |  | Empresa com Diferimento conforme Decreto 55.797/2021 |
| RS_CALCULAR_STAT_MVA_FORNECEDOR_SIMPLES | char(1) |  |  | RS - Calcular o imposto 31-ST/AT pela MVA original quando o fornecedor for do Simples Nacional |
| MT_SEPARAR_CONTAB_VALORES_FETHAB_NAS_SAIDAS_CLIENTES_CNPJ | char(1) |  |  | MT - Separar contabilização dos valores de FETHAB nas saídas para cliente com inscrição CNPJ |
| SC_CALCULAR_FUNDO_SOCIAL_ALIQUOTA_CONFORME_CREDITO_PRESUMIDO | char(1) |  |  | Calcular fundo social com alíquota conforme crédito presumido |
| SC_ESTORNAR_CREDITOS_ICMS_PROPORCIONAL_CREDITO_PRESUMIDO | char(1) |  |  | SC - Estornar créditos de ICMS proporcional as operações de crédito presumido |
| SC_POSSUI_NOTA_COMPLEMENTAR_REFERENCIADO_PERIODO_ANTERIOR | char(1) |  |  | SC - Empresa possui notas complementares referenciado notas de períodos anteriores |
| MS_UTILIZAR_SALDO_CREDOR_ANTERIOR_ICMS_CALCULO_BENEFICIO | char(1) |  |  | Utilizar o saldo credor anterior do ICMS no cálculo do benefício |
| MG_CALCULAR_RESTITUICAO_ICMS_ST | char(1) |  |  | MG - Calcular a restituição do ICMS ST - Art. 23, Anexo XV do RICMS |
| MG_CALCULAR_RESTITUICAO_ICMS_ST_TIPO | integer(4) |  |  | MG - Calcular a restituição do ICMS ST - Art. 23, Anexo XV do RICMS - Tipo |
| SETOR_TEXTIL_PAR_TIPO | integer(4) |  |  | Regime especial de tributação do ICMS - Estabelecimentos Indústriais dos setores têxtil - Tipo (1/2) |
| DEDUZIR_ICMS_AQUISICOES_SIMPLES_DA_BASE_CALCULO_PIS_COFINS | char(1) |  |  | Deduzir o valor do ICMS nas aquisições do Simples Nacional da base de cálculo do PIS e COFINS |
| RS_CALCULAR_RESSARC_COMP | char(1) |  |  | RS - Calcular o ressarcimento/complemento considerando |
| RS_CALCULAR_RESSARC_COMP_TIPO | integer(4) |  |  | RS - Calcular o ressarcimento/complemento considerando - Tipo |
| RJ_CREDITO_PRESUMIDO_BARES_RESTAURANTES_SIMILARES | char(1) |  |  | RJ - Crédito Presumido Bares, restaurantes e similares |
| DF_DECRETO_CALCULAR_BC_ENTRADAS_PAR_TIPO | char(1) |  |  | DF - Calcular BC das entradas conforme Ato Declaratório 97/20141 Tipo |
| MG_CONSIDERAR_DATA_EMISSAO_FATO_GERADOR_ICMS_ANTECIPADO | char(1) |  |  | MG - Considerar a data de emissão da nota como fator gerador do imposto ICMS Antecipado |
| RO_POSSUI_INCENTIVO_CONSIT_ESTABELECIMENTO | integer(4) |  |  | RO - Incentivo tributário CONSIT - Decreto n 12.988/2007 - Estabelecimento |
| MS_EFETUAR_RATEIO_CREDITOS_PROPORCIONAIS | char(1) |  |  | MS - Efetuar o rateio dos créditos proporcionais as saídas internas e interestaduais |
| ES_BENEFICIO_FISCAL_VENDAS_INTERESTADUAIS_IND_METALMECANICA | char(1) |  |  | ES - Possui benefício fiscal nas vendas interestaduais de indústria metalmecânica - Art. 530-LF RICMS |
| DEDUZIR_DIFALNC_FCP_DA_BASE_CALCULO_PIS_COFINS | char(1) |  |  | Deduzir o valor do DIFAL-NC e FCP da base de cálculo do PIS e COFINS |
| DEDUZIR_DIFALNC_FCP_DA_BASE_CALCULO_PIS_COFINS_TIPO | char(1) |  |  | Deduzir o valor do DIFAL-NC e FCP da base de cálculo do PIS e COFINS - Tipo |
| SC_CREDITO_PRESUMIDO_BARES_RESTAURANTES_SIMILARES_TIPO | integer(4) |  |  | SC - Crédito Presumido Bares, Restaurantes e Similares - An2, Art. 21, IV Tipo (1/2) |
| MS_CREDITO_PRESUMIDO_PRODUTOR_RURAL_HORTIFRUTI | char(1) |  |  | Credito presumido nas operacoes interestaduais com produtos agricolas - Lei n 2.783/2003 |
| RJ_CREDITO_PRESUMIDO_RIOLOG_LEI_9025_2020 | char(1) |  |  | RJ - Crédito Presumido do Programa RIOLOG - Lei 9.025/2020 |
| RJ_CREDITO_PRESUMIDO_RIOLOG_LEI_9025_2020_TIPO | integer(4) |  |  | RJ - Crédito Presumido do Programa RIOLOG - Lei 9.025/2020 - Tipo |
| RJ_CREDITO_PRESUMIDO_RIOLOG_LEI_9025_2020_CALCULO_ICMS_MINIMO_COM_BASE_VALOR | numeric(13) |  |  | RJ - Crédito Presumido do Programa RIOLOG - Lei 9.025/2020 - Cálculo ICMS mínimo com base no valor |
| APLICAR_ANTES_EXCLUSAO_PERCENTUAL_REDUC_BC_PIS_COFINS | char(1) |  |  | Aplicar antes das exclusões o percentual de redução na base de cálculo do PIS e COFINS |
| EMPRESA_SIMPLES_CREDITO_ESC | char(1) |  |  | Empresa Simples de Crédito - ESC |
| TO_CREDITO_PRESUMIDO_20_TRANSPORTADORA_CONVENIO_ICMS_106_96 | char(1) |  |  | TO - Crédito presumido de 20% para transportadoras - Convênio ICMS 106/96 |
| MT_REGIME_SIMPLIFICADO_RESTAURANTES_BARES_SIMILARES | char(1) |  |  | MT - Regime simplificado de trib. restaurantes, bares e estab. similares - Anexo XVIII do RICMS |
| MT_CREDITO_OUTORGADO_PRODEIC_INVESTE_288_2019 | char(1) |  |  | MT - Crédito outorgado do PRODEIC Investe - Decreto 288/2019 |
| MT_CREDITO_OUTORGADO_PRODEIC_INVESTE_288_2019_SUBMODULO | integer(4) |  | S | MT - Crédito outorgado do PRODEIC Investe - Decreto 288/2019 - Submódulos |
| SC_CALCULAR_REST_CONSIDERAR_NOTAS_REMETENTE_INDIRETO_SEM_TAG_XML | char(1) |  |  | SC - Considerar no cálculo notas de remetente indireto e que não possuir a TAG preenchida no XML |
| GO_EMPRESA_BENEFICIARIA_PROGOIAS | char(1) |  |  | GO - Empresa Beneficiária do Programa PROGOIÁS |
| RS_CREDITO_PRESUMIDO_MODALIDADE_COMERCIO_ELETRONICO_E_COMMERCE | char(1) |  |  | RS - Crédito presumido na modalidade de comércio eletrônico "e-commerce"- Livro I, Art. 32, CXCII |
| RO_CREDITO_PRESUMIDO_SAIDAS_INTERNAS_OVO_PROMOVIDO_POR_PRODUTOR | char(1) |  |  | RO - Crédito presumido nas saídas internas de ovo promovido por produtor - Item 10, Parte 2, Anexo IV |
| CONSIDERAR_LUCRO_OPERACAO_CALCULO_RATEIO_REVENDAS_VEICULOS | char(1) |  |  | Considerar o lucro da operação no cálculo do rateio nas revendas de veículos |
| SPED_FISCAL_TIPO_LAYOUT | integer(4) |  |  | Tipo de Layout para Sped Fiscal |
| SOMAR_VALOR_IPI_BASE_CALCULO_CREDITO_PIS_COFINS | char(1) |  |  | Não somar o valor de IPI na base de cálculo do crédito de PIS/COFINS - Art. 170, IN 2.121/22 |
| PI_REGIME_ESPECIAL_TRIBUTACAO_OPERACOES_PRODUTOS_FARMACEUTICOS_ART_791F | char(1) |  |  | PI - Regime especial de tributação nas operações com produtos farmacêuticos - Art. 791-F do RICMS |
| CALCULAR_CSLL_CONFORME_LEI_14_466_2022 | char(1) |  |  | Calcular a CSLL mensalmente conforme a vigência da alíquota - Lei 14.446/2022 |
| RJ_POLITICA_RECUPERACAO_INDUSTRIAL_REGIONALIZADA_PERCENTUAL | integer(4) |  |  | RJ - Regime especial de tributação de ICMS - Política de Recuperação Industrial Regionalizada - Percentual |
| RS_CREDITO_PRESUMIDO_PRODUTOS_TEXTEIS_VESTUARIO_CXXXV | char(1) |  |  | RS - Crédito presumido produtos texteis e vestuario |
| RS_CREDITO_PRESUMIDO_PRODUTOS_TEXTEIS_VESTUARIO_CXXXV_TIPO | char(1) |  |  | RS - Crédito presumido produtos texteis e vestuario - Tipo |
| APURACAO_CENTRALIZADA | integer(4) |  |  | Apuração Centralizada |
| SOMAR_ICMS_ENTRADAS_BASE_PIS_COFINS | char(1) |  |  | Somar o valor do ICMS das entradas na base de cálculo de PIS e COFINS |
| CONSIDERAR_IPI_ICMS_ST_NA_BASE_CALC_PIS_COFINS_REC_BONIFICACAO | char(1) |  |  | Considerar o valor do IPI e ICMS ST na base de cálculo do PIS/COFINS nas receitas de bonificação |
| MA_CREDITO_PRESUMIDO_PRODUTOS_FARMACEUTICOS | char(1) |  |  | Crédito presumido nas saídas interestaduais de produtos farmacêuticos - Anexo 4.24 do RICMS |
| SC_ESTORNAR_CREDITOS_DEVOLUCAO_FUNDOS_SOCIAIS_PROPORCIONAL_CREDITO_PRESUMIDO | char(1) |  |  | SC - Estornar créditos da devolução dos fundos sociais proporcional ao crédito presumido |
| RS_CREDITO_PRESUMIDO_CALCADOS_TIPO | integer(4) |  |  | Tipo de Crédito presumido fabric. calçados/artefatos de couro - Liv. I, art. 32, CXLI (1 - Calculado por nota / Calculado por produto) |
| CALCULAR_FATOR_AJUSTE_FRUICAO | char(1) |  |  | RS - Não calcular o Fator de Ajuste de Fruição - FAF |
| RS_CALCULAR_RESTITUICAO_ICMS_ST_PAGO_ETAPAS_ANTERIORES_FORMA_CALCULO | integer(4) |  |  | Calcular a restituição do ICMS Substituição Tributária pago nas etapas anteriores - Forma de cálculo |
| RN_CONSIDERAR_NO_CALCULO_AS_ENTRADAS_INTERESTADUAIS_ART_16B | char(1) |  |  | Considerar no cálculo as entradas interestaduais - Art. 16-B, §1º |
| RJ_PADARIAS_CONFEITARIAS_PAR | char(1) |  |  | RJ - Regime especial de tributação de ICMS - Padarias e Confeitarias (S/N) |
| RS_COMPENSAR_SALDO_CREDOR_ICMS_PROPRIO_NO_SUBTRI_MESMO_PERIODO | char(1) |  |  | RS - Compensar saldo credor do ICMS próprio no ICMS Subst. Tributária no mesmo período |
| SC_DEDUZIR_DEVOLUCOES_ESTORNO_CP_ENTRADAS | char(1) |  |  | SC- Deduzir as devoluções no cálculo do estorno do crédito presumido nas entradas |
| CONSIDERAR_IPI_ICMS_ST_NA_BASE_CALC_PIS_COFINS_REC_AMOSTRA_GRATIS | char(1) |  |  | Somar o valor do IPI e ICMS ST na base de cálculo do PIS/COFINS nas receitas de bonificação |
| RS_CREDITO_PRESUMIDO_AOS_ESTABELECIMENTOS_ABATEDORES_DE_SUINOS_LIVRO_I_ART_32_CXXXIII | char(1) |  |  | RS - Crédito presumido aos estabelecimentos abatedores de suínos - Livro I, Art. 32, CXXXIII |
| RS_DESCONSIDERAR_OUTROS_CREDITOS_LIMITE_CREDITO_PRESUMIDO | char(1) |  |  | RS - Desconsiderar outros créditos no limitador do crédito presumido |
| DEDUZIR_ICMS_MONOFASICO_DA_BASE_CALCULO_PIS_COFINS | char(1) |  |  | Deduzir o valor do ICMS monofásico da base de cálculo do PIS e COFINS |
| DF_CALCULAR_SALDO_CREDOR_TRANSF_PERIODO_LEI_5005_2012 | char(1) |  |  | Calcular saldo credor e transferir para o período seguinte - Lei nº 5.005/2012 |
| ES_DEDUZIR_DEVOLUCAO_VENDA_CALCULO_PROPORCAO_ESTORNO_CREDITO | char(1) |  |  | Deduzir o valor da devolução de venda do calculo de proporção do estorno de crédito |
| RS_CREDITO_PRESUMIDO_MICROCERVEJARIAS_ST | char(1) |  |  | Calcular o crédito presumido sobre a substituição tributária |
| DEDUZIR_ICMS_RECEITA_BRUTA_RATEIO_PROPORCIONAL_CREDITO | char(1) |  |  | Deduzir o ICMS da receita bruta no rateio proporcional de créditos |
| MA_CREDITO_PRESUMIDO_INDUSTRIA_AGROINDUSTRIA_LEI_10690_2017 | char(1) |  |  | MA - Crédito presumido indústria e agroindústria - Lei 10.690/2017 |
| MA_PERCENTUAL_DO_CREDITO_PRESUMIDO_INDUSTRIA_AGROINDUSTRIA_LEI_10690_2017 | numeric(4) |  |  | MA - Percentual do crédito presumido indústria e agroindústria - Lei 10.690/2017 |
| SC_CREDITO_PRESUMIDO_SAIDAS_INTERNAS_CAFE_TORRADO_ACUCAR | char(1) |  |  | SC - Crédito Presumido saídas internas de café torrado (grão ou moído) e açúcar - An2, art. 15. XIX |
| PE_REGIME_ESPECIAL_ICMS_ATACADISTA | char(1) |  |  | PE - Regime Especial de tributação do ICMS comércio atacadista (S/N) |
| RJ_CALCULAR_COMPLEMENTO_RESTITUICAO_ICMS_ST_CONFORME_RESOLUCAO_SEFAZ_578_2023 | char(1) |  |  | RJ - Calcular o complemento/restituição do ICMS ST conforme Resolução Sefaz nº 578/2023 |
| RJ_CONTROLAR_SALDO_COMPENSAR_PERIODO_FUTURO_CFE_ART_42_RESOLUCAO_578_2023 | char(1) |  |  | RJ - Controlar saldo a compensar em período futuro cfe § 1º e 2º do Art. 42 da Resolução 578/2023 |
| DEDUZIR_ICMS_DA_BASE_CALCULO_PIS_COFINS_RETIDOS | char(1) |  |  | Check para marcar se não para deduzir o valor do ICMS da base de calculo do PIS e COFINS Retidos |
| RJ_CREDITO_PRESUMIDO_ESTABELECIMENTO_ABATEDOR_INDUSTRIAL_FRIGORIFICO_ART_1_LEI_8792_2020 | char(1) |  |  | RJ - Crédito Presumido estabelecimento abatedor e industrial frigorífico - Art. 1º, V da Lei 8.792/2020 |
| RS_CREDITO_PRESUMIDO_SAIDAS_INTERNAS_LINGUICAS_MORTADELAS_SALSICHAS_LIVRO_I_ART_32_XXXV | char(1) |  |  | RS - Implementar o crédito presumido nas saídas internas de linguiças, mortadelas, salsichas e salsichões - Livro I, Art. 32, XXXV |
| CONSIDERAR_VALOR_DIFAL_NC_IRPJ_CSLL | char(1) |  |  | Considerar o valor do DIFAL-NC na base de cálculo do IRPJ e CSLL |
| MT_CONSIDERAR_FETHAB_BASE_IRPJ_CSLL | char(1) |  |  | Considerar o valor do FETHAB da parcela recebida na base de cálculo do IRPJ e CSLL |
| MT_CONSIDERAR_FETHAB_BASE_PIS_COFINS | char(1) |  |  | Considerar o valor do FETHAB da parcela recebida na base de cálculo do PIS e COFINS |
| RS_CREDITO_PRESUMIDO_SAIDAS_INTERNAS_GELEIAS_FRUTAS_LIVRO_I_ART_32_LXXIX | char(1) |  |  | Crédito presumido nas saídas internas de geleias de frutas - Livro I, Art. 32, LXXIX |
| TO_CONSIDERAR_SALDO_CREDOR_ICMS_PARA_CALCULO_DO_CREDITO_PRESUMIDO | char(1) |  |  | TO- Considerar o saldo credor do ICMS para cálculo do crédito presumido |
| AL_CALCULAR_ADICIONAL_FECOEP_ICMS | char(1) |  |  | AL - Calcular o adicional do FECOEP na apuração do ICMS |
| TRANSPORTADOR_AUTONOMO_CARGAS_MEI_CAMINHONEIRO_LC_188_2021 | char(1) |  |  | Transportador autônomo de cargas (MEI Caminhoneiro) - LC 188/2021 |
| SC_CREDITO_PRESUMIDO_SAIDA_PEIXE_PAR_APURAR_ESTAB_CENT | char(1) |  |  | Apurar o crédito presumido no estabelecimento centralizador |
| SC_CREDITO_PRESUMIDO_SAIDA_PEIXE_PAR_APURAR_ESTAB_CENT_ESTAB_CENT_EMP | integer(4) |  | S | Apurar o crédito presumido no estabelecimento centralizador - Empresa |
| PR_CREDITO_PRESUMIDO_COMERCIO_ELETRONICO_ART_11_DEC_6434_17 | char(1) |  |  | Crédito Presumido na modalidade de comércio eletrônico "e-commerce" - Art. 11-A Decreto 6.434/17 |
| RJ_CREDENCIADA_AO_REGIME_DA_SUBSTITUICAO_TRIBUTARIA_ROT_ST | char(1) |  |  | RJ - Credenciada ao regime da substituição tributária (ROT-ST) |
| RJ_NUMERO_PROCESSO_ADMINISTRATIVO_ROT_ST | varchar(21) |  | S | RJ - Número do processo administrativo (ROT-ST) |
| RS_DEDUZIR_RECEITA_BRUTA_VALOR_FUNDO_AMPARA | char(1) |  |  | RS - Não deduzir da receita bruta valor do Fundo do Ampara/RS - ICMS ST (S/N) |
| RS_CREDITO_PRESUMIDO_MODALIDADE_COMERCIO_ELETRONICO_E_COMMERCE_TIPO | char(1) |  |  | RS - Crédito presumido com. eletrônico "e-commerce" - Liv. I, Art. 32, CXCII - Tipo |
| RJ_SOMAR_VALOR_DOS_DEMAIS_IMPOSTOS_ESTADUAIS_PARA_CALCULO_DO_ICMS_MINIMO | char(1) |  |  | RJ - Somar o valor dos demais impostos estaduais para o cálculo do ICMS mínimo |
| BA_CALCULA_IMPOSTO_DIFALI_ALIQUOTA_INTERNA_ICMS_ORIGEM | char(1) |  |  | BA - Calcular o imposto 8-DIFALI sobre a alíquota interna descontando o ICMS de origem |
| SIMPLES_RECOLHER_ISS_FIXO_TIPO | integer(4) |  |  | Recolher o ISS fixo para |
| MG_CREDITO_PRESUMIDO_ARTEFATOS_SOBRE | char(1) |  |  | MG - Crédito presumido artefatos sobre |
| SC_CREDITO_PRESUMIDO_FABRICANTE_MERCADORIAS_CONSTRUCAO_CIVIL | char(1) |  |  | SC - Crédito Presumido ao fabricante de mercadorias para uso na construção civil - An2, Art. 249, II |
| DF_DEDUZIR_VALORES_ICMSST_E_IPI_DO_VALOR_TOTAL_VENDAS_VCV | char(1) |  |  | DF - Deduzir os valores de ICMS-ST e IPI do valor total contábil das vendas (VCv) |
| DEDUZIR_FCP_DA_BASE_CALCULO_PIS_COFINS | char(1) |  |  | Deduzir o DIFAL-NC da base de cálculo do PIS e COFINS |
| DEDUZIR_FCP_DA_BASE_CALCULO_PIS_COFINS_TIPO | char(1) |  |  | Deduzir o valor do FCP da base de cálculo do PIS e COFINS - Tipo |
| SC_POSSUI_TTD_09 | char(1) |  |  | SC - Possui Tratamento Tributário Diferenciado - TTD 09 |
| SC_NUMERO_TTD_09 | varchar(21) |  | S | SC - Número do TTD 09 |
| DEDUZIR_ISS_DA_BASE_CALCULO_PIS_COFINS_OPCOES | integer(4) |  |  | Deduzir o valor do ISS da base de cálculo do PIS e COFINS - Opção (1 - ISS Tributado, 2 - ISS Retido, 3 - ISS Tributado e Retido) |
| MG_ESTORNAR_CREDITO_ICMS_PROPORCIONAL_OPERACOES_CREDITO_PRESUMIDO | char(1) |  |  | MG - Estornar créditos de ICMS proporcional as operações de crédito presumido |
| RN_CALCULAR_REGIME_ATACADISTA_CONFORME_NUMERO_EMPREGOS_ART_16 | char(1) |  |  | RN - Regime Atacadista - Calcular conforme o número de empregos - Art. 16-R (S/N) |
| RN_CALCULAR_REGIME_ATACADISTA_CONFORME_NUMERO_EMPREGOS_ART_16_OPCAO | char(1) |  |  | RN - Regime Atacadista - Calcular conforme o número de empregos - Art. 16-R (Opção) |
| DCTF_WEB_EFETUAR_CALCULO_PREVIDENCIARIO_PAGAMENTO_DISCRIMINADO_TRIBUTO | char(1) |  |  | Efetuar cálculo de Tributos federais conforme DCTFWeb - Realizar o pagamento discriminado por tributo |
| MS_CREDITO_PRESUMIDO_ESTABELECIMENTO_FRIGORIFICO | char(1) |  |  | MS - Crédito presumido estabelecimentos frigoríficos - Art. 13 e 13-A Decreto 12.056/2006 |
| MS_CREDITO_PRESUMIDO_ESTABELECIMENTO_FRIGORIFICO_RECOLHE_FUNDERSUL | char(1) |  |  | MS - Crédito presumido estabelecimentos frigoríficos - Recolhe FUNDERSUL" |
| TO_CREDITO_PRESUMIDO_LEI_1790_2007_TIPO | integer(4) |  |  | TO - Crédito presumido - Lei Nº 1.790/2007, Art. 1º, I |
| SP_NAO_DEDUZIR_OPERACOES_ENTRADA_RETORNO_REMESSA_MEDIA_T | char(1) |  |  | SP - Deduzir as operações de entrada de Retorno de Remessa do cálculo da média T |
| SC_CREDITO_PRESUMIDO_ESTABELECIMENTO_ABATEDOR_OVINO | char(1) |  |  | SC - Crédito Presumido estabelecimento abatedor de ovino - An2, Art.15, XLV |
| PA_SUJEITO_CREDITO_PRESUMIDO_SAIDAS_CESTA_BASICA | char(1) |  |  | Crédito presumido nas saídas internas produtos cesta básica - Art. 126 do RICMS |
| RJ_CALCULAR_DEVOLUCAO_VENDA_SEPARADAMENTE | char(1) |  |  | Calcular devoluções de vendas separadamente conforme Resolução SEFAZ nº 705/2024, Art. 1º, §3º |
| DF_CALCULAR_RESTITUICAO_ICMS_SUBTRI_PAGO_ETAPAS_ANTERIORES | char(1) |  |  | DF - Calcular a restituição do ICMS Substituição Tributária pago nas etapas anteriores |
| MS_RECOLHE_FUNDERSUL_VALOR_OPERACAO | char(1) |  |  | Recolhe o FUNDERSUL sobre o valor da operação - Art. 12, § 3º -  Decreto 9.542/1999 |
| RJ_CREDITO_PRESUMIDO_EMPRESAS_FARMACEUTICAS | char(1) |  |  | RJ - Crédito Presumido empresas farmacêuticas - Art. 9º do Dec. 36.450/2004 |
| RJ_ICMS_MINIMO_USAR_VALOR_BASE | char(1) |  |  | RJ - Calcular o ICMS minimo com base no valor |
| RJ_ICMS_MINIMO_VALOR_BASE | numeric(13) |  |  | RJ - Valor base para o calculo do ICMS minimo |
| RJ_ICMS_MINIMO_SOMAR_VALOR_IMPOSTOS_ESTADUAIS | char(1) |  |  | RJ - Somar o valor dos demais impostos estaduais para o cálculo do ICMS mínimo |
| ES_ESTORNAR_CREDITOS_ICMS_DEVOLUCOES_VENDAS_PROPORCIONAL | char(1) |  |  | ES - Estornar os créditos de ICMS referentes as devoluções de vendas de forma proporcional |
| PR_CONSIDERAR_MATRIZ_FILIAIS_ICMS_MONOFASICO | char(1) |  |  | PR - Considerar matriz e filiais no coeficiente do ICMS Monofásico - Art. 25, § 5º do RICMS |
| SC_APURAR_TTD_409_410_411_ESTABELECIMENTO_CENTRALIZADOR | char(1) |  |  | SC - Apurar o TTD 409, 410 ou 411 no estabelecimento Consolidador |
| SC_APURAR_TTD_409_410_411_ESTABELECIMENTO_CENTRALIZADOR_CODIGO | integer(4) |  | S | SC - Código do estabelecimento Consolidador (TTD 409, 410 ou 411) |
| BA_CONSIDERAR_DATA_EMISSAO_FATO_GERADOR_ICMS_ANTECIPADO | char(1) |  |  | BA - Considerar a data de emissão do fato gerador ICMS antecipado |
| MA_CALCULA_DIFALI_ALIQ_FIXA_CIVIL | char(1) |  |  | Calcular o DIFALI com alíquota fixa para empresas de construção civil - Lei 9.094/2009 |
| MA_CRED_PRES_ATACADISTA_FORMA_DE_CALCULO | integer(4) |  |  | MA - Credito Presumido Atacadista: forma de cálculo |
| CALCULAR_MAJORACAO_PERCENTUAL_BASE_CALCULO | char(1) |  | S | Não calcular a majoração do percentual de base de cálculo - IN 2305/2025 |
| SP_CREDITO_OUTORGADO_SAIDAS_INTERNAS_CARNE | char(1) |  |  | SP - Crédito Outorgado nas saídas internas de carne - Anexo III, Art. 40 do RICMS |
| SP_CREDITO_OUTORGADO_SAIDAS_INTERNAS_CARNE_PCT | numeric(4) |  |  | SP - Percentual do Crédito Outorgado nas saídas internas de carne - Anexo III, Art. 40 do RICMS |
| CALCULAR_PISCOFINS_REDUCAO_LINEAR_LC224 | char(1) |  |  | Não calcular a redução linear dos incentivos e benefícios da LC 224/2025 |
| EMPRESA_COM_ATIVIDADE_IMOBILIARIA | char(1) |  |  | Empresa com atividade imobiliária |
| RS_COMPENSAR_SALDO_CREDOR_DIFALI_DEVOLUCAO_COMPRA | char(1) |  | S | RS - Compensar o saldo credor do DIFALI das devoluções de compras |
| BASE_DIRETA_PIS_COFINS_IMPORTACAO_PAR | char(1) |  | S | Considerar base direta no calculo do PIS/COFINS Importacao de servicos (S/N) |
