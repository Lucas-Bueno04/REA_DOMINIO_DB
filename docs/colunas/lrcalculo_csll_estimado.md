# LRCALCULO_CSLL_ESTIMADO — Cálculo do Lalur - Imposto CSLL Estimado
1.278 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CALCULO | integer(4) | PK |  | Código do cálculo |
| VALOR_BASE_CALCULO_VENDA | numeric(13) |  |  | Base de cálculo das vendas |
| VALOR_BASE_CALCULO_SERVICO | numeric(13) |  |  | Base de cálculo dos serviços |
| VALOR_BASE_CALCULO_GANHO | numeric(13) |  |  | Base de cálculo dos ganhos |
| VALOR_BASE_CALCULO | numeric(13) |  |  | Total da base de cálculo |
| VALOR_CSLL_DEVIDA | numeric(13) |  |  | CSLL devida |
| VALOR_DEDUCAO | numeric(13) |  |  | Deduções |
| VALOR_DEDUCAO_ORGAO_PUBLICO_FEDERAL | numeric(13) |  |  | Dedução - CSLL retida por Órgãos Públicos Federais |
| VALOR_DEDUCAO_PAGO_EM_MES_ANTERIOR | numeric(13) |  |  | Dedução - pago em meses anteriores |
| VALOR_DEDUCAO_OUTRA_PESSOA_JURIDICA | numeric(13) |  |  | Dedução - CSLL retida por outras pessoas jurídicas |
| VALOR_DEDUCAO_ESTADO_MUNICIPIO | numeric(13) |  |  | Dedução - CSLL retida por Esados, Municípios |
| VALOR_DEDUCAO_ADMINISTRACAO_PUBLICA | numeric(13) |  |  | Dedução - CSLL retida pela Administração Pública |
| VALOR_DEDUCAO_OUTRA_DEDUCAO | numeric(13) |  |  | Dedução - Outras Deduções |
| VALOR_BONUS_ADIMPLENCIA | numeric(13) |  |  | Bônus por adimplência |
| VALOR_DIFERIDO_PERIODO_ANTERIOR | numeric(13) |  |  | CSLL diferido do período anterior |
| VALOR_DIFERIDO_PERIODO | numeric(13) |  |  | CSLL diferido do período |
| VALOR_A_RECOLHER | numeric(13) |  |  | CSLL a recolher |
| VALOR_COMPENSAR_PERIODO_SEGUINTE | numeric(13) |  |  | Valor a compensar para o período seguinte |
| VALOR_COMPENSAR_PERIODO_SEGUINTE_GERAL | numeric(13) |  |  | Valor a compensar para o período seguinte - Geral |
| VALOR_COMPENSAR_PERIODO_SEGUINTE_RURAL | numeric(13) |  |  | Valor a compensar para o período seguinte - Rural |
| VALOR_DEDUZIR_PERIODO_SEGUINTE | numeric(13) |  |  | Valor a deduzir para o período seguinte |
| VALOR_DEDUCAO_PAGO_EXTERIOR | numeric(13) |  |  | Dedução - Pago no exterior sobre lucros, rendimentos e ganhos de capital |
| VALOR_DEDUCAO_RECUPERACAO_CREDITO | numeric(13) |  |  | Dedução - Recuperação de crédito de CSLL |
| VALOR_DEDUCAO_CREDITO_DEPRECIACAO_IMOBILIZADO | numeric(13) |  |  | Dedução - Créditos sobre depreciação de imobilizado |
| VALOR_ALIQUOTA_CSLL | numeric(5) |  |  | Alíquota do CSLL |
| VALOR_DEDUCAO_COMPENSACAO_IMPOSTO_FEDERAL_PERIODO_ANTERIOR | numeric(13) |  |  | Compensação de impostos federais de períodos anteriores |
| VALOR_DEDUCAO_SALDO_PERIODO_ANTERIOR | numeric(13) |  |  | Saldo de deduções do período anterior |
| VALOR_ADICIONAL_PROPORCIONALIDADE_CSLL | numeric(13) |  |  | Adicional proporcionalidade CSLL |
| VALOR_BASE_CALCULO_JUROS_MULTA_OUTRO | numeric(13) |  |  | Valor de base de calculo de juros, multa e outros |
| VALOR_DEDUCAO_PERSE_PGSC | decimal(13) |  | S | Lei Perse e PGSC - Lei 14.148/21 |
| VALOR_IMPOSTO_DEVIDO_MES_ANTES_RETENCOES_PAGAMENTOS | decimal(13) |  | S | Campo criado internamento para guardar o valor e apresentar no calculo quando o tipo do calculo for Anual/Balanço de Redução e Suspensão |
