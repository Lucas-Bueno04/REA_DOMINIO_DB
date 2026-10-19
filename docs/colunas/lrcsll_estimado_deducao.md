# LRCSLL_ESTIMADO_DEDUCAO — Deduções da Contribuição Social (Estimado)
152 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CSLL_ESTIMADO_DEDUCAO | integer(4) | PK |  | Código |
| COMPETENCIA | date(4) |  |  | Competência |
| VALOR_PAGO_EM_MES_ANTERIOR | numeric(13) |  |  | Pago em meses anteriores |
| VALOR_ORGAO_PUBLICO_FEDERAL | numeric(13) |  |  | Órgãos Públicos Federais |
| VALOR_OUTRA_PESSOA_JURIDICA | numeric(13) |  |  | Outras pessoas jurídicas |
| VALOR_ESTADO_MUNICIPIO | numeric(13) |  |  | Estados e Municípios |
| VALOR_ADMINISTRACAO_PUBLICA | numeric(13) |  |  | Administração Pública |
| VALOR_OUTRA_DEDUCAO | numeric(13) |  |  | Outras deduções |
| I_SCP | integer(4) |  | S | SCP |
| VALOR_PAGO_EXTERIOR | numeric(13) |  |  | Pago no exterior sobre lucros, rendimentos e ganhos de capital |
| VALOR_RECUPERACAO_CREDITO | numeric(13) |  |  | Recuperação de crédito de CSLL |
| VALOR_CREDITO_DEPRECIACAO_IMOBILIZADO | numeric(13) |  |  | Créditos sobre depreciação de imobilizado |
| VALOR_COMPENSACAO_IMPOSTO_FEDERAL_PERIODO_ANTERIOR | numeric(13) |  |  | Compensação de impostos federais de períodos anteriores |
| VALOR_DEDUCAO_PERSE_PGSC | decimal(13) |  | S | Lei Perse e PGSC - Lei 14.148/21 |
| DATA_INICIO_SALDO | date(4) |  | S | Data de início do controle de saldo. |
| DATA_HORA_ALTERACAO | timestamp(8) |  |  | Data de alteração (Usado para forçar disparo da trigger) |
