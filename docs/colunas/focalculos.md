# focalculos — Calculo - Sequencia de calculos
624.116 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CALCULOS_OLD | integer(4) |  | S | Codigo do calculo - Renomeado |
| I_CALCULOS_EXPORTA_IMPORTA_OLD | integer(4) |  | S | Código do cálculo para usar no exporta/importa - Renomeado |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Codigo do calculo |
| I_CALCULOS_EXPORTA_IMPORTA | uniqueidentifier(16) |  | S | Código do cálculo para usar no exporta/importa. |
