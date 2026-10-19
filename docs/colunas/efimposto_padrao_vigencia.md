# EFIMPOSTO_PADRAO_VIGENCIA — Tabela de Imposto Padrão - Vigência
32 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_IMP | integer(4) | PK |  | Codigo |
| UF | char(2) | PK |  | UF |
| VIGENCIA_IMP | date(4) | PK |  | Vigência |
| DESCRICAO_IMP | char(80) |  |  | Descricao |
| IREC_IMP | char(8) |  | S | Indexador para atualizacao monetaria |
| ABAS_IMP | numeric(5) |  | S | Aliquota da base de calculo |
| ALIQ_IMP | numeric(6) |  | S | Aliquota do imposto |
| COMP_IMP | char(1) |  |  | Competencia (F - federal/E - estadual/M - municipal) |
| PDIC_IMP | integer(4) |  |  | Periodicidade (1 - Mensal/2 - Quinzenal/3 - Decendial/4 - Trimestral/5 - Semanal/6 - Semestral) |
| FVEN_IMP | integer(4) |  |  | Forma de vencimento (1 - Dias corridos antecipado/2 - Dias corridos adiados/3 - Dias uteis/4 - Dias corridos direto/5 - Ultimo dia util) |
| NDIV_IMP | integer(4) |  |  | Dias para o vencimento |
| CDRN_IMP | char(6) |  | S | Codigo de recolhimento |
| CDRJ_IMP | char(6) |  | S | Codigo de recolhimento para os juros |
| CDRM_IMP | char(6) |  | S | Codigo de recolhimento para a multa |
| CDRC_IMP | char(6) |  | S | Codigo de recolhimento para a atualizacao monetaria |
| TCAL_IMP | char(1) |  |  | Tipo (L-Lancado por Nota / P-Lançado por Produto / C-Calculado) |
| CTRC_IMP | integer(4) |  | S | Conta contabil do imposto a recolher |
| CHIP_IMP | integer(4) |  | S | Historico padrao do imposto a recolher |
| CTRP_IMP | integer(4) |  | S | Conta contabil do imposto a recuperar |
| CHIR_IMP | integer(4) |  | S | Historico padrao do imposto a recuperar |
| PBCA_IMP | char(1) |  |  | Pede base de calculo no lancamento (S/N) |
| PALI_IMP | char(1) |  |  | Pede aliquota no lancamento (S/N) |
| PVIM_IMP | char(1) |  |  | Pede valor do imposto no lancamento (S/N) |
| PVIS_IMP | char(1) |  |  | Pede valor de isentas no lancamento (S/N) |
| PVOU_IMP | char(1) |  |  | Pede valor de outras no lancamento (S/N) |
| LANC_IMP | char(1) |  | S | Gera lancamentos contabeis por nota (S/N) |
| CTVD_IMP | integer(4) |  | S | Conta contabil para o imposto sobre vendas |
| CTCP_IMP | integer(4) |  | S | Conta contabil para o imposto sobre compras |
| QTDI_IMP | numeric(7) |  | S | Quantidade minima em indice para recolhimento |
| BCZR_IMP | integer(4) |  | S | Diferenca da base de calculo com valor contabil lancar em (1-Isentas/2-Outras/3-Nao lancar) |
| CTINC_IMP | integer(4) |  | S | Conta do incentivo da EPP(ICMS) |
| NDIV2_IMP | integer(4) |  | S | Nro de dias do vencimento do 2o Dec., 2a Quia=nz. ou 2a Sem. |
| NDIV3_IMP | integer(4) |  | S | Nro de dias do vencimento do 3o Dec. ou 3a Sem. |
| NDIV4_IMP | integer(4) |  | S | Nro de dias do vencimento da 4a Sem. |
| NDIV5_IMP | integer(4) |  | S | Nro de dias do vencimento da 5a Sem. |
| NMES_IMP | integer(4) |  | S | A partir de quantos meses vence o imposto(1o mes, 2o mes, 3o mes,...) |
| CTDV_IMP | integer(4) |  | S | Conta de devolucao de vendas |
| ALIQINSS_IMP | numeric(5) |  | S | Aliquota do INSS para o imposto Funrural |
| ALIQOUTRAS_IMP | numeric(6) |  | S | Aliquota Outras Entidades para calculo do Funrural |
| PIPI_IMP | char(1) |  | S | Pede valor de IPI no lancamento (S/N) |
| PSUBTRI_IMP | char(1) |  | S | Pede valor de Sub.Trib. no lancamento (S/N) |
| CLASSE_IMP | integer(4) |  | S | Classe de vencimento |
| CTADICFSOC_IMP | integer(4) |  | S | Conta do Adicional do FundoSocial |
| CHADICFSOC_IMP | integer(4) |  | S | Historico do Adicional do FundoSocial |
| CTDEVCOMPRA_IMP | integer(4) |  | S | Conta devolucao de compras |
| CHDEVCOMPRA_IMP | integer(4) |  | S | Historico devolucao de compras |
| CLASSE2_IMP | integer(4) |  | S | Classe de vencimento do 2o Dec., 2a Qui. ou 2a Sem. |
| CLASSE3_IMP | integer(4) |  | S | Classe de vencimento do 3o Dec. ou 3a Sem. |
| CLASSE4_IMP | integer(4) |  | S | Classe de vencimento da 4a Sem. |
| CLASSE5_IMP | integer(4) |  | S | Classe de vencimento da 5a Sem. |
| PISCRFOP_IMP | char(1) |  | S | Compensa PIS na CRFOP (S/N) |
| APISCRFOP_IMP | numeric(5) |  | S | Aliquota do PIS a compensar na CRFOP |
| COFCRFOP_IMP | char(1) |  | S | Compensa COFINS na CRFOP (S/N) |
| ACOFCRFOP_IMP | numeric(5) |  | S | Aliquota da COFINS a compensar na CRFOP |
| CSOCCRFOP_IMP | char(1) |  | S | Compensa CSLL na CRFOP (S/N) |
| ACSOCCRFOP_IMP | numeric(5) |  | S | Aliquota da CSLL a compensar na CRFOP |
| IRPJCRFOP_IMP | char(1) |  | S | Compensa IRPJ na CRFOP (S/N) |
| AIRPJCRFOP_IMP | numeric(5) |  | S | Aliquota do IRPJ a compensar na CRFOP |
| CODEXCED_IMP | char(6) |  | S | Codigo de recolhimento para o excedente |
| CONTABILIZA_ISSR_IMP | char(1) |  | S | Contabiliza ISS Retido (S/N) |
| CTPRESUMIDO_IMP | integer(4) |  | S | Conta do credito presumido |
| CHPRESUMIDO_IMP | integer(4) |  | S | Historico do credito presumido |
| PNTRI_IMP | char(1) |  | S | Pede nao tributadas |
| PREDU_IMP | char(1) |  | S | Pede parcela reduzida |
| CTPROTEGE_IMP | integer(4) |  | S | Conta do PROTEGE |
| CHPROTEGE_IMP | integer(4) |  | S | Historico do PROTEGE |
| CTICMSESTOQUE_IMP | integer(4) |  | S | Conta do ICMS sobre estoque |
| CHICMSESTOQUE_IMP | integer(4) |  | S | Historico do ICMS sobre estoque |
| CHCOMPENSACAO_IMP | integer(4) |  | S | Histórico do imposto a compensar |
| CTDEBITO_RESSARCIMENTO_IMP | integer(4) |  | S | Conta débito do ressarcimento |
| CTCREDITO_RESSARCIMENTO_IMP | integer(4) |  | S | Conta crédito do ressarcimento |
| CHRESSARCIMENTO_IMP | integer(4) |  | S | Histórico do ressarcimento |
| CTDEBITO_COMPLEMENTO_IMP | integer(4) |  | S | Conta débito do complemento |
| CTCREDITO_COMPLEMENTO_IMP | integer(4) |  | S | Conta crédito do complemento |
| CHCOMPLEMENTO_IMP | integer(4) |  | S | Histórico do complemento |
| CTABERTURA_ESTOQUE_IMP | integer(4) |  | S | Conta a compensar sobre abertura de estoque |
| CHABERTURA_ESTOQUE_IMP | integer(4) |  | S | Historico a compensar sobre abertura de estoque |
| CTBEM_IMOBILIZADO_AQUISICAO_IMP | integer(4) |  | S | Conta a compensar sobre bens do Imobilizado - Com base no valor de Aquisicao |
| CHBEM_IMOBILIZADO_AQUISICAO_IMP | integer(4) |  | S | Historico a compensar sobre bens do Imobilizado - Com base no valor de Aquisicao |
| CTBEM_IMOBILIZADO_DEPRECIACAO_IMP | integer(4) |  | S | Conta a compensar sobre bens do Imobilizado - Com base nos encargos da depreciacao |
| CHBEM_IMOBILIZADO_DEPRECIACAO_IMP | integer(4) |  | S | Historico a compensar sobre bens do Imobilizado - Com base nos encargos da depreciacao |
| CTACRESCIMO_DEBITO_IMP | integer(4) |  | S | Conta acrescimo no debito |
| CHACRESCIMO_DEBITO_IMP | integer(4) |  | S | Historico acrescimo no debito |
| CTREDUCAO_DEBITO_IMP | integer(4) |  | S | Conta reducao no debito |
| CHREDUCAO_DEBITO_IMP | integer(4) |  | S | Historico reducao no debito |
| CTACRESCIMO_CREDITO_IMP | integer(4) |  | S | Conta acrescimo no credito |
| CHACRESCIMO_CREDITO_IMP | integer(4) |  | S | Historico acrescimo no credito |
| CTREDUCAO_CREDITO_IMP | integer(4) |  | S | Conta reducao no credito |
| CHREDUCAO_CREDITO_IMP | integer(4) |  | S | Historico reducao no credito |
| CTOUTRAS_DEDUCOES_IMP | integer(4) |  | S | Conta outras deducoes |
| CHOUTRAS_DEDUCOES_IMP | integer(4) |  | S | Historico outras deducoes |
| LANCTO_PARTIDA_SIMPLES_IMP | char(1) |  |  | Gerar lançamentos de partida simples |
| CTICMS_FRETE_IMP | integer(4) |  | S | Conta do ICMS sobre o frete |
| CHICMS_FRETE_IMP | integer(4) |  | S | Histórico do ICMS sobre o frete |
| TTD_PRIMEIRO_VENCIMENTO | char(20) |  | S | Número do acordo TTD para o primeiro vencimento do imposto |
| TTD_SEGUNDO_VENCIMENTO | char(20) |  | S | Número do acordo TTD para o segundo vencimento do imposto |
| TTD_TERCEIRO_VENCIMENTO | char(20) |  | S | Número do acordo TTD para o terceiro vencimento do imposto |
| TTD_QUARTO_VENCIMENTO | char(20) |  | S | Número do acordo TTD para o quarto vencimento do imposto |
| TTD_QUINTO_VENCIMENTO | char(20) |  | S | Número do acordo TTD para o quinto vencimento do imposto |
| NAO_CONSIDERAR_FERIADO_MUNICIPAL_VENCIMENTO_IMP | char(1) |  |  | Não considerar feriados municipais para o vencimento do imposto |
| CTEFD_ALIQUOTA_BASICA_IMP | integer(4) |  | S | Conta crédito vinculado a alíquota básica - EFD |
| CHEFD_ALIQUOTA_BASICA_IMP | integer(4) |  | S | Histórico crédito vinculado a alíquota básica - EFD |
| CTEFD_ALIQUOTA_DIFERENCIADA_IMP | integer(4) |  | S | Conta crédito vinculado a alíquota diferenciada - EFD |
| CHEFD_ALIQUOTA_DIFERENCIADA_IMP | integer(4) |  | S | Histórico crédito vinculado a alíquota diferenciada - EFD |
| CTEFD_UNIDADE_DE_MEDIDA_IMP | integer(4) |  | S | Conta crédito vinculado a alíquota por unidade de medida - EFD |
| CHEFD_UNIDADE_DE_MEDIDA_IMP | integer(4) |  | S | Histórico crédito vinculado a alíquota por unidade de medida - EFD |
| CTEFD_AQUISICAO_DE_EMBALAGEM_IMP | integer(4) |  | S | Conta crédito vinculado a aquisição de embalagem - EFD |
| CHEFD_AQUISICAO_DE_EMBALAGEM_IMP | integer(4) |  | S | Histórico crédito vinculado a aquisição de embalagem - EFD |
| CTEFD_PRESUMIDO_AGROINDUSTRIA_IMP | integer(4) |  | S | Conta crédito presumido agroindústria - EFD |
| CHEFD_PRESUMIDO_AGROINDUSTRIA_IMP | integer(4) |  | S | Histórico crédito presumido agroindústria - EFD |
| CTEFD_IMPORTACAO_IMP | integer(4) |  | S | Conta crédito importação - EFD |
| CHEFD_IMPORTACAO_IMP | integer(4) |  | S | Histórico crédito importação - EFD |
| CTEFD_OUTROS_CREDITOS_IMP | integer(4) |  | S | Conta outros créditos - EFD |
| CHEFD_OUTROS_CREDITOS_IMP | integer(4) |  | S | Histórico outros créditos - EFD |
| CTEFD_OUTROS_CREDITOS_PRESUMIDOS_IMP | integer(4) |  | S | Conta outros créditos presumidos - EFD |
| CHEFD_OUTROS_CREDITOS_PRESUMIDOS_IMP | integer(4) |  | S | Histórico outros créditos presumidos - EFD |
| CTTRANSFERENCIA_CREDITO_ICMS_IMP | integer(4) |  | S | Conta transferência de crédito de ICMS |
| CTTRANSFERENCIA_DEBITO_ICMS_IMP | integer(4) |  | S | Conta transferência de débito de ICMS |
| CHTRANSFERENCIA_ICMS_IMP | integer(4) |  | S | Histórico transferência de ICMS |
| CTESTORNO_DEBITO_IMP | integer(4) |  | S | Conta estorno de débito |
| CHESTORNO_DEBITO_IMP | integer(4) |  | S | Histórico estorno de débito |
| CTDEBITO_BONUS_IMP | integer(4) |  | S | Conta débito do Bônus adimplência fiscal |
| CTCREDITO_BONUS_IMP | integer(4) |  | S | Conta crédito do Bônus adimplência fiscal |
| CHBONUS_IMP | integer(4) |  | S | Histórico do Bônus adimplência fiscal |
| CTDEVOLUCAO_ESTORNO_CREDITO_DEBITO_IMP | integer(4) |  | S | Conta débito da Devolução - Estorno de crédito |
| CTDEVOLUCAO_ESTORNO_CREDITO_CREDITO_IMP | integer(4) |  | S | Conta crédito da Devolução - Estorno de crédito |
| CHDEVOLUCAO_ESTORNO_CREDITO_IMP | integer(4) |  | S | Histórico da Devolução - Estorno de crédito |
| I_INDICE | integer(4) |  | S | Código do Índice |
| CTFUNDOSOCIAL_TTD_IMP | integer(4) |  | S | Fundo Social TTD - Conta |
| CHFUNDOSOCIAL_TTD_IMP | integer(4) |  | S | Fundo Social TTD - Histórico |
| CTRESSARCIMENTO_ICMSST_IMP | integer(4) |  | S | Ressarcimento ICMS ST - Conta |
| CHRESSARCIMENTO_ICMSST_IMP | integer(4) |  | S | Ressarcimento ICMS ST - Histórico |
| GERAR_LANCTO_ESTORNO_CRED_PRESUMIDO_IMP | char(1) |  |  | Gerar lançamento referente ao Estorno de Crédito nas operações com Crédito Presumido - (S/N) |
| CHESTORNO_CRED_PRESUMIDO_IMP | integer(4) |  | S | Estorno de Crédito nas operações com Crédito Presumido - Histórico |
| CTDEBITO_DIFERIDO_IMP | integer(4) |  | S | Débito Diferido - Conta |
| CHDEBITO_DIFERIDO_IMP | integer(4) |  | S | Débito Diferido - Histórico |
| CTCREDITO_DIFERIDO_IMP | integer(4) |  | S | Crédito Diferido - Conta |
| CHCREDITO_DIFERIDO_IMP | integer(4) |  | S | Crédito Diferido - Histórico |
| GERAR_PROVISAO_MENSAL_CTB | char(1) |  |  | Gerar provisão mensal do cálculo do imposto |
| ALIQUOTA_RAT | numeric(5) |  |  | Alíquota RAT |
| ALIQUOTA_TTD | numeric(5) |  |  | Alíquota TTD |
| CTDEDUCAO_PSDI | integer(4) |  | S | Dedução PSDI - Programa Sergipano de Desenvolvimento Industrial - Conta |
| HTDEDUCAO_PSDI | integer(4) |  | S | Dedução PSDI - Programa Sergipano de Desenvolvimento Industrial - Histórico |
| CT_REGIME_ESPECIAL_VENDAS | integer(4) |  | S | Regime Especial Vendas - Conta |
| CT_REGIME_ESPECIAL_COMPRAS | integer(4) |  | S | Regime Especial Compras - Conta |
| HT_REGIME_ESPECIAL | integer(4) |  | S | Regime Especial - Histórico |
| CT_ESTOQUE_EXCLUSAO_SIMPLES_NACIONAL | integer(4) |  | S | Estoque Exclusão Simples Nacional - Conta |
| HT_ESTOQUE_EXCLUSAO_SIMPLES_NACIONAL | integer(4) |  | S | Estoque Exclusão Simples Nacional - Histórico |
| CT_POSSUI_BENEFICIO_PROGRAMA_FOMENTO | integer(4) |  | S | Valor do benefício do Programa de Fomento à Industrialização - Lei Comp. nº 93/2001 - Conta |
| HT_POSSUI_BENEFICIO_PROGRAMA_FOMENTO | integer(4) |  | S | Valor do benefício do Programa de Fomento à Industrialização - Lei Comp. nº 93/2001 - Histórico |
| CT_CE_ESTIMATIVA_FIXA | integer(4) |  | S | Estimativa Fixa - Conta |
| HT_CE_ESTIMATIVA_FIXA | integer(4) |  | S | Estimativa Fixa - Histórico |
| CTCOMPENSACAO_IMP | integer(4) |  | S | Valor a Compensar - Conta |
| CHESTORNO_CREDITO_IMP | integer(4) |  | S | Estorno de crédito - Histórico |
| CTCREDITO_OUTORGADO_IMP | integer(4) |  | S | Crédito outorgado - Conta |
| HTCREDITO_OUTORGADO_IMP | integer(4) |  | S | Crédito outorgado - Histórico |
| GERAR_LANCTO_ESTORNO_CRED_OPER_CRE_OUTORGADO_IMP | char(1) |  |  | Gerar lançamento referente ao estorno de crédito nas operações com crédito outorgado (S/N) |
| HTESTORNO_CRED_OPER_CRE_OUTORGADO_IMP | integer(4) |  | S | Estorno de crédito nas operações com crédito outorgado - Histórico |
| CTPRODEPE_IMP | integer(4) |  | S | PRODEPE - Conta |
| HTPRODEPE_IMP | integer(4) |  | S | PRODEPE - Histórico |
| CT_VALOR_SUSPENSO | integer(4) |  | S | Valor suspenso - Conta |
| HT_VALOR_SUSPENSO | integer(4) |  | S | Valor suspenso - Histórico |
| CT_PISCOFINS_ESTORNO_CREDITO_PRAZO_DECADENCIAL | integer(4) |  | S | Estorno de crédito - Término do prazo decadencial - Conta |
| HT_PISCOFINS_ESTORNO_CREDITO_PRAZO_DECADENCIAL | integer(4) |  | S | Estorno de crédito - Término do prazo decadencial - Histórico |
| CT_APROP_CRED_ICMS_INSUMOS_PREST_SERV_TRANSP_IMP | integer(4) |  | S | Crédito ICMS sobre insumos - Conta |
| HT_APROP_CRED_ICMS_INSUMOS_PREST_SERV_TRANSP_IMP | integer(4) |  | S | Crédito ICMS sobre insumos - Histórico |
| CT_DEBITO_DIFERIDO_IN_247_2002 | integer(4) |  | S | Débito diferido - Art. 25 da IN 247/2002 - Conta |
| HT_DEBITO_DIFERIDO_IN_247_2002 | integer(4) |  | S | Débito diferido - Art. 25 da IN 247/2002 - Histórico |
| CT_PRIMEIRA_PARCELA_IN_1208 | integer(4) |  | S | Primeira parcela - IN 1.208/15-GSF - Conta |
| HT_PRIMEIRA_PARCELA_IN_1208 | integer(4) |  | S | Primeira parcela - IN 1.208/15-GSF - Histórico |
| CT_ATUALIZACAO_MONETARIA | integer(4) |  | S | Atualização monetária - Conta |
| HT_ATUALIZACAO_MONETARIA | integer(4) |  | S | Atualização monetária - Histórico |
| CTESTORNO_CREDITO_IMP | integer(4) |  | S | Conta estorno de crédito |
| CT_CREDITO_IN_1208 | integer(4) |  | S | Crédito IN 1.208/15-GSF - Conta |
| HT_CREDITO_IN_1208 | integer(4) |  | S | Crédito IN 1.208/15-GSF - Histórico |
| I_TABELA_ICMS | integer(4) |  | S | Código Tabela de Alíquota |
| PERCENTUAL_PARTILHA_UF_DESTINO | numeric(5) |  |  | Percentual de partilha do imposto para UF destino |
| EMPRESA_SN_CALC_DIFERENCIAL_ALIQUOTA_UF_ORIGEM | char(1) |  |  | Gerar lançamento referente ao estorno de crédito nas operações com crédito outorgado (S/N) |
| CHOUTROS_CREDITOS_VENDA_FORA_ESTABELECIMENTO | integer(4) |  | S | Crédito venda fora estabelecimento - Histórico |
| CONSIDERAR_VALOR_RETIDO_MENOR_MINIMO_RECOLHIMENTO | char(1) |  |  | Desconsiderar o valor retido do imposto menor ou igual a quantidade mínima para recolhimento |
| ES_COMPETE_CODIGO_RECOLHIMENTO | char(6) |  | S | ICMS COMPETE-ES fora estado - Código de recolhimento |
| ES_COMPETE_DIA_VENCIMENTO | integer(4) |  | S | ICMS COMPETE-ES fora estado - Vencimento |
| HT_DEDUCAO_CREDITO_TOTAL | integer(4) |  | S | Dedução do crédito total - Arts. 530-LRK e 534-ZZA - Histórico |
| CT_CREDITO_REGISTRADO_LIMITADO | integer(4) |  | S | Crédito registrado ou limitado - Arts. 530-LRK e 534-ZZA - Conta |
| HT_CREDITO_REGISTRADO_LIMITADO | integer(4) |  | S | Crédito registrado ou limitado - Arts. 530-LRK e 534-ZZA - Histórico |
| HT_ESTORNO_ADICIONAL_DEBITO | integer(4) |  | S | Estorno adicional de débito das saídas interestaduais - Art.530-LRK - Histórico |
| CTCREDITO_PROVISAO_IMP | integer(4) |  | S | Provisão - Conta |
| CHCREDITO_PROVISAO_IMP | integer(4) |  | S | Provisão - Histórico |
| I_TABELA_ICMS_STAT | integer(4) |  | S | Código Tabela de Alíquota ICMS STAT |
| CT_IMPOSTO_RECOLHER_OPER_PREST_BENEF_CP_IMP | integer(4) |  | S | Imposto a recolher das Operações e Prestações beneficiadas pelo Crédito Presumido - Conta |
| HT_IMPOSTO_RECOLHER_OPER_PREST_BENEF_CP_IMP | integer(4) |  | S | Imposto a recolher das Operações e Prestações beneficiadas pelo Crédito Presumido - Histórico |
| SC_CREDITO_PRESUMIDO_CODIGO_RECOLHIMENTO | char(6) |  | S | Crédito Presumido - Código de recolhimento |
| SC_CREDITO_PRESUMIDO_DIA_VENCIMENTO | integer(4) |  | S | Crédito Presumido - Vencimento |
| SC_CREDITO_PRESUMIDO_CLASSE_VENCIMENTO | integer(4) |  | S | Crédito Presumido - Classe de Vencimento |
| SC_CREDITO_PRESUMIDO_NUMERO_ACORDO_TTD | char(15) |  | S | Crédito Presumido - Número do acordo TTD |
| DESOBRIGADO_DEPOSITO_FEEF_DECISAO_JUDICIAL | varchar(1) |  |  | Desobrigado ao depósito no FEEF por decisão judicial |
| CT_CONTRIBUICAO_FACS | integer(4) |  | S | Contribuição ao Fundo de Apoio à Cultura da Soja - Conta |
| HT_CONTRIBUICAO_FACS | integer(4) |  | S | Contribuição ao Fundo de Apoio à Cultura da Soja - Histórico |
| CT_CONTRIBUICAO_FABOV | integer(4) |  | S | Contribuição ao Fundo de Apoio à Bovinocultura de Corte - Conta |
| HT_CONTRIBUICAO_FABOV | integer(4) |  | S | Contribuição ao Fundo de Apoio à Bovinocultura de Corte - Histórico |
| CT_CONTRIBUICAO_FAMAD | integer(4) |  | S | Contribuição ao Fundo de Apoio à Madeira - Conta |
| HT_CONTRIBUICAO_FAMAD | integer(4) |  | S | Contribuição ao Fundo de Apoio à Madeira - Histórico |
| CT_CONTRIBUICAO_IMAMT | integer(4) |  | S | Contribuição ao instituto Mato-grossense do Algodão - Conta |
| HT_CONTRIBUICAO_IMAMT | integer(4) |  | S | Contribuição ao instituto Mato-grossense do Algodão - Histórico |
| CT_CONTRIBUICAO_ADICIONAL_FETHAB | integer(4) |  | S | Contribuição adicional ao FETHAB - Conta |
| HT_CONTRIBUICAO_ADICIONAL_FETHAB | integer(4) |  | S | Contribuição adicional ao FETHAB - Histórico |
| CONSIDERAR_EMISSAO_PARA_VENCIMENTO | char(1) |  |  | Considerar emissão para vencimento (S/N) |
| CT_DEDUCAO_INCENTIVOS_COMPENSACAO_CREDITO | integer(4) |  | S | Deduções por Incentivos / Compensação de Crédito - Conta |
| HT_DEDUCAO_INCENTIVOS_COMPENSACAO_CREDITO | integer(4) |  | S | Deduções por Incentivos / Compensação de Crédito - Histórico |
| CT_DEBITO_TRANSITORIAS_ZERAMENTO_IMP | integer(4) |  | S | Conta Transitória de zeramento - Débito |
| CT_CREDITO_TRANSITORIAS_ZERAMENTO_IMP | integer(4) |  | S | Conta Transitória de zeramento - Crédito |
| CH_TRANSITORIAS_ZERAMENTO_IMP | integer(4) |  | S | Conta Transitória de zeramento - Histórico |
| CT_DEBITO_CREDITO_ICMS_PROPRIO_PORT_CAT_158_2015 | integer(4) |  | S | Crédito do ICMS Próprio Portaria CAT 158/2015 - Conta crédito |
| CT_CREDITO_CREDITO_ICMS_PROPRIO_PORT_CAT_158_2015 | integer(4) |  | S | Crédito do ICMS Próprio Portaria CAT 158/2015 - Conta débito |
| HT_CREDITO_ICMS_PROPRIO_PORTARIA_CAT_158_2015 | integer(4) |  | S | Crédito do ICMS Próprio Portaria CAT 158/2015 - Histórico |
| GERAR_LANCTO_ESTORNO_DEBITO_OP_CREDITO_PRESUMIDO_IMP | char(1) |  |  | MG - Gerar lançamento referente ao estorno de débitos nas operações com crédito presumido |
| CHESTORNO_DEBITO_OP_CREDITO_PRESUMIDO_IMP | integer(4) |  | S | Gerar lançamento referente ao estorno de débito nas operações com crédito presumido - Histórico |
| REALIZAR_CALCULO_INCREMENTO_ICMS_LEI_7428 | char(1) |  |  | Realizar o cálculo do incremento de ICMS - Art. 3º da Lei 7.428/2016 |
| CT_DEBITO_ESPECIAL_ART_530 | integer(4) |  | S | Conta - Débito especial - Benefício Art. 530-LRF RICMS |
| HT_DEBITO_ESPECIAL_ART_530 | integer(4) |  | S | Histórico - Débito especial - Benefício Art. 530-LRF RICMS |
| CDRN_IMP_FEEF | char(7) |  |  | Código de Recolhimento |
| CT_CREDITO_ICMS_NAO_APROPRIADO | integer(4) |  | S | Conta - Crédito ref. ao ICMS próprio não apropriado na aquisição de merc. sujeita ao ICMS-ST devolvida |
| HT_CREDITO_ICMS_NAO_APROPRIADO | integer(4) |  | S | Histórico - Crédito ref. ao ICMS próprio não apropriado na aquisição de merc. sujeita ao ICMS-ST devolvida |
| CT_CREDITO_PRESUMIDO | integer(4) |  | S | Conta - Crédito ref. ao Crédito Presumido |
| HT_CREDITO_PRESUMIDO | integer(4) |  | S | Histórico - Crédito ref. ao Crédito Presumido |
| CT_DEBITO_CREDITO_ICMS_PROPRIO_DECRETO_6875_2017 | integer(4) |  | S | Crédito de ICMS Próprio conforme Decreto 6.875/2017 - Conta Débito |
| CT_CREDITO_CREDITO_ICMS_PROPRIO_DECRETO_6875_2017 | integer(4) |  | S | Crédito de ICMS Próprio conforme Decreto 6.875/2017 - Conta Crédito |
| HT_CREDITO_ICMS_PROPRIO_DECRETO_6875_2017 | integer(4) |  | S | Crédito de ICMS Próprio conforme Decreto 6.875/2017 - Histórico |
| CT_DEBITO_RESSARCIMENTO_ICMS_ST_DECRETO_6875_2017 | integer(4) |  | S | Ressarcimento de ICMS ST conforme Decreto 6.875/2017 - Conta Débito |
| CT_CREDITO_RESSARCIMENTO_ICMS_ST_DECRETO_6875_2017 | integer(4) |  | S | Ressarcimento de ICMS ST conforme Decreto 6.875/2017 - Conta Crédito |
| HT_RESSARCIMENTO_ICMS_ST_DECRETO_6875_2017 | integer(4) |  | S | Ressarcimento de ICMS ST conforme Decreto 6.875/2017 - Histórico |
| CT_DEBITO_TAXA_SERVICO_ARRECADACAO | integer(4) |  | S | Conta - Taxa de Serviço de Arrecadação - Débito |
| CT_CREDITO_TAXA_SERVICO_ARRECADACAO | integer(4) |  | S | Conta - Taxa de Serviço de Arrecadação - Crédito |
| HT_TAXA_SERVICO_ARRECADACAO | integer(4) |  | S | Histórico - Taxa de Serviço de Arrecadação |
| GERAR_VALOR_APURADO_IMPOSTO_STAT_DESTDA | char(1) |  |  | Não gerar o valor apurado do imposto no informativo DeSTDA |
| CTDEVOLUCAO_RESSARCIMENTO_IMP | integer(4) |  | S | Ressarcimento de ICMS ST Portaria CAT 17/99 ou Portaria CAT 158/2015 - Conta Devolução |
| CT_DEVOLUCAO_CREDITO_ICMS_PROPRIO_PORT_CAT_158_2015 | integer(4) |  | S | Crédito de ICMS Próprio Portaria CAT 158/2015 - Conta Devolução |
| INVERTER_PERCENTUAL_PARTILHA_NAS_DEVOLUCAO_UF_ORIGEM_UF_DESTINO | char(1) |  |  | Nas devoluções não inverter o percentual da partilha da UF origem e UF destino |
| POSSUI_PAJ_IMP | char(1) |  |  | Possui Processo Administrativo Judicial |
| CONSIDERAR_EMISSAO_PARA_VENCIMENTO_TIPO | integer(4) |  |  | Data a ser considerada para o vencimento do imposto (1-Emissão da nota/ 2-Emissão do MDF-e) |
| CALCULA_ICMS_ANTECIPADO_DECRETO_53348_2018 | char(1) |  |  | Calcula ICMS antecipado conf. Dec. 53.348/2018 |
| CALCULA_ICMS_ANTECIPADO_DECRETO_53348_2018_PERCENTUAL | numeric(5) |  |  | Calcula ICMS antecipado conf. Dec. 53.348/2018 - Percentual |
| CT_ICMS_COMPETE_E_COMMERCE_BENEFICIO_ART_530 | integer(4) |  | S | lCMS-COMPETE- E-Commerce- Benefício Art. 530-LRI RICMS - Conta |
| HT_ICMS_COMPETE_E_COMMERCE_BENEFICIO_ART_530 | integer(4) |  | S | lCMS-COMPETE- E-Commerce- Benefício Art. 530-LRI RICMS - histórico |
| CT_RESSARCIMENTO_RESSARC_COMP_ICMS_ST_IMP | integer(4) |  | S | Ressarcimento/Complemento - Conta Ressarcimento |
| CT_COMPLEMENTO_RESSARC_COMP_ICMS_ST_IMP | integer(4) |  | S | Ressarcimento/Complemento - Conta Complemento |
| HT_RESSARC_COMP_ICMS_ST_IMP | integer(4) |  | S | Ressarcimento/Complemento - Histórico |
| ALIQUOTA_PJ | numeric(8) |  |  | Alíquota diária PJ |
| ALIQUOTA_PF | numeric(8) |  |  | Alíquota diária PF |
| ALIQUOTA_SN | numeric(8) |  |  | Alíquota diária SN |
| ALIQUOTA_ADICIONAL | numeric(8) |  |  | Alíquota adicional |
| RECOLHE_ADICIONAL_RETENCAO_CFE_LEI_977_98 | char(1) |  |  | Recolhe adicional de retenção cfe. Lei 9.711/98 |
| CT_CONTRIBUICAO_IAGRO_IMP | integer(4) |  | S | Contribuição ao Fundo do Instituto Mato-Grossense do Agronegócio - IAGRO - Conta |
| HT_CONTRIBUICAO_IAGRO_IMP | integer(4) |  | S | Contribuição ao Fundo do Instituto Mato-Grossense do Agronegócio - IAGRO - Histórico |
| ALIQUOTA_SOBRE_ENTRADAS_IMP | numeric(5) |  |  | Alíquota sobre entradas |
| ALIQUOTA_SOBRE_SAIDAS_IMP | numeric(5) |  |  | Alíquotas sobre saídas |
| ALIQUOTA_SOBRE_CREDITO_PRESUMIDO_IMP | numeric(5) |  |  | Alíquota sobre crédito presumido |
| CT_CONTRIBUICAO_CIPEM_IMP | integer(4) |  | S | Contribuição ao Centro das Indústrias Produtoras e Exportadoras de Madeira de Mato Grosso - CIPEM - Conta |
| HT_CONTRIBUICAO_CIPEM_IMP | integer(4) |  | S | Contribuição ao Centro das Indústrias Produtoras e Exportadoras de Madeira de Mato Grosso - CIPEM - Histórico |
| CODIGO_RECOLHIMENTO_COMPLEMENTO | char(6) |  | S | Código de Recolhimento - Complementação |
| I_INDICE_COMPLEMENTO | integer(4) |  | S | Código do Índice - Complementação |
| NMES_COMPLEMENTO_IMP | integer(4) |  | S | A partir de quantos meses vence o imposto - Complementação |
| FVEN_COMPLEMENTO_IMP | integer(4) |  | S | Forma de vencimento - Complementação |
| NAO_CONSIDERAR_FERIADO_MUNICIPAL_VENCIMENTO_COMPLEMENTO_IMP | char(1) |  |  | Não considerar feriados municipais para o vencimento do imposto - Complementação |
| NDIV_COMPLEMENTO_IMP | integer(4) |  | S | Dias para o vencimento - Complementação |
| CLASSE_COMPLEMENTO_IMP | integer(4) |  | S | Classe de vencimento - Complementação |
| CT_CREDITO_ICMS_PROPRIO_SAIDAS_OUTRAS_UF_IMP | integer(4) |  | S | Crédito de ICMS Próprio nas saídas para outras UFs - Conta |
| HT_CREDITO_ICMS_PROPRIO_SAIDAS_OUTRAS_UF_IMP | integer(4) |  | S | Crédito de ICMS Próprio nas saídas para outras UFs - Histórico |
| CT_CREDITO_AUC_IMP | integer(4) |  | S | Crédito de AUC - Autorização de Utilização de Créditos - Conta |
| HT_CREDITO_AUC_IMP | integer(4) |  | S | Crédito de AUC - Autorização de Utilização de Créditos - Histórico |
| CT_COMPLEMENTACAO_SUBTRI_IMP | integer(4) |  | S | Complementação SUBTRI - Conta |
| HT_COMPLEMENTACAO_SUBTRI_IMP | integer(4) |  | S | Complementação SUBTRI - Histórico |
| CT_ADICIONAL_ICMS_COMPETE_ES | integer(4) |  | S | Adicional ICMS COMPETE-ES - Conta |
| HT_ADICIONAL_ICMS_COMPETE_ES | integer(4) |  | S | Adicional ICMS COMPETE-ES - Histórico |
| ES_ADICIONAL_COMPETE_CODIGO_RECOLHIMENTO | char(6) |  | S | Adicional ICMS COMPETE-ES - Código Recolhimento |
| ES_ADICIONAL_COMPETE_DIA_VENCIMENTO | integer(4) |  | S | Adicional ICMS COMPETE-ES - Dia vencimento |
| CT_DEBITO_ICMS_ST_SUB_APUR_RESSARC_COMP_IMP | integer(4) |  | S | ICMS ST Sub-Apuração Ressarcimento/Complemento - Conta débito |
| CT_CREDITO_ICMS_ST_SUB_APUR_RESSARC_COMP_IMP | integer(4) |  | S | ICMS ST Sub-Apuração Ressarcimento/Complemento - Conta crédito |
| HT_CREDITO_ICMS_ST_SUB_APUR_RESSARC_COMP_IMP | integer(4) |  | S | ICMS ST Sub-Apuração Ressarcimento/Complemento - Histórico |
| CT_DEBITO_ICMS_ST_SUB_APUR_RESSARC_COMP_ESTOQUE_INICIAL_IMP | integer(4) |  | S | ICMS ST Sub-Apuração Ressarcimento/Complemento - Estoque Inicial - Conta débito |
| CT_CREDITO_ICMS_ST_SUB_APUR_RESSARC_COMP_ESTOQUE_INICIAL_IMP | integer(4) |  | S | ICMS ST Sub-Apuração Ressarcimento/Complemento - Estoque Inicial - Conta crédito |
| HT_CREDITO_ICMS_ST_SUB_APUR_RESSARC_COMP_ESTOQUE_INICIAL_IMP | integer(4) |  | S | ICMS ST Sub-Apuração Ressarcimento/Complemento - Estoque Inicial - Histórico |
| CT_CONTRIBUICAO_IMAFIR_IMP | integer(4) |  | S | Contribuição ao Instituto Mato-grossense do Feijão, Pulses, Grãos Especiais e Irrigação - IMAFIR/MT - Conta |
| HT_CONTRIBUICAO_IMAFIR_IMP | integer(4) |  | S | Contribuição ao Instituto Mato-grossense do Feijão, Pulses, Grãos Especiais e Irrigação - IMAFIR/MT - Histórico |
| CT_ICMS_MINIMO_RECOLHER_RIOLOG_IMP | integer(4) |  | S | ICMS mínimo a recolher do Programa RIOLOG - Conta |
| HT_ICMS_MINIMO_RECOLHER_RIOLOG_IMP | integer(4) |  | S | ICMS mínimo a recolher do Programa RIOLOG - Histórico |
| CTTRANSFERENCIA_ICMS_IMP | integer(4) |  | S | Transferência de crédito de ICMS - Conta |
| CONSIDERAR_VALOR_RETIDO_MENOR_MINIMO_RECOLHIMENTO_TIPO | char(1) |  |  | Desconsiderar o valor retido do imposto menor ou igual a quantidade mínima para recolhimento - Tipo (E-Entrada/S-Saída/T-Entrada e Saída) |
| CT_DEBITO_ICMS_NAO_DESTACA_NFE_SUSP_DIF_SAIDAS_IMP | integer(4) |  | S | Débito de ICMS (Não destacado em NF-e) pela suspensão do diferimento nas saídas - Conta |
| HT_DEBITO_ICMS_NAO_DESTACA_NFE_SUSP_DIF_SAIDAS_IMP | integer(4) |  | S | Débito de ICMS (Não destacado em NF-e) pela suspensão do diferimento nas saídas - Histórico |
| CODREC_ICMS_EXTEMP_IMP | char(6) |  | S | ICMS extemporâneo - Código de recolhimento |
| VENCIMENTO_ICMS_EXTEMP_IMP | integer(4) |  | S | ICMS extemporâneo - Vencimento |
| CT_CREDITO_INSUMOS_FORNECI_ALIMENTACAO_IMP | integer(4) |  | S | Crédito de insumos no fornecimento de alimentação - Conta |
| HT_CREDITO_INSUMOS_FORNECI_ALIMENTACAO_IMP | integer(4) |  | S | Crédito de insumos no fornecimento de alimentação - Histórico |
| POSSUI_PRORROGACAO_VENCIMENTO_TRIBUTOS | char(1) |  |  | Possui prorrogação do vencimento dos tributos |
| PRORROGACAO_TRIBUTOS_FEDERAIS | char(1) |  |  | Tributos federais |
| PRORROGACAO_TRIBUTOS_FEDERAIS_DIAS | integer(4) |  | S | Tributos federais - Dias |
| PRORROGACAO_TRIBUTOS_FEDERAIS_PERIODO_SUBSEQUENTE | integer(4) |  | S | Tributos federais - Período Subsequente |
| PRORROGACAO_TRIBUTOS_FEDERAIS_FORMA_VENCIMENTO | integer(4) |  | S | Tributos federais - Forma de vencimento |
| PRORROGACAO_TRIBUTOS_ESTADUAIS | char(1) |  |  | Tributos estaduais |
| PRORROGACAO_TRIBUTOS_ESTADUAIS_DIAS | integer(4) |  | S | Tributos estaduais - Dias |
| PRORROGACAO_TRIBUTOS_ESTADUAIS_PERIODO_SUBSEQUENTE | integer(4) |  | S | Tributos estaduais - Período Subsequente |
| PRORROGACAO_TRIBUTOS_ESTADUAIS_FORMA_VENCIMENTO | integer(4) |  | S | Tributos estaduais - Forma de vencimento |
| PRORROGACAO_TRIBUTOS_MUNICIPAIS | char(1) |  |  | Tributos municipais |
| PRORROGACAO_TRIBUTOS_MUNICIPAIS_DIAS | integer(4) |  | S | Tributos municipais - Dias |
| PRORROGACAO_TRIBUTOS_MUNICIPAIS_PERIODO_SUBSEQUENTE | integer(4) |  | S | Tributos municipais - Período Subsequente |
| PRORROGACAO_TRIBUTOS_MUNICIPAIS_FORMA_VENCIMENTO | integer(4) |  | S | Tributos municipais - Forma de vencimento |
| CT_ICMS_ST_RECUP_RESSARC_IMP | integer(4) |  | S | ICMS ST a recuperar/ressarcir conforme NPF 03/2020 - Conta |
| HT_ICMS_ST_RECUP_RESSARC_IMP | integer(4) |  | S | ICMS ST a recuperar/ressarcir conforme NPF 03/2020 - Histórico |
| CT_ICMS_ST_COMPTO_IMP | integer(4) |  | S | ICMS ST a complementar conforme NPF 03/2020 - Conta |
| HT_ICMS_ST_COMPTO_IMP | integer(4) |  | S | ICMS ST a complementar conforme NPF 03/2020 - Histórico |
| CT_FECOP_ST_RECUP_RESSARC_IMP | integer(4) |  | S | FECOP ST a recuperar/ressarcir conforme NPF 03/2020 - Conta |
| HT_FECOP_ST_RECUP_RESSARC_IMP | integer(4) |  | S | FECOP ST a recuperar/ressarcir conforme NPF 03/2020 - Histórico |
| CT_FECOP_ST_COMPTO_IMP | integer(4) |  | S | FECOP ST a complementar conforme NPF 03/2020 - Conta |
| HT_FECOP_ST_COMPTO_IMP | integer(4) |  | S | FECOP ST a complementar conforme NPF 03/2020 - Histórico |
| CT_DEBITO_CREDITO_ICMS_PROPRIO_ART_20_ANEXO_VI | integer(4) |  | S | Crédito ICMS Próprio - Conta Débito |
| CT_CREDITO_CREDITO_ICMS_PROPRIO_ART_20_ANEXO_VI | integer(4) |  | S | Crédito ICMS Próprio - Conta Crédito |
| HT_CREDITO_ICMS_PROPRIO_DECRETO_ART_20_ANEXO_VI | integer(4) |  | S | Crédito ICMS Próprio - Histórico |
| CT_DEBITO_RESSARCIMENTO_ICMS_ST_ART_20_ANEXO_VI | integer(4) |  | S | Ressarcimento de ICMS ST conforme Art. 20 do Anexo VI do RICMS - Conta Débito |
| CT_CREDITO_RESSARCIMENTO_ICMS_ST_ART_20_ANEXO_VI | integer(4) |  | S | Ressarcimento de ICMS ST conforme Art. 20 do Anexo VI do RICMS - Conta Crédito |
| HT_RESSARCIMENTO_ICMS_ST_ART_20_ANEXO_VI | integer(4) |  | S | Ressarcimento de ICMS ST conforme Art. 20 do Anexo VI do RICMS - Histórico |
| CT_CREDITOS_REGIME_ATACADISTA | integer(4) |  | S | Crédito regime especial - Decreto 22.199/11 - Conta |
| HT_CREDITOS_REGIME_ATACADISTA | integer(4) |  | S | Crédito regime especial - Decreto 22.199/11 - Histórico |
| DEDUZIR_VALOR_RETENCAO_INSS_SUBCONTRATADA | char(1) |  |  | Deduzir o valor de retenção INSS subcontratada |
| CT_CONTRIBUICAO_IMAD_IMP | integer(4) |  | S | Contribuição ao Instituto da Madeira do Estado de Mato Grosso - IMAD/MT - Conta |
| HT_CONTRIBUICAO_IMAD_IMP | integer(4) |  | S | Contribuição ao Instituto da Madeira do Estado de Mato Grosso - IMAD/MT - Histórico |
| SC_CREDITO_PRESUMIDO_SUBSEQUENTE_VENCIMENTO | integer(4) |  | S | A partir de quantos meses vence o imposto(1o mes, 2o mes, 3o mes,...) |
| CT_CREDITO_AQUISICAO_EMPRESA_SIMPLESN_IMP | integer(4) |  | S | Crédito na aquisição de empresas do Simples Nacional - Conta |
| HT_CREDITO_AQUISICAO_EMPRESA_SIMPLESN_IMP | integer(4) |  | S | Crédito na aquisição de empresas do Simples Nacional - Histórico |
| LANC_CREDITO_AQUISICAO_EMPRESA_SIMPLESN_IMP | char(1) |  |  | Crédito na aquisição de empresas do Simples Nacional - Histórico - Gera lançamentos contábeis por nota |
| SC_ICMS_COMPLEMENTAR_CODIGO_RECOLHIMENTO | char(6) |  | S | ICMS Complementar - Código de recolhimento |
| SC_ICMS_COMPLEMENTAR_DIA_VENCIMENTO | integer(4) |  | S | ICMS Complementar - Vencimento |
| SC_ICMS_COMPLEMENTAR_CLASSE_VENCIMENTO | integer(4) |  | S | ICMS Complementar - Classe de vencimento |
| PRORROGACAO_TRIBUTOS_QUOTAS | char(1) |  |  | Tributos |
| PRORROGACAO_TRIBUTOS_QUOTAS_DIAS | integer(4) |  | S | Tributos - Dias |
| PRORROGACAO_TRIBUTOS_QUOTAS_PERIODO_SUBSEQUENTE | integer(4) |  | S | Tributos - Período Subsequente |
| PRORROGACAO_TRIBUTOS_QUOTAS_FORMA_VENCIMENTO | integer(4) |  | S | Tributos - Forma de vencimento |
| PRORROGACAO_TRIBUTOS_QUOTAS_QTDE | integer(4) |  |  | Tributos - Quantidade de Quotas |
| CT_CONTRIBUICAO_INPECMT | integer(4) |  | S | Contribuição ao Instituto da Pecuária de Corte Mato-grossense - INPECMT - Conta |
| HT_CONTRIBUICAO_INPECMT | integer(4) |  | S | Contribuição ao Instituto da Pecuária de Corte Mato-grossense - INPECMT - Histórico |
| ALIQUOTA_CONFORME_CREDITO_PRESUMIDO | char(1) |  |  | Alíquota TTD conforme crédito presumido |
| RJ_ICMS_COMPLEMENTAR_CODIGO_RECOLHIMENTO | char(6) |  | S | ICMS Complementar - Código de recolhimento |
| RJ_ICMS_COMPLEMENTAR_DIA_VENCIMENTO | integer(4) |  | S | ICMS Complementar - Vencimento |
| CT_COMPENSACAO_VALOR_MINIMO_RIOLOG_IMP | integer(4) |  | S | Compensação de valor mínimo do programa RIOLOG - Conta |
| HT_COMPENSACAO_VALOR_MINIMO_RIOLOG_IMP | integer(4) |  | S | Compensação de valor mínimo do programa RIOLOG - Histórico |
| CT_DEBITO_JUROS_MULTA_EXTEMPORANEO_DOCUMENTOS_FISCAIS | integer(4) |  | S | Juros e multa por escrituração extemporânea de documentos fiscais - Conta débito |
| CT_CREDITO_JUROS_MULTA_EXTEMPORANEO_DOCUMENTOS_FISCAIS | integer(4) |  | S | Juros e multa por escrituração extemporânea de documentos fiscais - Conta crédito |
| HT_JUROS_MULTA_EXTEMPORANEO_DOCUMENTOS_FISCAIS | integer(4) |  | S | Juros e multa por escrituração extemporânea de documentos fiscais - Histórico |
| DEDUCOES_TIPO | integer(4) |  |  | Tipos de deduções - 1- Por dependente/ 2- Simplificada mensal / 3- Mais vantajosa |
| CT_ICMS_COMPETE_BENEFICIO_ART_530 | integer(4) |  | S | lCMS-COMPETE- Benefício Art. 530-LF RICMS - Conta |
| HT_ICMS_COMPETE_BENEFICIO_ART_530 | integer(4) |  | S | lCMS-COMPETE- Benefício Art. 530-LF RICMS - histórico |
| CT_PRESUMIDO_REGIME_ATACADISTA | integer(4) |  | S | Conta Crédito Presumido Regime Atacadista |
| HT_PRESUMIDO_REGIME_ATACADISTA | integer(4) |  | S | Histórico Crédito Presumido Regime Atacadista |
| CT_RECOLHIMENTO_VENDAS_CONSUMIDOR_FINAL | integer(4) |  | S | Conta para recolhimento específico vendas a consumidor final não inscrito no CNPJ |
| HT_RECOLHIMENTO_VENDAS_CONSUMIDOR_FINAL | integer(4) |  | S | Histórico para recolhimento específico vendas a consumidor final não inscrito no CNPJ |
| RJ_CT_RESSARCIMENTO_ICMS_ST_RESOLUCAO_578_2023 | integer(4) |  | S | Ressarcimento/Complemento - Conforme Resolução Sefaz Nº 578/2023 - Conta Ressarcimento |
| RJ_CT_COMPLEMENTO_RESSARCIMENTO_ICMS_ST_RESOLUCAO_578_2023 | integer(4) |  | S | Ressarcimento/Complemento - Conforme Resolução Sefaz nº 578/2023 - Complemento Ressarcimento |
| RJ_HT_RESSARCIMENTO_ICMS_ST_RESOLUCAO_578_2023 | integer(4) |  | S | Ressarcimento/Complemento - Conforme Resolução Sefaz nº 578/2023 - Historico Ressarcimento |
| RJ_CT_RESSARCIMENTO_ICMS_ST_RESOLUCAO_578_2023_DEBITO_SUBTRI | integer(4) |  | S | Débito Ressarcimento ICMS Próprio - Conta Débito Subtri |
| RJ_CT_RESSARCIMENTO_ICMS_ST_RESOLUCAO_578_2023_CREDITO_SUBTRI | integer(4) |  | S | Crédito Ressarcimento ICMS Próprio - Conta Crédito Subtri |
| RJ_HT_RESSARCIMENTO_ICMS_ST_RESOLUCAO_578_2023_SUBTRI | integer(4) |  | S | Crédito Ressarcimento ICMS Próprio - Ressarcimento Histórico Subtri |
| RJ_CT_COMPLEMENTO_ICMS_ST_RESOLUCAO_578_2023_SUBTRI | integer(4) |  | S | Ressarcimento de ICMS ST conforme Art. 20 do Anexo VI do RICMS - Conta Complemento Subtri |
| RJ_HT_COMPLEMENTO_ICMS_ST_RESOLUCAO_578_2023_SUBTRI | integer(4) |  | S | Ressarcimento de ICMS ST conforme Art. 20 do Anexo VI do RICMS - Complemento Histórico Subtri |
| CT_PISCOFINS_RECEITA_FINANCEIRA_DOCUMENTO_NAO_FISCAL | integer(4) |  | S | Receita financeira - Documento não fiscal - Conta |
| HT_PISCOFINS_RECEITA_FINANCEIRA_DOCUMENTO_NAO_FISCAL | integer(4) |  | S | Receita financeira - Documento não fiscal - Histórico |
| DF_CT_RESTITUICAO_ICMS_PAGO_ETAPAS_ANT_ART_329_330 | integer(4) |  | S | Restituição do ICMS Substituição Tributária pago nas etapas anteriores - Artigos 329 e 330 do Decreto 18.955/97 - Conta Restituição |
| DF_HT_RESTITUICAO_ICMS_PAGO_ETAPAS_ANT_ART_329_330 | integer(4) |  | S | Restituição do ICMS Substituição Tributária pago nas etapas anteriores - Artigos 329 e 330 do Decreto 18.955/97 - Conta Historico Restituição |
