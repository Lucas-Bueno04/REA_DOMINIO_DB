# ctnatureza_conta — NATUZA DAS CONTAS
7.829 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | EMPRESA |
| ordem | tinyint(1) | PK |  | ORDEM |
| clas_cta | char(20) |  |  | CLASSIFICACAO |
| natureza | char(1) |  |  | NATUREZA (C=CREDORA/D=DEVEDORA) |
| grupo | char(1) |  |  | GRUPO (A=ATIVO/P=PASSIVO/L=PATRIMONIO LIQUIDO/R=CONTAS DE RESULTADO/C=CONTAS DE COMPENSACAO/O=OUTRAS) |
