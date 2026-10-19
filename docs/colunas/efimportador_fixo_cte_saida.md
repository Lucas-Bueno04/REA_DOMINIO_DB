# EFIMPORTADOR_FIXO_CTE_SAIDA — Configuração do leiaute CT-e XML do Importador Fixo - Saída
1.259 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| IMPORTAR_PARCELAS | char(1) |  |  | Importar parcelas |
| GERAR_PAGAMENTO_PARCELA | char(1) |  |  | Gerar pagamento para parcelas com data de vencimento igual a data da nota |
| GERAR_PARCELA_COM_PAGAMENTO | char(1) |  |  | Gerar parcela com pagamento para notas sem parcelas |
| GERAR_OBSERVACAO_ACUMULADOR | char(1) |  |  | Gerar observação informada no cadastro do acumulador |
| ACUMULADOR_EXCECAO | char(1) |  |  | Definir acumulador para exceção |
| CODI_ACU_EXCECAO | integer(4) |  | S | Código do acumulador para exceção |
| CANC_EXCLUI_PARCELAS | char(1) |  |  | Excluir parcelas |
| CANC_EXCLUI_LANCTOS_CONTABEIS | char(1) |  |  | Excluir lançamentos contábeis |
| GERAR_LANCAMENTOS_CONTABEIS | char(1) |  |  | Gerar lançamentos contábeis |
| IMPORTAR_NOTA_ENTRADA_OUTRA_EMPRESA | char(1) |  |  | Importar nota de entrada em outra empresa |
| REORDENAR_CODIGO_NOTAS | char(1) |  |  | Gravar as notas importadas na ordem do número do documento e sem intervalo no código sequencial |
| INFORMAR_DATA_SAIDA | char(1) |  |  | Informar data de saída no momento da importação |
| CONSIDERAR_ICMS_ACUMULADOR | char(1) |  |  | Considerar as definições do imposto ICMS do cadastro do acumulador |
| GERAR_INFO_COMPLEMENTAR_ACUMULADOR | char(1) |  |  | Gerar informações complementares informada no cadastro do acumulador (S/N) |
| DIFERENCA_BC_ICMS_EXCECAO | char(1) |  |  | Definir exceção para diferença entre valor contábil e base de cálculo ICMS |
| DEFINICAO_BC_ICMS_EXCECAO | char(1) |  | S | Lançar diferença entre valor contábil e base de cálculo ICMS em |
| INFORMAR_DETALHAMENTO_ISENTAS | char(1) |  |  | Informar o detalhamento de isentas no momento da importação |
| IMPORTAR_VALOR_CONTABIL_ATRAVES | char(1) |  |  | Importar o Valor Contábil através do campo |
| INFORMAR_KM_PERCORRIDO | char(1) |  |  | Informar o KM percorrido no momento da importação (S / N) |
| DEDUZIR_VALOR_ICMS_BASE_CALCULO_PISCOFINS | varchar(1) |  |  | Deduzir o valor do ICMS da base de cálculo do PIS e COFINS |
| DEDUZIR_VALOR_DIFALNC_FCP_BASE_CALCULO_PISCOFINS_SAIDA | char(1) |  | S | Deduzir o imposto 145-DIFAL-NC e 146-FCP da base de cÃ¡lculo do PIS/COFINS. (Saida) |
| DEDUZIR_VALOR_ICMS_OUTRA_UF_BC_PISCOFINS_SAIDA | char(1) |  | S | Deduzir o valor do ICMS Outra UF da base de cálculo do PIS e COFINS. (Saida) |
| DEDUZIR_VALOR_DIFALNC_FCP_BASE_CALCULO_PISCOFINS_SAIDA_DEFINICAO | char(1) |  |  | Deduzir o imposto 145-DIFAL-NC e 146-FCP da base de cÃ¡lculo do PIS/COFINS. (Saida) - DefiniÃ§Ã£o (A-DIFAL-NC e FCP/D-Valor do DIFAL-NC/F-Valor do FCP) |
| CONSIDERAR_ICMS_ACUMULADOR_DEFINICAO | char(1) |  |  | Considerar as definiÃ§Ãµes do imposto ICMS do cadastro do acumulador - DefiniÃ§Ã£o |
| GERAR_OBSERVACAO_DEFINICAO | integer(4) |  | S | Gerar observação na nota conforme informado no(a)- Definição |
