# LRCALCULO_CSLL_ESTIMADO_DEDUCAO — Cálculo do Lalur - Imposto CSLL Estimado - Detalhamento de Deduções
93 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CALCULO | integer(4) | PK |  | Código do cálculo |
| AJUSTE_ANUAL | integer(4) | PK |  | Ajuste Anual |
| I_CSLL_ESTIMADO_DEDUCAO | integer(4) | PK |  | Dedução |
| VALOR_ORGAO_PUBLICO_FEDERAL | numeric(13) |  |  | Valor CSLL Órgãos Públicos Federais |
| VALOR_OUTRA_PESSOA_JURIDICA | numeric(13) |  |  | Valor CSLL Outras Pessoas Jurídicas |
| VALOR_ESTADO_MUNICIPIO | numeric(13) |  |  | Valor CSLL Estados e Municípios |
| VALOR_ADMINISTRACAO_PUBLICA | numeric(13) |  |  | Valor CSLL Administração Pública |
