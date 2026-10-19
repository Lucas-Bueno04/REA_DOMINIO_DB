# CTNATUREZA_CONTA_BC_GERAL — Natureza das Contas Banco Central
8 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_NATUREZA | integer(4) | PK |  | Codigo da tabela |
| CLAS_CTA | char(20) |  |  | Classificacao da conta |
| NATUREZA | char(1) |  |  | Natureza da conta (C=Credora/D=Devedora) |
| GRUPO | char(1) |  |  | Grupo da conta (A=Ativo/P=Passivo/L=Patrimonio Liquido/R=Contas de Resultado/C=Contas de Compensacao/O=Outras) |
