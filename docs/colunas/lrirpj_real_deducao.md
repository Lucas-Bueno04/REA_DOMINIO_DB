# LRIRPJ_REAL_DEDUCAO — Deduções do Imposto de Renda (Real)
551 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_IRPJ_REAL_DEDUCAO | integer(4) | PK |  | Código |
| COMPETENCIA | date(4) |  |  | Competência |
| VALOR_IR_PAGO_EM_MES_ANTERIOR | numeric(13) |  |  | IR pgo em meses anteriores |
| VALOR_IRRF | numeric(13) |  |  | IRRF |
| VALOR_IRRF_ORGAO_PUBLICO_FEDERAL | numeric(13) |  |  | IRRF por Órgãos Públicos Federais |
| VALOR_IRRF_ADMINISTRACAO_PUBLICA | numeric(13) |  |  | IRRF Administração Pública |
| VALOR_OUTRA_DEDUCAO | numeric(13) |  |  | Outras deduções |
| I_SCP | integer(4) |  | S | SCP |
| VALOR_PAGO_EXTERIOR | numeric(13) |  |  | Pago no exterior sobre lucros, rendimentos e ganhos de capital |
| VALOR_PAGO_INCIDENTE_SOBRE_GANHOS | numeric(13) |  |  | Pago incidente sobre ganhos no mercado de renda variável |
| VALOR_PARCELAMENTO_FORMALIZADO | numeric(13) |  |  | Parcelamento formalizado de IR sobre a base de cálculo estimada |
| VALOR_COMPENSACAO_IMPOSTO_FEDERAL_PERIODO_ANTERIOR | numeric(13) |  |  | Compensação de impostos federais de períodos anteriores |
| AJUSTE_ANUAL | integer(4) |  |  | Ajuste Anual |
| VALOR_DEDUCAO_PERSE_PGSC | decimal(13) |  | S | Lei Perse e PGSC - Lei 14.148/21 |
| RETENCOES_PAGO_MESES_ANT | char(1) |  |  | Importar retenções como valor pago em meses anteriores |
| DATA_INICIO_SALDO | date(4) |  | S | Data de início do controle de saldo. |
| DATA_HORA_ALTERACAO | timestamp(8) |  |  | Data de alteração (Usado para forçar disparo da trigger) |
| VALOR_IRRF_DESCONSIDERAR | numeric(13) |  | S | Valor IRRF a ser desconsiderado no calculo |
| DESCONSIDERAR_SALDO_DEZEMBRO | char(1) |  |  | Desconsiderar saldo de Dezembro |
