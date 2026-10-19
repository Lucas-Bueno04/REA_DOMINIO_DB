# foguiapis — Guia PIS
1.066 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_GUIAPIS_OLD | integer(4) |  | S | Sequencial de guias - Renomeado |
| codi_emp | integer(4) |  |  | Codigo da empresa |
| competencia | date(4) |  |  | Competencia |
| tipo_process | integer(4) |  |  | Tipo de calculo (Mensal, complementar ou Resilicao) |
| valor | numeric(13) |  |  | Valor |
| vencimento | date(4) |  |  | Vencimento |
| I_GUIAPIS_INI_ACUM_OLD | integer(4) |  | S | Inicio do acumulo - Renomeado |
| situacao | tinyint(1) |  |  | Situacao (1=Emitida, 2=Acumulada, 3=Acumulada Lançada Manualmente) |
| i_pagto | integer(4) |  | S | Sequencia de pagamento |
| valor_mes | numeric(13) |  |  | Valor do mes sem o acumulado |
| SOMOU_ENCARGOS_NA_FOLHA_MENSAL | smallint(2) |  |  | Somou encargos da folha complementar na folha mensal quando forem inferiores ao mínimo de recolhimento. (0=Não/1=Sim) |
| I_PARCELAMENTO_ENCARGO_PAGAMENTO | integer(4) |  | S | Código do parcelamento. |
| I_PARCELAMENTO_ITEM | integer(4) |  | S | Código do item do parcelamento. |
| VALOR_PARCELADO | numeric(13) |  | S | Valor parcelado no parcelamento. |
| VENCIMENTO_PRORROGADO_CONFORME_MP_139_2020 | smallint(2) |  |  | Identifica que o vencimento da guia pis foi prorrogado conforme MP 139/2020. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_GUIAPIS | uniqueidentifier(16) | PK |  | Sequencial de guias |
| I_GUIAPIS_INI_ACUM | uniqueidentifier(16) |  |  | Inicio do acumulo |
| I_GUIAPIS_EXPORTA_IMPORTA | uniqueidentifier(16) |  | S | Coluna utilizada durante o exporta/importa |
| GUIAPIS_DATA_HORA | timestamp(8) |  | S | Data e hora da gravação da guia |
