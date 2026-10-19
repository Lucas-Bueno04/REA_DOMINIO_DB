# LRRECEITA_BRUTA_ITEM — Receita Bruta
787 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_RECEITA_BRUTA | integer(4) | PK |  | Código Receita Bruta |
| I_ITEM | integer(4) | PK |  | Sequencial |
| I_OPERACAO_RECEITA | integer(4) |  |  | Código Operação de Receita |
| VALOR_RECEITA | numeric(13) |  |  | Receita Bruta |
| ALIQUOTA_CSLL | numeric(5) |  |  | Alíquota CSLL |
| BASE_CALCULO_CSLL | numeric(13) |  |  | Base de cálculo CSLL |
| ALIQUOTA_IRPJ | numeric(5) |  |  | Alíquota IRPJ |
| BASE_CALCULO_IRPJ | numeric(13) |  |  | Base de cálculo IRPJ |
| VALOR_JUROS_MULTA_OUTRA | numeric(13) |  |  | Valor de juros, multa e outros |
| ALIQUOTA_JUROS_MULTA_OUTRA | numeric(5) |  |  | Aliquota de juros, multa e outros |
| BASE_CALCULO_JUROS_MULTA_OUTRA | numeric(13) |  |  | Base de calculo de juros, multa e outros |
| RECEITA | numeric(13) |  |  | Receita |
| DEDUCAO | numeric(13) |  |  | Dedução |
