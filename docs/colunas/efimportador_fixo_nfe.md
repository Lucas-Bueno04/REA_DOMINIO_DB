# EFIMPORTADOR_FIXO_NFE — Configuração do leiaute NF-e XML do Importador Fixo
1.220 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| SOBRESCREVER_CADASTROS | char(1) |  |  | Sobrescrever cadastros existentes |
| SOBRESCREVER_MOVIMENTOS | char(1) |  |  | Sobrescrever movimentos existentes |
| IDENTIFICACAO_FORCLI | integer(4) |  |  | Identificação do cadastro do fornecedor/cliente |
| DATA_CADASTRO_FORCLI | char(1) |  |  | Data do cadastro do fornecedor/cliente |
| CRIAR_CONTA_FORCLI | char(1) |  |  | Criar conta contábil para fornecedor/cliente |
| IMPOSTOS_SEGMENTADA | char(1) |  |  | Define onde irão os impostos em notas segmentadas |
| CODI_IMP_PIS | integer(4) |  | S | Código do imposto PIS |
| CODI_IMP_COFINS | integer(4) |  | S | Código do imposto COFINS |
| CODI_ESP | integer(4) |  |  | Código da espécie do documento modelo NF-e |
| CONTA_MESMO_GRUPO_CNPJ | char(1) |  |  | Utilizar a mesma conta do grupo CNPJ do fornecedor/cliente |
| CODI_ESP_AVULSA | integer(4) |  |  | Código da espécie do documento modelo NF-e avulsa. |
| FORMATO_LETRAS_CADASTROS | char(1) |  |  | Formato de letras nos cadastros |
| REORDENAR_CODIGO_FORCLI | char(1) |  |  | Não gerar intervalo no código sequencial do fornecedor/cliente |
| INSS_RECEITA_BRUTA_CONFORME_PRODUTOS | char(1) |  |  | Gerar valores para o cálculo do INSS Receita Bruta conforme produtos |
| INSS_RECEITA_BRUTA_CONFORME_ACUMULADORES | char(1) |  |  | Gerar valores para o cálculo do INSS Receita Bruta conforme acumuladores |
| CRIAR_CONTA_FORNECEDOR | char(1) |  |  | Criar conta contábil fornecedor |
| CRIAR_CONTA_CLIENTE | char(1) |  |  | Criar conta contábil cliente |
| CONSIDERAR_MUNICIPIO_FORCLI_CPF | char(1) |  |  | Considerar o município para cadastrar um novo quando a inscrição for CPF |
| CRIAR_CONTA_FORCLI_PARA | char(1) |  |  | Criar conta contábil para: |
| SOBRESCREVER_OPCOES_CADASTROS | char(1) |  |  | Sobrescrever registros existentes(T - Todos os cadastros/C - Somente Clientes e Fornecedores/P - Somente Produtos) |
| CONTA_MESMO_CPF | char(1) |  |  | Utilizar a mesma conta para fornecedor/cliente com o mesmo CPF |
| CONTA_PADRAO_CLIENTES | integer(4) |  | S | Conta padrÃ£o clientes CPF/CNPJ |
| NAO_VERIFICAR_NOTAS_BANCO | char(1) |  |  | Não verificar a existência dos documentos nos lançamentos. |
