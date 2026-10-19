# EFIMPORTADOR_FIXO_CTE — Configuração do leiaute CT-e XML do Importador Fixo
1.260 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| SOBRESCREVER_CADASTROS | char(1) |  |  | Sobrescrever cadastros existentes |
| SOBRESCREVER_MOVIMENTOS | char(1) |  |  | Sobrescrever movimentos existentes |
| IDENTIFICACAO_FORCLI | integer(4) |  |  | Identificação do cadastro do fornecedor/cliente |
| DATA_CADASTRO_FORCLI | char(1) |  |  | Data do cadastro do fornecedor/cliente |
| CRIAR_CONTA_FORCLI | char(1) |  |  | Criar conta contábil para fornecedor/cliente |
| CODI_IMP_PIS | integer(4) |  | S | Código do imposto PIS |
| CODI_IMP_COFINS | integer(4) |  | S | Código do imposto COFINS |
| CODI_ESP | integer(4) |  |  | Código da espécie do documento modelo CT-e |
| CONTA_MESMO_GRUPO_CNPJ | char(1) |  |  | Utilizar a mesma conta do grupo CNPJ do fornecedor/cliente |
| REORDENAR_CODIGO_FORCLI | char(1) |  |  | Não gerar intervalo no código sequencial do fornecedor/cliente |
| CONSIDERAR_MUNICIPIO_FORCLI_CPF | char(1) |  |  | Considerar o município para cadastrar um novo quando a inscrição for CPF |
| CODI_ESP_OS | integer(4) |  | S | Código da espécie do documento modelo CT-eOS. |
| NAO_VERIFICAR_NOTAS_BANCO | char(1) |  |  | Não verificar a existência dos documentos nos lançamentos. |
| FORMATO_LETRAS_CADASTROS | char(1) |  |  | Formato de letras nos cadastros |
