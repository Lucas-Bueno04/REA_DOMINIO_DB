# pomarcacao — Marcacoes das batidas
1.228 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  |  |
| i_empregados | integer(4) | PK |  |  |
| data_apu | date(4) | PK |  |  |
| data_mar | date(4) | PK |  |  |
| hora | integer(4) | PK |  |  |
| funcao | smallint(2) |  |  |  |
| i_relogios | smallint(2) |  | S |  |
| origem | char(1) |  |  |  |
| hora_aprox | integer(4) |  | S |  |
| seq_entsai | smallint(2) |  | S |  |
| TIPO_ENTSAI | char(1) |  |  | Tipo de marcaCAo E entrada S Saida |
| ORIGEM_MARCACAO | char(1) |  |  | Origem da marcacao: I=Importacao do relogio/M=Manual/C=Convertido/A=Automatico(Gera Marcacoes)/G=Manual em grupo/P=Pre-assinalado(Gera Horario) |
| GRUPO_ENTSAI | integer(4) |  |  | Grupo de Entrada ou Saida |
