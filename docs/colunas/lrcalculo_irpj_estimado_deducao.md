# LRCALCULO_IRPJ_ESTIMADO_DEDUCAO — Cálculo do Lalur - Imposto IRPJ Estimado - Detalhamento de Deduções
200 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CALCULO | integer(4) | PK |  | Código do cálculo |
| AJUSTE_ANUAL | integer(4) | PK |  | Ajuste Anual |
| I_IRPJ_ESTIMADO_DEDUCAO | integer(4) | PK |  | Dedução |
| VALOR_IRRF | numeric(13) |  |  | Valor IRRF |
| VALOR_IRRF_ORGAO_PUBLICO_FEDERAL | numeric(13) |  |  | Valor IRRF por Órgãos Públicos Federais |
| VALOR_IRRF_ADMINISTRACAO_PUBLICA | numeric(13) |  |  | Valor IRRF Administração Pública |
