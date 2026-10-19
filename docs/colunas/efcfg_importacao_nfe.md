# efcfg_importacao_nfe — Configuracao de importacao da Nota Fiscal Eletronica
3.104 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo da empresa |
| nota | integer(4) | PK |  | Tipo de nota(1 - entradas/2 - saidas/3 - servicos) |
| tipo_rps | integer(4) |  | S | Codigo da especie |
| tipo_rpsm | integer(4) |  | S | Codigo da especie |
| tipo_rpsc | integer(4) |  | S | Codigo da especie |
| situacao_t | integer(4) |  | S | Codigo do acumulador |
| situacao_i | integer(4) |  | S | Codigo do acumulador |
| situacao_f | integer(4) |  | S | Codigo do acumulador |
| situacao_c | integer(4) |  | S | Codigo do acumulador |
| situacao_e | integer(4) |  | S | Codigo do acumulador |
| situacao_j | integer(4) |  | S | Codigo do acumulador |
| SITUACAO_T_RETIDO | integer(4) |  | S | Código do acumulador Retido |
| TIPO_NOTA_I_TABELA | integer(4) |  | S | Tipo nota - Codigo da Tabela Municipal |
| TIPO_NOTA_I_ITEM | char(20) |  | S | Tipo nota - Valor do item |
| TIPO_NOTA_IMPORTAR | char(1) |  | S | Tipo nota - Importar (P=Conforme padrao do acumulador/ I=Informar/ N=Nao importar) |
| SERVICO_PRESTADO_I_TABELA | integer(4) |  | S | Servico Prestado - Codigo da Tabela Municipal |
| SERVICO_PRESTADO_I_ITEM | char(20) |  | S | Servico Prestado - Valor do item |
| SERVICO_PRESTADO_IMPORTAR | char(1) |  | S | Servico Prestado - Importar (A=Conforme informacao no arquivo/ P=Conforme informacao do acumulador/ I=Informar/ N=Nao importar) |
| SITUACAO_NF_I_TABELA | integer(4) |  | S | Situacao Nota Fiscal - Codigo da Tabela Municipal |
| SITUACAO_NF_I_ITEM | char(20) |  | S | Situacao Nota Fiscal - Valor do item |
| SITUACAO_NF_IMPORTAR | char(1) |  | S | Servico Prestado - Importar (A=Conforme informacao no arquivo/ P=Conforme informacao do acumulador/ I=Informar/ N=Nao importar) |
| OBJETO_ISENCAO_I_TABELA | integer(4) |  | S | Objeto Isencao - Codigo da Tabela Municipal |
| OBJETO_ISENCAO_I_ITEM | char(20) |  | S | Objeto Isencao - Valor do item |
| OBJETO_ISENCAO_IMPORTAR | char(1) |  | S | Tipo nota - Importar (P=Conforme padrao do acumulador/ I=Informar/ N=Nao importar) |
| ESPECIE_DOC_DISPENSADO | integer(4) |  | S | Código da espécie do documento dispensado |
| ESPECIE_DOC_AUTORIZADO | integer(4) |  | S | Código da espécie do documento autorizado |
| ESPECIE_DOC_OBRIGADO | integer(4) |  | S | Código da espécie do documento obrigado |
| SITUACAO_S | integer(4) |  | S | Codigo do acumulador |
| SITUACAO_A | integer(4) |  | S | Codigo do acumulador |
| SITUACAO_B | integer(4) |  | S | Codigo do acumulador |
| SITUACAO_M | integer(4) |  | S | Codigo do acumulador |
| SITUACAO_N | integer(4) |  | S | Codigo do acumulador |
| SITUACAO_X | integer(4) |  | S | Codigo do acumulador |
| SITUACAO_V | integer(4) |  | S | Codigo do acumulador |
| SITUACAO_P | integer(4) |  | S | Codigo do acumulador |
| SOBRESCREVER_MOVIMENTOS | char(1) |  |  | Sobrescrever movimentos existentes |
| CRIAR_CONTA_FORCLI | char(1) |  |  | Criar conta contábil para fornecedor/cliente |
| CONTA_MESMO_GRUPO_CNPJ | char(1) |  |  | Utilizar a mesma conta do grupo CNPJ do fornecedor/cliente |
| DATA_CADASTRO_FORCLI | char(1) |  |  | Data do cadastro do fornecedor/cliente |
| FORMATO_LETRAS_CADASTROS | char(1) |  |  | Formato de letras nos cadastros |
| CRIAR_CONTA_CLIENTE | char(1) |  |  | Criar conta contábil cliente |
| CRIAR_CONTA_FORNECEDOR | char(1) |  |  | Criar conta contábil fornecedor |
| CODI_CLI_PADRAO | integer(4) |  | S | Cliente padrão |
| UTILIZAR_CLIENTE_PADRAO | char(1) |  |  | Utilizar o cliente padrão |
| IMPORTAR_SERVICO_PRESTADO_NA_OBS | char(1) |  |  | Importar o código do serviço prestado para o campo observação |
| GERAR_LANCAMENTOS_CONTABEIS | char(1) |  |  | Gerar lançamentos contábeis |
| CONSIDERAR_ISS_ACUMULADOR | char(1) |  |  | Considerar as definições do imposto ISS do cadastro do acumulador |
| CONSIDERAR_IMPOSTOS_RETIDOS_SOMENTE_ARQUIVO | char(1) |  |  | Considerar os impostos retigos somente se estiverem informados no arquivo |
| CONSIDERAR_CAMPO_DATA | char(1) |  | S | Considerar para a data da nota |
| GERAR_MOVIMENTO_PRODUTOS | char(1) |  |  | Gerar movimento de produtos |
| CODI_PDI_PADRAO | char(14) |  | S | Código produto padrão |
| ACUMULADOR_EXCECAO | char(1) |  |  | Definir acumulador para exceção |
| CODI_ACU_EXCECAO | integer(4) |  | S | Código do acumulador para exceção |
| GERAR_PARCELAS_SAIDAS | varchar(1) |  |  | Gerar parcelas nas notas fiscais de saída |
| GERAR_PARCELAS_ENTRADAS | varchar(1) |  |  | Gerar parcelas nas notas fiscais de entrada |
| GERAR_PARCELAS_SERVICOS | varchar(1) |  |  | Gerar parcelas nas notas fiscais de serviço |
| ITENS_EXCECAO_ENTRADA | char(1) |  |  | Se deve ter produto exceção dos Itens |
| ITENS_EXCECAO_SAIDA | char(1) |  |  | Se deve ter produto exceção dos Itens |
| ITENS_EXCECAO_SERVICO | char(1) |  |  | Se deve ter produto exceção dos Itens |
| CODI_PDI_EXCECAO_ENTRADA | char(14) |  | S | Código do produto exceção dos Itens |
| CODI_PDI_EXCECAO_SAIDA | char(14) |  | S | Código do produto exceção dos Itens |
| CODI_PDI_EXCECAO_SERVICO | char(14) |  | S | Código do produto exceção dos Itens |
| EXCLUIR_MOVIMENTACAO_SERVICOS | varchar(1) |  |  | Excluir movimentação de itens |
| EXCLUIR_MOVIMENTACAO_SAIDAS | varchar(1) |  |  | Excluir movimentação de itens |
| EXCLUIR_MOVIMENTACAO_ENTRADAS | varchar(1) |  |  | Excluir movimentação de itens |
| CONSIDERAR_CLIENTE_ESTRANGEIRO | char(1) |  | S | Considerar o cliente como estrangeiro e identificá-lo pela Razão Social quando o mesmo não possuir Inscrição Federal e UF no arquivo |
| CONSIDERAR_TODOS_COMO_EXCECAO_ACU | char(1) |  |  | Considerar como exceção a opção "Todos" das colunas para relacionamento do acumulador |
| INSS_RECEITA_BRUTA_CONFORME_PRODUTOS | char(1) |  | S | Gerar valores para o cálculo do INSS Receita Bruta conforme produtos |
| INSS_RECEITA_BRUTA_CONFORME_ACUMULADORES | char(1) |  | S | Gerar valores para o cálculo do INSS Receita Bruta conforme acumuladores |
| DEDUZIR_ISS_DA_BASE_CALCULO_PIS_COFINS_SAIDA | char(1) |  | S | Deduzir o valor do ISS da base de cÃ¡lculo do PIS e COFINS. (Saida) |
| DEDUZIR_ISS_DA_BASE_CALCULO_PIS_COFINS_SAIDA_DEFINICAO | char(1) |  |  | Deduzir o valor do ISS da base de cÃ¡lculo do PIS e COFINS. (Saida) - DefiniÃ§Ã£o (T-ISS Tributado/R-ISS Retido/A-ISS Tributado e Retido) |
| DEDUZIR_ISS_DA_BASE_CALCULO_PIS_COFINS_SERVICO | char(1) |  | S | Deduzir o valor do ISS da base de cÃ¡lculo do PIS e COFINS. (ServiÃ§o) |
| DEDUZIR_ISS_DA_BASE_CALCULO_PIS_COFINS_SERVICO_DEFINICAO | char(1) |  |  | Deduzir o valor do ISS da base de cÃ¡lculo do PIS e COFINS. (ServiÃ§o) - DefiniÃ§Ã£o (T-ISS Tributado/R-ISS Retido/A-ISS Tributado e Retido) |
