# EFENTRADAS_NOTA_DEVOLVIDA_CSOC_IRPJ — Notas Fiscais de Entrada - Complementar - Geral - Nota Devolvida - CSOC/IRPJ
10 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da Empresa |
| CODI_ENT | integer(4) | PK |  | Código da Nota de Entrada |
| I_NOTA_DEVOLVIDA | integer(4) | PK |  | Sequencial da Nota Devolvida |
| I_CSOC_IRPJ | integer(4) | PK |  | Sequencial do CSOC/IRPJ |
| VALOR_DEDUCAO | numeric(13) |  |  | Valor da recdução |
| PERCENTUAL_BC_CSOC | numeric(5) |  |  | % Base de calculo CSOC |
| PERCENTUAL_BC_IRPJ | numeric(5) |  |  | % Base de calculo IRPJ |
| BASE_CALCULO_CSOC | numeric(13) |  |  | Base calculo CSOC |
| BASE_CALCULO_IRPJ | numeric(13) |  |  | Base calculo IRPJ |
| VALOR_IPI | numeric(13) |  |  | Valor IPI |
| VALOR_SUBTRI | numeric(13) |  |  | Valor Subtri |
| VALOR_ICMS | numeric(13) |  |  | Valor ICMS |
