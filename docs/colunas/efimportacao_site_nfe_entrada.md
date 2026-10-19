# EFIMPORTACAO_SITE_NFE_ENTRADA — Configuração da importação da NFe - Entrada
1.210 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| DIFERENCA_BC_ICMS_EXCECAO | char(1) |  |  | Definir exceção para diferença entre valor contábil e base de cálculo ICMS |
| DEFINICAO_BC_ICMS_EXCECAO | char(1) |  | S | Lançar diferença entre valor contábil e base de cálculo ICMS em |
| NAO_CONSIDERA_DEFINICAO_VALORES | char(1) |  |  | Não considerar as definições para os valores de IPI e SUBTRI da linha do ICMS |
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
| DETERMINAR_RELACIONAMENTO_CST_IPI | char(1) |  |  | IPI - Determinar o relacionamento de CST |
| DEFINIR_EXCECAO_RELACIONAMENTO_CST_IPI | char(1) |  |  | IPI - Definir exceção do relacionamento de CST |
| DEFINICAO_EXCECAO_RELACIONAMENTO_CST_IPI | integer(4) |  | S | IPI - Definição da exceção do relacionamento de CST |
| DEFINIR_EXCECAO_PIS_COFINS_CONFORME_CFOP | char(1) |  |  | Definir exceção dos dados de PIS/COFINS |
| DEFINICAO_EXCECAO_PIS_COFINS_CONFORME_CFOP | char(1) |  | S | Definição da exceção dos dados de PIS/COFINS |
| REALIZAR_LANCAMENTO_PRODUTO_GENERICO | char(1) |  |  | Realizar lançamento de produto genérico |
| IMPORTAR_DESCRICAO_COMPLEMENTAR_PRODUTO | char(1) |  | S | Importar descrição complementar do produto |
