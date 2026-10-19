# EFENTRADAS_NOTA_DEVOLVIDA_PIS_COFINS — Notas Fiscais de Entrada - Complementar - Geral - Nota Devolvida - PIS/COFINS
8 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_ENT | integer(4) | PK |  | Código da Entrada |
| I_NOTA_DEVOLVIDA | integer(4) | PK |  | Sequencial da Nota Devolvida |
| I_PIS_COFINS | integer(4) | PK |  | Sequencial |
| CST | integer(4) |  |  | CST |
| VALOR_DEDUCAO | numeric(13) |  |  | Valor da Dedução |
| BASE_CALCULO | numeric(13) |  |  | Base de Cálculo |
| ALIQUOTA_PIS | numeric(7) |  |  | Alíquota do PIS |
| ALIQUOTA_COFINS | numeric(7) |  |  | Alíquota da COFINS |
| QUANTIDADE_TRIBUTADA | numeric(13) |  |  | Quantidade Tributada |
| VALOR_UNIDADE_MEDIDA_PIS | numeric(13) |  |  | Valor Unidade Medida PIS |
| VALOR_UNIDADE_MEDIDA_COFINS | numeric(13) |  |  | Valor Unidade Medida COFINS |
| VALOR_PIS | numeric(13) |  |  | Valor PIS |
| VALOR_COFINS | numeric(13) |  |  | Valor COFINS |
| EXCLUSAO | numeric(13) |  |  | Exclusão |
| PERCENTUAL_REDUCAO_BC | numeric(5) |  |  | Percentual Redução Base Cálculo |
