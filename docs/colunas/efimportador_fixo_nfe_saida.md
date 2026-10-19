# EFIMPORTADOR_FIXO_NFE_SAIDA — Configuração do leiaute NF-e XML do Importador Fixo - Saída
1.220 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| IMPORTAR_PARCELAS | char(1) |  |  | Importar parcelas |
| GERAR_PAGAMENTO_PARCELA | char(1) |  |  | Gerar pagamento para parcelas com data de vencimento igual a data da nota |
| GERAR_PARCELA_COM_PAGAMENTO | char(1) |  |  | Gerar parcela com pagamento para notas sem parcelas |
| GERAR_OBSERVACAO_ACUMULADOR | char(1) |  |  | Gerar observação informada no cadastro do acumulador |
| ACUMULADOR_EXCECAO | char(1) |  |  | Definir acumulador para exceção |
| CODI_ACU_EXCECAO | integer(4) |  | S | Código do acumulador para exceção |
| IMPORTAR_PROD | char(1) |  |  | Importar produtos e movimentação de produtos |
| PROCURA_PROD | char(1) |  |  | Campo a ser considerado para verificar a existência do produto |
| PROD_NOVO | char(1) |  |  | Quando o produto a ser importado não estiver cadastrado |
| CODI_GRU | integer(4) |  | S | Grupo para cadastros de produtos |
| COMPLEMENTO_CFOP_CAT_17_99 | integer(4) |  | S | Complemento padrão do ICMS-CAT 17/99 |
| CANC_EXCLUI_MOV_PRODUTOS | char(1) |  |  | Excluir movimentação de produtos |
| CANC_EXCLUI_PARCELAS | char(1) |  |  | Excluir parcelas |
| CANC_EXCLUI_LANCTOS_CONTABEIS | char(1) |  |  | Excluir lançamentos contábeis |
| DIFERENCA_BC_ICMS_EXCECAO | char(1) |  |  | Diferença base de cálculo para exceção |
| DEFINICAO_BC_ICMS_EXCECAO | char(1) |  | S | Definição da diferença base de cálculo para exceção |
| INFORMAR_DATA_SAIDA | char(1) |  |  | Informar data de saída no momento da importação |
| CONSIDERAR_ICMS_ACUMULADOR | char(1) |  |  | Considerar o percentual de base de cálculo e alíquota do ICMS do cadastro do acumulador sobre o valor |
| GERAR_LANCAMENTOS_CONTABEIS | char(1) |  |  | Gerar lançamentos contábeis |
| PRODUTOS_NOTAS_SEGMENTADAS | char(1) |  |  | Produtos para notas segmentadas |
| IMPORTAR_NOTA_ENTRADA_OUTRA_EMPRESA | char(1) |  |  | Importar nota de entrada em outra empresa |
| REORDENAR_CODIGO_NOTAS | char(1) |  |  | Gravar as notas importadas na ordem do número do documento e sem intervalo no código sequencial |
| CONSIDERAR_SUBTRI_ACUMULADOR | char(1) |  |  | Considerar as definições do imposto SUBTRI do cadastro do acumulador |
| DADOS_DO_FRETE_GERAR_LOCAL_SAIDA_EMPRESA | char(1) |  |  | Gerar no local de saída dos dados do frete os dados da empresa |
| DADOS_DO_FRETE_GERAR_LOCAL_RECIBIMENTO_CLIENTE | char(1) |  |  | Gerar no local de recebimento dos dados do frete os dados do cliente |
| NAO_SOMAR_SUBTRI_ICMS | char(1) |  |  | Não somar o valor do imposto de Substituição Tributária nas colunas Isentas/Outras do imposto ICMS |
| NAO_CONSIDERAR_DIFERENCA_BC_IPI_EXCECAO | char(1) |  |  | Não considerar as definições para os valores do IPI |
| DEFINICAO_DIFERENCA_BC_IPI_EXCECAO | char(1) |  | S | Lançar IPI em |
| NAO_CONSIDERAR_DIFERENCA_BC_SUBTRI_EXCECAO | char(1) |  |  | Não considerar as definições para os valores do SUBTRI |
| DEFINICAO_DIFERENCA_BC_SUBTRI_EXCECAO | char(1) |  | S | Lançar SUBTRI em |
| PROTEGE_GO_DETERMINAR_DISPOSITIVO_SEM_BENEFICIO_FISCAL | char(1) |  |  | Determinar dispositivo para os produtos que não foram relacionados no Benefício Fiscal |
| DATA_CUPOM_FISCAL_REFERENCIADO | char(1) |  |  | Data do Cupom Fiscal Referenciado |
| PRODUTOS_DEFINE_CONTA | char(1) |  |  | Produtos - Define conta contábil |
| PRODUTOS_CONTA_EM_SEU_PODER | integer(4) |  | S | Produtos - Conta contábil - Em seu poder |
| PRODUTOS_CONTA_EM_PODER_DE_TERCEIROS | integer(4) |  | S | Produtos - Conta contábil - Em poder de terceiros |
| PRODUTOS_CONTA_DE_TERCEIROS_EM_SEU_PODER | integer(4) |  | S | Produtos - Conta contábil - De terceiros em seu poder |
| DETERMINAR_TIPO_TITULO_PADRAO | char(1) |  |  | Determinar tipo do título padrão para notas a prazo |
| TITULO_PADRAO | integer(4) |  | S | Título padrão para notas a prazo |
| DEFINIR_EXCECAO_DIFERENCA_BC_IPI | char(1) |  |  | Definir exceção para diferença entre valor contábil e base de cálculo IPI |
| DEFINICAO_EXCECAO_DIFERENCA_BC_IPI | char(1) |  | S | Lançar diferença entre valor contábil e base de cálculo IPI em (I=Isentas/ O=Outras/ N=Nenhuma) |
| NAO_CONSIDERAR_DIFERENCA_BC_SUBTRI_EXCECAO_IPI | char(1) |  |  | IPI - Não considerar as definições para os valores do SUBTRI |
| DEFINICAO_DIFERENCA_BC_SUBTRI_EXCECAO_IPI | char(1) |  | S | IPI - Lançar SUBTRI em |
| DETERMINAR_DADOS_PIS_COFINS_CONFORME_CFOP | char(1) |  |  | Determinar os dados de PIS/COFINS conforme o CFOP |
| DEFINIR_EXCECAO_PIS_COFINS_CONFORME_CFOP | char(1) |  |  | Definir exceção dos dados de PIS/COFINS |
| DEFINICAO_EXCECAO_PIS_COFINS_CONFORME_CFOP | char(1) |  | S | Definição da exceção dos dados de PIS/COFINS |
| NAO_INCLUIR_CODIGO_ATIVIDADE_INSS | char(1) |  |  | Não incluir o código de atividade conforme NCM para cálculo do INSS Receita Bruta |
| IDENTIFICAR_PRODUTO_RELACIONAR_ACUMULADOR | char(1) |  |  | Identificar o produto para relacionar ao acumulador por |
| TIPO_ITEM_NOVOS_PRODUTOS | char(1) |  |  | Tipo do item a ser informado no cadastro de novos produtos |
| TIPO_ITEM_DEFINIR_EXCECAO | char(1) |  |  | Definir exceção do tipo do item |
| TIPO_ITEM_EXCECAO | integer(4) |  | S | Exceção do tipo do item |
| TABELA_ICMS_PROD | integer(4) |  | S | Tabela de alíquota interestadual de ICMS |
| CFOP_EXCECAO | char(1) |  |  |  |
| CFOP_ESTADUAL_EXCECAO | integer(4) |  | S |  |
| VERSAO_CFOP_ESTADUAL_EXCECAO | smallint(2) |  | S |  |
| CFOP_INTERESTADUAL_EXCECAO | integer(4) |  | S |  |
| VERSAO_CFOP_INTERESTADUAL_EXCECAO | smallint(2) |  | S |  |
| IMPORTAR_SOMENTE_NOTAS_POSSUEM_PROTOCOLO_AUTORIZACAO | char(1) |  |  | Importar somente notas que possuem o protocolo de autorização de uso da NF-e |
| NOTAS_FISCAIS_REFERENCIADAS_TIPO_OPERACAO | char(1) |  |  | Documentos referenciados - Notas fiscais - Tipo de operação |
| NOTAS_FISCAIS_REFERENCIADAS_TIPO_EMITENTE | char(1) |  |  | Documentos referenciados - Notas fiscais - Tipo de emitente |
| NOTAS_FISCAIS_REFERENCIADAS_DATA_CONSIDERADA | char(1) |  |  | Documentos referenciados - Notas fiscais - Data a ser considerada |
| CONSIDERAR_ICMS_ACUMULADOR_SOBRE_VALOR_DEFINICAO | char(1) |  |  | Considerar o percentual de base de cálculo e alíquota do ICMS do cadastro do acumulador sobre o valor - Definição |
| INFORMAR_NOTA_ENTRADA_DEVOLVIDA_IMPORTACAO | char(1) |  |  | Informar nota de entrada devolvida no momento da importação |
| DOC_INUTILIZADOS_CFOP | integer(4) |  | S | CFOP documentos inutilizados |
| DOC_INUTILIZADOS_VERSAO_CFOP | integer(4) |  | S | Versão do CFOP documentos inutilizados |
| DOC_INUTILIZADOS_CODI_ACU | integer(4) |  | S | Acumulador documentos inutilizados |
| DOC_INUTILIZADOS_CODI_CLI | integer(4) |  | S | Cliente documentos inutilizados |
| GERAR_INFORMACOES_COMPLEMENTARES | char(1) |  |  | Gerar informações complementares na nota conforme informado no(a) |
| GERAR_INFORMACOES_COMPLEMENTARES_DEFINICAO | integer(4) |  | S | Gerar informações complementares na nota conforme informado no(a) - Definição |
| GERAR_OBSERVACAO_DEFINICAO | integer(4) |  | S | Gerar observação na nota conforme informado no(a) - Definição |
| GRAVAR_PRODUTOS_ORDEM_NFE | char(1) |  |  | Gravar os produtos na mesma ordem que estão informados na NF-e |
| CRIAR_AMPARA_PROD_POSSUI_INF_ALIQUOTA | char(1) |  |  | Calcular o Ampara/RS somente para produtos que possuem informado na nota as seguintes alíquotas de ICMS |
| REALIZAR_LANCAMENTO_PRODUTO_GENERICO | char(1) |  |  | Realizar lançamento de produto genérico |
| CONSIDERAR_ISS_ACUMULADOR | char(1) |  |  | Considerar as definições do imposto ISS do cadastro do acumulador |
| DEDUZIR_VALOR_ICMS_BASE_CALCULO_PISCOFINS | varchar(1) |  |  | Deduzir o valor do ICMS da base de cálculo do PIS e COFINS |
| ADICIONAR_VALOR_FCP_NO_SUBTRI | varchar(1) |  |  | Adicionar o valor do Fundo de Combate a Pobreza ao valor da SUBTRI |
| ADICIONAR_VALOR_FCP_NO_ICMS | varchar(1) |  |  | Adicionar o valor do Fundo de Combate a Pobreza ao valor do ICMS |
| PRODUTO_EM_DUPLICIDADE | char(1) |  | S | Quando o produto a ser importado estiver cadastrado em duplicidade |
| DEDUZIR_VALOR_FUNRURAL_NO_VALOR_PARCELA | varchar(1) |  |  | Deduzir o valor do FUNRURAL no valor da parcela |
| GERAR_PROCESSO_REFERENCIADO_NA_NOTA | char(1) |  |  | Gerar processo referenciado na nota (Check) |
| GERAR_PROCESSO_REFERENCIADO_NA_NOTA_OPCOES | integer(4) |  | S | Gerar processo referenciado na nota (Opções: Acumulador - 1, Nota - 2, Acumulador e nota - 3) |
| IMPORTAR_ANEXO_VA_VB_NOTA | char(1) |  | S | Importar as informaÃ§Ãµes do Anexo VA e VB conforme o cÃ³digo do benefÃ­cio informado na nota |
| CONSIDERAR_TODOS_COMO_EXCECAO_CFOP_SAI | char(1) |  | S | Considerar como exceção a opção "Todos" das colunas para relacionamento do CFOP saída |
| CONSIDERAR_TODOS_COMO_EXCECAO_ACU_SAI | char(1) |  | S | Considerar como exceção a opção "Todos" das colunas para relacionamento do acumulador saída |
| IMPORTAR_VALOR_DIFERIDO_ICMS_DECRETO_55_797_2021 | char(1) |  |  | Importar valor diferido de ICMS conforme Decreto 55.797/2021 |
| DEDUZIR_VALOR_DIFALNC_FCP_BASE_CALCULO_PISCOFINS_SAIDA | char(1) |  | S | Deduzir o imposto 145-DIFAL-NC e 146-FCP da base de cÃ¡lculo do PIS/COFINS. (Saida) |
| CST_CSOSN_EXCECAO | char(1) |  |  | Definir exceção para CST/CSOSN |
| GERAR_CST_CSOSN_INFORMADO_NOTA | char(1) |  |  | Gerar CST/CSOSN |
| CST_CSOSN_DEFINIDO | integer(4) |  | S | Código do CST/CSOSN para exceção das saidas |
| I_SEQUENCIAL_CST_CSOSN_DEFINIDO | integer(4) |  | S | Chave sequencial do CST/CSOSN para exceção das saidas |
| IMPORTAR_VALOR_IPI_COMO_DESP_ACESSO_NOTA_OP_NACIONAL_SAI | char(1) |  | S | Importar o valor de IPI como despesas acessórias para notas com operação nacional. |
| IMPORTAR_DESCRICAO_COMPLEMENTAR_PRODUTO | char(1) |  | S | Importar descrição complementar do produto |
| IDENTIFICAR_CLIENTE_RELACIONAR_ACUMULADOR | char(1) |  |  | Identificar o cliente para relacionar ao acumulador por |
| REGISTRAR_ALTERACAO_NCM_CAD_PROD | char(1) |  |  | Registrar alteração de NCM ao sobrescrever o cadastro de produto. |
| DEDUZIR_VALOR_ICMS_BASE_CALCULO_PISCOFINS_RETIDOS | varchar(1) |  |  | Deduzir o valor do ICMS da base de cálculo do PIS e COFINS Retidos |
| DEDUZIR_VALOR_DIFALNC_FCP_BASE_CALCULO_PISCOFINS_SAIDA_DEFINICAO | char(1) |  |  | Deduzir o imposto 145-DIFAL-NC e 146-FCP da base de cÃƒÂ¡lculo do PIS/COFINS. (Saida) - DefiniÃ§Ã£o (A-DIFAL-NC e FCP/D-Valor do DIFAL-NC/F-Valor do FCP) |
| DEDUZIR_ISS_DA_BASE_CALCULO_PIS_COFINS_SAIDA | char(1) |  | S | Deduzir o valor do ISS da base de cÃ¡lculo do PIS e COFINS. (Saida) |
| DEDUZIR_ISS_DA_BASE_CALCULO_PIS_COFINS_SAIDA_DEFINICAO | char(1) |  |  | Deduzir o valor do ISS da base de cÃ¡lculo do PIS e COFINS. (Saida) - DefiniÃ§Ã£o (T-ISS Tributado/R-ISS Retido/A-ISS Tributado e Retido) |
| GERAR_PARCELAS_NOTAS_NAO_POSSUEM_PARCELAS | char(1) |  |  | Gerar parcelas para notas que não possuem parcelas |
| GERAR_PAGAMENTO_PARCELA_PARA | char(1) |  |  | Gerar pagamento para as parcelas: |
| EFETUAR_IMPORTACAO_NOTAS_SAIDA_CONFORME_CFOP_PRODUTOS | char(1) |  |  | Efetuar a importação de NF-e conforme CFOP de cadastro de produtos |
| NAO_IMPORTAR_NOTAS_SAIDAS_TERCEIROS | char(1) |  |  | Não importar notas de saídas com emissão de terceiros |
