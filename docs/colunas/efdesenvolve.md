# efdesenvolve — DESENVOLVE - BA
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| sequencial | integer(4) | PK |  | Sequencial |
| inicial | date(4) |  |  | Periodo inicial |
| final | date(4) |  |  | Periodo final |
| mes_base | tinyint(1) |  |  | Mes base da correcao |
| percentual | numeric(5) |  |  | Percentual do incentivo |
| carencia | tinyint(1) |  |  | Carencia |
| vencimento | tinyint(1) |  |  | Vencimento |
| resolucao | char(30) |  |  | Resolucao |
| empreendimentos | char(1) |  |  | Empreendimentos ja instalados (S/N) |
