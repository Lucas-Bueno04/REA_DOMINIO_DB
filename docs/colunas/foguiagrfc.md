# foguiagrfc — Guia GRFC
4.129 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo da empresa |
| i_empregados | integer(4) | PK |  | Código do empregado |
| tipo | integer(4) | PK |  | Tipo de cálculo de rescisão. (1=Normal/2=Complementar/3=Parcial/4=Simulação) |
| mes_ant_base | numeric(13) |  |  | Base de fgts do mes anterior |
| mes_ant_valor | numeric(13) |  |  | valor de fgts do mes anterior |
| resc_base | numeric(13) |  |  | Base de fgts da rescisao |
| resc_valor | numeric(13) |  |  | Valor de fgts da rescisao |
| aviso_previo_base | numeric(13) |  |  | Base de fgts do aviso previo indenizado |
| aviso_previo_valor | numeric(13) |  |  | Valor de fgts do aviso previo indenizado |
| saldo_fins_resc | numeric(16) |  |  | Saldo para fins rescisórios |
| multa_fgts | numeric(15) |  |  | Multa de fgts |
| i_pagto | integer(4) |  | S | Sequencia de pagamento |
| vencimento | date(4) |  |  | Data de vencimento |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo - Renomeado |
| AGRUPAR_PAGAMENTOS_COMPETENCIA_COMPLEMENTAR | smallint(2) |  |  | Agrupar pagamentos por competência complementar. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| TIPO_ENCARGO | integer(4) |  |  | Tipo de Encargo (1=GRRF/2=FGTS Rescisório) |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo |
