# foliquidosfil — Liquidos por filial
44.929 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_LIQUIDOSFIL_OLD | integer(4) |  | S | Sequencial - Renomeado |
| codi_emp | integer(4) |  |  | Codigo da empresa |
| i_filiais | integer(4) |  |  | Código da filial |
| competencia | date(4) |  |  | Competencia do calculo |
| tipo_process | integer(4) |  |  | Tipo de calculo |
| vencimento | date(4) |  |  | Data de vencimento/pagto da folha |
| tipo_contrib | char(1) |  |  | Tipo de contribuinte |
| liquido | numeric(13) |  |  | Liquido da folha |
| i_pagto | integer(4) |  | S | Sequencia de pagamento |
| ORIGEM_COMPLEMENTO | smallint(2) |  | S | Origem do complemento. (1=Lançamento de eventos/2=Alteração salarial/3=Rescisão/4=Alteração salarial CCT) |
| INDIVIDUALIZADO | smallint(2) |  |  | Individualizado por RPA. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_LIQUIDOSFIL | uniqueidentifier(16) | PK |  | Sequencial |
| I_LIQUIDOSFIL_EXPORTA_IMPORTA | uniqueidentifier(16) |  | S | Coluna utilizada durante o exporta/importa |
