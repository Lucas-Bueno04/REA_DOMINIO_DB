# eftabela_credito_presumido_faixa — Credito Presumido Importacao - Faixas
121.574 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| vigencia | date(4) | PK |  | Vigencia |
| aliquota | numeric(5) | PK |  | Aliquota |
| percentual | numeric(6) |  |  | Percentual de credito |
| TABELA | integer(4) | PK |  | TABELA CRÉDITO PRESUMIDO (1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 / 11 / 12 / 13 / 17 / 18 / 21 / 22 / 26 / 28/ 31/ 34/ 39/40) |
| CODI_EMP | integer(4) | PK |  | Codigo Empresa |
| OPERACAO | char(1) | PK |  | Operação (I - Interna, E - Interestadual, A - Ambas) |
