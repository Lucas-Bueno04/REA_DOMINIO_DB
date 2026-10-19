# EFIMPORTADOR_FIXO_SINTEGRA — Configuração do leiaute SINTEGRA do Importador Fixo
61 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| SOBRESCREVER_MOVIMENTOS | char(1) |  |  | Sobrescrever movimentos existentes |
| DADOS_EXCECAO | char(1) |  |  | Definir dados para exceção |
| CFOP_EXCECAO | integer(4) |  | S | CFOP para exceção |
| VERSAO_CFOP_EXCECAO | smallint(2) |  | S | Versão do CFOP para exceção |
| CODI_ACU_EXCECAO | integer(4) |  | S | Código do acumulador para exceção |
| IMPORTAR_PROD | char(1) |  |  | Importar movimento de produtos das notas de saída |
| PROCURA_PROD | char(1) |  |  | Campo a ser considerado para verificar a existência do produto |
| PROD_NOVO | char(1) |  |  | Quando o produto a ser importado não estiver cadastrado |
| CODI_GRU | integer(4) |  | S | Grupo para cadastros novos de produtos |
| COMPLEMENTO_CFOP_CAT_17_99 | integer(4) |  | S | Complemento padrão do ICMS-CAT 17/99 |
| VALOR_PRODUTO_CONFORME | char(1) |  |  | Valor do produto/serviço informado conforme |
| GERAR_LANCAMENTOS_CONTABEIS | char(1) |  | S | Gerar lançamentos contábeis |
| INSS_RECEITA_BRUTA_CONFORME_PRODUTOS | char(1) |  | S | Gerar valores para o cálculo do INSS Receita Bruta conforme produtos |
| INSS_RECEITA_BRUTA_CONFORME_ACUMULADORES | char(1) |  | S | Gerar valores para o cálculo do INSS Receita Bruta conforme acumuladores |
| TABELA_ICMS_PROD | integer(4) |  | S | Tabela de alíquota interestadual de ICMS |
| CONSIDERAR_ICMS_ACU | char(1) |  |  | Considerar as definições do imposto ICMS do cadastro do acumulador |
| RATEAR_DESCONTO_SITUACAO_TRIBUTARIA | char(1) |  |  | Ratear o valor do desconto informado na situação tributária entre os produtos e os cupons fiscais |
| SOBRESCREVER_CADASTROS | char(1) |  |  | Sobrescrever cadastros existentes |
| IDENTIFICACAO_FORCLI | integer(4) |  |  | Identifição do cadastro do fornecedor/cliente |
| DATA_CADASTRO_FORCLI | char(1) |  |  | Data do cadastro do fornecedor/cliente |
| CRIAR_CONTA_FORCLI | char(1) |  |  | Criar conta contábil para fornecedor/cliente |
| IMPOSTOS_SEGMENTADA | char(1) |  |  | Define onde irão os impostos em notas segmentadas |
| CODI_IMP_PIS | integer(4) |  | S | Código do imposto PIS |
| CODI_IMP_COFINS | integer(4) |  | S | Código do imposto COFINS |
| CONTA_MESMO_GRUPO_CNPJ | char(1) |  |  | Utilizar a mesma conta do grupo CNPJ do fornecedor/cliente |
| PRODUTOS_NOTAS_SEGMENTADAS | char(1) |  |  | Produtos para notas segmentadas |
| VERIFICACAO_EXISTENCIA_UNIDADE_ARQUIVO | char(1) |  |  | Verificar a existência da unidade no arquivo |
| VERIFICACAO_EXISTENCIA_UNIDADE_SISTEMA | char(1) |  |  | Verificar a existência da unidade no sistema |
| REORDENAR_CODIGO_FORCLI | char(1) |  |  | Não gerar intervalo no código sequencial do fornecedor/cliente |
| FORMATO_LETRAS_CADASTROS | char(1) |  |  | Formato de letras nos cadastros |
| CRIAR_CONTA_FORNECEDOR | char(1) |  |  | Criar conta contábil fornecedor |
| CRIAR_CONTA_CLIENTE | char(1) |  |  | Criar conta contábil cliente |
| CONSIDERAR_MUNICIPIO_FORCLI_CPF | char(1) |  |  | Considerar o município para cadastrar um novo quando a inscrição for CPF |
| PRODUTO_EM_DUPLICIDADE | char(1) |  | S | Quando o produto a ser importado estiver cadastrado em duplicidade. |
