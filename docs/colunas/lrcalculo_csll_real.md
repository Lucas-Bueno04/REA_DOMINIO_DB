# LRCALCULO_CSLL_REAL — Cálculo do Lalur - Imposto CSLL Real
3.108 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CALCULO | integer(4) | PK |  | Código do cálculo |
| VALOR_LUCRO_LIQUIDO_ANTES_CSLL_IRPJ_GERAL | numeric(13) |  |  | Lucro líquido antes da CSLL e do IRPJ - Geral |
| VALOR_ADICAO_GERAL | numeric(13) |  |  | Adições - Geral |
| VALOR_EXCLUSAO_GERAL | numeric(13) |  |  | Exclusões - Geral |
| VALOR_BASE_CALCULO_ANTES_COMPENSACAO_GERAL | numeric(13) |  |  | Base de cálculo antes da compensação - Geral |
| VALOR_COMPENSACAO_GERAL | numeric(13) |  |  | Compensação - Geral |
| VALOR_BASE_CALCULO_GERAL | numeric(13) |  |  | Base de cálculo - Geral |
| VALOR_LUCRO_LIQUIDO_ANTES_CSLL_IRPJ_RURAL | numeric(13) |  |  | Lucro líquido antes da CSLL e do IRPJ - Rural |
| VALOR_ADICAO_RURAL | numeric(13) |  |  | Adições - Rural |
| VALOR_EXCLUSAO_RURAL | numeric(13) |  |  | Exclusões - Rural |
| VALOR_BASE_CALCULO_ANTES_COMPENSACAO_RURAL | numeric(13) |  |  | Base de cálculo antes da compensação - Rural |
| VALOR_COMPENSACAO_RURAL | numeric(13) |  |  | Compensação - Rural |
| VALOR_BASE_CALCULO_RURAL | numeric(13) |  |  | Base de cálculo - Rural |
| VALOR_LUCRO_LIQUIDO_ANTES_CSLL_IRPJ | numeric(13) |  |  | Lucro líquido antes da CSLL e do IRPJ |
| VALOR_ADICAO | numeric(13) |  |  | Adições |
| VALOR_EXCLUSAO | numeric(13) |  |  | Exclusões |
| VALOR_BASE_CALCULO_ANTES_COMPENSACAO | numeric(13) |  |  | Base de cálculo antes da compensação |
| VALOR_COMPENSACAO | numeric(13) |  |  | Compensação |
| VALOR_BASE_CALCULO | numeric(13) |  |  | Base de cálculo |
| VALOR_CSLL_DEVIDA | numeric(13) |  |  | CSLL devida |
| VALOR_DEDUCAO | numeric(13) |  |  | Deduções |
| VALOR_DEDUCAO_ORGAO_PUBLICO_FEDERAL | numeric(13) |  |  | Dedução - CSLL retida por Órgãos Públicos Federais |
| VALOR_DEDUCAO_PAGO_EM_MES_ANTERIOR | numeric(13) |  |  | Dedução - pago em meses anteriores |
| VALOR_DEDUCAO_OUTRA_PESSOA_JURIDICA | numeric(13) |  |  | Dedução - CSLL retida por outras pessoas jurídicas |
| VALOR_DEDUCAO_ESTADO_MUNICIPIO | numeric(13) |  |  | Dedução - CSLL retida por Esados, Municípios |
| VALOR_DEDUCAO_ADMINISTRACAO_PUBLICA | numeric(13) |  |  | Dedução - CSLL retida pela Administração Pública |
| VALOR_DEDUCAO_OUTRA_DEDUCAO | numeric(13) |  |  | Dedução - Outras Deduções |
| VALOR_ISENCAO_PROUNI | numeric(13) |  |  | Isenção Prouni |
| VALOR_BONUS_ADIMPLENCIA | numeric(13) |  |  | Bônus por adimplência |
| VALOR_DIFERIDO_PERIODO_ANTERIOR | numeric(13) |  |  | CSLL diferido do período anterior |
| VALOR_DIFERIDO_PERIODO | numeric(13) |  |  | CSLL diferido do período |
| VALOR_A_RECOLHER | numeric(13) |  |  | CSLL a recolher |
| VALOR_COMPENSAR_PERIODO_SEGUINTE | numeric(13) |  |  | Valor a compensar para o período seguinte |
| VALOR_COMPENSAR_PERIODO_SEGUINTE_GERAL | numeric(13) |  |  | Valor a compensar para o período seguinte - Geral |
| VALOR_COMPENSAR_PERIODO_SEGUINTE_RURAL | numeric(13) |  |  | Valor a compensar para o período seguinte - Rural |
| VALOR_DEDUZIR_PERIODO_SEGUINTE | numeric(13) |  |  | Valor a deduzir para o período seguinte |
| VALOR_CISAO | numeric(13) |  |  | Valor da Cisão Parcial |
| VALOR_CISAO_GERAL | numeric(13) |  |  | Valor da Cisão Parcial - Geral |
| VALOR_CISAO_RURAL | numeric(13) |  |  | Valor da Cisão Parcial - Rural |
| VALOR_DEDUCAO_PAGO_EXTERIOR | numeric(13) |  |  | Dedução - Pago no exterior sobre lucros, rendimentos e ganhos de capital |
| VALOR_DEDUCAO_PARCELAMENTO_FORMALIZADO | numeric(13) |  |  | Dedução - Parcelamento formalizado de CSLL sobre a base de cálculo estimada |
| AJUSTE_ANUAL | integer(4) | PK |  | Ajuste Anual |
| VALOR_PREJUIZO_PERIODO | numeric(13) |  |  | Prejuízo do período |
| VALOR_ALIQUOTA_CSLL | numeric(5) |  |  | Alíquota do CSLL |
| VALOR_DEDUCAO_COMPENSACAO_IMPOSTO_FEDERAL_PERIODO_ANTERIOR | numeric(13) |  |  | Compensação de impostos federais de períodos anteriores |
| VALOR_DEDUCAO_SALDO_PERIODO_ANTERIOR | numeric(13) |  |  | Saldo de deduções do período anterior |
| VALOR_ADICIONAL_PROPORCIONALIDADE_CSLL | numeric(13) |  |  | Adicional proporcionalidade CSLL |
| VALOR_BASE_CALCULO_MES_ANTERIOR | numeric(13) |  |  | Base de cálculo mês anterior |
| VALOR_BASE_CALCULO_MES_ANTERIOR_GERAL | numeric(13) |  |  | Base de cálculo mês anterior - Geral |
| VALOR_BASE_CALCULO_MES_ANTERIOR_RURAL | numeric(13) |  |  | Base de cálculo mês anterior - Rural |
| VALOR_BONUS_ADIMPLENCIA_ACUMULADO | numeric(13) |  |  | Bônus por adimplência - Valor acumulado |
| VALOR_BONUS_ADIMPLENCIA_UTILIZADO | numeric(13) |  |  | Bônus por adimplência - Valor já utilizado |
| VALOR_DEDUCAO_PERSE_PGSC | decimal(13) |  | S | Lei Perse e PGSC - Lei 14.148/21 |
| VALOR_ISENCAO_PERSE_PGSC | decimal(13) |  | S | Isenção Lei Perse e PGSC - Lei 14.148/21 |
| VALOR_IMPOSTO_DEVIDO_MES_ANTES_RETENCOES_PAGAMENTOS | decimal(13) |  | S | Campo criado internamento para guardar o valor e apresentar no calculo quando o tipo do calculo for Anual/Balanço de Redução e Suspensão |
| VALOR_BASE_CALCULO_ANTERIOR_PERIODO_GERAL | decimal(13) |  | S | Base de Cálculo Antes da Compensação de BC Negativa de Períodos Anteriores |
| VALOR_BASE_CALCULO_ANTERIOR_PERIODO_RURAL | decimal(13) |  | S | (=) Base de Cálculo Antes da Compensação de BC Negativa de Períodos Anteriores |
| VALOR_COMPENSACAO_BC_NEGATIVA_RURAL | decimal(13) |  | S | Compensação da BC Negativa do Próprio Período - Atividade Geral |
| VALOR_COMPENSACAO_BC_NEGATIVA_GERAL | decimal(13) |  | S | Compensação da BC Negativa do Próprio Período - Atividade Rural |
