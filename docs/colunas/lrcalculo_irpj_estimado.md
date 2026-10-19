# LRCALCULO_IRPJ_ESTIMADO — Cálculo do Lalur - Imposto IRPJ Estimado
1.278 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CALCULO | integer(4) | PK |  | Código do cálculo |
| VALOR_BASE_CALCULO_VENDA | numeric(13) |  |  | Base de cálculo das vendas |
| VALOR_BASE_CALCULO_SERVICO | numeric(13) |  |  | Base de cálculo dos serviços |
| VALOR_BASE_CALCULO_NAO_OPERACIONAL | numeric(13) |  |  | Base de cálculo do valor não operacional |
| VALOR_BASE_CALCULO | numeric(13) |  |  | Total da base de cálculo |
| VALOR_IRPJ_DEVIDO | numeric(13) |  |  | IRPJ devido |
| VALOR_ADICIONAL | numeric(13) |  |  | Adicional de IRPJ |
| VALOR_DEDUCAO | numeric(13) |  |  | Deduções |
| VALOR_DEDUCAO_PAGO_EM_MES_ANTERIOR | numeric(13) |  |  | Dedução - IR pago em meses anteriores |
| VALOR_DEDUCAO_IRRF | numeric(13) |  |  | Dedução - IRRF |
| VALOR_DEDUCAO_ORGAO_PUBLICO_FEDERAL | numeric(13) |  |  | Dedução - IRRF por Órgãos Públicos Federais |
| VALOR_DEDUCAO_ADMINISTRACAO_PUBLICA | numeric(13) |  |  | Dedução - IRRF Administração Pública |
| VALOR_DEDUCAO_OUTRA_DEDUCAO | numeric(13) |  |  | Dedução - Outras Deduções |
| VALOR_INCENTIVO_FISCAL | numeric(13) |  |  | Incentivos Fiscais |
| VALOR_DIFERIDO_PERIODO_ANTERIOR | numeric(13) |  |  | IRPJ diferido do período anterior |
| VALOR_DIFERIDO_PERIODO | numeric(13) |  |  | IRPJ diferido do período |
| VALOR_A_RECOLHER | numeric(13) |  |  | IRPJ a recolher |
| VALOR_COMPENSAR_PERIODO_SEGUINTE | numeric(13) |  |  | Valor a compensar para o período seguinte |
| VALOR_COMPENSAR_PERIODO_SEGUINTE_GERAL_OP | numeric(13) |  |  | Valor a compensar para o período seguinte - Geral - Operacional |
| VALOR_COMPENSAR_PERIODO_SEGUINTE_GERAL_NAO_OP | numeric(13) |  |  | Valor a compensar para o período seguinte - Geral - Não Operacional |
| VALOR_COMPENSAR_PERIODO_SEGUINTE_RURAL | numeric(13) |  |  | Valor a compensar para o período seguinte - Rural |
| VALOR_DEDUZIR_PERIODO_SEGUINTE | numeric(13) |  |  | Valor a deduzir para o período seguinte |
| VALOR_NAO_OPERACIONAL_TRANSFERIDO | numeric(13) |  |  | Valor não operacional transferido |
| VALOR_DEDUCAO_PAGO_EXTERIOR | numeric(13) |  |  | Dedução - Pago no exterior sobre lucros, rendimentos e ganhos de capital |
| VALOR_DEDUCAO_PAGO_INCIDENTE_SOBRE_GANHOS | numeric(13) |  |  | Dedução - Pago incidente sobre ganhos no mercado de renda variável |
| VALOR_DEDUCAO_COMPENSACAO_IMPOSTO_FEDERAL_PERIODO_ANTERIOR | numeric(13) |  |  | Compensação de impostos federais de períodos anteriores |
| VALOR_DEDUCAO_SALDO_PERIODO_ANTERIOR | numeric(13) |  |  | Saldo de deduções do período anterior |
| VALOR_BASE_CALCULO_JUROS_MULTA_OUTRO | numeric(13) |  |  | Valor de base de calculo de juros, multa e outros |
| VALOR_DEDUCAO_PERSE_PGSC | decimal(13) |  | S | Lei Perse e PGSC - Lei 14.148/21 |
| VALOR_IMPOSTO_DEVIDO_MES_ANTES_RETENCOES_PAGAMENTOS | decimal(13) |  | S | Campo criado internamento para guardar o valor e apresentar no calculo quando o tipo do calculo for Anual/Balanço de Redução e Suspensão |
