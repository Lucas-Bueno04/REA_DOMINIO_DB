# EFIMPORTADOR_FIXO_CAT52 — Configuração do leiaute CAT52 do Importador Fixo
1.191 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| SOBRESCREVER_MOVIMENTOS | char(1) |  |  | Sobrescrever movimentos existentes |
| DATA_CADASTRO_CLI | char(1) |  |  | Data do cadastro do cliente |
| DADOS_EXCECAO | char(1) |  |  | Definir dados para exceção |
| CFOP_EXCECAO | integer(4) |  | S | CFOP para exceção |
| VERSAO_CFOP_EXCECAO | smallint(2) |  | S | Versão do CFOP para exceção |
| CODI_ACU_EXCECAO | integer(4) |  | S | Código do acumulador para exceção |
| IMPORTAR_PROD | char(1) |  |  | Importar movimento de produtos das notas de saída |
| PROCURA_PROD | char(1) |  |  | Campo a ser considerado para verificar a existência do produto |
| CODI_GRU | integer(4) |  | S | Grupo para cadastros novos de produtos |
| COMPLEMENTO_CFOP_CAT_17_99 | integer(4) |  | S | Complemento padrão do ICMS-CAT 17/99 |
| AJUSTAR_DIFERENCA_ICMS_ESTOQUE | char(1) |  | S | Ajustar diferença entre o valor do ICMS do estoque com o valor do ICMS das situações tributárias(S/N) |
| GERAR_LANCAMENTOS_CONTABEIS | char(1) |  |  | Gerar lançamentos contábeis |
| UTILIZAR_CLIENTE_PADRAO_PARAMETROS | char(1) |  |  | Utilizar o cliente padrão informado nos parâmetros |
| UTILIZAR_CLIENTE_PADRAO_PARAMETROS_QUANDO | integer(4) |  | S | Utilizar o cliente padrão informado nos parâmetros quando |
| BILHETE_PASSAGEM_MUNICIPIO_ORIGEM_MESMO_EMPRESA | char(1) |  |  | Redução Z - Bilhete de Passagem - Informar o município de origem o mesmo município do cadastro de empresa |
| PROD_NOVO | char(1) |  |  | Quando o produto a ser importado não estiver cadastrado |
| DEFINIR_CFOPS_ACUMULADORES | integer(4) |  |  | Definir CFOPs/Acumuladores |
| CODIGO_UNIDADE_PADRAO | integer(4) |  | S | Unidade inventariada a ser utilizada quando não existir no arquivo |
| CRIAR_CONTA_FORCLI | char(1) |  |  | Criar conta contábil para cliente |
| CONTA_MESMO_GRUPO_CNPJ | char(1) |  |  | Utilizar a mesma conta do grupo CNPJ do cliente |
| RATEAR_DESCONTO_CUPOM_FISCAL_PRODUTOS | char(1) |  |  | Ratear o valor do desconto informado no cupom fiscal entre os produtos |
| RATEAR_ACRESCIMO_CUPOM_FISCAL_PRODUTOS | char(1) |  |  | Ratear o valor do acréscimo informado no cupom fiscal entre os produtos |
| TABELA_ICMS_PROD | integer(4) |  | S | Tabela de alíquota interestadual de ICMS |
| CONSIDERAR_SITUACAO_TRIBUTARIA_PRODUTOS | char(1) |  |  | Considerar a Situação Tributária informada nos produtos |
| DETERMINAR_DADOS_PIS_COFINS | char(1) |  |  | Determinar o CST de PIS/COFINS ao cadastrar novos produtos |
| IDENTIFICAR_PRODUTO_RELACIONAR_ACUMULADOR_POR | char(1) |  |  | Identificar o produto para relacionar ao acumulador por |
| MANTER_DADOS_QUANDO_ALTERADO_CONTADOR_REINICIO | char(1) |  |  | Manter o contador de operaÃ§Ã£o inicial, o grande total anterior e o nÃºmero do mapa resumo quando alterado o contador de reinÃ­cio |
| CONSIDERAR_ICMS_ACUMULADOR | char(1) |  |  | Considerar as definições do ICMS do cadastro do acumulador |
| SELECIONAR_MEIOS_PAGAMENTOS_UTILIZADOS | char(1) |  |  | Selecionar os meios de pagamentos que serão utilizados na importação |
| PRODUTO_EM_DUPLICIDADE | char(1) |  | S | Quando o produto a ser importado estiver cadastrado em duplicidade |
