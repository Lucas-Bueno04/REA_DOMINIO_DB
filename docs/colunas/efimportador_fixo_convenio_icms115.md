# EFIMPORTADOR_FIXO_CONVENIO_ICMS115 — Configuração do leiaute Convênio ICMS 115/03
20 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| SOBRESCREVER_MOVIMENTOS | char(1) |  |  | Sobrescrever movimentos existentes |
| ACUMULADOR_EXCECAO | char(1) |  |  | Definir acumulador para exceção |
| CODI_ACU_EXCECAO | integer(4) |  | S | Código do acumulador para exceção |
| IMPORTAR_PROD | char(1) |  |  | Importar movimento de produtos das notas de saída |
| PROCURA_PROD | char(1) |  |  | Campo a ser considerado para verificar a existência do produto |
| PROD_NOVO | char(1) |  |  | Quando o produto a ser importado não estiver cadastrado |
| CODI_GRU | integer(4) |  | S | Grupo para cadastros de produtos |
| COMPLEMENTO_CFOP_CAT_17_99 | integer(4) |  | S | Complemento padrão do ICMS-CAT 17/99 |
| TABELA_ICMS_PROD | integer(4) |  | S | Tabela de alíquota interestadual de ICMS |
| CRIAR_CONTA_FORCLI | char(1) |  |  | Criar conta contábil para fornecedor/cliente |
| CONTA_MESMO_GRUPO_CNPJ | char(1) |  |  | Utilizar a mesma conta do grupo CNPJ do fornecedor/cliente |
| CRIAR_CONTA_FORNECEDOR | char(1) |  |  | Criar conta contábil fornecedor |
| IDENTIFICACAO_FORCLI | integer(4) |  |  | Identificação do cadastro do fornecedor/cliente |
| DETERMINA_TIPO_ASSINANTE_PADRAO_SAI | char(1) |  |  | Determinar tipo de assinante padrão para notas de saída de comunicação/telecomunicação |
| TIPO_ASSINANTE_SAI | integer(4) |  | S | Tipo de assinante padrão para notas de saída de comunicação/telecomunicação |
| IMPORTAR_MUNICIPIO_ORIGEM_CONFORME_EMPRESA | char(1) |  |  | Importar o Município Origem conforme o município da empresa |
