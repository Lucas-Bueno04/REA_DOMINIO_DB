# EFIMPORTADOR_FIXO_NFSE — Configuração do leiaute NFS-e XML do Importador Fixo
1.190 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| SOBRESCREVER_CADASTROS | char(1) |  |  | Sobrescrever cadastros existentes |
| SOBRESCREVER_MOVIMENTOS | char(1) |  |  | Sobrescrever movimentos existentes |
| IDENTIFICACAO_FORCLI | integer(4) |  |  | Identificação do cadastro do fornecedor/cliente |
| CRIAR_CONTA_FORCLI | char(1) |  |  | Criar conta contábil para fornecedor/cliente |
| CONTA_MESMO_GRUPO_CNPJ | char(1) |  |  | Utilizar a mesma conta do grupo CNPJ do fornecedor/cliente |
| DATA_CADASTRO_FORCLI | char(1) |  |  | Data do cadastro do fornecedor/cliente |
| FORMATO_LETRAS_CADASTROS | char(1) |  |  | Formato de letras nos cadastros |
| CRIAR_CONTA_FORNECEDOR | char(1) |  |  | Criar conta contábil fornecedor |
| REORDENAR_CODIGO_FORCLI | char(1) |  |  | Não gerar intervalo no código sequencial do fornecedor/cliente |
| CONSIDERAR_MUNICIPIO_FORCLI_CPF | char(1) |  |  | Considerar o município para cadastrar um novo quando a inscrição for CPF |
| CODI_IMP_PIS | integer(4) |  | S | Código do imposto PIS |
| CODI_IMP_COFINS | integer(4) |  | S | Código do imposto COFINS |
| INSS_RECEITA_BRUTA_CONFORME_PRODUTOS | char(1) |  |  | Gerar valores para o cálculo do INSS Receita Bruta conforme produtos |
| INSS_RECEITA_BRUTA_CONFORME_ACUMULADORES | char(1) |  |  | Gerar valores para o cálculo do INSS Receita Bruta conforme acumuladores |
| CODI_ESP | integer(4) |  |  | Código da espécie do documento modelo NFS-e |
| SERIE | char(7) |  |  | Série do documento modelo NFS-e |
| CONSIDERAR_MUNICIPIO_CADASTRO_EMPRESA | char(1) |  | S | Considerar município do cadastro da empresa |
| CRIAR_CONTA_FORCLI_PARA | char(1) |  |  | Criar conta contábil para: |
