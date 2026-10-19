# LRCALCULO_CSLL_ESTIMADO_OPERACAO_RECEITA — Cálculo do Lalur - Imposto CSLL Estimado - Detalhamento de Vendas e Serviços
713 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CALCULO | integer(4) | PK |  | Código do cálculo |
| I_OPERACAO_RECEITA | integer(4) | PK |  | Operação de receita (vendas ou serviços) |
| VALOR_RECEITA | numeric(13) |  |  | Receita Bruta |
| ALIQUOTA | numeric(5) |  |  | Alíquota |
| VALOR_BASE_CALCULO | numeric(13) |  |  | Base de cálculo |
| VALOR_JUROS_MULTA_OUTRA | numeric(13) |  |  | Valor de juros, multa e outros |
| ALIQUOTA_JUROS_MULTA_OUTRA | numeric(5) |  |  | Aliquota de juros, multa e outros |
| BASE_CALCULO_JUROS_MULTA_OUTRA | numeric(13) |  |  | Base de calculo de juros, multa e outros |
| RECEITA | numeric(13) |  |  | Receita |
| DEDUCAO | numeric(13) |  |  | Dedução |
