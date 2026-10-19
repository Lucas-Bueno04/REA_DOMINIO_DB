# EFIMPORTADOR_FIXO_NFCE_SAIDA — Configuração do leiaute NFC-e XML do Importador Fixo - Saída
51 linhas

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
| REORDENAR_CODIGO_NOTAS | char(1) |  |  | Gravar as notas importadas na ordem do número do documento e sem intervalo no código sequencial |
| PROTEGE_GO_DETERMINAR_DISPOSITIVO_SEM_BENEFICIO_FISCAL | char(1) |  |  | Determinar dispositivo para os produtos que não foram relacionados no Benefício Fiscal |
| PRODUTOS_DEFINE_CONTA | char(1) |  |  | Produtos - Define conta contábil |
| PRODUTOS_CONTA_EM_SEU_PODER | integer(4) |  | S | Produtos - Conta contábil - Em seu poder |
| PRODUTOS_CONTA_EM_PODER_DE_TERCEIROS | integer(4) |  | S | Produtos - Conta contábil - Em poder de terceiros |
| PRODUTOS_CONTA_DE_TERCEIROS_EM_SEU_PODER | integer(4) |  | S | Produtos - Conta contábil - De terceiros em seu poder |
| DETERMINAR_TIPO_TITULO_PADRAO | char(1) |  |  | Determinar tipo do título padrão para notas a prazo |
| TITULO_PADRAO | integer(4) |  | S | Título padrão para notas a prazo |
| CODI_CLI_PADRAO | integer(4) |  | S | Cliente padrão |
| UTILIZAR_CLIENTE_PADRAO_QUANDO | integer(4) |  |  | Utilizar o cliente padrão quando |
| IDENTIFICAR_PRODUTO_RELACIONAR_ACUMULADOR | char(1) |  |  | Identificar o produto para relacionar ao acumulador por |
| TABELA_ICMS_PROD | integer(4) |  | S | Tabela de alíquota interestadual de ICMS |
| DOC_INUTILIZADOS_CFOP | integer(4) |  | S | CFOP documentos inutilizados |
| DOC_INUTILIZADOS_VERSAO_CFOP | integer(4) |  | S | Versão do CFOP documentos inutilizados |
| DOC_INUTILIZADOS_CODI_ACU | integer(4) |  | S | Acumulador documentos inutilizados |
| DOC_INUTILIZADOS_CODI_CLI | integer(4) |  | S | Cliente documentos inutilizados |
| IMPORTAR_SOMENTE_NOTAS_POSSUEM_PROTOCOLO_AUTORIZACAO | char(1) |  |  | Importar somente notas que possuem o protocolo de autorização de uso da NF-e |
| CRIAR_AMPARA_PROD_POSSUI_INF_ALIQUOTA | char(1) |  |  | Calcular o Ampara/RS somente para produtos que possuem informado na nota as seguintes alíquotas de ICMS |
| CONSIDERAR_ISS_ACUMULADOR | char(1) |  |  | Considerar as definições do imposto ISS do cadastro do acumulador |
| IDENTIFICAR_BICO_LANCTO_PRODUTO | varchar(1) |  |  | Identificar o bico para os lançamentos dos produtos por C - Código/ N - Número do bico |
| IDENTIFICAR_TANQUE_LANCTO_PRODUTO | varchar(1) |  |  | Identificar o tanque para os lançamentos dos produtos por C - Código/ I - Identificador |
| ADICIONAR_VALOR_FCP_NO_ICMS | varchar(1) |  |  | Adicionar o valor do Fundo de Combate a Pobreza ao valor do ICMS |
| CONSIDERAR_DATA_CONTINGENCIA_COMO_EMISSAO | varchar(1) |  |  | Considerar a data de contingência como data da emissão |
| PRODUTO_EM_DUPLICIDADE | char(1) |  | S | Quando o produto a ser importado estiver cadastrado em duplicidade |
| CONSIDERAR_ICMS_ACUMULADOR_SOBRE_VALOR_DEFINICAO | char(1) |  |  | Considerar o percentual de base de cálculo e alíquota do ICMS do cadastro do acumulador sobre o valor - Definição |
| DEDUZIR_VALOR_ICMS_BASE_CALCULO_PISCOFINS | char(1) |  |  | Deduzir o valor do ICMS da base de cálculo do PIS e COFINS |
| IMPORTAR_ANEXO_VA_VB_NOTA | char(1) |  | S | Importar as informaÃ§Ãµes do Anexo VA e VB conforme o cÃ³digo do benefÃ­cio informado na nota |
| EFETUAR_IMPORTACAO_NOTAS_SAIDA_CONFORME_CFOP_PRODUTOS | char(1) |  | S | Efetuar a importação das notas de saída conforme o CFOP do cadastro de produtos. |
| CST_CSOSN_EXCECAO | char(1) |  |  | Definir exceção para CST/CSOSN |
| GERAR_CST_CSOSN_INFORMADO_NOTA | char(1) |  |  | Gerar CST/CSOSN informado na nota |
| CST_CSOSN_DEFINIDO | integer(4) |  | S | Código do CST/CSOSN para exceção das saídas |
| I_SEQUENCIAL_CST_CSOSN_DEFINIDO | integer(4) |  | S | Chave sequencial do CST/CSOSN para exceção das saídas |
| CONSIDERAR_TODOS_COMO_EXCECAO_ACU_SAI | char(1) |  |  | Considerar como exceção a opção "Todos" das colunas para relacionamento do acumulador saída |
| GERAR_OBSERVACAO_DEFINICAO | integer(4) |  | S | Gerar observação na nota conforme informado no(a) - Definição |
| GERAR_INFORMACOES_COMPLEMENTARES | char(1) |  |  | Gerar informações complementares na nota conforme informado no(a) |
| GERAR_INFORMACOES_COMPLEMENTARES_DEFINICAO | integer(4) |  | S | Gerar informações complementares na nota conforme informado no(a) - Definição |
| REGISTRAR_ALTERACAO_NCM_CAD_PROD | char(1) |  |  | Registrar alteração de NCM ao sobrescrever o cadastro de produto. |
