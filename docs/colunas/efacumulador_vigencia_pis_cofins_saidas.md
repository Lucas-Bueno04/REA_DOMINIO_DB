# EFACUMULADOR_VIGENCIA_PIS_COFINS_SAIDAS — Acumuladores - Cadastro - PIS/COFINS - Saídas
70.702 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_ACU | integer(4) | PK |  | Acumulador |
| VIGENCIA_ACU | date(4) | PK |  | Vigência do acumulador |
| I_PIS_COFINS_SAIDAS | integer(4) | PK |  | Sequencial |
| CST | integer(4) |  |  | CST |
| NATUREZA_RECEITA | integer(4) |  | S | Natureza da receita |
| ALIQUOTA_PIS | numeric(7) |  |  | Alíquota do PIS |
| ALIQUOTA_COFINS | numeric(7) |  |  | Alíquota do COFINS |
| VALOR_PIS_UNIDADE_MEDIDA | numeric(13) |  |  | Valor do PIS por unidade de medida |
| VALOR_COFINS_UNIDADE_MEDIDA | numeric(13) |  |  | Valor da COFINS por unidade de medida |
| PERCENTUAL_REDUCAO_BASE_CALCULO_PIS_COFINS_SAIDA | numeric(5) |  |  | Percentual de Redução da Base de Cálculo |
| I_RECOLHIMENTO_PIS | integer(4) |  | S | Código Sequencial do Recolhimento do PIS |
| CODIGO_RECOLHIMENTO_PIS | char(6) |  |  | Código do Recolhimento do PIS |
| I_RECOLHIMENTO_COFINS | integer(4) |  | S | Código Sequencial do Recolhimento do COFINS |
| CODIGO_RECOLHIMENTO_COFINS | char(6) |  |  | Código do Recolhimento do COFINS |
| CODIGO_BENEFICIO_DIRBI | integer(4) |  | S | Código do Benefício DIRBI |
| CALCULAR_PISCOFINS_REDUCAO_LINEAR_LC224 | char(1) |  |  | Calcular redução conf. LC 224/2025 |
