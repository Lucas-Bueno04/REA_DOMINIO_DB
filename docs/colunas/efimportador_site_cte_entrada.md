# EFIMPORTADOR_SITE_CTE_ENTRADA — Configuração da importação do CT-e pelo site da Receita Federal - Entrada
1.254 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| IGNORAR_IMPOSTOS_NAO_DEF_ACU | char(1) |  |  | Ignorar impostos não definidos no acumulador |
| CONSIDERAR_ICMS_ACUMULADOR | char(1) |  |  | Considerar as definições do imposto ICMS do cadastro do acumulador |
| GERAR_OBSERVACAO_ACUMULADOR | char(1) |  |  | Gerar observação informada no cadastro do acumulador |
| INFORMAR_DATA_ENTRADA | char(1) |  |  | Informar data de entrada no momento da importação |
| GERAR_LANCAMENTOS_CONTABEIS | char(1) |  |  | Gerar lançamentos contábeis |
| CFOP_EXCESSAO | char(1) |  |  | Definir CFOPs para exceção |
| CFOP_ESTADUAL_EXCECAO | integer(4) |  | S | CFOP para exceção nas entradas estaduais |
| VERSAO_CFOP_ESTADUAL_EXCECAO | smallint(2) |  | S | Versão do CFOP para exceção nas entradas estaduais |
| CFOP_INTERESTADUAL_EXCECAO | integer(4) |  | S | CFOP para exceção nas entradas interestaduais |
| VERSAO_CFOP_INTERESTADUAL_EXCECAO | smallint(2) |  | S | Versão do CFOP para exceção nas entradas interestaduais |
| ACUMULADOR_EXCECAO | char(1) |  |  | Definir acumulador para exceção |
| CODI_ACU_EXCECAO | integer(4) |  | S | Código do acumulador para exceção |
| CST_CSOSN_EXCECAO | char(1) |  |  | Definir exceção para CST/CSOSN |
| GERAR_CST_CSOSN_INFORMADO_NOTA | char(1) |  |  | Gerar CST/CSOSN informado na nota |
| CST_CSOSN_DEFINIDO | integer(4) |  | S | Código do CST/CSOSN para exceção das entradas |
| I_SEQUENCIAL_CST_CSOSN_DEFINIDO | integer(4) |  | S | Chave sequencial do CST/CSOSN para exceção das entradas |
| GERAR_INFO_COMPLEMENTAR_ACUMULADOR | char(1) |  |  | Gerar informações complementares informada no cadastro do acumulador (S/N) |
| PERMITE_RELACIONAR_CFOP_MAIS_ACU | char(1) |  |  | Permitir relacionar o mesmo CFOP de entrada para mais de um acumulador |
| DIFERENCA_BC_ICMS_EXCECAO | char(1) |  |  | Definir exceção para diferença entre valor contábil e base de cálculo ICMS |
| DEFINICAO_BC_ICMS_EXCECAO | char(1) |  | S | Lançar diferença entre valor contábil e base de cálculo ICMS em |
| INCLUI_IPI_NOTA_SEM_IPI | char(1) |  |  | Incluir o imposto IPI nas notas que não possuem IPI e o imposto estiver informado no acumulador |
| IMPORTAR_VALOR_CONTABIL_ATRAVES | char(1) |  |  | Importar o Valor Contábil através do campo |
| DEDUZIR_VALOR_ICMS_BASE_CALCULO_PISCOFINS_DEVOLUCAO | varchar(1) |  |  | Deduzir o valor do ICMS da base de cálculo do PIS e COFINS nas notas de devolução |
| DEDUZIR_VALOR_ICMS_BASE_CALCULO_PISCOFINS_DEFINICAO | char(1) |  |  | Deduzir o valor do ICMS da base de cálculo do PIS e COFINS nas notas de devolução - Definição (D-Notas de devolução/E-Notas de entradas/T-Devolução e Entradas) |
| DEDUZIR_VALOR_DIFALNC_FCP_BASE_CALCULO_PISCOFINS_ENTRADA | char(1) |  | S | Deduzir o imposto 145-DIFAL-NC e 146-FCP da base de cÃ¡lculo do PIS/COFINS. (Entrada) |
| NOTAS_FISCAIS_REFERENCIADAS_TIPO_OPERACAO | char(1) |  |  | Documentos referenciados - Notas fiscais - Tipo de operação |
| NOTAS_FISCAIS_REFERENCIADAS_TIPO_EMITENTE | char(1) |  |  | Documentos referenciados - Notas fiscais - Tipo de emitente |
| DEDUZIR_VALOR_DIFALNC_FCP_BASE_CALCULO_PISCOFINS_ENTRADA_DEFINICAO | char(1) |  |  | Deduzir o imposto 145-DIFAL-NC e 146-FCP da base de cÃ¡lculo do PIS/COFINS. (Entrada) - DefiniÃ§Ã£o (A-DIFAL-NC e FCP/D-Valor do DIFAL-NC/F-Valor do FCP) |
| CONSIDERAR_ICMS_ACUMULADOR_DEFINICAO | char(1) |  |  | Considerar as definiÃ§Ãµes do imposto ICMS do cadastro do acumulador - DefiniÃ§Ã£o |
