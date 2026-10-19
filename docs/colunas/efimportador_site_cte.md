# EFIMPORTADOR_SITE_CTE — Configuração da importação do CT-e pelo site da Receita Federal
1.255 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| SOBRESCREVER_CADASTROS | char(1) |  |  | Sobrescrever cadastros existentes |
| SOBRESCREVER_MOVIMENTOS | char(1) |  |  | Sobrescrever movimentos existentes |
| IDENTIFICACAO_FORCLI | integer(4) |  |  | Identificação do cadastro do fornecedor/cliente |
| DATA_CADASTRO_FORCLI | char(1) |  |  | Data do cadastro do fornecedor/cliente |
| CRIAR_CONTA_FORCLI | char(1) |  |  | Criar conta contábil para fornecedor/cliente |
| CONTA_MESMO_GRUPO_CNPJ | char(1) |  |  | Utilizar a mesma conta do grupo CNPJ do fornecedor/cliente |
| CODI_IMP_PIS | integer(4) |  | S | Código do imposto PIS |
| CODI_IMP_COFINS | integer(4) |  | S | Código do imposto COFINS |
| CONSIDERAR_MUNICIPIO_FORCLI_CPF | char(1) |  |  | Considerar o município para cadastrar um novo quando a inscrição for CPF |
| FORMATO_LETRAS_CADASTROS | char(1) |  |  | Formato de letras nos cadastros |
| CONSULTA_COMPLETA_ORIGEM_CERTIFICADO | char(1) |  |  | Realizar a consulta completa da CT-e com o certificado digital do(a): (E: Empresa, C: Contador) |
