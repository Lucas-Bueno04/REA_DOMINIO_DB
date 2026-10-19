# fofgtsfilial — Valor de fgts por filial
14.301 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_FGTSFILIAL_OLD | integer(4) |  | S | Sequencial - Renomeado |
| codi_emp | integer(4) |  |  | Codigo da empresa |
| i_filiais | integer(4) |  |  | Código da filial |
| competencia | date(4) |  |  | Competencia do calculo |
| tipo_process | integer(4) |  |  | Tipo de calculo |
| total_fgts | numeric(13) |  |  | Total de fgts do mes |
| i_pagto | integer(4) |  | S | Sequencia de pagamento |
| vencimento | date(4) |  |  | Data de vencimento |
| TIPO_FGTS | tinyint(1) |  |  | Tipo de FGTS 1 FGTS Normal 2 FGTS CCT |
| COMPETENCIA_RETROATIVA | date(4) |  | S | Competência retroativa(CCT) |
| I_PARCELAMENTO_ENCARGO_PAGAMENTO | integer(4) |  | S | Código do parcelamento. |
| I_PARCELAMENTO_ITEM | integer(4) |  | S | Código do item do parcelamento. |
| VALOR_PARCELADO | numeric(13) |  | S | Valor parcelado no parcelamento. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_FGTSFILIAL | uniqueidentifier(16) | PK |  | Sequencial |
