# ctgruposdva — ESTRUTURA DO DVA
47.624 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | EMPRESA |
| codigo | integer(4) | PK |  | CODIGO |
| classificacao | char(20) |  |  | CLASSIFICACAO |
| descricao | varchar(100) |  |  | DESCRICAO |
| natureza | char(1) |  |  | NATURAZA (S=SINTETICA/A=ANALITICA/T=SUB-TOTAL/L=LUCRO-PREJUIZO) |
| tipo | char(1) |  |  | TIPO (V=VA A DISTRIBUIR/D=DISTRIBUICAO VA) |
| contas | varchar(800) |  |  | CONTAS |
| SALDO | char(1) |  | S | Saldo (D=Total Débito/ C=Total Crédito/ P=Saldo Período/ E=Saldo Exercício) |
