# foguiainssserv — Guia Inss vs Servico
29.609 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo da empresa |
| i_servicos | integer(4) | PK |  | Código do serviço |
| I_GUIAINSS_OLD | integer(4) |  | S | Sequencial da Guia - Renomeado |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_GUIAINSS | uniqueidentifier(16) | PK |  | Sequencial da Guia |
