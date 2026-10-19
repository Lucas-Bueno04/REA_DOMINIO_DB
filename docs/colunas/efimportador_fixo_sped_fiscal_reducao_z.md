# EFIMPORTADOR_FIXO_SPED_FISCAL_REDUCAO_Z — Configuração do leiaute SPED Fiscal do Importador Fixo - Redução Z
1.185 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CONSIDERAR_ICMS_ACUMULADOR | char(1) |  |  | Considerar as definições do imposto ICMS no acumulador |
| SAI_DADOS_EXCECAO | char(1) |  |  | Definir dados para exceção das saídas |
| SAI_CODI_ACU_EXCECAO | integer(4) |  | S | Código do acumulador para exceção das saídas |
| AJUSTAR_DIFERENCA_ICMS_ESTOQUE | char(1) |  |  | Ajustar diferença entre o valor do ICMS do estoque com o valor do ICMS das situações tributárias |
| GERAR_LANCAMENTOS_CONTABEIS | char(1) |  |  | Gerar lançamentos contábeis |
| UTILIZAR_CLIENTE_PADRAO_PARAMETROS | char(1) |  |  | Utilizar o cliente padrão informado nos parâmetros |
| UTILIZAR_CLIENTE_PADRAO_PARAMETROS_QUANDO | integer(4) |  | S | Utilizar o cliente padrão informado nos parâmetros quando |
| DEFINIR_ACUMULADOR_SAIDAS | integer(4) |  |  | Definir o acumulador |
| RATEAR_ACRESCIMO_TOTALIZADOR_PRODUTOS | char(1) |  |  | Ratear o valor do acréscimo informado nos totalizadores parciais da redução Z entre os produtos |
| CONSIDERAR_BC_ICMS_ACUMULADOR | char(1) |  |  | Considerar o percentual de base de cálculo do ICMS do cadastro do acumulador |
| DEDUZIR_VALOR_ICMS_BASE_CALCULO_PISCOFINS | varchar(1) |  |  | Deduzir o valor do ICMS da base de cálculo do PIS e COFINS |
| DEFINIR_ACUMULADOR_SAIDAS_PRODUTOS | char(1) |  |  | Definir acumulador saÃ­das produtos |
| CONSIDERAR_ST_TRIBUTACAO_MONOFASICA | char(1) |  |  | Considerar a situação tributária para tributação monofásica com CST 061 |
| CONSIDERAR_ST_TRIBUTACAO_MONOFASICA_QUANDO | char(1) |  |  | Considerar a situação tributária para tributação monofásica com CST 061 como: |
| DEDUZIR_ISS_DA_BASE_CALCULO_PIS_COFINS | char(1) |  | S | Deduzir o valor do ISS da base de cÃ¡lculo do PIS e COFINS. |
