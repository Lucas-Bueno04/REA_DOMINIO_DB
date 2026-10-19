# EFACUMULADOR_VIGENCIA — Acumuladores - Cadastro
460.804 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_ACU | integer(4) | PK |  | Codigo |
| VIGENCIA_ACU | date(4) | PK |  | Vigencia |
| DESCRICAO_ACU | char(80) |  |  | Descricao |
| IFAT_ACU | char(1) |  |  | Incide sobre Faturamento (S/N) |
| IREC_ACU | char(1) |  |  | Incide sobre Receita Bruta (S/N) |
| IENQ_ACU | char(1) |  |  | Enquadramento EPP (S/N) |
| CDEB_ACU | integer(4) |  |  | Conta Debito |
| CCRE_ACU | integer(4) |  |  | Conta Credito |
| CHIS_ACU | integer(4) |  |  | Historico Padrao |
| IAX1_ACU | char(1) |  |  | Incide sobre Acrescimo financeiro (S/N) |
| IAX2_ACU | char(1) |  |  | Auxiliar 2 - Nao utilizada |
| IAX3_ACU | char(1) |  |  | Auxiliar 3 - Nao utilizada |
| ESTO_ACU | char(1) |  |  | Faz estoque/DIPI (S/N) |
| IDEV_ACU | char(1) |  |  | Incide sobre Devolucao (S/N) |
| GPAT_ACU | char(1) |  |  | Gera bens automaticamento no patrimonio (S/N) |
| PMUN_ACU | char(1) |  | S | Habilitar digitacao do codigo do municipio (S/N) |
| RMAN_ACU | char(1) |  | S | Gera resumo de manifesto no livro de saidas (S/N) |
| DCTB_ACU | char(1) |  | S | Mostra sempre a contabilizacao no lancamento (S/N) |
| PARC_ACU | char(1) |  | S | Gera parcelas nas notas (S/N) |
| CTCP_ACU | integer(4) |  | S | Conta de contra partida para pagto das notas parceladas |
| CTJR_ACU | integer(4) |  | S | Conta dos Juros dos pagamentos |
| CTMT_ACU | integer(4) |  | S | Conta da multa dos pagamentos |
| CTDT_ACU | integer(4) |  | S | Conta do desconto das parcelas |
| CHCP_ACU | integer(4) |  | S | Historico do lancto da Contra Partida |
| CHJR_ACU | integer(4) |  | S | Historico do lancto dos juros |
| CHMT_ACU | integer(4) |  | S | Historico do lancto da multa |
| CHDT_ACU | integer(4) |  | S | Historico do lancto do desconto |
| CHPG_ACU | integer(4) |  | S | Historico do lancto do pagamento |
| DMUN_ACU | char(1) |  | S | Mostra sempre as tabelas municipais no lancamento (S/N) |
| TIPONOTA_ACU | char(1) |  |  | Tipo de nota (V - a vista/P - a prazo/O - outras) |
| TRANSFERENCIA_ACU | char(1) |  |  | Nota de transferencia de credito (S/N) |
| CNAT_ACU | char(1) |  |  | Confere natureza no lancamento (S/N) |
| CTDV_ACU | integer(4) |  | S | Conta de devolucao das parcelas |
| CHDV_ACU | integer(4) |  | S | Historico do lancto da devolucao |
| CODI_OBS | integer(4) |  | S | Codigo da observacao |
| SMUN_ACU | char(1) |  | S | Incide sobre Simples Municipal (S/N) |
| DETANEXO_ACU | char(1) |  | S | RS: Detalhamento do Anexo VA e VB (S/N) |
| CANCEL_ACU | char(1) |  | S | Nota cancelada (S/N) |
| SERVTERC_ACU | char(1) |  | S | Nota de Servico terceirizado (S/N) |
| ORIGEM_REG | integer(4) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| IMPORTACAO_ACU | char(1) |  | S | Notas de importacao com aproveitamento de credito de ICMS (S/N) |
| NAOSOMARSIMPLES_ACU | char(1) |  | S | Nao somar com servico para aumento de 50% na aliquota do SIMPLES (S/N) |
| DFTAREDECRETO_ACU | char(1) |  | S | Discriminar item TARE / Decreto 23806/2003 - DF (S/N) |
| FRETE_ACU | char(1) |  | S | Informar dados do frete |
| CTAICMSCP_ACU | integer(4) |  | S | Conta ICMS sobre compras |
| SEICMSVENDA_ACU | char(1) |  | S | SE: Calcular 7% de ICMS sobre a venda |
| GERAENTRADA_ACU | char(1) |  | S | Gerar Nota de Entrada em outra empresa (S=Sim/N=Nao) |
| RATEIOCCUSTO_ACU | char(1) |  | S | Mostrar rateio de Centro de Custo (S=Sim/N=Nao) |
| TRANSRECBRUTA_ACU | char(1) |  | S | PR: Transgerencia de Receita Bruta (S=Sim/N=Nao) |
| RSCREDITOSNAOCOMPENSAVEIS_ACU | char(1) |  | S | RS: Operacoes com creditos nao compensaveis (S=Sim/N=Nao) |
| SIMPLES_ALIQ_DIFERENCIADA_ACU | char(1) |  |  | Calcular Simples com aliquota diferenciada(S/N) |
| ICMS_FRETE_ACU | char(1) |  |  | ICMS sobre o frete(S/N) |
| HABILITA_COP_ACU | char(1) |  |  | Habilita Codigo de Operacao e Prestacao |
| COP_ACU | char(3) |  |  | Codigo de Operacao e Prestacao |
| AGROP_SUJEITOS_ST_ACU | char(1) |  | S | Produtos agropecuarios sujeitos a substituicao tributaria(S/N) |
| GERA_CRED_PAG_IMPORT_ACU | char(1) |  | S | Gera credito referente ao pagamento (S/N) |
| TIPO_SERVICO_ACU | integer(4) |  | S | Tipo de Servico (1 - Transportes/2 - Comunicacao/3 - Fornecimento de Agua/4 - Fornecimento de energia eletrica/5 - Outros/6 - Extracao Mineral) |
| PRODUTOS_SUJEITOS_ST_ACU | char(1) |  | S | Produtos sujeitos ao regime de substituicao tributaria(S/N) |
| CREDITO_PRESUMIDO_ACU | char(1) |  | S | Gera credito presumido na apuracao (S/N) |
| SAIDA_ICMSGI_ACU | char(1) |  | S | Saida interestadual com imposto garantido recolhido(S/N) |
| DEVOLUCAO_ICMSGI_ACU | char(1) |  | S | Devolucao de operacoes internas com incidencia do ICMS garantido(S/N) |
| ICMS_FRETE_SOBRE_ACU | char(1) |  | S | Soma o frete sobre o imposto(I - ICMS/S - SUBTRI) |
| SAIDA_ESTORNO_CREDITO_ACU | char(1) |  | S | Saidas com estorno de credito de ICMS (S/N) |
| ITEM_PADRAO_ACU | integer(4) |  | S | Item padrao do estorno de credito do ICMS das saidas |
| TIPO_CALCULO_ESTORNO_ACU | char(1) |  | S | Tipo de calculo do estorno de credito do ICMS das saidas (V-valor /P-proporcao) |
| SIMPLESN_CREDITO_PRESUMIDO_ACU | char(1) |  | S | Calcula credito presumido simples nacional (S/N) |
| SIMPLESN_ENTRADAS_ACU | char(1) |  | S | Entradas de mercadoria para calculo do Simples Nacional - Decreto 662/2007 (S/N) |
| ICMS_CONTA_GRAFICA_PRO_EMPREGO_ACU | char(1) |  | S | Gerar Credito de ICMS em conta grafica - Programa Pro-emprego (S/N) |
| FOMENTAR_ACU | char(1) |  | S | Saidas de Operacoes Incentivadas do Programa Fomentar/Produzir/Microproduzir(S/N) |
| FOMENTAR_SAIDAS_ACU | char(1) |  | S | Saidas de Operacoes Incentivadas do Programa Fomentar/Produzir/Microproduzir - Tipo de saidas (E/I) |
| TABELA_CREDITO_PRESUMIDO_ACU | integer(4) |  |  | TABELA CRÉDITO PRESUMIDO |
| DFDECRETO_ITEM_PADRAO_ACU | integer(4) |  | S | Item padrao do Decreto/DF |
| SUBTRI_CREDITO_ICMS_ACU | char(1) |  | S | Aproveitar o valor do imposto Substituicao Tributaria como credito no imposto ICMS |
| ANEXO_VA_PADRAO_ACU | integer(4) |  | S | Item padrao do Anexo VA |
| ANEXO_VB_PADRAO_ACU | integer(4) |  | S | Item padrao do Anexo VB |
| SIMPLESN_CREDITO_PRESUMIDO_TIPO_ACU | char(1) |  | S | Tipo de Crédito Presumido SN (A - Conforme Alíquota sn / I - Crédito Presumido (Indústria) - Alíq. 10% / D - Crédito Presumido (Indústria) - Alíq. 12%) |
| LANCTO_DEB_CRE_REF_ANT_ACU | char(1) |  |  | Lancamento de debito/credito referente a antecipacao do imposto - entradas interestaduais (S/N) |
| LANCTO_DEB_REF_ANT_ACU | char(1) |  |  | Lancamento de debito referente a antecipacao do imposto - mercadorias sujeita a substituicao tributaria (S/N) |
| MERC_PROD_ADQ_DIF_ICMS_ACU | char(1) |  |  | Mercadorias e/ou Produtos Adquiridos com diferimento de ICMS (S/N) |
| DET_ANEXO_VA_ACU | char(1) |  | S | Detalha Anexo VA(S/N) |
| DET_ANEXO_VB_ACU | char(1) |  | S | Detalha Anexo VB(S/N) |
| POSSUI_COMPLEMENTAR_ACU | char(1) |  | S | Possui informacao complementar(S/N) |
| CODIGO_INFORMACAO | integer(4) |  | S | Código da informação complementar |
| ICMSST_ESTOQUE_ACU | char(1) |  | S | Nota de Debito de ICMS Subst. Tributaria sobre estoques(S/N) |
| PROCESSO_REFERENCIADO_ACU | char(1) |  | S | Informar dados de processo referenciado(S/N) |
| DOCUMENTO_REFERENCIADO_ACU | char(1) |  | S | Informar dados de documento de arrecadação referenciado(S/N) |
| NOTA_REFERENCIADA_ACU | char(1) |  | S | Informar dados de notas fiscais referenciadas(S/N) |
| CUPOM_REFERENCIADO_ACU | char(1) |  | S | Informar dados de cupons fiscais referenciados(S/N) |
| DIREITO_CREDITO_ACU | char(1) |  | S | Operações com direito a crédito acumulado(S/N) |
| DEFINE_OPERACAO_CREDITO_ACU | char(1) |  | S | Definir operação de crédito para notas de saídas(S/N) |
| TIPO_CREDITO_ACU | char(1) |  | S | Tipo do crédito acumulado(D - Operação com diferimento/S - Operação com suspensão/R - Operação com redução de Base de Cálculo/V - Valores a excluir do ICMS) |
| RESSARCIMENTO_COMPLEMENTO_CAT_17_99_ACU | char(1) |  | S | Ressarcimento ou complemento do ICMS-CAT 17/99 (S/N) |
| COMPLEMENTO_PADRAO_CFOP_CAT_17_99_ACU | char(1) |  | S | Definir Complemento padrão por CFOP - Portaria Cat nº 17/99 (S/N) |
| RESPONSAVEL_DIF_BENEFICIARIO_ACU | char(1) |  |  | Responsavel pelo pagamento do servico de saude e diferente do beneficiario (S/N) |
| NATUREZA_FRETE_ACU | tinyint(1) |  |  | Natureza do frete |
| CODIGO_CST_PISCOFINS_ENTRADA_ACU | integer(4) |  | S | CST PISCOFINS - Entradas |
| BASE_CREDITO_ACU | integer(4) |  | S | Base do credito |
| CODIGO_CST_PISCOFINS_SAIDA_ACU | integer(4) |  | S | CST PISCOFINS - Saidas |
| NATUREZA_RECEITA_ACU | integer(4) |  | S | Natureza da receita |
| OPERACAO_SERVICO_TRANSPORTE_ACU | char(1) |  |  | Operacao de servico de transporte (S/N) |
| CALCULAR_CREDITO_PRESUMIDO_NOTA_ACU | char(1) |  |  | Calcular o crédito Presumido no lançamento da nota, conforme Decreto 3.346/2010 - Subst. Tributária (S=Sim / N=Não) |
| DEVOLUCAO_ISS_ACU | char(1) |  |  | Deduções de ISS Conforme Art. 7º, § 2, Inc.I, L.C. 116/2003 (S=Sim / N=Não) |
| VALOR_PRESENTE_ENT_PROV_AVP_COMPRA_CTA_ACU | integer(4) |  |  | Conta AVP - compras/estoque - Valor Presente - Entradas - Provisao |
| VALOR_PRESENTE_ENT_PROV_AVP_FORNEC_CTA_ACU | integer(4) |  |  | Conta AVP - fornecedores - Valor Presente - Entradas - Provisao |
| VALOR_PRESENTE_ENT_PROV_AVP_HIS_ACU | integer(4) |  |  | Historico AVP - Valor Presente - Entradas - Provisao |
| VALOR_PRESENTE_ENT_PROV_AVP_JUROS_CTA_ACU | integer(4) |  |  | Conta juros a pagar - AVP - Valor Presente - Entradas - Provisao |
| VALOR_PRESENTE_ENT_PROV_AVP_JUROS_HIS_ACU | integer(4) |  |  | Historico juros a pagar - AVP - Valor Presente - Entradas - Provisao |
| VALOR_PRESENTE_ENT_APRO_DESPESA_CTA_ACU | integer(4) |  |  | Conta despesa finaneira - Valor Presente - Entradas - Apropriacao mensal das despesas financeiras |
| VALOR_PRESENTE_ENT_APRO_DESPESA_HIS_ACU | integer(4) |  |  | Historico despesa finaneira - Valor Presente - Entradas - Apropriacao mensal das despesas financeiras |
| VALOR_PRESENTE_SAISER_PROV_AVP_CLIENTE_CTA_ACU | integer(4) |  |  | Conta AVP - clientes - Valor Presente - Saidas ou Servicos - Provisao |
| VALOR_PRESENTE_SAISER_PROV_AVP_RECEITA_CTA_ACU | integer(4) |  |  | Conta AVP - receitas - Valor Presente - Saidas ou Servicos - Provisao |
| VALOR_PRESENTE_SAISER_PROV_AVP_RECEITA_HIS_ACU | integer(4) |  |  | Historico AVP - receitas - Valor Presente - Saidas ou Servicos - Provisao |
| VALOR_PRESENTE_SAISER_PROV_AVP_JUROS_CTA_ACU | integer(4) |  |  | Conta juros a receber - AVP - Valor Presente - Saidas ou Servicos - Provisao |
| VALOR_PRESENTE_SAISER_PROV_AVP_HIS_ACU | integer(4) |  |  | Historico AVP - Valor Presente - Saidas ou Servicos - Provisao |
| VALOR_PRESENTE_SAISER_APRO_RECEITA_CTA_ACU | integer(4) |  |  | Conta receita finaneira - Valor Presente - Saidas ou Servicos - Apropriacao mensal das receitas financeiras |
| VALOR_PRESENTE_SAISER_APRO_RECEITA_HIS_ACU | integer(4) |  |  | Historico receita finaneira - Valor Presente - Saidas ou Servicos - Apropriacao mensal das receitas financeiras |
| AQUISICAO_EMPREENDIMENTO_IMOBILIARIO_ACU | char(1) |  |  | Aquisição para empreendimento imobiliário (S/N) |
| I_EMPREENDIMENTO | integer(4) |  | S | Código do empreendimento imobiliário |
| DISCRIMINAR_CODIGO_NATUREZA_ACU | char(1) |  |  | Discriminar Código da Natureza |
| CODIGO_NATUREZA_ACU | integer(4) |  | S | Código da Natureza |
| SC_ESTORNAR_CREDITO_ICMS_ACU | char(1) |  |  | SC - Estornar créditos de ICMS - Crédito presumido transportes (S/N) |
| GERA_DMED_ACU | char(1) |  |  | Gera para o informativo DMED(S/N) |
| CREDITO_PRESUMIDO_ENTRADA | char(1) |  |  | Crédito presumido - Entrada Guajará-Mirim |
| BA_OPERACAO_PROJETO_DESENVOLVE | char(1) |  |  | Operação vinculada ao Projeto DESENVOLVE |
| SC_CREDITO_PRESUMIDO_CONFECCAO_ART_15 | char(1) |  |  | Operação de crédito presumido confecção art. 15 |
| PIS_COFINS_RECEITA_DIFERIDA | char(1) |  |  | Receita diferida para as contribuições do PIS e COFINS - Art. 25 da IN 247/2002 |
| RS_NOTA_APROPRIACAO_CREDITO_PRESUMIDO_ICMS | char(1) |  |  | RS - Nota de apropriação de crédito presumido de ICMS |
| GO_NOTA_TRANSFERENCIA_CREDITO_CHEQUE_MORADIA | char(1) |  |  | Nota de transferência de crédito - Cheque Moradia |
| MS_APROVEITAR_SUBTRI_CREDITO_ICMS | char(1) |  |  | Aproveitar o valor do imposto Substituição Tributária como crédito no imposto ICMS |
| OUTROS_CREDITOS_PRESUMIDOS_PIS_COFINS | char(1) |  |  | Outros créditos presumidos PIS/COFINS (S/N) |
| RO_INFORMA_SAIDA_DISPOSITIVO_LEGAL | char(1) |  |  | Informar nas saídas o dispositivo legal da isenção ou redução da base de cálculo do ICMS (S/N) |
| RO_INFORMA_SAIDA_DISPOSITIVO_LEGAL_AJUSTE | integer(4) |  | S | Código de Ajuste |
| MG_OPERACAO_SUJEITA_CRED_PRESUMIDO | char(1) |  |  | MG - Operação sujeita ao crédito presumido (S/N) |
| MG_OPERACAO_SUJEITA_CRED_PRESUMIDO_TIPO | integer(4) |  |  | MG - OPERAÇÃO SUJEITA AO CRÉDITO PRESUMIDO TIPO |
| SC_CREDITO_ENERGIA_ELETRICA_LAUDO_TECNICO | char(1) |  |  | Crédito de energia elétrica com base em laudo técnico |
| EFETUA_CONTROLE_CFOP_POR_UF_CLIENTE | char(1) |  |  | Efetuar controle de CFOP por UF do cliente |
| RS_CREDITO_PRESUMIDO_VENDA_TEXTIL_VESTUARIO | char(1) |  |  | Gerar crédito presumido nas vendas de produtos têxteis e do vestuário - Livro I Art. 32, CXXXV |
| SC_ESTORNAR_CREDITO_ICMS_CREDITO_PRESUMIDO_TIPO | integer(4) |  | S | SC - Estornar Crédito para Crédito Presumido |
| SE_TARE_TIPO | integer(4) |  |  | SE - Optante TARE - Tipo (1 - Decreto n° 22.958/2004 - Comércio Atacadista / 2 - Decreto n° 26.169/2009 - Comércio Atacadista de Prod. de Higiene e perfumaria) |
| CONSIDERAR_PARA_CALCULO_COEFICIENTE_CREDITO_ICMS | char(1) |  |  | Considerar saídas para cálculo do coeficiente de crédito de ICMS |
| SC_OPERACAO_SAIDA_MERCADORIAS_TTDS_409_410_411 | char(1) |  |  | SC - Operação de saída subsequente de mercadorias alcançadas pelos TTDS 409, 410 ou 411 (S/N) |
| MT_ESTORNAR_CREDITO_ICMS_CREDITO_PRESUMIDO_TIPO | integer(4) |  |  | MT - Estornar créditos de ICMS nas operações com crédito presumido - Tipo |
| MT_CREDITO_PRESUMIDO | integer(4) |  |  | Gera crédito presumido na apuração - Seleção |
| MT_CREDITO_PRESUMIDO_PERCENTUAL | numeric(8) |  |  | Gera crédito presumido na apuração - Percentual |
| RETORNO_REMESSA | char(1) |  |  | Retorno de Remessa |
| MOSTRAR_LANCAMENTO_NOTA_INSS_RB | char(1) |  |  | Mostrar no lançamento da nota - INSS Receita Bruta (S/N) |
| POSSUI_RECEITA_ATIVIDADE_DIFERENTE_CNAE | char(1) |  |  | Possui receita de atividade diferente do CNAE principal (S/N) |
| RECEITA_NOTA_DIFERENTE_CNAE | char(1) |  |  | Receita total da nota é diferente do CNAE principal (S/N) |
| EXCLUIR_RECEITA_BASE_CALCULO_INSS_RB | char(1) |  |  | Excluir receita total da base de cálculo do INSS Receita Bruta (S/N) |
| PR_REGIME_ESPECIAL_RECOLHIMENTO_ICMS | char(1) |  |  | Regime especial de recolhimento de ICMS - RERI |
| MOSTRAR_LANCAMENTO_NOTA_ENTIDADES_EQUIPARADAS | char(1) |  |  | Mostrar no lançamento da nota - Entidades Financeiras Equiparadas (S/N) |
| SC_OPERACAO_RESSARCIMENTO_ICMS_ST | char(1) |  |  | Operação com direito a ressarcimento nas vendas com Substituição Tributária |
| SC_OPERACAO_RESSARCIMENTO_ICMS_ST_APROVEITAR | integer(4) |  |  | Operação com direito a ressarcimento nas vendas com Substituição Tributária - Aproveitar o crédito do ICMS ST na apuração do imposto |
| CTOUTRAS_ACU | integer(4) |  | S | Conta de Outras das parcelas |
| CHOUTRAS_ACU | integer(4) |  | S | Histórico do lancto de Outras |
| RS_CREDITO_PRESUMIDO_ACU | char(1) |  |  | RS - Gerar crédito presumido na apuração (S/N) |
| RS_TABELA_CREDITO_PRESUMIDO_ACU | integer(4) |  |  | RS - Tabela crédito presumido na apuração |
| I_SCP | integer(4) |  | S | Sequencial do SCP |
| POSSUI_OBSERVACAO_ACU | char(1) |  |  | Possui observações |
| RJ_SOMAR_BASE_CALCULO_REGIME_ESPECIAL_OPCAO | char(1) |  | S | RJ - Não somar na base de cálculo do regime especial - Opção (B=Bares, Restaurantes e Similares/ I=Indústrias do setor têxtil/ P=Política de Recuperação Industrial Regionalizada) |
| RJ_SOMAR_BASE_CALCULO_REGIME_ESPECIAL | char(1) |  |  | RJ - Somar na base de cálculo do regime especial (S/N) |
| RS_LANC_DEBITO_ANTECIPA_IMP_PROD_FARMACIA | char(1) |  |  | RS - Lançamento de débito referente a antecipação do imposto - produtos farmacêuticos recebidos em bonificação |
| TO_GERAR_CREDITO_PRESUMIDO_ICMS_MERCADORIA_ST | char(1) |  |  | TO - Gerar crédito presumido de ICMS nas aquisições de mercadorias sujeita a ST - Lei N° 1.201/2000, Art. 1°, III |
| SC_TIPO_PRODUTO | integer(4) |  | S | Tipo de produto (1-Demais produtos / 2-Aço e Cobre) |
| RS_GERAR_CREDITO_ICMS_EMP_SN | char(1) |  |  | Gerar crédito de ICMS na aquisição de empresas do Simples Nacional |
| RS_NOTA_APROP_CREDITO_ICMS_EMP_SN | char(1) |  |  | Nota de apropriação do crédito de ICMS na aquisição de empresas do Simples Nacional |
| OPERACAO_VEICULOS_USADOS_ACU | char(1) |  |  | Operação com veículos usados (S/N) |
| RS_LANC_DEB_PARC_ICMSST_PRODUTO | char(1) |  |  | RS - Lançamento de débito referente a parcela do ICMS Substituição Tributária sobre estoques (S/N) |
| GERAR_DEDUCAO_ISS_OPCOES | integer(4) |  |  | Gerar deduções de ISS - Opções (1/2) |
| DISCRIMINA_CFPS_LANCAMENTO | char(1) |  |  | Discriminar CFPS para o lançamento (S/N) |
| RO_CREDITO_PRESUMIDO_BARES_RESTAURANTES_ACU | char(1) |  |  | RO - Crédito presumido de bares e restaurantes - Item 21 Tabela 1 Anexo IV (S/N) |
| SOMAR_DIFERENCIAL_ALIQ_VALOR_BEM | char(1) |  |  | Somar o valor do diferencial de alíquota ao valor original do bem (S/N) |
| BA_CREDITO_PRESUMIDO_CONFECCAO | char(1) |  |  | BA - Crédito Presumido de Confecção (S/N) |
| RS_TRANSFERENCIA_ACU_TIPO | integer(4) |  |  | RS - Nota de Transferência de Crédito Tipo (1/2) |
| OPERACAO_GERADORA_CRED_ACU | char(1) |  |  | Operação geradora de crédito acumulado |
| TIPO_CRED_ACU | integer(4) |  | S | Tipo de crédito acumulado |
| TO_CREDITO_PRESUMIDO_75_ICMS_APURADO_ACU | char(1) |  |  | TO - Crédito presumido de 75% sobre o ICMS apurado (S/N) |
| AGENTE_REGULADO_OPERACAO | integer(4) |  | S | Agente Regulado - Operação |
| AGENTE_REGULADO_MODAL | integer(4) |  | S | Agente Regulado - Modal |
| AGENTE_REGULADO_CODIGO_VEICULO | varchar(7) |  |  | Agente Regulado - Código Veículo |
| AGENTE_REGULADO_SERVICO | integer(4) |  | S | Agente Regulado - Serviço |
| AGENTE_REGULADO_TERCEIRO | char(1) |  |  | Agente Regulado - Terceiro |
| AGENTE_NAO_REGULADO_OPERACAO | integer(4) |  | S | Agente Não Regulado - Operação |
| AGENTE_NAO_REGULADO_MODAL | integer(4) |  | S | Agente Não Regulado - Modal |
| AGENTE_NAO_REGULADO_CODIGO_VEICULO | char(7) |  |  | Agente Não Regulado - Código Veículo |
| AGENTE_NAO_REGULADO_SERVICO | integer(4) |  | S | Agente Não Regulado - Serviço |
| AGENTE_NAO_REGULADO_TERCEIRO | char(1) |  |  | Agente Não Regulado - Terceiro |
| MG_NOTA_APROPRIACAO_CREDITO_PRESUMIDO_ICMS | char(1) |  |  | MG - Nota de apropriação de crédito presumido de ICMS (S/N) |
| SE_OPERACAO_VINCULADA_PSDI | char(1) |  |  | Operação não vinculada ao PSDI - Programa Sergipano de Desenvolvimento Industrial |
| SC_ESTORNAR_DEBITO_ICMS_INDEVIDO | char(1) |  |  | Estornar débito de ICMS destacado e lançado indevidamente |
| SC_ESTORNAR_DEBITO_ICMS_INDEVIDO_TIPO | integer(4) |  | S | Estornar débito de ICMS destacado e lançado indevidamente - Tipo |
| MG_ESTORNAR_CREDITO_ICMS_CREDITO_PRESUMIDO | char(1) |  |  | MG - Estornar créditos de ICMS nas operações com crédito presumido |
| MG_ESTORNAR_CREDITO_ICMS_CREDITO_PRESUMIDO_TIPO | integer(4) |  | S | MG - Estornar créditos de ICMS nas operações com crédito presumido - Tipo |
| RS_NOTA_APROP_CREDITO_ICMS_EMP_SN_TIPO | integer(4) |  | S | RS - Nota de aproveitamento de crédito - Tipo |
| SC_TIPO_ATIVIDADE_VALOR_ADICIONADO_DIME | integer(4) |  | S | SC - Tipo de atividade do Valor Adicionado - DIME |
| CE_CREDITO_PRESUMIDO | char(1) |  |  | CE - Gerar crédito presumido na apuração (S/N) |
| CE_CREDITO_PRESUMIDO_TIPO | integer(4) |  | S | CE - Gerar crédito presumido na apuração - Tipo |
| CE_ESTORNAR_CREDITO_ICMS | char(1) |  |  | CE - Estornar créditos de ICMS nas operações com crédito presumido |
| CE_ESTORNAR_CREDITO_ICMS_TIPO | integer(4) |  | S | CE - Estornar créditos de ICMS nas operações com crédito presumido - Tipo |
| DF_OPERACAO_VINCULADA_REGIME_ESPECIAL_LEI_5005 | char(1) |  |  | DF - Operação vinculada ao Regime Especial (S/N) |
| MS_CREDITO_PRESUMIDO | char(1) |  |  | MS - Gerar crédito presumido na apuração (S/N) |
| MS_CREDITO_PRESUMIDO_TIPO | integer(4) |  |  | MS - Gerar crédito presumido na apuração - Tipo |
| MS_ESTORNAR_CREDITO_ICMS | char(1) |  |  | MS - Estornar créditos de ICMS nas operações de crédito presumido (S/N) |
| MS_ESTORNAR_CREDITO_ICMS_TIPO | integer(4) |  |  | MS - Estornar créditos de ICMS nas operações de crédito presumido - Tipo |
| MS_OPER_VINCULADA_BENEFICIO_PROGRAMA_FOMENTO | char(1) |  |  | MS - Operação vinculada ao benefício do Programa de Fomento à Industrialização - Lei Comp. nº 93/2001 |
| MG_NOTA_APROPRIACAO_CREDITO_ICMS_POR_ICMSA | char(1) |  |  | MG - Nota de apropriação de crédito de ICMS pelo recolhimento do ICMS Antecipado |
| PR_ESTORNAR_VALOR_ICMS_CREDITO_ART_71 | char(1) |  |  | PR - Operações de saída com Isenção/Redução BC - Estornar valor do ICMS creditado |
| CODIGO_MUNICIPIO_DESTINO | integer(4) |  | S | Código do município destino |
| RJ_OPERACAO_BENEFICIO_DUB_ICMS | char(1) |  |  | RJ - Operação com outros benefícios para informação no DUB-ICMS (S/N) |
| RJ_OPERACAO_BENEFICIO_DUB_ICMS_I_DUB_ICMS | integer(4) |  | S | RJ - Operação com outros benefícios para informação no DUB-ICMS - Código |
| RO_GERAR_CREDITO_PRESUMIDO_APURACAO | char(1) |  |  | RO - Gerar crédito presumido na apuração |
| RO_GERAR_CREDITO_PRESUMIDO_APURACAO_TIPO | integer(4) |  |  | RO - Gerar crédito presumido na apuração - Tipo |
| MT_OPERACAO_CREDITO_ICMS_ESTIMATIVA_SIMPLIFICADO | char(1) |  |  | MT - Operação com direito ao crédito do ICMS pelo regime de estimativa simplificado |
| PE_CALCULAR_PRODEPE | char(1) |  |  | PE - Calcular PRODEPE (S/N) |
| RJ_ESTORNAR_CREDITO_ICMS_PROP_ISENTA_NAO_TRIB | char(1) |  |  | Estornar crédito de ICMS proporcional a saída ou prestação de serviço isenta/não tributada |
| SC_APROPRIAR_CREDITO_DEVOLUCAO_SUBTRI | char(1) |  |  | SC - Apropriar o crédito por devolução sujeita à Subt. Trib. An. 3, art. 23, no imposto |
| SC_APROPRIAR_CREDITO_DEVOLUCAO_SUBTRI_TIPO | integer(4) |  | S | SC - Apropriar o crédito por devolução sujeita à Subt. Trib. An. 3, art. 23, no imposto - Imposto |
| PE_GERA_CREDITO_PRESUMIDO | char(1) |  |  | PE -  Gerar crédito presumido na apuração |
| PE_GERA_CREDITO_PRESUMIDO_TIPO | integer(4) |  |  | PE -  Gerar crédito presumido na apuração - Tipo |
| PA_PRODUTOS_SUJEITOS_ST_SAIDA_TIPO | integer(4) |  | S | PA - Saídas - Operação com produtos sujeitos ao regime de substituição tributária(1/2/3/4) |
| PA_PRODUTOS_SUJEITOS_ST_ENTRADA_INTERNA_TIPO | integer(4) |  | S | PA - Entradas Internas - Operação com produtos sujeitos ao regime de substituição tributária (1/2/3/4/5) |
| PA_PRODUTOS_SUJEITOS_ST_ENTRADA_INTERESTAD_TIPO | integer(4) |  | S | PA - Entradas Interestaduais - Operação com produtos sujeitos ao regime de substituição tributária (1/2/3/5) |
| TO_CREDITO_PRESUMIDO_ICMS_APURADO | char(1) |  |  | TO - Gerar crédito presumido na apuração (S/N) |
| TO_CREDITO_PRESUMIDO_ICMS_APURADO_TIPO | integer(4) |  |  | TO - Gerar crédito presumido na apuração - Tipo |
| PR_APROP_CRED_ICMS_INSUMOS_PREST_SERV_TRANSP | char(1) |  |  | PR - Apropriar crédito de ICMS sobre insumos |
| SE_GERAR_CFOP_ESTENDIDO | char(1) |  |  | SE - Gerar CFOP estendido |
| SE_GERAR_CFOP_ESTENDIDO_CODIGO | integer(4) |  | S | SE - Gerar CFOP estendido - Código |
| RECEITA_DIFERIDA_IRPJ_CSLL_IN_247_2002 | char(1) |  |  | Receita diferida para as contribuições do IRPJ e CSLL - Art. 25 da IN 247/2002 |
| PB_GERAR_CREDITO_PRESUMIDO | char(1) |  |  | PB - Gerar crédito presumido na apuração (S/ N) |
| PB_GERAR_CREDITO_PRESUMIDO_TIPO | integer(4) |  |  | PB - Gerar crédito presumido na apuração - Tipo |
| EXCLUIR_VALORES_PROPAGANDA_PUBLICIDADE_DA_BASE | char(1) |  |  | Excluir da base de cálculo os valores repassados pelas agências de propaganda a empresas de rádio, televisão e outros |
| CT_PROPAGANDA_PUBLICIDADE | integer(4) |  | S | Conta agências de propaganda a empresas de rádio, televisão e outros |
| CH_PROPAGANDA_PUBLICIDADE | integer(4) |  | S | Histórico agências de propaganda a empresas de rádio, televisão e outros |
| SC_OPERACAO_RESSARC_ICMS_ST_APROV_I_RECOLHIMENTO | integer(4) |  | S | SC - Operação Ressarcimento ICMS ST Aproveitar |
| SC_OPERACAO_RESSARC_ICMS_ST_APROV_CODIGO_RECOLHIMENTO | char(6) |  | S | SC - Operação Ressarcimento ICMS ST Aproveitar Código Recolhimento |
| SC_CONSIDERAR_DEVOLUCAO_NO_SEITEC | char(1) |  |  | SC - Considerar valor de ICMS da devolução de compras no cálculo do SEITEC |
| MT_DETALHAR_VALORES_ISENTOS_ICMS | char(1) |  |  | MT - Detalhar valores isentos de ICMS |
| MT_DETALHAR_VALORES_ISENTOS_ICMS_CODIGO | integer(4) |  | S | MT - Detalhar valores isentos de ICMS - Código |
| CT_DESCONTO | integer(4) |  | S | Conta do desconto das notas |
| CH_DESCONTO | integer(4) |  | S | Histórico do desconto das notas |
| CT_ACRESCIMO | integer(4) |  | S | Conta de acréscimo das notas |
| CH_ACRESCIMO | integer(4) |  | S | Histórico de acréscimo das notas |
| RJ_CREDITO_PRESUMIDO_ACU | char(1) |  |  | RJ - Gerar crédito presumido na apuração |
| RJ_TABELA_CREDITO_PRESUMIDO_ACU | integer(4) |  | S | RJ - Gerar crédito presumido na apuração - Crédito |
| RJ_ESTORNAR_CREDITO_ICMS_CREDITO_PRESUMIDO | char(1) |  |  | RJ - Gerar estorno de crédito presumido na apuração |
| RJ_ESTORNAR_CREDITO_ICMS_CREDITO_PRESUMIDO_TIPO | integer(4) |  | S | RJ - Gerar estorno de crédito presumido na apuração - Crédito |
| DF_OPER_VINCULADA_CRED_PRESUMIDO_20_TRANSP_ICMS | char(1) |  |  | Operação vinculada ao Crédito presumido de 20% para transportadoras - Convênio ICMS 106/96 |
| CONTROLA_LANCAMENTOS | char(1) |  |  | Lançar somente em (S/N) |
| LANCAR_SOMENTE_ENTRADA | char(1) |  |  | Lançar somente em Entrada (S/N) |
| LANCAR_SOMENTE_SAIDA | char(1) |  |  | Lançar somente em Saída (S/N) |
| LANCAR_SOMENTE_SERVICO | char(1) |  |  | Lançar somente em Serviço (S/N) |
| LANCAR_SOMENTE_REDUCAO_Z | char(1) |  |  | Lançar somente em Reduções Z - Modelo 2D (S/N) |
| LANCAR_SOMENTE_REDUCAO_Z_BILHETE | char(1) |  |  | Lançar somente em Reduções Z - Bilhetes de Passagens (S/N) |
| LANCAR_SOMENTE_CFE | char(1) |  |  | Lançar somente em Cupom Fiscal Eletrônico - CF-e (S/N) |
| LANCAR_SOMENTE_RMD | char(1) |  |  | Lançar somente em Resumo de Movimento Diário - Modelo 18 (S/N) |
| LANCAR_SOMENTE_BILHETE | char(1) |  |  | Lançar somente em Bilhetes de Passagens (S/N) |
| LANCAR_SOMENTE_OUTROS | char(1) |  |  | Lançar somente em Outros (S/N) |
| RS_EXCLUSOES_PARCIAIS_CFOP_NA_GIA | char(1) |  |  | Exclusões parciais de CFOPs na GIA (S/N) |
| RS_EXCLUSOES_PARCIAIS_CFOP_NA_GIA_ESPECIFICACAO | varchar(60) |  |  | Exclusões parciais de CFOPs na GIA - Especificação |
| AM_CREDITO_ESTIMULO_ICMS_ART_13_LEI_2826_03 | char(1) |  |  | AM - Calcular incentivo fiscal do Crédito Estímulo do ICMS |
| PR_SAIDA_COM_DIREITO_RESSARCIMENTO_ICMS_ST | char(1) |  |  | PR - Calcular ressarcimento de ICMS ST nas vendas interestaduais |
| INFORMAR_ICMS_DESONERADO | char(1) |  |  | Informar os dados do ICMS desonerado |
| VENDAS_POR_MEIO_REVENDEDORES_AMBULANTES_AUTONOMOS | char(1) |  |  | Vendas por meio de revendedores ambulantes autônomos (S/N) |
| GERAR_LANCAMENTO_CONTA_COMPENSACAO | char(1) |  |  | Gerar lançamento na conta de compensação |
| COMPENSACAO_CONTA_DEBITO | integer(4) |  | S | Conta débito - Compensação |
| COMPENSACAO_CONTA_CREDITO | integer(4) |  | S | Conta crédito - Compensação |
| COMPENSACAO_HISTORICO | integer(4) |  | S | Histórico - Compensação |
| DEDUZIR_PEDAGIO_BASE_CALCULO_ICMS | char(1) |  |  | Deduzir o valor do pedágio da base de cálculo do ICMS nas operações de transporte (S/N) |
| CT_FRETE | integer(4) |  | S | Conta - Frete |
| CH_FRETE | integer(4) |  | S | Histórico - Frete |
| CT_SEGURO | integer(4) |  | S | Conta - Seguro |
| CH_SEGURO | integer(4) |  | S | Histórico - Seguro |
| CT_DESPESAS_ACESSORIAS | integer(4) |  | S | Conta - Despesas Acessórios |
| CH_DESPESAS_ACESSORIAS | integer(4) |  | S | Histórico - Despesas Acessórios |
| CT_PEDAGIO | integer(4) |  | S | Conta - Pedágio |
| CH_PEDAGIO | integer(4) |  | S | Histórico - Pedágio |
| MG_APROVEITAMENTO_CREDITO_ICMS_485515 | char(1) |  |  | Nota de aproveitamento de crédito de ICMS - Res. 4.855/15 (S/N) |
| MG_APROVEITAMENTO_CREDITO_ICMS_485515_TIPO | integer(4) |  |  | Nota de aproveitamento de crédito de ICMS - Res. 4.855/15 - Tipo (1/2/3/4) |
| RO_APROVEITAMENTO_ICMS_ESTOQUE_EXCLUIDO_2070916 | char(1) |  |  | Nota de aproveitamento de crédito de ICMS sobre estoque mercadoria excluída da Subst. Tributária - Decreto 20.709/16 (S/N) |
| MG_NOTA_ESTORNO_CREDITO_ICMS_ART_73 | char(1) |  |  | MG - Estorna créditos ICMS nas operações crédito presumido |
| ES_COMERCIAL_ATACADISTA_OPERACAO_CONTEMPLADA | char(1) |  |  | Enquadramento no benefício fiscal estabelecimento Comercial Atacadista - S/Contempla - N/Fora |
| ES_COMERCIAL_ATACADISTA_OPERACAO_SAIDA_PARTICIPA_RATEIO | char(1) |  |  | Saída fora do benefício fiscal com participação na proporção do rateio dos créditos |
| MG_CALCULAR_CREDITO_PRESUMIDO_SOBRE_VALOR_OPER_NOTAS_REDUCAO_BC_ANEXO_IV | char(1) |  |  | Calcular o créd. presumido sobre o valor da operação para notas com Redução B. de Cálculo - Anexo IV, Parte 1, item 20 |
| CONSIDERAR_RECEITA_TOTAL_BASE_CALCULO_INSS_RB | char(1) |  |  | Considerar a receita total na base de cálculo do INSS Receita Bruta |
| SC_ESTORNAR_CREDITOS_OPERACAO_SAIDA_MERCADORIAS_TTDS_409_410_411 | char(1) |  |  | Estornar créditos de ICMS nas operações com mercadorias alcançadas pelos TTDS 409, 410 ou 411 |
| DEDUZIR_DESPESAS_ACESSORIAS_BASE_IRPJ_CSLL | char(1) |  |  | Deduzir o valor de despesas acessórias da base do IRPJ e CSLL |
| ONUS_IRRF_ASSUMIDO_PELA_FONTE_PAGADORA | char(1) |  |  | Ônus do IRRF devido pelo beneficiário assumido pela fonte pagadora |
| SP_OPERACAO_RESSAR_ICMS_PORT_CAT_158_2015 | char(1) |  |  | Operação com ressarcimento de ICMS conforme Portaria CAT 158/2015 |
| SP_OPERACAO_RESSAR_ICMS_PORT_CAT_158_2015_TIPO | char(1) |  |  | Operação com ressarcimento de ICMS conforme Portaria CAT 158/2015 - Valores |
| DF_CODIGO_SERVICO_CONFORME_LC_116_03 | char(1) |  |  | Código do Serviço conforme LC nº 116/03 |
| DF_CODIGO_SERVICO_CONFORME_LC_116_03_CODIGO | integer(4) |  | S | Código do Serviço conforme LC nº 116/03 - Código |
| EFD_REINF_TIPO_SERVICO | varchar(10) |  | S | EFD Reinf - Tipo de seviço |
| ES_POSSUI_BENEFICIO_BARES_RESTAURANTES | char(1) |  |  | Operação com Benefício Bares, Rest. Refeições coletivas e similares - Art. 530-LRF RICMS |
| ES_POSSUI_BENEFICIO_BARES_RESTAURANTES_ESTORNAR_CREDITO | char(1) |  |  | Estornar crédito de ICMS - Benefício Bares, Rest. Refeições coletivas e similares - Art. 530-LRF RICMS |
| GO_APROVEITAR_CREDITO_ICMS_ST_DEVOLUCAO | char(1) |  |  | Aproveitar o crédito do ICMS ST nas devoluções de vendas conforme Art. 47, § 3º - Anexo VIII do RCTE |
| RS_OPERACAO_RESTITUICAO_ICMS_ST_PAGO_ETAPAS_ANTERIORES | char(1) |  |  | Operação de saída com direito à restituição do ICMS Substituição Tributária pago nas etapas anteriores |
| CE_CREDITO_PRESUMIDO_20_TRANSPORTADORA_ICMS | char(1) |  |  | CE - Operação não vinculada ao crédito presumido de 20% para trasportadoras - Convênio ICMS 106/96 |
| RJ_CREDITO_ICMS_NAO_APROPRIADO | char(1) |  |  | RJ - Crédito ref. ao ICMS próprio não apropriado na aquisição de merc. sujeita ao ICMS-ST devolvida |
| RJ_COMPRA_COM_ST_SEM_CONVENIO_PROTOCOLO | char(1) |  |  | RJ - Compra de mercadoria sujeita ao regime de substituição tributária sem convênio/protocolo com o estado de origem |
| SP_OPERACAO_CREDITO_OUTORGADO_EMPRESAS_TEXTEIS | char(1) |  |  | SP - Operação com crédito outorgado para empresas têxteis - Cap. IV, Anexo III, Art. 41 do RICMS |
| SC_HABILITA_DIGITACAO_EXCLUSAO_DIME | char(1) |  |  | SC - Habilitar digitação de Exclusões na DIME |
| ES_OPERACAO_INCLUIDA_MOVIMENTACAO_CAFE_CRU | char(1) |  |  | ES - Operação incluída na movimentação de Café Cru |
| MA_GERAR_CREDITO_PRESUMIDO | char(1) |  |  | MA - Gerar crédito presumido na apuração |
| MA_GERAR_CREDITO_PRESUMIDO_TIPO | integer(4) |  | S | MA - Gerar crédito presumido na apuração - Tipo |
| MA_ESTORNAR_CREDITO_PRESUMIDO | char(1) |  |  | MA - Estornar créditos de ICMS nas operações de crédito presumido |
| MA_ESTORNAR_CREDITO_PRESUMIDO_TIPO | integer(4) |  | S | MA - Estornar créditos de ICMS nas operações de crédito presumido - Tipo |
| AC_OPERACAO_RESSARCIMENTO_DECRETO_6875_2017 | char(1) |  |  | AC - Operação com ressarcimento conforme seção IV do decreto 6.875/2017 |
| AC_OPERACAO_RESSARCIMENTO_DECRETO_6875_2017_TIPO | char(1) |  |  | AC - Operação com ressarcimento conforme seção IV do decreto 6.875/2017 - Tipo |
| SC_CREDITO_ENERGIA_ELETRICA_LAUDO_TECNICO_PERCENTUAL | numeric(15) |  | S | SC - Crédito de energia elétrica com base em laudo técnico |
| CONFIGURAR_IMPORTACAO_PARA_CALCULO_COEFICIENTE_CREDITO_ICMS | char(1) |  |  | Configurar importação para cálculo de coeficiente de crédito de ICMS |
| IMPORTAR_SAIDAS_TRIBUTADAS_VALOR_CONTABIL | char(1) |  |  | Importar saidas tributadas valor contábil |
| IMPORTAR_SAIDAS_TRIBUTADAS_VALOR_BASE_CALCULO | char(1) |  |  | Importar saidas tributadas valor base de cálculo |
| IMPORTAR_SAIDAS_TRIBUTADAS_VALOR_IPI | char(1) |  |  | Importar saidas tributadas valor IPI |
| IMPORTAR_SAIDAS_TRIBUTADAS_VALOR_ICMS_ST | char(1) |  |  | Importar saidas tributadas valor ICMS ST |
| IMPORTAR_SAIDAS_TRIBUTADAS_VALOR_OUTRAS | char(1) |  |  | Importar saidas tributadas valor outras |
| IMPORTAR_SAIDAS_ISENTAS_VALOR_ISENTAS | char(1) |  |  | Importar saidas isentas velor isentas |
| IMPORTAR_SAIDAS_ISENTAS_VALOR_IPI | char(1) |  |  | Importar saidas isentas valor IPI |
| IMPORTAR_SAIDAS_ISENTAS_VALOR_ICMS_ST | char(1) |  |  | Importar saidas isentas valor ICMS ST |
| IMPORTAR_SAIDAS_ISENTAS_VALOR_OUTRAS | char(1) |  |  | Importar saidas isentas valor outras |
| GO_CREDITO_PRESUMIDO_20_TRANSPORTADORA_ICMS | char(1) |  |  | GO -  Operação não vinculada ao crédito presumido de 20% para transportadoras - Convênio ICMS 106/96 |
| NOTA_ENTRADA_PROF_PARC_DEDUZIR_RECEITA | char(1) |  |  | Nota de entrada emitida pelo profissional-parceiro para deduzir da receita |
| NOTA_SAIDA_SERVICO_DEDUCAO_VALOR_REPASSADO_PROF_PARC | char(1) |  |  | Nota de saída/serviço com dedução do valor repassado ao profissional-parceiro |
| POSSUI_PAJ_TIPO_ACU | char(1) |  |  | Tipo Processo Administrativo Judicial |
| POSSUI_PAJ_ACU | char(1) |  |  | Possui Processo Administrativo Judicial |
| SEQUENCIAL_PAJ_ACU | integer(4) |  | S | Sequencial Processo Administrativo Judicial |
| SEQUENCIAL_PAJ_SE_ACU | integer(4) |  | S | Sequencial da Suspensão de Exigibilidade |
| SP_RESSARCIMENTO_ICMS_PORT_CAT_42_2018 | char(1) |  |  | Ressarcimento ou complemento do ICMS - CAT 42/2018 |
| SP_RESSARCIMENTO_ICMS_PORT_CAT_42_2018_TIPO | integer(4) |  |  | Ressarcimento ou complemento do ICMS - CAT 42/2018  - Tipo |
| SC_CREDITO_ENERGIA_ELETRICA_LAUDO_TECNICO_PERCENTUAL_TIPO | integer(4) |  |  | Crédito de energia elétrica com base em laudo técnico |
| ES_OPERACAO_INTERESTADUAL_NAO_PRESENCIAL_CONSUMIDOR_FINAL_ART_530 | char(1) |  |  | Operação interestadual não presencial a consumidor final - Art. 530-LRI RICMS |
| GO_OPERACAO_SUJEITA_DIFERENCIAL_ALIQUOTA_ART3_DECRETO_9162_2018 | char(1) |  |  | Operação sujeita ao Diferencial de alíquota conf. Art. 3º, I do Decreto nº 9.162/2018 |
| SC_TRIBUTACAO_EFETIVA | char(1) |  |  | SC - Tributação efetiva (P-Parâmetros/I-Informar) |
| EFD_REINF_INDICATIVO_PRESTACAO_SERVICOS | integer(4) |  | S | Indicativo de Prestação de Serviço |
| RS_CONSIDERAR_CALCULAR_RESSARC_COMP_ICMS_ST | char(1) |  |  | RS - Considerar calcular ressarcimento/complemento do ICMS ST-livro lll |
| CT_IPI_ENTRADA | integer(4) |  | S | Conta IPI entrada |
| CH_IPI_ENTRADA | integer(4) |  | S | Historico IPI entrada |
| CT_ICMS_ST_ENTRADA | integer(4) |  | S | Conta ICMS ST entrada |
| CH_ICMS_ST_ENTRADA | integer(4) |  | S | Historico ICMS ST entrada |
| INFORMAR_ICMS_DESONERADO_TIPO | char(1) |  |  | Informar ICMS desonerado( D- Deduzir do valor contábil/ N- Não deduzir do valor contábil) |
| SC_OPERACAO_VENDA_CALCULAR_REST_COMP_RESSARC_ICMS_ST | char(1) |  |  | SC - Operação de venda incluída no cálculo da restituição, complemento e ressarcimento do ICMS ST (DRCST) |
| SC_NOTA_ACOBERTA_RESSARC_ICMS_ST | char(1) |  |  | SC - Nota de acobertamento do ressarcimento de ICMS substituição tributária |
| SP_CONSIDERAR_CALCULO_RESSARCIMENTO_ICMS_PORT_CAT_42_18 | char(1) |  |  | Não considerar no cálculo do ressarcimento/complemento do ICMS ST - Portaria CAT 42/18 |
| DEDUZIR_VALOR_PEDAGIO_BASE_CALCULO_PIS_COFINS | char(1) |  |  | Dedzuir valor do pedagio na base de calculo do Pis/Cofins(S/N) |
| RS_OPER_INC_OUTROS_DEBITOS_ICMS_SUSPENSAO_DIF_SAIDAS_CONTRIB_REF | char(1) |  |  | Operação com incidência de Outros Débitos de ICMS, pela suspensão do diferimento nas saídas a contribuinte do REF |
| MG_CALCULAR_COMPLEMENTO_RESTITUICAO_ICMS_ST_CONFORME_ART31 | char(1) |  |  | MG - Calcular o complemento/restituição do ICMS ST conforme Art. 31-A a 31-I, Anexo XV do RICMS |
| MG_NOTA_COMPLEMENTO_RESTITUICAO_ICMS_ST_CONFORME_ART31 | char(1) |  |  | MG - Nota de complemento/restituição de ICMS ST conforme Art. 31-F, Anexo XV do RICMS |
| PR_CREDITO_PRESUMIDO_20_TRANSPORTADORA_ICMS | char(1) |  |  | Operação vinculada ao crédito presumido de 20% para transportadoras - Convênio ICMS 106/96 e 85/03 |
| AP_UTILIZAR_ICMS_DESONERADO_COMO_CREDITO_PRESUMIDO_ALCMS | char(1) |  |  | Utilizar o ICMS Desonerado como crédito presumido da ALCMS na apuração do imposto ICMS - Art. 278 do RICMS |
| SOMAR_VALOR_FUNSOMAR_VALOR_FUNDO_PROBREZA_DIFERENCIAL_ALIQ_VALOR_BEM | char(1) |  |  | Somar valor fundo probreza valor do bem |
| SP_AQUISICAO_DIREITO_CRED_OPER_FORNECI_ALIMENTACAO | char(1) |  |  | SP - Aquisição com direito ao crédito nas operações com fornecimento de alimentação - Art. 1º, § 4º do Dec. 51.597/07 |
| SP_OPER_SAIDA_REGIME_ESP_TRIBUTA_ICMS_FORNECI_ALIMENTACAO | char(1) |  |  | SP - Operação de saída com regime especial de tributação do ICMS no fornecimento de alimentação - Dec. 51.597/07 |
| SP_GERAR_INFORMACOES_QUADRO_3_1_OU_3_5_DIPAM | char(1) |  |  | SP - Gerar informações no quadro 3.1 ou 3.5 na guia DIPAM-B da Nova Gia |
| RS_HIPOTESE_RESSARCIMENTO | integer(4) |  |  | RS - Hipótese de ressarcimento |
| BA_CALCULAR_ESTORNO_CREDITO_ICMS_ART_312 | char(1) |  | S | Calcular estorno de crédito nas saídas isentas ou não tributadas - Art. 312, I do RICMS |
| GO_OPERACAO_VINCULADA_ESTORNO_CREDITO_CONFORME_IN_1237 | char(1) |  |  | GO - Operação não vinculada ao estorno de crédito conforme IN 1.237/15-GSF |
| SE_ESTORNAR_CREDITO_ICMS_OPERACOES_NAO_ALCANCADAS_TARE | char(1) |  |  | Estornar créditos de ICMS nas operações não alcançadas pelo TARE |
| PR_OPERACAO_VENDA_INC_CALC_RECUP_RESSARC_COMPTO_ICMS_ST | char(1) |  |  | PR - Operação de venda incluída no cálculo da recuperação, ressarcimento e complementação do ICMS-ST (ADRC-ST) |
| PR_OPERACAO_SAIDA_INTERNA | char(1) |  |  | PR - Operação de saída interna que trata o art. 119 do Anexo IX do RICMS/17 |
| SC_NOTA_ACOBERTA_RESSARC_ICMS_ST_IMPOSTO | integer(4) |  |  | SC - Nota de acobertamento do ressarcimento de ICMS substituição tributária (9 - SUBTRI / 31 - STAT) |
| MA_CONSIDERAR_OPER_CALC_CRED_PRES_ESTAV_ATACADISTA | char(1) |  |  | MA - Não considerar operação no cálculo do Créd. Pres. Estabelecimento Atacadista - Anexo 1.5, Art. 8 do RICMS |
| MT_OPERACAO_VINCULADA_CREDITO_OUTORGADO_ESTAB_COMER_VAREJISTA | char(1) |  |  | MT - Operação não vinculada ao crédito outorgado estabelecimento comercial varejista - Art. 2°, I, Anexo XVII do RICMS |
| DEDUZIR_VALOR_DESPESAS_ACESSORIAS_BASE_CALCULO_PIS_COFINS | char(1) |  |  | Deduzir valor despesas acessoriais base de calculo PIS COFINS |
| RO_OPERACAO_RESSARCIMENTO_ART_20_ANEXO_VI | char(1) |  |  | RO - Operação de saída com direito ao ressarcimento de ICMS - Art. 20 do Anexo VI do RICMS |
| RN_CALCULAR_REGIME_ESPECIAL_TRIB_ICMS_CONTRIB_ATACADISTAS | char(1) |  |  | Calcular o regime especial de tributação do ICMS aos contribuintes atacadistas - Decreto 22.199/11 |
| RN_COMPRAS_REGIME_ESPECIAL_DIREITO_A_CREDITO | char(1) |  |  | Compras no regime especial com direito a crédito - Decreto 22.199/11 |
| RN_COMPRAS_REGIME_ESPECIAL_DIREITO_A_CREDITO_TIPO | char(1) |  |  | Compras no regime especial com direito a crédito - Decreto 22.199/11 - Tipo |
| AC_UTILIZAR_ICMS_DESONERADO_COMO_CREDITO_PRESUMIDO | char(1) |  |  | AC - Utilizar o ICMS Desonerado como crédito presumido da ALCB e ALCCS na apuração do imposto ICMS - Art. 45 do RICMS |
| MG_MOTIVO_TRANSFERENCIA_CFE_RES_4757_2015 | char(1) |  |  | TIPO DE UTILIZAÇÃO DO CRÉDITO CFE RES. Nº 4.757/2015 |
| MG_MOTIVO_TRANSFERENCIA_CFE_RES_4757_2015_TIPO | integer(4) |  | S | TIPO DE UTILIZAÇÃO DO CRÉDITO CFE RES. Nº 4.757/2015 - TIPO |
| MG_ORIGEM_CREDITO_CFE_RES_4757_2015 | char(1) |  |  | MG - Origem do crédito cfe Resolução nº 4.757/2015 |
| MG_ORIGEM_CREDITO_CFE_RES_4757_2015_TIPO | integer(4) |  | S | MG - Origem do crédito cfe Resolução nº 4.757/2015 - Tipo |
| RJ_ESTORNAR_CREDITO_ICMS_PROP_POSSUIR_RED_BC | char(1) |  |  | RJ - Estornar crédito de ICMS proporcional a saída com redução da base de cálculo (Cesta básica) - Dec. 32.161/02 |
| CT_CREDITO_AQUISICAO_EMPRESA_SIMPLESN | integer(4) |  | S | Conta Crédito na aquisição de empresas do Simples Nacional |
| HT_CREDITO_AQUISICAO_EMPRESA_SIMPLESN | integer(4) |  | S | Histórico Crédito na aquisição de empresas do Simples Nacional |
| PR_APROVEITAR_VALOR_IMPOSTO_ST_CREDITO_ICMS | char(1) |  |  | PR - Aproveitar o valor do imposto Substituição Tributária como crédito no imposto ICMS |
| INFORMAR_DADOS_CONTRATO_LOCACAO_INTERMEDIACAO | char(1) |  |  | Informar dados Locação/Intermediação (S/N) |
| TIPO_CONTRATO_LOCACAO_INTERMEDIACAO | char(1) |  |  | Tipo do contrato Locação/Intermediação (L/I) |
| MT_CONSIDERAR_TRANSFERENCIA_CREDITO_PRESUMIDO_PRODEIC | char(1) |  |  | MT - Considerar notas de transferência no cálculo do crédito presumido PRODEIC (S/N) |
| CONFIGURAR_RATEIO_CENTRO_CUSTO | char(1) |  |  | Configurar rateio do centro de custos |
| PR_GERAR_CREDITO_ICMSA_APURACAO_ICMS | char(1) |  |  | PR - Gerar crédito de ICMS Antecipado na apuração do imposto ICMS |
| SP_CREDITO_PRESUMIDO_20_TRANSPORTADORA_ICMS | char(1) |  |  | SP - Operação não vinculada ao crédito presumido de 20% para transportadoras - Convênio ICMS 106/96 |
| SC_CREDITO_TRANSPORTADOR_AQUISICAO_MERCADORIA_USO_CONSUMO_ART_29 | char(1) |  |  | SC - Gerar crédito ao transportador nas aquisições de mercadoria para uso e consumo - Art. 29, § 8º do RICMS |
| BA_CREDITO_PRESUMIDO_20_SOBRE_ICMS_ST_TRANS | char(1) |  |  | BA - Calcular o crédito presumido de 20% sobre o imposto ICMS ST Transportes |
| MG_CALCULAR_RESTITUICAO_ICMS_ST_ART_23 | char(1) |  |  | MG - Calcular a restituição do ICMS ST conforme Art. 23, Anexo XV do RICMS |
| MG_CALCULAR_RESTITUICAO_ICMS_ST_ART_23_TIPO | integer(4) |  |  | MG - Calcular a restituição do ICMS ST conforme Art. 23, Anexo XV do RICMS - Tipo |
| MG_NOTA_FISCAL_RESTITUICAO_ICMS_ST | char(1) |  |  | MG - Nota fiscal de restituição do ICMS ST |
| MG_NOTA_FISCAL_RESTITUICAO_ICMS_ST_TIPO | integer(4) |  |  | MG - Nota fiscal de restituição do ICMS ST - Tipo |
| SOMAR_FRETE_SEGURO_DESPESAS_ACESSORIAS_BASE_CALCULO_PIS_COFINS | char(1) |  |  | Somar o valor de frete, seguro e despesas acessórias na base de cálculo de PIS e COFINS |
| CONSIDERAR_RECEITA_EXPORTACAO_NAO_RELACIONADA_CALCULO_PERCENTUAL_INSS_RECEITA_BRUTA | char(1) |  |  | Considerar receitas de exportação como não relacionadas para o cálculo do percentual do INSS Receita Bruta |
| SC_ESTORNAR_DEBITO_DEVOLUCAO_SEM_APROVEITAMENTO | char(1) |  |  | Estornar débito de devolução cuja entrada ocorreu sem o aproveitamento total ou parcial no imposto |
| SC_ESTORNAR_DEBITO_DEVOLUCAO_SEM_APROVEITAMENTO_TIPO | integer(4) |  | S | Estornar débito de devolução cuja entrada ocorreu sem o aproveitamento total ou parcial no imposto - Tipo |
| DESCONSIDERAR_IPI_ICMSST_VALOR_RECEITA_PIS_COFINS | char(1) |  |  | Desconsiderar o valor de IPI e ICMS ST do valor da receita do PIS e COFINS |
| DF_OPERACAO_INCLUIDA_CALCULO_REGIME_ESPECIAL_FRIGORIFICOS_ART_320 | char(1) |  |  | Operação incluída no cálculo do regime especial de Frigoríficos/Abatedouros - Art. 320-D do RICMS |
| SIMPLESN_DEDUZIR_DESPESAS_ACESSORIAS_DEVOLUCAO_DE_VENDA | char(1) |  |  | Deduzir o valor de despesas acessórias na devolução de venda para o cálculo do Simples Nacional |
| MG_CREDITO_PRESUMIDO_TRANSPORTE_RODOVIARIO | char(1) |  |  | Calcular o crédito presumido para empresas de transporte rodoviário |
| MG_CREDITO_PRESUMIDO_TRANSPORTE_RODOVIARIO_TIPO | integer(4) |  | S | Calcular o crédito presumido para empresas de transporte rodoviário tipo |
| ES_BENEFICIO_FISCAL_VENDAS_INTERESTADUAIS_IND_METALMECANICA | char(1) |  |  | ES - Operação interestadual com benefício fiscal realizada por indústria metalmecânica - Art. 530-LF RICMS |
| SC_CREDITO_PRESUMIDO_20_TRANSPORTADORA_ICMS | char(1) |  |  | SC - Operação não vinculada ao crédito presumido de 20% para transportadoras |
| MG_NOTA_FISCAL_ESTORNO_DEBITO_ICMS_REDUCAO_Z_SUJEITAS_RET | char(1) |  |  | MG - Nota fiscal de estorno de débito de ICMS das reduções Z sujeitas ao RET |
| MG_NOTA_FISCAL_ESTORNO_DEBITO_ICMS_REDUCAO_Z_SUJEITAS_RET_TIPO | integer(4) |  |  | Nota fiscal de estorno de débito de ICMS das reduções Z sujeitas ao RET - Apuração normal para: (1-Apuração 1/2-Apuração 2) |
| RS_REGULARIZACAO_DEBITO_NAO_DESTACADO_DOCUMENTO_FISCAL_DESENQUADRAMENTO_ST | char(1) |  |  | Regularização débito não destacado em documento fiscal - Desenquadramento ST |
| TO_OP_NAO_VINCULADA_CREDITO_PRESUMIDO_20_TRANSPORTADORAS_CONVENIO_ICMS_106_96 | char(1) |  |  | TO - Operação não vinculada ao crédito presumido de 20% para transportadoras - Convênio ICMS 106/96 |
| MT_OPERACAO_SAIDA_REGIME_SIMPLIFICADO_ART_1_XVIII_RICMS | char(1) |  |  | Operacao de saida com regime simplificado de tributacao - Art. 1o, Anexo XVIII do RICMS |
| GO_OPERACAO_INCENTIVADAS_PROGOIAS | char(1) |  |  | GO - Operações incentivadas pelo programa PROGOIÁS |
| CT_DEBITO_SALAO_PARCEIRO | integer(4) |  | S | Conta Débito Salão Parceiro |
| CT_CREDITO_SALAO_PARCEIRO | integer(4) |  | S | Conta Crédiito Salão Parceiro |
| HT_SALAO_PARCEIRO | integer(4) |  | S | Histórico Salão Parceiro |
| RO_CONSIDERAR_NO_CALCULO_INCENTIVO_TRIBUTARIO_CONSIT_12988_2007 | char(1) |  |  | RO - Não considerar no cálculo do incentivo tributário CONSIT - Decreto n° 12.988/2007 |
| PI_REGIME_ESPECIAL_TRIBUTACAO_OPERACOES_PRODUTOS_FARMACEUTICOS_ART_791F | char(1) |  |  | Operação sujeita ao regime especial de tributação com produtos farmacêuticos - Art. 791-F do RICMS |
| DISPENSA_REG_E115_VA_VB_NFCE | char(1) |  | S | Dispensa do registro E115 anexo V.A e V.B da GIA com Oper. NFC-e |
| RN_TRANSFERENCIA_ACU | char(1) |  |  | RN - Nota de transferência de crédito de ICMS |
| ESTORNAR_DEBITO_IMPOSTOS_OPERACOES_CTE_SUBSTITUTO | char(1) |  |  | Estornar débito dos impostos nas operações com CT-e substituto |
| RS_OPERACOES_REMESSA_TRANSPORTES_MERCADORIAS_IMPORTADAS | char(1) |  |  | Operações de remessa para transportes das mercadorias importadas |
| SC_CREDITO_TRANSPORTADOR_INDUSTRIA_AQUISICAO_COMBUST_TRIB_MONOFASICA_ICMS | char(1) |  |  | SC - Gerar crédito ao transportador/indústria aquis. combust. suj. à trib. monofásica do ICMS - Conv. ICMS 199/22 e 15/23 |
| SP_APROVEITAR_CREDITO_ICMS_MONOFASICO_SOB_COMBUSTIVEL_CREDITO_ICMS | char(1) |  |  | SP - Aproveitar o crédito do ICMS monofásico sobre combustíveis como crédito no imposto ICMS |
| RS_GERAR_COMO_CREDITO_VALOR_DE_ANTECIPACAO_NA_APURACAO_DO_MES_SEGUINTE | char(1) |  |  | RS - Não gerar como crédito o valor da antecipação do imposto na apuração do mês seguinte |
| RS_APROVEITAR_CREDITO_ICMS_MONOFASICO_SOB_COMBUSTIVEL_CREDITO_ICMS | char(1) |  |  | RS - Aproveitar o crédito do ICMS monofásico sobre combustíveis como crédito no imposto ICMS |
| RS_NOTA_APROPRIACAO_CREDITO_ICMS_AQUISICAO_COMBUSTIVEIS | char(1) |  |  | RS - Nota de apropriação do credito de ICMS na aquisição de combustíveis para insumo |
| PR_GERAR_CREDITO_ICMS_AQUISICAO_COMBUSTIVEL_INSUMO | char(1) |  |  | PR - Gerar crédito de ICMS na aquisição de combustíveis para insumos - Art. 25, § 4º e § 5º do RICMS |
| RJ_OPERACAO_REG_ESPECIAL_PADARIAS_CONFEITARIAS | char(1) |  |  | RJ - Operação sujeita ao regime especial padarias e confeitarias (S/N) |
| MG_OPERACAO_SUJEITA_CRED_PRESUMIDO_I_SEQUENCIAL_INCENTIVO | integer(4) |  | S | MG - Estornar créditos de ICMS nas operações com crédito presumido - E-PTA-RE nº (Sequencial incentivo) |
| MG_ESTORNAR_CREDITO_ICMS_CREDITO_PRESUMIDO_I_SEQUENCIAL_INCENTIVO | integer(4) |  | S | MG - Operação sujeita ao crédito presumido (S/N) - E-PTA-RE nº (Sequencial incentivo) |
| MG_NOTA_ESTORNO_CREDITO_ICMS_ART_73_I_SEQUENCIAL_INCENTIVO | integer(4) |  | S | MG - Estorna créditos ICMS nas operações crédito presumido - E-PTA-RE nº (Sequencial incentivo) |
| RS_CREDITO_PRESUMIDO_20_TRANSPORTADORA_ICMS_TR | char(1) |  |  | RS - Gerar crédito presumido de 20% para transportadoras na apuração do imposto 98-ICMSA-TR(S/N) |
| MG_APROVEITAR_CREDITO_ICMS_MONOFASICO_SOB_COMBUSTIVEL_CREDITO_ICMS | char(1) |  |  | MG - Aproveitar o crédito do ICMS monofásico sobre combustíveis como crédito no imposto ICMS |
| RJ_CREDITO_PRESUMIDO_20_TRANSPORTADORA_ICMS | char(1) |  |  | RJ -  Operação não vinculada ao crédito presumido de 20% para transportadoras |
| CONSIDERAR_RECEITA_ATIVIDADE_ALCANCADA_PERSE_BASE_CALCULO_ADICIONAL_IRPJ | char(1) |  |  | Desconsiderar as receitas com atividade alcançada pelo Perse na base de cálculo do adicional do IRPJ |
| MA_CREDITO_PRESUMIDO_20_TRANSPORTADORA_ICMS | char(1) |  |  | MA - Operação não vinculada ao crédito presumido de 20% para transportadoras - Convênio ICMS 106/96 |
| DF_ESTORNAR_CREDITO_DEVOLUCAO_REG_ESPECIAL | char(1) |  |  | DF - Estornar crédito das devoluções do Regime Especial - Lei 5.005/2012 |
| DF_ESTORNAR_CREDITO_DEVOLUCAO_REG_ESPECIAL_TIPO | integer(4) |  |  | DF - Estornar crédito das devoluções DO Regime Especial - Lei 5.005/2012_Tipo |
| MS_APROVEITAR_CREDITO_ICMS_IMPOSTO | integer(4) |  |  | MS - Aproveitar como crédito de ICMS o valor do imposto |
| PE_CALCULAR_ICMS_ANTECIPADO_ATACADISTA | char(1) |  |  | PE - Calcular o ICMS antecipado nas empresas atacadistas (S/N) |
| RJ_CALCULAR_COMPLEMENTO_RESTITUICAO_ICMS_ST_CONFORME_RESOLUCAO_SEFAZ_578_2023 | char(1) |  |  | RJ - Calcular o complemento/restituição do ICMS ST conforme Resolução Sefaz nº 578/2023 |
| IMPORTAR_SAIDAS_ISENTAS_VALOR_CONTABIL | char(1) |  |  | Importar Saídas Isentas Valor Contábil |
| EXCLUIR_RECEITA_EXPORTACAO_INSS_RECEITA_BRUTA | char(1) |  |  | Excluir as receitas de exportação indireta da base de cálculo do INSS Receita Bruta |
| MS_OPERACAO_COM_RECOLHIMENTO_DIFERENCIAL_ALIQUOTA_POR_TVF | char(1) |  |  | MS - Operação com recolhimento de diferencial de alíquota por TVF |
| ES_APROVEITAR_CREDITO_ICMS_MONOFASICO_SOB_COMBUSTIVEL_CREDITO_ICMS | char(1) |  |  | ES - Aproveitar o crédito do ICMS monofásico sobre combustíveis como crédito no imposto ICMS |
| MT_APROVEITAR_CREDITO_ICMS_MONOFASICO_SOB_COMBUSTIVEL_CREDITO_ICMS | char(1) |  |  | MT - Aproveitar o crédito do ICMS monofásico sobre combustíveis como crédito no imposto ICMS |
| RS_OPERACAO_NAO_SUJEITA_AO_PAGAMENTO_DO_ICMS_ENT | char(1) |  |  | RS - Operação não sujeita ao pagamento do ICMS na entrada quando decorrente do diferimento-Art.37, §1º, "f" do RICMS |
| RS_PROD_SEG_AUTOPECAS_SUJ_ANTECIP_IMP_ENTRADAS | char(1) |  |  | RS - Produto do segmento de autopeças sujeito à antecipação do imposto nas entradas |
| RJ_OPERACAO_REG_ESPECIAL_TRIBUTACAO_ICMS_ART_6_LEI_6979_2015 | char(1) |  |  | Operação sujeita ao regime especial de tributação do ICMS conf. Art.6° da Lei n°6.979/2015 |
| MG_OPERACAO_SUJEITA_CRED_PRESUMIDO_TRIBUTACAO_EFETIVA | char(1) |  |  | MG - Operação sujeita ao crédito presumido - Tributação efetiva |
| CE_APROVEITAR_CREDITO_ICMS_MONOFASICO_SOB_COMBUSTIVEL_CREDITO_ICMS | char(1) |  |  | CE - Aproveitar o crédito do ICMS monofásico sobre combustíveis como crédito no imposto ICMS - Conv. 26/23 |
| DEDUZIR_VALOR_PEDAGIO_BASE_CALCULO_IRPJ_CSLL | char(1) |  |  | Dedzuir valor do pedágio na base de cálculo do Irpj/Csll(S/N) |
| EFD_REINF_PRODUTOR_RURAL_EXPORTACAO | char(1) |  |  | Aquisição de produção de produtor rural pessoa física ou segurado especial para fins de exportação |
| PR_CREDITO_PRESUMIDO_20_TRANSPORTADORA_APURACAO_ICMSA_TR | char(1) |  |  | Gerar crédito presumido de 20% para transportadoras na apuração do imposto 98-ICMSA-TR |
| MT_OPERACAO_VINCULADA_CREDITO_OUTORGADO_PRODEIC | char(1) |  |  | MT - Operação não vinculada ao crédito outorgado do PRODEIC Investe - Decreto 288/2019 |
| GO_APROVEITAR_CREDITO_ICMS_MONOFASICO_SOB_COMBUSTIVEL_CREDITO_ICMS | char(1) |  |  | GO - Aproveitar o crédito do ICMS monofásico sobre combustíveis como crédito no imposto ICMS |
| MT_ESTORNAR_DEBITO_DEVOLUCAO_ENTRADA_SEM_APROVEITAMENTO_TOTAL_PARCIAL_ICMS | char(1) |  |  | MT - Estornar débito de devolução cuja entrada ocorreu sem o aproveitamento total ou parcial do imposto icms |
| ES_TIPO_ATIVIDADE_PARA_VALOR_ADICIONADO_FISCAL_VAF | integer(4) |  | S | ES - Tipo de Atividade para o Valor Adicionado Fiscal - VAF |
| PR_OPERACAO_NAO_VINCULADA_AO_ESTORNO_DE_CREDITO_AQUISICAO_COMBUSTIVEIS_INSUMOS | char(1) |  |  | Operação não vinculada ao estorno de crédito aquisição combustíveis para insumos - Art. 25, IV do § 4º e § 5º do RICMS |
| BA_APROVEITAR_CREDITO_ICMS_MONOFASICO_SOB_COMBUSTIVEL_CREDITO_ICMS | char(1) |  |  | BA - Aproveitar o crédito do ICMS monofásico sobre combustíveis como crédito no imposto ICMS |
| RJ_OPERACAO_SUJEITA_AO_CALCULO_IMPOSTO_154_FOT_SOBRE_BENEFICIO | char(1) |  |  | RJ - Operação sujeita ao calculo do imposto 154-FOT sobre o beneficio |
| RJ_TIPO_OPER_SUJEITA_AO_CALCULO_IMPOSTO_154_FOT_SOBRE_BENEFICIO | char(1) |  |  | RJ - Tipo de Operação sujeita ao calculo do imposto 154-FOT sobre o beneficio |
| TO_APROVEITAR_CREDITO_ICMS_MONOFASICO_SOB_COMBUSTIVEL_CREDITO_ICMS | char(1) |  |  | TO - Aproveitar o crédito do ICMS monofásico sobre combustíveis como crédito no imposto ICMS |
| SE_APROVEITAR_CREDITO_ICMS_MONOFASICO_SOB_COMBUSTIVEL_CREDITO_ICMS | char(1) |  |  | SE - Aproveitar o crédito do ICMS monofásico sobre combustíveis como crédito no imposto ICMS |
| RJ_APROVEITAR_CREDITO_ICMS_MONOFASICO_SOB_COMBUSTIVEL_CREDITO_ICMS | char(1) |  |  | RJ - Aproveitar o crédito do ICMS monofásico sobre combustíveis como crédito no imposto ICMS |
| PI_APROVEITAR_CREDITO_ICMS_MONOFASICO_SOB_COMBUSTIVEL_CREDITO_ICMS | char(1) |  |  | PI - Aproveitar o crédito do ICMS monofásico sobre combustíveis como crédito no imposto ICMS |
| CCLASS_TRIB_IBS | varchar(6) |  |  | Classificação Tributária do IBS (cClassTrib IBS) |
| ALIQUOTA_IBS | numeric(5) |  |  | ALIQUOTA IBS |
| I_CST_IBS | integer(4) |  |  | CST IBS |
| CCLASS_TRIB_CBS | varchar(6) |  |  | Classificação Tributária do CBS (cClassTrib CBS) |
| ALIQUOTA_CBS | numeric(5) |  |  | ALIQUOTA CBS |
| I_CST_CBS | integer(4) |  |  | CST CBS |
| CT_ESTORNO_RECEITA_CTE_CTEOS | integer(4) |  | S | Conta receita - Anulação CT-e e/ou CT-eOS |
| HT_ESTORNO_RECEITA_CTE_CTEOS | integer(4) |  | S | Histórico padrão - Estorno receita - Anulação CT-e e/ou CT-eOS |
| RJ_SOMAR_ICMS_ST_VALOR_CONTABIL_REDUCAO_BASE_CALCULO | char(1) |  |  | RJ - Não somar o valor de ICMS ST no valor contábil do cálculo da redução de base de cálculo |
| RJ_OPERACAO_SUJEITA_AO_FOT_ICMS_ST_COM_MVA_REDUZIDA | char(1) |  |  | RJ - Operação sujeita ao FOT sobre o ICMS ST com MVA reduzida (S/N) |
| RJ_OPERACAO_SUJEITA_AO_FOT_ICMS_ST_MVA_REDUZIDA_PERCENTUAL | numeric(5) |  |  | RJ - Operação sujeita ao FOT sobre o ICMS ST com MVA reduzida (Percentual) |
| RJ_ESTORNAR_DEBITO_ICMS_INDEVIDO_TRANSPORTE_INICIADO_EM_OUTRA_UF | char(1) |  |  | RJ - Estornar débito de ICMS indevido - Transporte iniciado em outra UF - Res. 720/14, Art. 7º |
| RS_ESTORNAR_DEBITO_DEVOLUCAO_ENTRADA_SEM_APROVEITAMENTO_ICMS_OU_ICMSST | char(1) |  |  | RS - Estornar débito de devolução cuja entrada ocorreu sem o aproveitamento total ou parcial do ICMS e/ou ICMS ST |
| ES_OPERACAO_INTERESTADUAL_NAO_PRESENCIAL_CONSUMIDOR_FINAL_ART_530_TIPO | integer(4) |  |  | Operação interestadual não presencial a consumidor final - Art. 530-LRI RICMS |
| ES_SAIDA_FORA_BENEFICIO_FISCAL_SEM_PART_RATEIO_CRED_ART_530 | char(1) |  |  | Saí­da fora do benefí­cio fiscal sem participação na proporção do rateio dos créditos |
| MA_APROVEITAR_CREDITO_ICMS_MONOFASICO_SOB_COMBUSTIVEL_CREDITO_ICMS | char(1) |  |  | MA - Aproveitar o crédito do ICMS monofásico sobre combustíveis como crédito no imposto ICMS |
| MA_APROVEITAR_CREDITO_ICMS_MONOFASICO_SOB_COMBUSTIVEL_CREDITO_ICMS_INFO | char(1) |  |  | MA - Aproveitar o crédito do ICMS monofásico sobre combustíveis como crédito no imposto ICMS - Informar Dados |
| MA_APROVEITAR_CREDITO_ICMS_MONOFASICO_SOB_COMBUSTIVEL_CREDITO_ICMS_INFO_PROCESSO | varchar(45) |  |  | MA - Aproveitar o crédito do ICMS monofásico sobre combustíveis como crédito no imposto ICMS - Informar Dados - Processo |
| PA_OPERACAO_CREDITO_PRESUMIDO_SAIDAS_CESTA_BASICA | char(1) |  |  | Operação com crédito presumido nas saídas internas de produtos cesta básica |
| DF_OPERACAO_SAIDA_DIREITO_RESTIT_ICMS_SUBTRI_PAGO_ETAPAS_ANTERIORES | char(1) |  |  | DF - Operação de saída com direito à restituição do ICMS Substituição Tributária pago nas etapas anteriores |
| DF_OPERACAO_SAIDA_DIREITO_RESTIT_ICMS_SUBTRI_PAGO_ETAPAS_ANTERIORES_HIPOTESE | char(1) |  |  | DF - Hipótese de restituição |
| DF_NOTA_APROVEITAMENTO_CREDITO_ICMS_ST_PAGO_ETAPAS_ANTERIORES | char(1) |  |  | DF - Nota de aproveitamento de crédito de ICMS ST pago nas etapas anteriores - Art. 330 do Decreto 18.955/97 |
| CCLASS_TRIB_IS | varchar(6) |  |  | Classificação tributaria do imposto seletivo - IS |
| ALIQUOTA_AD_VALOREM | numeric(5) |  |  | Aliquota ad valorem do imposto IS |
| ALIQUOTA_AD_REM_FIXA | numeric(13) |  |  | Aliquota ad rem fixa do imposto IS |
| UTILIZA_CCLASSTRIB_POR_OPERACAO_IS | char(1) |  |  | Utilizar o cClass Trib por operação |
| I_CST_IS | integer(4) |  |  | CST IS - Imposto Seletivo |
| PE_APROVEITAR_CREDITO_ICMS_MONOFASICO_SOB_COMBUSTIVEL_CREDITO_ICMS | char(1) |  |  | PE - Aproveitar o crédito do ICMS monofásico sobre combustíveis como crédito no imposto ICMS (S/N) |
| SP_OPERACAO_CREDITO_OUTORGADO_SAIDAS_INTERNAS_CARNE | char(1) |  |  | SP - Operação com crédito outorgado nas saídas internas de carne - Anexo III, Art. 40 do RICMS |
| SP_OPERACAO_NAO_VINCULADA_ESTORNO_CREDITO_SAIDAS_INTERNAS_CARNE | char(1) |  |  | SP - Operação não vinculada ao estorno de crédito - Anexo III, art. 40 do RICMS |
| RO_NOTA_TRANSFERENCIA_CREDITO_ICMS_ITENS_39_40_IN_33_2018 | char(1) |  |  | Nota de transferência de crédito de ICMS - Itens 39 e 40 da IN 33/2018 |
| DEDUZIR_VALOR_DESPESAS_ACESSORIAS_BASE_CALCULO_PIS_COFINS_TIPO_NOTA | char(1) |  |  | Deduzir o valor de despesas acessórias da base de cálculo de PIS e COFINS - Tipo Nota |
| CONSIDERAR_CTE_SUBSTITUTO_PERIODO_NORMAL | char(1) |  |  | Considerar o CT-e e/ou CT-eOS substituto no período de apuração do CT-e e/ou CT-eOS normal. (S=Sim/N=Não) |
| NOTA_DEBITO_AJUSTE_APURACAO_LC_214_2025 | char(1) |  |  | Nota de débito para fins de ajuste da apuração assistida conforme LC 214/2025 e NT 2025.002_v1.34 |
| NOTA_APROP_CRED_PRESUM_PROD_RURAL | char(1) |  |  | Nota de apropriação de crédito presumido IBS/CBS produtor rural não contribuinte |
| PR_GERAR_CREDITO_ICMS_AQUISICAO_COMBUSTIVEL_INSUMO_TIPO | integer(4) |  |  | Gerar crédito de ICMS de combustíveis para insumos - Art. 25 do RICMS Tipo |
| NOTA_PAG_INTEGRAL_LIBERACAO_CRED_PRESUMIDO_ADQUIRENTE | char(1) |  |  | Nota com pagamento integral e liberação do crédito presumido ao adquirente |
| PISCOFINS_OPERACAO_NAO_SUJEITA_REDUCAO_LINEAR_LC224 | char(1) |  |  | Operacao nao sujeita a reducao linear de PIS e COFINS da LC 224/2025 |
