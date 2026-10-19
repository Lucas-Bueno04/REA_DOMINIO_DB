# LRCALCULO_IRPJ_REAL — Cálculo do Lalur - Imposto IRPJ Real
3.108 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CALCULO | integer(4) | PK |  | Código do cálculo |
| VALOR_LUCRO_LIQUIDO_ANTES_IRPJ_GERAL | numeric(13) |  |  | Lucro líquido antes do IRPJ - Geral |
| VALOR_ADICAO_GERAL | numeric(13) |  |  | Adições - Geral |
| VALOR_EXCLUSAO_GERAL | numeric(13) |  |  | Exclusões - Geral |
| VALOR_LUCRO_REAL_ANTES_COMPENSACAO_GERAL | numeric(13) |  |  | Lucro Real antes da compensação - Geral |
| VALOR_COMPENSACAO_GERAL | numeric(13) |  |  | Compensação - Geral |
| VALOR_COMPENSACAO_OPERACIONAL_GERAL | numeric(13) |  |  | Compensação Operacional - Geral |
| VALOR_COMPENSACAO_NAO_OPERACIONAL_GERAL | numeric(13) |  |  | Compensação Não operacional - Geral |
| VALOR_LUCRO_REAL_GERAL | numeric(13) |  |  | Lucro Real da atividade - Geral |
| VALOR_LUCRO_LIQUIDO_ANTES_IRPJ_RURAL | numeric(13) |  |  | Lucro líquido antes do IRPJ - Rural |
| VALOR_ADICAO_RURAL | numeric(13) |  |  | Adições - Rural |
| VALOR_EXCLUSAO_RURAL | numeric(13) |  |  | Exclusões - Rural |
| VALOR_LUCRO_REAL_ANTES_COMPENSACAO_RURAL | numeric(13) |  |  | Lucro Real antes da compensação - Rural |
| VALOR_COMPENSACAO_RURAL | numeric(13) |  |  | Compensação - Rural |
| VALOR_LUCRO_REAL_RURAL | numeric(13) |  |  | Lucro Real da atividade - Rural |
| VALOR_LUCRO_LIQUIDO_ANTES_IRPJ | numeric(13) |  |  | Lucro líquido antes do IRPJ |
| VALOR_ADICAO | numeric(13) |  |  | Adições |
| VALOR_EXCLUSAO | numeric(13) |  |  | Exclusões |
| VALOR_LUCRO_REAL_ANTES_COMPENSACAO | numeric(13) |  |  | Lucro Real antes da compensação |
| VALOR_COMPENSACAO | numeric(13) |  |  | Compensação |
| VALOR_LUCRO_REAL | numeric(13) |  |  | Lucro Real da atividade |
| VALOR_IRPJ_DEVIDO | numeric(13) |  |  | IRPJ devido |
| VALOR_ADICIONAL | numeric(13) |  |  | Adicional de IRPJ |
| VALOR_DEDUCAO | numeric(13) |  |  | Deduções |
| VALOR_DEDUCAO_PAGO_EM_MES_ANTERIOR | numeric(13) |  |  | Dedução - IR pago em meses anteriores |
| VALOR_DEDUCAO_IRRF | numeric(13) |  |  | Dedução - IRRF |
| VALOR_DEDUCAO_ORGAO_PUBLICO_FEDERAL | numeric(13) |  |  | Dedução - IRRF por Órgãos Públicos Federais |
| VALOR_DEDUCAO_ADMINISTRACAO_PUBLICA | numeric(13) |  |  | Dedução - IRRF Administração Pública |
| VALOR_DEDUCAO_OUTRA_DEDUCAO | numeric(13) |  |  | Dedução - Outras Deduções |
| VALOR_INCENTIVO_FISCAL | numeric(13) |  |  | Incentivos Fiscais |
| VALOR_REDUCAO_LUCRO_EXPLORACAO | numeric(13) |  |  | Redução Lucro da Exploração |
| VALOR_REDUCAO_POR_REINVESTIMENTO | numeric(13) |  |  | Redução por Reinvestimento |
| VALOR_ADICAO_LUCRO_EXPLORACAO | numeric(13) |  |  | Adições Lucro Exploração |
| VALOR_EXCLUSAO_LUCRO_EXPLORACAO | numeric(13) |  |  | Exclusões Lucro Exploração |
| VALOR_DIFERIDO_PERIODO_ANTERIOR | numeric(13) |  |  | IRPJ diferido do período anterior |
| VALOR_DIFERIDO_PERIODO | numeric(13) |  |  | IRPJ diferido do período |
| VALOR_A_RECOLHER | numeric(13) |  |  | IRPJ a recolher |
| VALOR_COMPENSAR_PERIODO_SEGUINTE | numeric(13) |  |  | Valor a compensar para o período seguinte |
| VALOR_COMPENSAR_PERIODO_SEGUINTE_GERAL_OP | numeric(13) |  |  | Valor a compensar para o período seguinte - Geral - Operacional |
| VALOR_COMPENSAR_PERIODO_SEGUINTE_GERAL_NAO_OP | numeric(13) |  |  | Valor a compensar para o período seguinte - Geral - Não Operacional |
| VALOR_COMPENSAR_PERIODO_SEGUINTE_RURAL | numeric(13) |  |  | Valor a compensar para o período seguinte - Rural |
| VALOR_DEDUZIR_PERIODO_SEGUINTE | numeric(13) |  |  | Valor a deduzir para o período seguinte |
| VALOR_NAO_OPERACIONAL_TRANSFERIDO | numeric(13) |  |  | Valor não operacional transferido |
| VALOR_CISAO | numeric(13) |  |  | Valor da Cisão Parcial |
| VALOR_CISAO_GERAL_OPERACIONAL | numeric(13) |  |  | Valor da Cisão Parcial - Geral - Operacional |
| VALOR_CISAO_GERAL_NAO_OPERACIONAL | numeric(13) |  |  | Valor da Cisão Parcial - Geral - Não Operacional |
| VALOR_CISAO_RURAL | numeric(13) |  |  | Valor da Cisão Parcial - Rural |
| VALOR_DEDUCAO_PAGO_EXTERIOR | numeric(13) |  |  | Dedução - Pago no exterior sobre lucros, rendimentos e ganhos de capital |
| VALOR_DEDUCAO_PAGO_INCIDENTE_SOBRE_GANHOS | numeric(13) |  |  | Dedução - Pago incidente sobre ganhos no mercado de renda variável |
| VALOR_DEDUCAO_PARCELAMENTO_FORMALIZADO | numeric(13) |  |  | Dedução - Parcelamento formalizado de IR sobre a base de cálculo estimada |
| AJUSTE_ANUAL | integer(4) | PK |  | Ajuste Anual |
| VALOR_PREJUIZO_PERIODO | numeric(13) |  |  | Prejuízo do período |
| VALOR_DEDUCAO_COMPENSACAO_IMPOSTO_FEDERAL_PERIODO_ANTERIOR | numeric(13) |  |  | Compensação de impostos federais de períodos anteriores |
| VALOR_DEDUCAO_SALDO_PERIODO_ANTERIOR | numeric(13) |  |  | Saldo de deduções do período anterior |
| VALOR_DEDUCAO_PERSE_PGSC | decimal(13) |  | S | Lei Perse e PGSC - Lei 14.148/21 |
| VALOR_REDUCAO_LUCRO_EXPLORACAO_LIMITE | numeric(13) |  | S | Valor limite para o lucro da exploracao |
| VALOR_IMPOSTO_DEVIDO_MES_ANTES_RETENCOES_PAGAMENTOS | decimal(13) |  | S | Campo criado internamento para guardar o valor e apresentar no calculo quando o tipo do calculo for Anual/Balanço de Redução e Suspensão |
| VALOR_LUCRO_REAL_APOS_COMPENSACAO_PROPRIO_PERIODO_GERAL | decimal(13) |  | S | Lucro Real Após a Compensação de Prejuízos do Próprio Período |
| VALOR_LUCRO_REAL_APOS_COMPENSACAO_PROPRIO_PERIODO_RURAL | decimal(13) |  | S | Lucro Real Após a Compensação de Prejuízos do Próprio Período |
| VALOR_COMPENSACAO_BC_NEGATIVA_RURAL | decimal(13) |  | S | Compensação da BC Negativa do Próprio Período - Atividade Geral |
| VALOR_COMPENSACAO_BC_NEGATIVA_GERAL | decimal(13) |  | S | Compensação da BC Negativa do Próprio Período - Atividade Rural |
