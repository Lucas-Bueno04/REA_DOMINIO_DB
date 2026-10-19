# EFIMPORTADOR_FIXO_NFCE_ENTRADA — Configuração do leiaute NFC-e XML do Importador Fixo - Entrada
51 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| IMPORTAR_PARCELAS | char(1) |  |  | Importar parcelas |
| IGNORAR_IMPOSTOS_NAO_DEF_ACU | char(1) |  |  | Ignorar impostos não definidos no acumulador |
| CONSIDERAR_ICMS_ACUMULADOR | char(1) |  |  | Considerar o percentual de base de cálculo e alíquota do ICMS do cadastro do acumulador sobre o valor |
| GERAR_OBSERVACAO_ACUMULADOR | char(1) |  |  | Gerar observação informada no cadastro do acumulador |
| CFOP_EXCESSAO | char(1) |  |  | Definir CFOPs para exceção |
| CFOP_ESTADUAL_EXCECAO | integer(4) |  | S | CFOP para exceção nas entradas estaduais |
| VERSAO_CFOP_ESTADUAL_EXCECAO | smallint(2) |  | S | Versão do CFOP para exceção nas entradas estaduais |
| CFOP_INTERESTADUAL_EXCECAO | integer(4) |  | S | CFOP para exceção nas entradas interestaduais |
| VERSAO_CFOP_INTERESTADUAL_EXCECAO | smallint(2) |  | S | Versão do CFOP para exceção nas entradas interestaduais |
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
| INFORMAR_DATA_ENTRADA | char(1) |  |  | Informar data de entrada no momento da importação |
| CST_CSOSN_EXCECAO | char(1) |  |  | Definir exceção para CST/CSOSN |
| GERAR_CST_CSOSN_INFORMADO_NOTA | char(1) |  |  | Gerar CST/CSOSN |
| CST_CSOSN_DEFINIDO | integer(4) |  | S | Código do CST/CSOSN para exceção das entradas |
| GERAR_LANCAMENTOS_CONTABEIS | char(1) |  |  | Gerar lançamentos contábeis |
| PRODUTOS_NOTAS_SEGMENTADAS | char(1) |  |  | Produtos para notas segmentadas |
| I_SEQUENCIAL_CST_CSOSN_DEFINIDO | integer(4) |  | S | Chave sequencial do CST/CSOSN para exceção das entradas |
| UTILIZAR_CFOP_CADASTRO_PRODUTO | char(1) |  |  | Efetuar a importação das notas de entrada conforme o CFOP do cadastro de produtos |
| PRODUTOS_DEFINE_CONTA | char(1) |  |  | Produtos - Define conta contábil |
| PRODUTOS_CONTA_EM_SEU_PODER | integer(4) |  | S | Produtos - Conta contábil - Em seu poder |
| PRODUTOS_CONTA_EM_PODER_DE_TERCEIROS | integer(4) |  | S | Produtos - Conta contábil - Em poder de terceiros |
| PRODUTOS_CONTA_DE_TERCEIROS_EM_SEU_PODER | integer(4) |  | S | Produtos - Conta contábil - De terceiros em seu poder |
| DETERMINAR_TIPO_TITULO_PADRAO | char(1) |  |  | Determinar tipo do título padrão para notas a prazo |
| TITULO_PADRAO | integer(4) |  | S | Título padrão para notas a prazo |
| IDENTIFICAR_PRODUTO_RELACIONAR_ACUMULADOR | char(1) |  |  | Identificar o produto para relacionar ao acumulador por |
| TABELA_ICMS_PROD | integer(4) |  | S | Tabela de alíquota interestadual de ICMS |
| IMPORTAR_SOMENTE_NOTAS_POSSUEM_PROTOCOLO_AUTORIZACAO | char(1) |  |  | Importar somente notas que possuem o protocolo de autorização de uso da NF-e |
| CONSIDERAR_DATA_CONTINGENCIA_COMO_EMISSAO | varchar(1) |  |  | Considerar a data de contingência como data da emissão |
| PRODUTO_EM_DUPLICIDADE | char(1) |  | S | Quando o produto a ser importado estiver cadastrado em duplicidade |
| CONSIDERAR_ICMS_ACUMULADOR_DEFINICAO | char(1) |  |  | Considerar o percentual de base de cálculo e alíquota do ICMS do cadastro do acumulador sobre o valor - Definição |
| CONSIDERAR_TODOS_COMO_EXCECAO_CFOP_ENT | char(1) |  |  | Considerar como exceção a opção "Todos" das colunas para relacionamento do CFOP entrada |
| CONSIDERAR_TODOS_COMO_EXCECAO_ACU_ENT | char(1) |  |  | Considerar como exceção a opção "Todos" das colunas para relacionamento do acumulador entrada |
