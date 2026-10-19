# foguiainssemissao — Controle de emissao da guia
21.244 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_GUIAINSS_OLD | integer(4) |  | S | Sequencial da Guia - Renomeado |
| I_GUIAINSS_EMISSAO_OLD | integer(4) |  | S | Sequencial da Guia que pagou(em caso de acumulo) - Renomeado |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_GUIAINSS | uniqueidentifier(16) | PK |  | Sequencial da Guia |
| I_GUIAINSS_EMISSAO | uniqueidentifier(16) | PK |  | Sequencial da Guia que pagou(em caso de acumulo) |
