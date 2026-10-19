# EFIMPORTACAO_SITE_NFE_CONFIGURACAO — Configuração da importação da NFe pelo site da Receita Federal
1.215 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| DATA_CADASTRO_FORCLI | char(1) |  |  | Data do cadastro do fornecedor cliente |
| CODI_IMP_PIS | integer(4) |  | S | Código do imposto PIS |
| CODI_IMP_COFINS | integer(4) |  | S | Código do imposto COFINS |
| PIS_COFINS_SEGUIMENTADA | char(1) |  | S | Define onde irá o PIS e o COFINS em notas seguimentadas |
| ACU_SAI_EXCESSAO | char(1) |  |  | Definir acumulador para excessão nas saídas |
| CODI_ACU_SAI_EXCESSAO | integer(4) |  | S | Código do acumulador para excessão nas saídas |
| CFOP_ENT_EXCESSAO | char(1) |  |  | Definir CFOP Para excessão nas entradas |
| CFOP_ENT_EXCESSAO_ESTADUAL | integer(4) |  | S | CFOP para excessão nas entradas estaduais |
| CFOP_ENT_VERSAO_ESTADUAL | smallint(2) |  | S | Versão do CFOP estadual na entrada |
| CFOP_ENT_EXCESSAO_INTERESTADUAL | integer(4) |  | S | CFOP para excessão nas entradas interestaduais |
| CFOP_ENT_VERSAO_INTERESTADUAL | smallint(2) |  | S | Versão do CFOP interestadual na entrada |
| ACU_ENT_EXCESSAO | char(1) |  |  | Definir acumulador para excessão nas saídas |
| CODI_ACU_ENT_EXCESSAO | integer(4) |  | S | Código do acumulador para excessão nas entradas |
| CFOP_SAI_CANCELADA_ESTADUAL | integer(4) |  | S | CFOP para notas estaduais de saídas canceladas |
| CFOP_SAI_VERSAO_CANCELADA_ESTADUAL | smallint(2) |  | S | Versão do CFOP para notas estaduais de saídas canceladas |
| CFOP_SAI_CANCELADA_INTERESTADUAL | integer(4) |  | S | CFOP para notas interestaduais de saídas canceladas |
| CFOP_SAI_VERSAO_CANCELADA_INTERESTADUAL | smallint(2) |  | S | Versão do CFOP para notas interestaduais de saídas canceladas |
| CFOP_SAI_CANCELADA_EXTERIOR | integer(4) |  | S | CFOP para notas do exterior canceladas |
| CFOP_SAI_VERSAO_CANCELADA_EXTERIOR | smallint(2) |  | S | Versão do CFOP para notas do exterior canceladas |
| IMPORTAR_PROD_SAI | char(1) |  | S | Importar movimento de produtos das notas de saída |
| PROCURA_PROD_SAI | char(1) |  | S | Notas de saída: Campo a ser considerado para verificar a existência do produto |
| PROD_NOVO_SAI | char(1) |  | S | Notas de saída: Quando o produto a ser importado não estiver cadastrado |
| CODI_GRU_SAI | integer(4) |  | S | Notas de saída: Grupo para cadastros novos de produtos |
| CAD_UNI_AUTO_SAI | char(1) |  | S | Notas de saída: Cadastrar unidade automaticamente |
| IMPORTAR_PROD_ENT | char(1) |  | S | Importar movimento de produtos das notas de entrada |
| PROCURA_PROD_ENT | char(1) |  | S | Notas de entrada: Campo a ser considerado para verificar a existência do produto |
| PROD_NOVO_ENT | char(1) |  | S | Notas de entrada: Quando o produto a ser importado não estiver cadastrado |
| CODI_GRU_ENT | integer(4) |  | S | Notas de entrada: Grupo para cadastros novos de produtos |
| CAD_UNI_AUTO_ENT | char(1) |  | S | Notas de entrada: Cadastrar unidade automaticamente |
| IGNORAR_IMPOSTOS_ACU_ENT | char(1) |  | S | Ignorar impostos não definidos no acumulador |
| GERAR_PAGAMENTO_PARCELA_SAI | char(1) |  | S | Gerar pagamento para parcelas com data de vencimento igual a data da nota |
| GERAR_PARCELA_COM_PAGAMENTO_SAI | char(1) |  | S | Gerar parcela com pagamento para notas sem parcelas |
| INFORMAR_DATA_SAIDA | char(1) |  |  | Informar data de saída no momento da importação(S/N) |
| INFORMAR_DATA_ENTRADA | char(1) |  |  | Informar data de entrada no momento da importação(S/N) |
| COMPLEMENTO_CFOP_CAT_17_99_SAI | integer(4) |  | S | Notas de saída: Complemento padrão do ICMS-CAT 17/99 |
| COMPLEMENTO_CFOP_CAT_17_99_ENT | integer(4) |  | S | Notas de entrada: Complemento padrão do ICMS-CAT 17/99 |
| CONSIDERAR_ICMS_ACU_ENT | char(1) |  |  | Considerar o percentual de base de cálculo e alíquota do ICMS do cadastro do acumulador sobre o valor |
| BENEFICIARIA_CREDITO_PRESUMIDO_ENTRADA | char(1) |  | S | Beneficiário de crédito fiscal presumido conforme Art. 24 RICMS |
| SOBRESCREVER_CADASTROS | char(1) |  |  | Sobrescrever cadastros existentes |
| SOBRESCREVER_MOVIMENTOS | char(1) |  |  | Sobrescrever movimentos existentes |
| CST_CSOSN_EXCECAO | char(1) |  |  | Definir exceção para CST/CSOSN |
| GERAR_CST_CSOSN_INFORMADO_NOTA | char(1) |  |  | Gerar CST/CSOSN |
| CST_CSOSN_DEFINIDO | integer(4) |  | S | Código do CST/CSOSN para exceção das entradas |
| GERAR_LANCAMENTOS_CONTABEIS_ENT | char(1) |  |  | Notas de entrada: Gerar lançamentos contábeis |
| GERAR_LANCAMENTOS_CONTABEIS_SAI | char(1) |  |  | Notas de saída: Gerar lançamentos contábeis |
| IDENTIFICACAO_FORCLI | integer(4) |  |  | Identificação do cadastro do fornecedor/cliente |
| CRIAR_CONTA_FORCLI | char(1) |  |  | Criar conta contábil para fornecedor/cliente |
| CONTA_MESMO_GRUPO_CNPJ | char(1) |  |  | Utilizar a mesma conta do grupo CNPJ do fornecedor/cliente |
| PERMITE_RELACIONAR_MAIS_CFOP_ENT | char(1) |  |  | Permitir relacionar o mesmo CFOP de saída com mais de um CFOP de entrada |
| GERAR_OBSERVACAO_ACUMULADOR_ENT | char(1) |  | S | Gerar observação informada no cadastro do acumulador das notas de entrada |
| GERAR_OBSERVACAO_ACUMULADOR_SAI | char(1) |  | S | Gerar observação informada no cadastro do acumulador das notas de saída |
| PRODUTOS_NOTAS_SEGMENTADAS_SAI | char(1) |  |  | Notas de saída: Produtos para notas segmentadas |
| PRODUTOS_NOTAS_SEGMENTADAS_ENT | char(1) |  |  | Notas de entrada: Produtos para notas segmentadas |
| FORMATO_LETRAS_CADASTROS | char(1) |  |  | Formato de letras nos cadastros |
| I_SEQUENCIAL_CST_CSOSN_DEFINIDO | integer(4) |  | S | Sequencial do CST/CSOSN para exceção das entradas |
| UTILIZAR_CFOP_CADASTRO_PRODUTO_ENT | char(1) |  |  | Notas de entrada: Efetuar a importação das notas de entrada conforme o CFOP do cadastro de produtos |
| CONSIDERAR_IPI_ACU_ENT | char(1) |  |  | Notas de entrada: Considerar as definições do imposto IPI do cadastro do acumulador |
| IMPORTAR_CREDITO_ICMS_ART23_ENT | char(1) |  |  | Notas de entrada: Importar o valor do crédito do ICMS nos termos do Art. 23 da Lei Complementar 123/2006(Simples Nacional) |
| PERMITE_RELACIONAR_CFOP_MAIS_ACU_ENT | char(1) |  |  | Notas de entrada: Permitir relacionar o mesmo CFOP de entrada para mais de um acumulador |
| INSS_RECEITA_BRUTA_CONFORME_PRODUTOS | char(1) |  |  | Gerar valores para o cálculo do INSS Receita Bruta conforme produtos |
| INSS_RECEITA_BRUTA_CONFORME_ACUMULADORES | char(1) |  |  | Gerar valores para o cálculo do INSS Receita Bruta conforme acumuladores |
| CONSIDERAR_SUBTRI_ACU_SAI | char(1) |  |  | Notas de saída: Considerar as definições do imposto SUBTRI do cadastro do acumulador |
| CONSIDERAR_SUBTRI_ACU_ENT | char(1) |  |  | Notas de entrada: Considerar as definições do imposto SUBTRI do cadastro do acumulador |
| DADOS_DO_FRETE_GERAR_LOCAL_SAIDA_EMPRESA_SAI | char(1) |  |  | Notas de saída: Gerar no local de saída dos dados do frete os dados da empresa |
| DADOS_DO_FRETE_GERAR_LOCAL_RECIBIMENTO_CLIENTE_SAI | char(1) |  |  | Notas de saída: Gerar no local de recebimento dos dados do frete os dados do cliente |
| DADOS_DO_FRETE_GERAR_LOCAL_SAIDA_EMPRESA_ENT | char(1) |  |  | Notas de saída: Gerar no local de saída dos dados do frete os dados da empresa |
| DADOS_DO_FRETE_GERAR_LOCAL_RECIBIMENTO_FORNECEDOR_ENT | char(1) |  |  | Notas de saída: Gerar no local de recebimento dos dados do frete os dados do fornecedor |
| INCLUI_IPI_NOTA_SEM_IPI_ENT | char(1) |  |  | Notas de entrada: Incluir o imposto IPI nas notas que não possuem IPI e o imposto estiver informado no acumulador |
| DETERMINAR_TIPO_TITULO_PADRAO_SAI | char(1) |  |  | Notas de saída: Determinar tipo do título padrão para notas a prazo |
| TITULO_PADRAO_SAI | integer(4) |  | S | Notas de saída: Título padrão para notas a prazo |
| DETERMINAR_TIPO_TITULO_PADRAO_ENT | char(1) |  |  | Notas de entrada: Determinar tipo do título padrão para notas a prazo |
| TITULO_PADRAO_ENT | integer(4) |  | S | Notas de entrada: Título padrão para notas a prazo |
| CRIAR_CONTA_FORNECEDOR | char(1) |  |  | Criar conta contábil fornecedor |
| CRIAR_CONTA_CLIENTE | char(1) |  |  | Criar conta contábil cliente |
| GERAR_PARCELA_A_PRAZO_SEM_DUPLICATA_ENT | char(1) |  |  | Notas de entrada: Gerar parcela para nota com forma de pagamento à prazo sem dados de duplicatas (S/N) |
| GERAR_PARCELA_A_PRAZO_SEM_DUPLICATA_SAI | char(1) |  |  | Notas de saída: Gerar parcela para nota com forma de pagamento à prazo sem dados de duplicatas (S/N) |
| IDENTIFICAR_PRODUTO_RELACIONAR_ACUMULADOR_ENT | char(1) |  |  | Notas de entrada: Identificar o produto para relacionar ao acumulador por |
| IDENTIFICAR_PRODUTO_RELACIONAR_ACUMULADOR_SAI | char(1) |  |  | Notas de saída: Identificar o produto para relacionar ao acumulador por |
| CONSIDERAR_MUNICIPIO_FORCLI_CPF | char(1) |  |  | Considerar o município para cadastrar um novo quando a inscrição for CPF |
| TABELA_ICMS_PROD_ENT | integer(4) |  | S | Notas de entrada: Tabela de alíquota interestadual de ICMS |
| TABELA_ICMS_PROD_SAI | integer(4) |  | S | Notas de saída: Tabela de alíquota interestadual de ICMS |
| IMPORTAR_COMO_EXTEMPORANEA_ENT | char(1) |  | S | Importar como extemporânea notas com data de entrada dentro do período fechado |
| DESCONSIDERAR_IE_EMPRESA_CPF_ENT | char(1) |  |  | Notas de entrada: Desconsiderar a inscrição estadual na determinação da empresa a ser importada quando esta possuir inscrição CPF |
| PERMITE_RELACIONAR_CFOP_MAIS_ACU_SAI | char(1) |  |  | Notas de saída: Permitir relacionar o mesmo CFOP de entrada para mais de um acumulador |
| DETERMINAR_DADOS_PIS_COFINS_CONFORME_CFOP_ENT | char(1) |  |  | Notas de entrada: Determinar os dados de PIS/COFINS conforme o CFOP |
| DETERMINAR_DADOS_PIS_COFINS_CONFORME_CFOP_SAI | char(1) |  |  | Notas de saída: Determinar os dados de PIS/COFINS conforme o CFOP |
| CRIAR_CONTA_FORCLI_PARA | char(1) |  |  | Criar conta contábil para: |
| GERAR_OBSERVACAO_DEFINICAO_ENT | integer(4) |  | S | Notas de entrada: Gerar observação na nota conforme informado no(a) - Definição |
| GERAR_OBSERVACAO_DEFINICAO_SAI | integer(4) |  | S | Notas de saída: Gerar observação na nota conforme informado no(a) - Definição |
| GERAR_INFORMACOES_COMPLEMENTARES_ENT | char(1) |  |  | Notas de entrada: Gerar informações complementares na nota conforme informado no(a) |
| GERAR_INFORMACOES_COMPLEMENTARES_DEFINICAO_ENT | integer(4) |  | S | Notas de entrada: Gerar informações complementares na nota conforme informado no(a) - Definição |
| GERAR_INFORMACOES_COMPLEMENTARES_SAI | char(1) |  |  | Notas de saída: Gerar informações complementares na nota conforme informado no(a) |
| GERAR_INFORMACOES_COMPLEMENTARES_DEFINICAO_SAI | integer(4) |  | S | Notas de saída: Gerar informações complementares na nota conforme informado no(a) - Definição |
| GERAR_INFORMACOES_EMPREENDIMENTO_IMOBILIARIO_ACUMULADOR | char(1) |  |  | Gerar informações do empreendimento imobiliário informado no cadastro do acumulador |
| GRAVAR_PRODUTOS_ORDEM_NFE_SAI | char(1) |  |  | Gravar os produtos na mesma ordem que estão informados na NF-e |
| GRAVAR_PRODUTOS_ORDEM_NFE_ENT | char(1) |  |  | Gravar os produtos na mesma ordem que estão informados na NF-e |
| CRIAR_AMPARA_PROD_POSSUI_INF_ALIQUOTA_SAI | char(1) |  |  | Calcular o Ampara/RS somente para produtos que possuem informado na nota as seguintes alíquotas de ICMS |
| CONSIDERAR_ISS_ACUMULADOR | char(1) |  |  | Considerar as definições do imposto ISS do cadastro do acumulador |
| INFORMAR_CARACTERES_AUTOMATICAMENTE | char(1) |  |  | Informar os caracteres anti-robô automaticamente |
| INFORMAR_VALOR_RESSARCIMENTO_ICMS_ST | char(1) |  |  | Informar valor do ressarcimento de ICMS ST conforme Art. 47, § 3º Anexo VIII do RCTE no momento da importação (S / N) |
| DEDUZIR_VALOR_ICMS_BASE_CALCULO_PISCOFINS | varchar(1) |  |  | Deduzir o valor do ICMS da base de cálculo do PIS e COFINS |
| DEDUZIR_VALOR_ICMS_BASE_CALCULO_PISCOFINS_DEVOLUCAO | varchar(1) |  |  | Deduzir o valor do ICMS da base de cálculo do PIS e COFINS nas notas de devolução |
| IMPORTAR_NOTAS_SITUACAO_TERCEIROS_REGIME_ESPECIAL_NORM_ESPECIFICA | varchar(1) |  |  | Importar situação das notas com emissão de terceiros como Documento emitido com base em Regime Especial ou Normal Específica |
| CONSIDERAR_ICMS_ACU_ENT_DEFINICAO | char(1) |  |  | Considerar o percentual de base de cálculo e alíquota do ICMS do cadastro do acumulador sobre o valor - Definição |
| ADICIONAR_VALOR_FCP_NO_SUBTRI_SAI | varchar(1) |  |  | Adicionar o valor do Fundo de Combate a Pobreza ao valor da SUBTRI |
| ADICIONAR_VALOR_FCP_NO_ICMS_SAI | varchar(1) |  |  | Adicionar o valor do Fundo de Combate a Pobreza ao valor do ICMS |
| ADICIONAR_VALOR_FCP_NO_SUBTRI_ENT | varchar(1) |  |  | Adicionar o valor do Fundo de Combate a Pobreza ao valor da SUBTRI |
| INFORMAR_DATA_EMISSAO_MDFE_ENT | varchar(1) |  |  | Informar data de emissão do MDF-e no momento da importação |
| ADICIONAR_VALOR_FCP_NO_ICMS_ENT | varchar(1) |  |  | Adicionar o valor do Fundo de Combate a Pobreza ao valor do ICMS |
| IMPORTAR_TIPO_DOCUMENTO_IMPORTACAO_ENT_ENT | char(1) |  |  | Informar o tipo do documento de importação (S/N) |
| TIPO_DOCUMENTO_IMPORTACAO_ENT | tinyint(1) |  | S | Tipo do documento de importação (0-Declaração de importação/ 1-Declaração simplificada de importação/ 2-Declaração única de importação) |
| PRODUTO_EM_DUPLICIDADE_SAI | char(1) |  | S | Quando o produto a ser importado estiver cadastrado em duplicidade |
| PRODUTO_EM_DUPLICIDADE_ENT | char(1) |  | S | Quando o produto a ser importado estiver cadastrado em duplicidade |
| ADICIONAR_VALOR_AFRMM | varchar(1) |  |  | Adicionar o valor do Adicional ao Frete para a RenovaÃ§Ã£o da Marinha Mercante ao valor das Despesas AcessÃ³rias |
| DEDUZIR_VALOR_SUBTRI_CALCULO_ICMS_ANTECIPACAO_TOTAL_ENT | char(1) |  | S | Deduzir o valor do SUBTRI no cálculo do imposto ICMS Antecipação Total - ST |
| DETERMINAR_ACUMULADORES_PERCENTUAL_BC_ALIQ_ICMS | char(1) |  | S | Determinar acumuladores para considerar o percentual de base de calculo e aliquota do ICMS |
| CONSIDERAR_TODOS_COMO_EXCECAO_ACU_SAI | char(1) |  | S | Considerar como exceÃ§Ã£o a opÃ§Ã£o "Todos" das colunas para relacionamento do acumulador saÃ­da |
| CONSIDERAR_TODOS_COMO_EXCECAO_CFOP_ENT | char(1) |  | S | Considerar como exceÃ§Ã£o a opÃ§Ã£o "Todos" das colunas para relacionamento do CFOP entrada |
| CONSIDERAR_TODOS_COMO_EXCECAO_ACU_ENT | char(1) |  | S | Considerar como exceÃ§Ã£o a opÃ§Ã£o "Todos" das colunas para relacionamento do acumulador entrada |
| DETERMINAR_IMPOSTOS_NOTAS_DE_IMPORTACAO | char(1) |  | S | Determinar impostos que serão considerados como despesas acessórias para notas de importação |
| DEDUZIR_VALOR_FUNRURAL_VALOR_PARCELA_ENTRADA | varchar(1) |  |  | Deduzir o valor do FUNRURAL no valor da parcela |
| DEDUZIR_VALOR_FUNRURAL_VALOR_PARCELA_SAIDA | varchar(1) |  |  | Deduzir o valor do FUNRURAL no valor da parcela |
| CONSULTA_COMPLETA_ORIGEM_CERTIFICADO | char(1) |  |  | Realizar a consulta completa da NF-e com o certificado digital do(a): (E: Empresa, C: Contador) |
| GERAR_PROCESSO_REFERENCIADO_NA_NOTA_SAI | char(1) |  |  | Gerar processo referenciado na nota de saída (Check) |
| GERAR_PROCESSO_REFERENCIADO_NA_NOTA_OPCOES_SAI | integer(4) |  | S | Gerar processo referenciado na nota de saída (Opções: Acumulador - 1, Nota - 2, Acumulador e nota - 3) |
| GERAR_PROCESSO_REFERENCIADO_NA_NOTA_ENT | char(1) |  |  | Gerar processo referenciado na nota de entrada (Check) |
| GERAR_PROCESSO_REFERENCIADO_NA_NOTA_OPCOES_ENT | integer(4) |  | S | Gerar processo referenciado na nota de entrada (Opções: Acumulador - 1, Nota - 2, Acumulador e nota - 3) |
| IMPORTAR_ANEXO_VA_VB_NOTA | char(1) |  | S | Importar as informaÃ§Ãµes do Anexo VA e VB conforme o cÃ³digo do benefÃ­cio informado na nota |
| IMPORTAR_VALOR_DIFERIDO_ICMS_DECRETO_55_797_2021_SAI | char(1) |  |  | Importar valor diferido de ICMS conforme Decreto 55.797/2021 |
| IMPORTAR_VALOR_DIFERIDO_ICMS_DECRETO_55_797_2021_ENT | char(1) |  |  | Importar valor diferido de ICMS conforme Decreto 55.797/2021 |
| DEDUZIR_VALOR_ICMS_BASE_CALCULO_PISCOFINS_DEFINICAO | char(1) |  |  | Deduzir o valor do ICMS da base de cálculo do PIS e COFINS nas notas de devolução - Definição (D-Notas de devolução/E-Notas de entradas/T-Devolução e Entradas) |
| DEDUZIR_VALOR_DIFALNC_FCP_BASE_CALCULO_PISCOFINS_SAIDA | char(1) |  | S | Deduzir o imposto 145-DIFAL-NC e 146-FCP da base de cÃ¡lculo do PIS/COFINS. (Saida) |
| DEDUZIR_VALOR_DIFALNC_FCP_BASE_CALCULO_PISCOFINS_ENTRADA | char(1) |  | S | Deduzir o imposto 145-DIFAL-NC e 146-FCP da base de cÃ¡lculo do PIS/COFINS. (Entrada) |
| CST_CSOSN_EXCECAO_SAI | char(1) |  |  | Definir exceção para CST/CSOSN |
| GERAR_CST_CSOSN_INFORMADO_NOTA_SAI | char(1) |  |  | Gerar CST/CSOSN |
| CST_CSOSN_DEFINIDO_SAI | integer(4) |  | S | Código do CST/CSOSN para exceção das saidas |
| I_SEQUENCIAL_CST_CSOSN_DEFINIDO_SAI | integer(4) |  | S | Chave sequencial do CST/CSOSN para exceção das saidas |
| IMPORTAR_VALOR_IPI_COMO_DESP_ACESSO_NOTA_OP_NACIONAL_SAI | char(1) |  | S | Importar o valor de IPI como despesas acessórias para notas com operação nacional. |
| IMPORTAR_VALOR_IPI_COMO_DESP_ACESSO_NOTA_OP_NACIONAL_ENT | char(1) |  | S | Determinar impostos que serão considerados como despesas acessórias para notas com operação nacional |
| DEDUZIR_VALOR_ICMS_BASE_CALCULO_PISCOFINS_RETIDOS | varchar(1) |  |  | Deduzir o valor do ICMS da base de cálculo do PIS e COFINS Retidos |
| CONTA_PADRAO_CLIENTES | integer(4) |  | S | Conta padrÃ£o clientes CPF/CNPJ |
| ZERAR_VALORES_NOTAS_PRODUTOR_RURAL | varchar(1) |  |  | Zerar valores das notas de produtor rural |
| IMPORTAR_DATA_DESEMBARACO_MERCADORIA | varchar(1) |  |  | Importar a data de desembaraço da mercadoria |
| DEDUZIR_VALOR_DIFALNC_FCP_BASE_CALCULO_PISCOFINS_ENTRADA_DEFINICAO | char(1) |  |  | Deduzir o imposto 145-DIFAL-NC e 146-FCP da base de cÃ¡lculo do PIS/COFINS. (Entrada) - DefiniÃ§Ã£o (A-DIFAL-NC e FCP/D-Valor do DIFAL-NC/F-Valor do FCP) |
| DEDUZIR_VALOR_DIFALNC_FCP_BASE_CALCULO_PISCOFINS_SAIDA_DEFINICAO | char(1) |  |  | Deduzir o imposto 145-DIFAL-NC e 146-FCP da base de cÃƒÂ¡lculo do PIS/COFINS. (Saida) - DefiniÃ§Ã£o (A-DIFAL-NC e FCP/D-Valor do DIFAL-NC/F-Valor do FCP) |
| DEDUZIR_ISS_DA_BASE_CALCULO_PIS_COFINS_SAIDA | char(1) |  | S | Deduzir o valor do ISS da base de cÃ¡lculo do PIS e COFINS. (Saida) |
| DEDUZIR_ISS_DA_BASE_CALCULO_PIS_COFINS_SAIDA_DEFINICAO | char(1) |  |  | Deduzir o valor do ISS da base de cÃ¡lculo do PIS e COFINS. (Saida) - DefiniÃ§Ã£o (T-ISS Tributado/R-ISS Retido/A-ISS Tributado e Retido) |
| NAO_IMPORTAR_NOTAS_SAIDAS_TERCEIROS_SAIDAS | char(1) |  |  | Não importar notas de saídas com emissão de terceiros |
