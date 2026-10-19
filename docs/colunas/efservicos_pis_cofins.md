# EFSERVICOS_PIS_COFINS — Notas Fiscais de Servico - PIS/COFINS
364.565 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_SER | integer(4) | PK |  | Código do serviço |
| I_PIS_COFINS | integer(4) | PK |  | Sequencial |
| CST | integer(4) |  |  | CST |
| NATUREZA_RECEITA | integer(4) |  | S | Natureza da receita |
| VALOR_CONTABIL | numeric(13) |  |  | Valor contábil |
| EXCLUSOES | numeric(13) |  |  | Exclusões |
| BASE_CALCULO | numeric(13) |  |  | Base de cálculo |
| ALIQUOTA_PIS | numeric(7) |  |  | Alíquota do PIS |
| ALIQUOTA_COFINS | numeric(7) |  |  | Alíquota da COFINS |
| QUANTIDADE_TRIBUTADA | numeric(13) |  |  | Quantidade tributada |
| VALOR_UNIDADE_MEDIDA_PIS | numeric(13) |  |  | Valor por unidade do PIS por unidade de medida |
| VALOR_UNIDADE_MEDIDA_COFINS | numeric(13) |  |  | Valor por unidade da COFINS por unidade de medida |
| VALOR_PIS | numeric(13) |  |  | Valor do PIS |
| VALOR_COFINS | numeric(13) |  |  | Valor da COFINS |
| EXCLUSAO_COOPERATIVA | numeric(13) |  |  | Exclusão Cooperativa |
| PERCENTUAL_REDUCAO_BC | numeric(5) |  |  | Percentual Redução Base Cálculo |
| I_RECOLHIMENTO_PIS | integer(4) |  | S | Código Sequencial do Recolhimento do PIS |
| CODIGO_RECOLHIMENTO_PIS | char(6) |  |  | Código do Recolhimento do PIS |
| I_RECOLHIMENTO_COFINS | integer(4) |  | S | Código Sequencial do Recolhimento do COFINS |
| CODIGO_RECOLHIMENTO_COFINS | char(6) |  |  | Código do Recolhimento do COFINS |
| CODIGO_BENEFICIO_DIRBI | integer(4) |  | S | Código do Benefício DIRBI |
| CALCULAR_REDUCAO_LINEAR_LC224 | char(1) |  |  | Calcular redução conf. LC 224/2025 |
