# EFIMPORTADOR_FIXO_SPED_FISCAL_SAIDA — Configuração do leiaute SPED Fiscal do Importador Fixo - Saída
1.185 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CFOP_CANCELADA | integer(4) |  |  | CFOP das notas canceladas |
| VERSAO_CFOP_CANCELADA | smallint(2) |  |  | Versão do CFOP das notas canceladas |
| CODI_CLI_CANCELADA | integer(4) |  |  | Cliente das notas canceladas |
| DATA_CANCELADA | char(1) |  |  | Data das notas canceladas |
| CODI_CLI_C300 | integer(4) |  |  | Cliente padrão das notas modelo 02 |
| IMPORTAR_PARCELAS | char(1) |  |  | Importar pacelas |
| GERAR_PAGAMENTO_PARCELA | char(1) |  |  | Gerar pagamento para parcelas com data de vencimento igual a data da nota |
| GERAR_PARCELA_COM_PAGAMENTO | char(1) |  |  | Gerar parcela com pagamento para notas sem parcelas |
| CONSIDERAR_ICMS_ACUMULADOR | char(1) |  |  | Considerar o percentual de base de cálculo do ICMS do cadastro do acumulador |
| ACUMULADOR_EXCECAO | char(1) |  |  | Definir acumulador para exceção |
| CODI_ACU_EXCECAO | integer(4) |  | S | Código do acumulador para exceção |
| CODI_ACU_CANCELADA | integer(4) |  | S | Código do acumulador para nota cancelada |
| DIFERENCA_BC_ICMS_EXCECAO | char(1) |  |  | Diferença base de cálculo para exceção |
| DEFINICAO_BC_ICMS_EXCECAO | char(1) |  | S | Definição da diferença base de cálculo para exceção |
| GERAR_LANCAMENTOS_CONTABEIS | char(1) |  |  | Gerar lançamentos contábeis |
| UTILIZAR_CLIENTE_PADRAO_C300_QUANDO | integer(4) |  |  | Utilizar o cliente padrão das notas modelo 02 quando |
| REORDENAR_CODIGO_NOTAS | char(1) |  |  | Gravar as notas importadas em ordem de número e sem intervalo no código sequencial |
| GERAR_OBSERVACAO_ACUMULADOR | char(1) |  |  | Gerar observação informada no cadastro do acumulador |
| UTILIZAR_CHAVE_PARA_IDENTIFICAR_NOTAS | char(1) |  | S | Utilizar somente a chave da NF-e, NFC-e e CT-e para identificar as notas já lançadas |
| IDENTIFICAR_CODIGO_NATUREZA_OPERACAO | char(1) |  |  | Identificar o código de natureza de operação conforme |
| DEDUZIR_VALOR_ICMS_BASE_CALCULO_PISCOFINS | varchar(1) |  |  | Deduzir o valor do ICMS da base de cálculo do PIS e COFINS |
| NAO_CONSIDERAR_DIFERENCA_BC_IPI_EXCECAO | char(1) |  |  | Não considerar as definições para os valores de IPI e lança-los em: |
| DEFINICAO_DIFERENCA_BC_IPI_EXCECAO | char(1) |  | S | Lançar IPI em |
| NAO_CONSIDERAR_DIFERENCA_BC_SUBTRI_EXCECAO | char(1) |  |  | Não considerar as definições para os valores de SUBTRI e lança-los em: |
| DEFINICAO_DIFERENCA_BC_SUBTRI_EXCECAO | char(1) |  | S | IPI - Lançar SUBTRI em |
| GERAR_OBSERVACAO_DEFINICAO | integer(4) |  | S | Notas de saída: Gerar observação na nota conforme informado no(a) - Definição |
| GERAR_INFORMACOES_COMPLEMENTARES | char(1) |  |  | Notas de saída: Gerar informações complementares na nota conforme informado no(a) |
| GERAR_INFORMACOES_COMPLEMENTARES_DEFINICAO | integer(4) |  | S | Notas de saída: Gerar informações complementares na nota conforme informado no(a) - Definição |
| DEDUZIR_VALOR_DIFALNC_FCP_BASE_CALCULO_PISCOFINS_SAIDA | char(1) |  | S | Deduzir o imposto 145-DIFAL-NC e 146-FCP da base de cÃ¡lculo do PIS/COFINS. (Saida) |
| INFORMAR_NOTA_ENTRADA_DEVOLVIDA_IMPORTACAO | char(1) |  | S | Informar a nota de saÃ­da devolvida no momento da importaÃ§Ã£o |
| CST_CSOSN_EXCECAO | char(1) |  |  | Definir exceção para CST/CSOSN |
| GERAR_CST_CSOSN_INFORMADO_NOTA | char(1) |  |  | Gerar CST/CSOSN informado na nota |
| I_SEQUENCIAL_CST_CSOSN_DEFINIDO | integer(4) |  | S | Chave sequencial do CST/CSOSN para exceção das saídas |
| CST_CSOSN_DEFINIDO | integer(4) |  | S | Código do CST/CSOSN para exceção das saídas |
| IDENTIFICAR_PRODUTO_RELACIONAR_ACUMULADOR | char(1) |  |  | Identificar o produto para relacionar ao acumulador por |
| CONSIDERAR_TODOS_COMO_EXCECAO_ACU_SAI | char(1) |  |  | Considerar como exceÃ§Ã£o a opÃ§Ã£o "Todos" das colunas para relacionamento do acumulador |
| DEDUZIR_VALOR_DIFALNC_FCP_BASE_CALCULO_PISCOFINS_SAIDA_DEFINICAO | char(1) |  |  | Deduzir o imposto 145-DIFAL-NC e 146-FCP da base de cÃ¡lculo do PIS/COFINS. (Saida) - DefiniÃ§Ã£o (A-DIFAL-NC e FCP/D-Valor do DIFAL-NC/F-Valor do FCP) |
| AJUSTAR_RATEIO_FRETE_SEGURO_DESP_ACESS | char(1) |  |  | Ajuste do rateio frete/seguro/despesas: P=Primeiro produto, U=Ultimo produto |
