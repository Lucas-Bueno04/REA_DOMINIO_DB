# EFIMPORTADOR_FIXO_SPED_FISCAL_CFE_SAIDA — Configuração do leiaute CF-e do Importador Fixo SPED Fiscal - Saída
1.077 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CONSIDERAR_ICMS_ACUMULADOR | char(1) |  |  | Considerar o percentual de base de cálculo e alíquota do ICMS do cadastro do acumulador |
| GERAR_LANCAMENTOS_CONTABEIS | char(1) |  |  | Gerar lançamentos contábeis |
| REORDENAR_CODIGO_CUPONS | char(1) |  |  | Gravar os cupons importados na ordem do número do documento e sem intervalo no código sequencial |
| IDENTIFICAR_PRODUTO_RELACIONAR_ACUMULADOR | char(1) |  |  | Identificar o produto para relacionar ao acumulador por |
| CODI_CLI_PADRAO | integer(4) |  | S | Cliente padrão |
| UTILIZAR_CLIENTE_PADRAO_QUANDO | integer(4) |  |  | Utilizar o cliente padrão quando |
| ACUMULADOR_EXCECAO | char(1) |  |  | Definir acumulador para exceção |
| CODI_ACU_EXCECAO | integer(4) |  | S | Código do acumulador para exceção |
| IMPORTAR_PROD | char(1) |  |  | Importar produtos e movimentação de produtos |
| PROCURA_PROD | char(1) |  |  | Campo a ser considerado para verificar a existência do produto |
| PROD_NOVO | char(1) |  |  | Quando o produto a ser importado não estiver cadastrado |
| CODI_GRU | integer(4) |  | S | Grupo para cadastros de produtos |
| TABELA_ICMS_PROD | integer(4) |  | S | Tabela de alíquota interestadual de ICMS |
| PRODUTOS_DEFINE_CONTA | char(1) |  |  | Produtos - Define conta contábil |
| PRODUTOS_CONTA_EM_SEU_PODER | integer(4) |  | S | Produtos - Conta contábil - Em seu poder |
| PRODUTOS_CONTA_EM_PODER_DE_TERCEIROS | integer(4) |  | S | Produtos - Conta contábil - Em poder de terceiros |
| PRODUTOS_CONTA_DE_TERCEIROS_EM_SEU_PODER | integer(4) |  | S | Produtos - Conta contábil - De terceiros em seu poder |
| DIFERENCA_BC_ICMS_EXCECAO | char(1) |  |  | Diferença base de cálculo para exceção |
| DEFINICAO_BC_ICMS_EXCECAO | char(1) |  | S | Definição da diferença base de cálculo para exceção |
| CUPOM_FISCAL_ELETRONICO_LANCAMENTO_CANCELAMENTO | integer(4) |  |  | Data lançamento documento cancelado |
