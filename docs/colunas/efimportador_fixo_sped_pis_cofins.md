# EFIMPORTADOR_FIXO_SPED_PIS_COFINS — Configuração do leiaute SPED PIS/COFINS do Importador Fixo
19 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| SOBRESCREVER_CADASTROS | char(1) |  |  | Sobrescrever cadastros existentes |
| SOBRESCREVER_MOVIMENTOS | char(1) |  |  | Sobrescrever movimentos existentes |
| IDENTIFICACAO_FORCLI | integer(4) |  |  | Identifição do cadastro do fornecedor/cliente |
| DATA_CADASTRO_FORCLI | char(1) |  |  | Data do cadastro do fornecedor/cliente |
| CRIAR_CONTA_FORCLI | char(1) |  |  | Criar conta contábil para fornecedor/cliente |
| IMPOSTOS_SEGMENTADA | char(1) |  |  | Define onde irão os impostos em notas segmentadas |
| CODI_IMP_PIS | integer(4) |  | S | Código do imposto PIS |
| CODI_IMP_COFINS | integer(4) |  | S | Código do imposto COFINS |
| IMPORTAR_PROD | char(1) |  |  | Importar movimento de produtos das notas de saída |
| PROCURA_PROD | char(1) |  |  | Campo a ser considerado para verificar a existência do produto |
| COMPLEMENTO_CFOP_CAT_17_99 | integer(4) |  | S | Complemento padrão do ICMS-CAT 17/99 |
| CONTA_MESMO_GRUPO_CNPJ | char(1) |  |  | Utilizar a mesma conta do grupo CNPJ do fornecedor/cliente |
| PRODUTOS_NOTAS_SEGMENTADAS | char(1) |  |  | Produtos para notas segmentadas |
| REORDENAR_CODIGO_FORCLI | char(1) |  |  | Não gerar intervalo no código sequencial do fornecedor/cliente |
| VERIFICACAO_EXISTENCIA_UNIDADE_ARQUIVO | char(1) |  |  | Verificar a existência da unidade no arquivo |
| VERIFICACAO_EXISTENCIA_UNIDADE_SISTEMA | char(1) |  |  | Verificar a existência da unidade no sistema |
| INSS_RECEITA_BRUTA_CONFORME_PRODUTOS | char(1) |  |  | Gerar valores para o cálculo do INSS Receita Bruta conforme produtos |
| INSS_RECEITA_BRUTA_CONFORME_ACUMULADORES | char(1) |  |  | Gerar valores para o cálculo do INSS Receita Bruta conforme acumuladores |
| PROD_NOVO | char(1) |  |  | Quando o produto a ser importado não estiver cadastrado |
| FORMATO_LETRAS_CADASTROS | char(1) |  |  | Formato de letras nos cadastros |
| CRIAR_CONTA_FORNECEDOR | char(1) |  |  | Criar conta contábil fornecedor |
| CRIAR_CONTA_CLIENTE | char(1) |  |  | Criar conta contábil cliente |
| CONSIDERAR_MUNICIPIO_FORCLI_CPF | char(1) |  |  | Considerar o município para cadastrar um novo quando a inscrição for CPF |
| REALIZAR_VALIDACAO_PRODUTOS | char(1) |  |  | Realizar a validação dos produtos |
| TABELA_ICMS_PROD | integer(4) |  | S | Tabela de alíquota interestadual de ICMS |
| IMPORTAR_REGISTRO_F100 | char(1) |  |  | Importar documentos não fiscais do registro F100 |
| IMPORTAR_CADASTRO_TANQUES_BICOS_BOMBAS | char(1) |  |  | Importar cadastros de tanques, bicos e bombas |
| IMPORTAR_ALTERACOES_CADASTRO_BOMBAS | char(1) |  |  | Importar alterações do cadastro das bombas |
| PRODUTO_EM_DUPLICIDADE | char(1) |  | S | Quando o produto a ser importado estiver cadastrado em duplicidade |
| CRIAR_CONTA_FORCLI_PARA | char(1) |  |  | Criar conta contábil para: |
| CONTA_MESMO_CPF | char(1) |  |  | Utilizar a mesma conta para fornecedor/cliente com o mesmo CPF |
