# EFIMPORTADOR_FIXO_SPED_FISCAL_ENTRADA — Configuração do leiaute SPED Fiscal do Importador Fixo - Entrada
1.185 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| IMPORTAR_PARCELAS | char(1) |  |  | Importar pacelas |
| IGNORAR_IMPOSTOS_NAO_DEF_ACU | char(1) |  |  | Ignorar impostos não definidos no acumulador |
| CONSIDERAR_ICMS_ACUMULADOR | char(1) |  |  | Considerar o percentual de base de cálculo do ICMS do cadastro do acumulador |
| CODI_ACU_CANCELADA | integer(4) |  |  | Código do acumulador para nota cancelada |
| ACUMULADOR_EXCECAO | char(1) |  |  | Definir acumulador para exceção |
| CODI_ACU_EXCECAO | integer(4) |  | S | Código do acumulador para exceção |
| CFOP_CANCELADA | integer(4) |  | S | CFOP das notas canceladas |
| VERSAO_CFOP_CANCELADA | smallint(2) |  | S | Versão do CFOP das notas canceladas |
| CODI_FOR_CANCELADA | integer(4) |  | S | Fornecedor das notas canceladas |
| DATA_CANCELADA | char(1) |  |  | Data das notas canceladas |
| DATA_DOCUMENTO_EXTEMPORANEO | char(1) |  |  | Data de escrituração dos documentos extemporâneos |
| DIFERENCA_BC_ICMS_EXCECAO | char(1) |  |  | Diferença base de cálculo para exceção |
| DEFINICAO_BC_ICMS_EXCECAO | char(1) |  | S | Definição da diferença base de cálculo para exceção |
| NAO_CONSIDERA_DEFINICAO_VALORES | char(1) |  |  | Não considerar as definições para os valores de IPI e SUBTRI da linha do ICMS |
| GERAR_LANCAMENTOS_CONTABEIS | char(1) |  |  | Gerar lançamentos contábeis |
| CONSIDERAR_IPI_ACUMULADOR | char(1) |  |  | Considerar as definições do imposto IPI do cadastro do acumulador |
| GERAR_OBSERVACAO_ACUMULADOR | char(1) |  |  | Gerar observação informada no cadastro do acumulador |
| UTILIZAR_CHAVE_PARA_IDENTIFICAR_NOTAS | char(1) |  | S | Utilizar somente a chave da NF-e, NFC-e e CT-e para identificar as notas já lançadas |
| IDENTIFICAR_CODIGO_NATUREZA_OPERACAO | char(1) |  |  | Identificar o código de natureza de operação conforme |
| DEDUZIR_VALOR_ICMS_BASE_CALCULO_PISCOFINS_DEVOLUCAO | varchar(1) |  |  | Deduzir o valor do ICMS da base de cálculo do PIS e COFINS nas notas de devolução |
| IMPORTAR_NOTAS_SITUACAO_TERCEIROS_REGIME_ESPECIAL_NORM_ESPECIFICA | varchar(1) |  |  | Importar situação das notas com emissão de terceiros como Documento emitido com base em Regime Especial ou Normal Específica |
| NAO_CONSIDERAR_DIFERENCA_BC_IPI_EXCECAO | char(1) |  |  | Não considerar as definições para os valores de IPI e lança-los em: |
| DEFINICAO_DIFERENCA_BC_IPI_EXCECAO | char(1) |  | S | Lançar IPI em |
| NAO_CONSIDERAR_DIFERENCA_BC_SUBTRI_EXCECAO | char(1) |  |  | Não considerar as definições para os valores de SUBTRI e lança-los em: |
| DEFINICAO_DIFERENCA_BC_SUBTRI_EXCECAO | char(1) |  | S | IPI - Lançar SUBTRI em |
| GERAR_OBSERVACAO_DEFINICAO | integer(4) |  | S | Notas de entrada: Gerar observação na nota conforme informado no(a) - Definição |
| GERAR_INFORMACOES_COMPLEMENTARES | char(1) |  |  | Notas de entrada: Gerar informações complementares na nota conforme informado no(a) |
| GERAR_INFORMACOES_COMPLEMENTARES_DEFINICAO | integer(4) |  | S | Notas de entrada: Gerar informações complementares na nota conforme informado no(a) - Definição |
| IMPORTAR_MONTANTE_IMPOSTO_PRESUMIDO_REGISTRO_1923 | varchar(1) |  |  | Importar o montante do imposto presumido do registro 1923 para o cálculo do Ressarcimento/Complemento ICMS ST |
| IMPORTAR_BASE_CALCULO_VALOR_ICMSST_RETIDO_REG_C197 | varchar(1) |  |  | Importar a Base de Cálculo e Valor do ICMS ST Retido através do Registro C197 conforme ajustes. |
| DEDUZIR_VALOR_ICMS_BASE_CALCULO_PISCOFINS_DEFINICAO | char(1) |  |  | Deduzir o valor do ICMS da base de cálculo do PIS e COFINS nas notas de devolução - Definição (D-Notas de devolução/E-Notas de entradas/T-Devolução e Entradas) |
| DEDUZIR_VALOR_DIFALNC_FCP_BASE_CALCULO_PISCOFINS_ENTRADA | char(1) |  | S | Deduzir o imposto 145-DIFAL-NC e 146-FCP da base de cÃ¡lculo do PIS/COFINS. (Entrada) |
| INFORMAR_NOTA_SAIDA_DEVOLVIDA_IMPORTACAO | char(1) |  | S | Informar a nota de entrada no momento da importaÃ§Ã£o |
| CST_CSOSN_EXCECAO | char(1) |  |  | Definir exceção para CST/CSOSN |
| GERAR_CST_CSOSN_INFORMADO_NOTA | char(1) |  |  | Gerar CST/CSOSN informado na nota |
| I_SEQUENCIAL_CST_CSOSN_DEFINIDO | integer(4) |  | S | Chave sequencial do CST/CSOSN para exceção das entradas |
| CST_CSOSN_DEFINIDO | integer(4) |  | S | Código do CST/CSOSN para exceção das entradas |
| IDENTIFICAR_PRODUTO_RELACIONAR_ACUMULADOR | char(1) |  |  | Identificar o produto para relacionar ao acumulador por |
| ADICIONAR_VALOR_FCP_NO_SUBTRI | varchar(1) |  |  | Adicionar o valor do Fundo de Combate a Pobreza ao valor da SUBTRI |
| CONSIDERAR_TODOS_COMO_EXCECAO_ACU_ENT | char(1) |  |  | Considerar como exceÃ§Ã£o a opÃ§Ã£o "Todos" das colunas para relacionamento do acumulador |
| DEDUZIR_VALOR_DIFALNC_FCP_BASE_CALCULO_PISCOFINS_ENTRADA_DEFINICAO | char(1) |  |  | Deduzir o imposto 145-DIFAL-NC e 146-FCP da base de cÃ¡lculo do PIS/COFINS. (Entrada) - DefiniÃ§Ã£o (A-DIFAL-NC e FCP/D-Valor do DIFAL-NC/F-Valor do FCP) |
| IMPORTAR_BC_ALIQ_VALOR_ICMS_STAT_REG_C197 | char(1) |  |  | Importar a Base de Cálculo, Alíquota e Valor do ICMS Antecipação Total - ST através do Registro C197 conforme ajustes. |
| AJUSTAR_RATEIO_FRETE_SEGURO_DESP_ACESS | char(1) |  |  | Ajuste do rateio frete/seguro/despesas: P=Primeiro produto, U=Ultimo produto |
