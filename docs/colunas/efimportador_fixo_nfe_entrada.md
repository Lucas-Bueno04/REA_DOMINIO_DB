# EFIMPORTADOR_FIXO_NFE_ENTRADA — Configuração do leiaute NF-e XML do Importador Fixo - Entrada
1.220 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| IMPORTAR_PARCELAS | char(1) |  |  | Importar parcelas |
| IGNORAR_IMPOSTOS_NAO_DEF_ACU | char(1) |  |  | Ignorar impostos não definidos no acumulador |
| CONSIDERAR_ICMS_ACUMULADOR | char(1) |  |  | Considerar o percentual de base de cálculo e alíquota do ICMS do cadastro do acumulador sobre o valor |
| GERAR_OBSERVACAO_ACUMULADOR | char(1) |  |  | Gerar observação informada no cadastro do acumulador |
| CFOP_EXCESSAO | char(1) |  |  | Definir CFOPs para exceção |
| CFOP_ESTADUAL_EXCECAO | integer(4) |  | S | CFOP para exceção nas entradas estaduais |
| VERSAO_CFOP_ESTADUAL_EXCECAO | smallint(2) |  | S | Versão do CFOP para exceção nas entradas estaduais |
| CFOP_INTERESTADUAL_EXCECAO | integer(4) |  | S | CFOP para exceção nas entradas interestaduais |
| VERSAO_CFOP_INTERESTADUAL_EXCECAO | smallint(2) |  | S | Versão do CFOP para exceção nas entradas interestaduais |
| ACUMULADOR_EXCECAO | char(1) |  |  | Definir acumulador para exceção |
| CODI_ACU_EXCECAO | integer(4) |  | S | Código do acumulador para exceção |
| IMPORTAR_PROD | char(1) |  |  | Importar produtos e movimentação de produtos |
| PROCURA_PROD | char(1) |  |  | Campo a ser considerado para verificar a existência do produto |
| PROD_NOVO | char(1) |  |  | Quando o produto a ser importado não estiver cadastrado |
| CODI_GRU | integer(4) |  | S | Grupo para cadastros de produtos |
| COMPLEMENTO_CFOP_CAT_17_99 | integer(4) |  | S | Complemento padrão do ICMS-CAT 17/99 |
| CANC_EXCLUI_MOV_PRODUTOS | char(1) |  |  | Excluir movimentação de produtos |
| CANC_EXCLUI_PARCELAS | char(1) |  |  | Excluir parcelas |
| CANC_EXCLUI_LANCTOS_CONTABEIS | char(1) |  |  | Excluir lançamentos contábeis |
| BENEFICIARIA_CREDITO_PRESUMIDO | char(1) |  | S | Beneficiário de crédito fiscal presumido conforme Art. 24 RICMS |
| DIFERENCA_BC_ICMS_EXCECAO | char(1) |  |  | Diferença base de cálculo para exceção |
| DEFINICAO_BC_ICMS_EXCECAO | char(1) |  | S | Definição da diferença base de cálculo para exceção |
| INFORMAR_DATA_ENTRADA | char(1) |  |  | Informar data de entrada no momento da importação |
| CST_CSOSN_EXCECAO | char(1) |  |  | Definir exceção para CST/CSOSN |
| GERAR_CST_CSOSN_INFORMADO_NOTA | char(1) |  |  | Gerar CST/CSOSN |
| CST_CSOSN_DEFINIDO | integer(4) |  | S | Código do CST/CSOSN para exceção das entradas |
| GERAR_LANCAMENTOS_CONTABEIS | char(1) |  |  | Gerar lançamentos contábeis |
| NAO_CONSIDERA_DEFINICAO_VALORES | char(1) |  |  | Não considerar as definições para os valores de IPI e SUBTRI da linha do ICMS |
| INCLUI_IPI_NOTA_SEM_IPI | char(1) |  |  | Incluir o imposto IPI nas notas que não possuem IPI e o imposto estiver informado no acumulador |
| PRODUTOS_NOTAS_SEGMENTADAS | char(1) |  |  | Produtos para notas segmentadas |
| I_SEQUENCIAL_CST_CSOSN_DEFINIDO | integer(4) |  | S | Chave sequencial do CST/CSOSN para exceção das entradas |
| UTILIZAR_CFOP_CADASTRO_PRODUTO | char(1) |  |  | Efetuar a importação das notas de entrada conforme o CFOP do cadastro de produtos |
| CONSIDERAR_IPI_ACUMULADOR | char(1) |  |  | Considerar as definições do imposto IPI do cadastro do acumulador |
| IMPORTAR_CREDITO_ICMS_ART23 | char(1) |  |  | Importar o valor do crédito do ICMS nos termos do Art. 23 da Lei Complementar 123/2006(Simples Nacional) |
| CONSIDERAR_SUBTRI_ACUMULADOR | char(1) |  |  | Considerar as definições do imposto SUBTRI do cadastro do acumulador |
| DADOS_DO_FRETE_GERAR_LOCAL_SAIDA_EMPRESA | char(1) |  |  | Gerar no local de saída dos dados do frete os dados da empresa |
| DADOS_DO_FRETE_GERAR_LOCAL_RECIBIMENTO_FORNECEDOR | char(1) |  |  | Gerar no local de recebimento dos dados do frete os dados do fornecedor |
| PRODUTOS_DEFINE_CONTA | char(1) |  |  | Produtos - Define conta contábil |
| PRODUTOS_CONTA_EM_SEU_PODER | integer(4) |  | S | Produtos - Conta contábil - Em seu poder |
| PRODUTOS_CONTA_EM_PODER_DE_TERCEIROS | integer(4) |  | S | Produtos - Conta contábil - Em poder de terceiros |
| PRODUTOS_CONTA_DE_TERCEIROS_EM_SEU_PODER | integer(4) |  | S | Produtos - Conta contábil - De terceiros em seu poder |
| DETERMINAR_TIPO_TITULO_PADRAO | char(1) |  |  | Determinar tipo do título padrão para notas a prazo |
| TITULO_PADRAO | integer(4) |  | S | Título padrão para notas a prazo |
| IMPORTAR_TIPO_DOCUMENTO_IMPORTACAO | char(1) |  |  | Informar o tipo do documento de importação (S/N) |
| TIPO_DOCUMENTO_IMPORTACAO | tinyint(1) |  | S | Tipo do documento de importação (0-Declaração de importação/ 1-Declaração simplificada de importação/ 2-Declaração única de importação) |
| DEFINIR_EXCECAO_DIFERENCA_BC_IPI | char(1) |  |  | Definir exceção para diferença entre valor contábil e base de cálculo IPI |
| DEFINICAO_EXCECAO_DIFERENCA_BC_IPI | char(1) |  | S | Lançar diferença entre valor contábil e base de cálculo IPI em (I=Isentas/ O=Outras/ N=Nenhuma) |
| NAO_CONSIDERAR_DIFERENCA_BC_SUBTRI_EXCECAO_IPI | char(1) |  |  | IPI - Não considerar as definições para os valores do SUBTRI |
| DEFINICAO_DIFERENCA_BC_SUBTRI_EXCECAO_IPI | char(1) |  | S | IPI - Lançar SUBTRI em |
| DETERMINAR_DADOS_PIS_COFINS_CONFORME_CFOP | char(1) |  |  | Determinar os dados de PIS/COFINS conforme o CFOP |
| DEFINIR_EXCECAO_PIS_COFINS_CONFORME_CFOP | char(1) |  |  | Definir exceção dos dados de PIS/COFINS |
| DEFINICAO_EXCECAO_PIS_COFINS_CONFORME_CFOP | char(1) |  | S | Definição da exceção dos dados de PIS/COFINS |
| NAO_INCLUIR_CODIGO_ATIVIDADE_INSS | char(1) |  |  | Não incluir o código de atividade conforme NCM para cálculo do INSS Receita Bruta |
| IDENTIFICAR_PRODUTO_RELACIONAR_ACUMULADOR | char(1) |  |  | Identificar o produto para relacionar ao acumulador por |
| TIPO_ITEM_NOVOS_PRODUTOS | char(1) |  |  | Tipo do item a ser informado no cadastro de novos produtos |
| TIPO_ITEM_DEFINIR_EXCECAO | char(1) |  |  | Definir exceção do tipo do item |
| TIPO_ITEM_EXCECAO | integer(4) |  | S | Exceção do tipo do item |
| DETERMINAR_RELACIONAMENTO_CST_IPI | char(1) |  |  | IPI - Determinar o relacionamento de CST |
| DEFINIR_EXCECAO_RELACIONAMENTO_CST_IPI | char(1) |  |  | IPI - Definir exceção do relacionamento de CST |
| DEFINICAO_EXCECAO_RELACIONAMENTO_CST_IPI | integer(4) |  | S | IPI - Definição da exceção do relacionamento de CST |
| TABELA_ICMS_PROD | integer(4) |  | S | Tabela de alíquota interestadual de ICMS |
| IMPORTAR_COMO_EXTEMPORANEA | char(1) |  | S | Importar como extemporânea notas com data de entrada dentro do período fechado |
| DESCONSIDERAR_IE_EMPRESA_CPF | char(1) |  |  | Desconsiderar a inscrição estadual na determinação da empresa a ser importada quando esta possuir inscrição CPF |
| PERMITIR_IMPORTAR_DESTINATARIO_DIFERENTE_EMPRESA_CORRENTE | char(1) |  |  | Permitir importar NF-e mesmo que o destinatário da nota não seja a empresa corrente (Matriz/Filial) |
| IMPORTAR_SOMENTE_NOTAS_POSSUEM_PROTOCOLO_AUTORIZACAO | char(1) |  |  | Importar somente notas que possuem o protocolo de autorização de uso da NF-e |
| NAO_SOMAR_VALOR_II | char(1) |  |  | Não somar o valor do imposto de importação nos totais da NF-e |
| INFORMAR_NOTA_SAIDA_DEVOLVIDA_IMPORTACAO | char(1) |  |  | Informar nota de saída devolvida no momento da importação |
| GERAR_OBSERVACAO_DEFINICAO | integer(4) |  | S | Gerar observação na nota conforme informado no(a) - Definição |
| GERAR_INFORMACOES_COMPLEMENTARES | char(1) |  |  | Gerar informações complementares na nota conforme informado no(a) |
| GERAR_INFORMACOES_COMPLEMENTARES_DEFINICAO | integer(4) |  | S | Gerar informações complementares na nota conforme informado no(a) - Definição |
| GRAVAR_PRODUTOS_ORDEM_NFE | char(1) |  |  | Gravar os produtos na mesma ordem que estão informados na NF-e |
| REALIZAR_LANCAMENTO_PRODUTO_GENERICO | char(1) |  |  | Realizar lançamento de produto genérico |
| INFORMAR_VALOR_RESSARCIMENTO_ICMS_ST | char(1) |  |  | Informar valor do ressarcimento de ICMS ST conforme Art. 47, § 3º Anexo VIII do RCTE no momento da importação (S / N) |
| DEDUZIR_VALOR_ICMS_BASE_CALCULO_PISCOFINS_DEVOLUCAO | varchar(1) |  |  | Deduzir o valor do ICMS da base de cálculo do PIS e COFINS nas notas de devolução |
| IMPORTAR_NOTAS_SITUACAO_TERCEIROS_REGIME_ESPECIAL_NORM_ESPECIFICA | varchar(1) |  |  | Importar situação das notas com emissão de terceiros como Documento emitido com base em Regime Especial ou Normal Específica |
| CONSIDERAR_ICMS_ACUMULADOR_DEFINICAO | char(1) |  |  | Considerar o percentual de base de cálculo e alíquota do ICMS do cadastro do acumulador sobre o valor - Definição |
| ADICIONAR_VALOR_FCP_NO_SUBTRI | varchar(1) |  |  | Adicionar o valor do Fundo de Combate a Pobreza ao valor da SUBTRI |
| ADICIONAR_VALOR_FCP_NO_ICMS | varchar(1) |  |  | Adicionar o valor do Fundo de Combate a Pobreza ao valor do ICMS |
| PRODUTO_EM_DUPLICIDADE | char(1) |  | S | Quando o produto a ser importado estiver cadastrado em duplicidade |
| ADICIONAR_VALOR_AFRMM | varchar(1) |  |  | Adicionar o valor do Adicional ao Frete para a RenovaÃ§Ã£o da Marinha Mercante ao valor das Despesas AcessÃ³rias |
| DEDUZIR_VALOR_SUBTRI_CALCULO_ICMS_ANTECIPACAO_TOTAL | char(1) |  | S | Deduzir o valor do SUBTRI no cálculo do imposto ICMS Antecipação Total - ST |
| DETERMINAR_ACUMULADORES_PERCENTUAL_BC_ALIQ_ICMS | char(1) |  | S | Determinar acumuladores para considerar o percentual de base de calculo e aliquota do ICMS |
| DETERMINAR_IMPOSTOS_NOTAS_DE_IMPORTACAO | char(1) |  | S | Determinar impostos que serão considerados como despesas acessórias para notas de importação |
| DEDUZIR_VALOR_FUNRURAL_NO_VALOR_PARCELA | varchar(1) |  |  | Deduzir o valor do FUNRURAL no valor da parcela |
| GERAR_PROCESSO_REFERENCIADO_NA_NOTA | char(1) |  |  | Gerar processo referenciado na nota (Check) |
| GERAR_PROCESSO_REFERENCIADO_NA_NOTA_OPCOES | integer(4) |  | S | Gerar processo referenciado na nota (Opções: Acumulador - 1, Nota - 2, Acumulador e nota - 3) |
| CONSIDERAR_TODOS_COMO_EXCECAO_CFOP_ENT | char(1) |  | S | Considerar como exceção a opção "Todos" das colunas para relacionamento do CFOP entrada |
| CONSIDERAR_TODOS_COMO_EXCECAO_ACU_ENT | char(1) |  | S | Considerar como exceção a opção "Todos" das colunas para relacionamento do acumulador entrada |
| IMPORTAR_VALOR_DIFERIDO_ICMS_DECRETO_55_797_2021 | char(1) |  |  | Importar valor diferido de ICMS conforme Decreto 55.797/2021 |
| DEDUZIR_VALOR_ICMS_BASE_CALCULO_PISCOFINS_DEFINICAO | char(1) |  |  | Deduzir o valor do ICMS da base de cálculo do PIS e COFINS nas notas de devolução - Definição (D-Notas de devolução/E-Notas de entradas/T-Devolução e Entradas) |
| DEDUZIR_VALOR_DIFALNC_FCP_BASE_CALCULO_PISCOFINS_ENTRADA | char(1) |  | S | Deduzir o imposto 145-DIFAL-NC e 146-FCP da base de cÃ¡lculo do PIS/COFINS. (Entrada) |
| IMPORTAR_VALOR_IPI_COMO_DESP_ACESSO_NOTA_OP_NACIONAL_ENT | char(1) |  | S | Determinar impostos que serão considerados como despesas acessórias para notas com operação nacional |
| IDENTIFICAR_PRODUTO_RELACIONAR_CFOP_ENT | char(1) |  |  | Identificar o produto para relacionar ao acumulador por |
| IMPORTAR_DESCRICAO_COMPLEMENTAR_PRODUTO | char(1) |  | S | Importar descrição complementar do produto |
| DEDUZIR_VALOR_ICMS_MONOFASICO_BASE_CALCULO_PISCOFINS | char(1) |  | S | Deduzir o valor do ICMS monofásico da base de cálculo do PIS e COFINS |
| IDENTIFICAR_CLIENTE_RELACIONAR_ACUMULADOR | char(1) |  |  | Identificar o cliente para relacionar ao acumulador por |
| REGISTRAR_ALTERACAO_NCM_CAD_PROD | char(1) |  |  | Registrar alteração de NCM ao sobrescrever o cadastro de produto. |
| ZERAR_VALORES_NOTAS_PRODUTOR_RURAL | varchar(1) |  |  | Zerar valores das notas de produtor rural |
| IMPORTAR_DATA_DESEMBARACO_MERCADORIA | varchar(1) |  |  | Importar a data de desembaraço da mercadoria |
| DEDUZIR_VALOR_DIFALNC_FCP_BASE_CALCULO_PISCOFINS_ENTRADA_DEFINICAO | char(1) |  |  | Deduzir o imposto 145-DIFAL-NC e 146-FCP da base de cÃ¡lculo do PIS/COFINS. (Entrada) - DefiniÃ§Ã£o (A-DIFAL-NC e FCP/D-Valor do DIFAL-NC/F-Valor do FCP) |
| GERAR_PARCELAS_NOTAS_NAO_POSSUEM_PARCELAS | char(1) |  |  | Gerar parcelas para notas que não possuem parcelas |
