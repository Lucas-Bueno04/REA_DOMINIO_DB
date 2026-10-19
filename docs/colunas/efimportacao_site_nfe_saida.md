# EFIMPORTACAO_SITE_NFE_SAIDA — Configuração da importação da NFe - Saída
1.210 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| DIFERENCA_BC_ICMS_EXCECAO | char(1) |  |  | Definir exceção para diferença entre valor contábil e base de cálculo ICMS |
| DEFINICAO_BC_ICMS_EXCECAO | char(1) |  | S | Lançar diferença entre valor contábil e base de cálculo ICMS em |
| NAO_CONSIDERAR_DIFERENCA_BC_IPI_EXCECAO | char(1) |  |  | Não considerar as definições para os valores do IPI |
| DEFINICAO_DIFERENCA_BC_IPI_EXCECAO | char(1) |  | S | Lançar IPI em |
| NAO_CONSIDERAR_DIFERENCA_BC_SUBTRI_EXCECAO | char(1) |  |  | Não considerar as definições para os valores do SUBTRI |
| DEFINICAO_DIFERENCA_BC_SUBTRI_EXCECAO | char(1) |  | S | Lançar SUBTRI em |
| PROTEGE_GO_DETERMINAR_DISPOSITIVO_SEM_BENEFICIO_FISCAL | char(1) |  |  | Determinar dispositivo para os produtos que não foram relacionados no Benefício Fiscal |
| DATA_CUPOM_FISCAL_REFERENCIADO | char(1) |  |  | Data do Cupom Fiscal Referenciado |
| PRODUTOS_DEFINE_CONTA | char(1) |  |  | Produtos - Define conta contábil |
| PRODUTOS_CONTA_EM_SEU_PODER | integer(4) |  | S | Produtos - Conta contábil - Em seu poder |
| PRODUTOS_CONTA_EM_PODER_DE_TERCEIROS | integer(4) |  | S | Produtos - Conta contábil - Em poder de terceiros |
| PRODUTOS_CONTA_DE_TERCEIROS_EM_SEU_PODER | integer(4) |  | S | Produtos - Conta contábil - De terceiros em seu poder |
| DEFINIR_EXCECAO_DIFERENCA_BC_IPI | char(1) |  |  | Definir exceção para diferença entre valor contábil e base de cálculo IPI |
| DEFINICAO_EXCECAO_DIFERENCA_BC_IPI | char(1) |  | S | Lançar diferença entre valor contábil e base de cálculo IPI em (I=Isentas/ O=Outras/ N=Nenhuma) |
| NAO_CONSIDERAR_DIFERENCA_BC_SUBTRI_EXCECAO_IPI | char(1) |  |  | IPI - Não considerar as definições para os valores do SUBTRI |
| DEFINICAO_DIFERENCA_BC_SUBTRI_EXCECAO_IPI | char(1) |  | S | IPI - Lançar SUBTRI em |
| NAO_INCLUIR_CODIGO_ATIVIDADE_INSS | char(1) |  |  | Não incluir o código de atividade conforme NCM para cálculo do INSS Receita Bruta |
| TIPO_ITEM_NOVOS_PRODUTOS | char(1) |  |  | Tipo do item a ser informado no cadastro de novos produtos |
| TIPO_ITEM_DEFINIR_EXCECAO | char(1) |  |  | Definir exceção do tipo do item |
| TIPO_ITEM_EXCECAO | integer(4) |  | S | Exceção do tipo do item |
| CFOP_EXCECAO | char(1) |  |  |  |
| CFOP_ESTADUAL_EXCECAO | integer(4) |  | S |  |
| VERSAO_CFOP_ESTADUAL_EXCECAO | smallint(2) |  | S |  |
| CFOP_INTERESTADUAL_EXCECAO | integer(4) |  | S |  |
| VERSAO_CFOP_INTERESTADUAL_EXCECAO | smallint(2) |  | S |  |
| DEFINIR_EXCECAO_PIS_COFINS_CONFORME_CFOP | char(1) |  |  | Definir exceção dos dados de PIS/COFINS |
| DEFINICAO_EXCECAO_PIS_COFINS_CONFORME_CFOP | char(1) |  | S | Definição da exceção dos dados de PIS/COFINS |
| REALIZAR_LANCAMENTO_PRODUTO_GENERICO | char(1) |  |  | Realizar lançamento de produto genérico |
| CONSIDERAR_TODOS_COMO_EXCECAO_CFOP_SAI | char(1) |  | S | Considerar como exceÃ§Ã£o a opÃ§Ã£o "Todos" das colunas para relacionamento do CFOP saÃ­da |
| IMPORTAR_DESCRICAO_COMPLEMENTAR_PRODUTO | char(1) |  | S | Importar descrição complementar do produto |
