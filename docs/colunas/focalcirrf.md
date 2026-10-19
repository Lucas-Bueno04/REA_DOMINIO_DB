# focalcirrf — Calculo da Guia de IRRF
10.387 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| periodo_inicio | date(4) | PK |  | Inicio periodo |
| periodo_fim | date(4) |  |  | Fim periodo |
| codigo_rec | integer(4) | PK |  | Codigo recolhimento |
| valor | numeric(13) |  |  | Valor |
| juros | numeric(13) |  |  | Juros |
| multa | numeric(13) |  |  | Multa |
| valor_acum | numeric(13) |  |  | Valor acumulado |
| data_pagto | date(4) |  | S | Data pagamento |
| guia_emitida | tinyint(1) |  |  | is Guia emitida |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| i_pagto | integer(4) |  | S | Sequencial de pagamento |
| vencimento | date(4) |  |  | Data de vencimento |
| I_PARCELAMENTO_ENCARGO_PAGAMENTO | integer(4) |  | S | Código do parcelamento. |
| I_PARCELAMENTO_ITEM | integer(4) |  | S | Código do item do parcelamento. |
| VALOR_PARCELADO | numeric(13) |  | S | Valor parcelado no parcelamento. |
| TIPO_GUIA | smallint(2) | PK |  | Tipo de guia. (1=Empregados e Contribuintes/2=Domésticos) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
