# PCPROCESSO — Processos
20 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_PROCESSO | integer(4) | PK |  | Código |
| NOME | varchar(60) |  |  | Nome |
| PERIODICIDADE | tinyint(1) |  |  | PERIODICIDADE (1=MENSAL/ 2=BIMESTRAL/ 3=TRIMESTRAL/ 4=QUADRIMESTRAL/ 6=SEMESTRAL/ 12=ANUAL / 24=BIENAL / 36=TRIENAL / 48=QUADRIENAL / 60=QUINQUENAL / 98=DIÁRIA / 99=SEM PERIODICIDADE) |
| I_DEPARTAMENTO | integer(4) |  |  | Código do departamento |
