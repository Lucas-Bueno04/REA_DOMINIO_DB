# foguiapisfiliais — Valor de pis por filiais
1.066 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_GUIAPIS_OLD | integer(4) |  | S | Sequencial de guias - Renomeado |
| codi_emp | integer(4) | PK |  | Codigo da empresa |
| valor | numeric(13) |  |  | Valor do pis da filial |
| I_GUIAPIS | uniqueidentifier(16) | PK |  | Sequencial de guias |
