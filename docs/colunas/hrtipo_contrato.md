# HRTIPO_CONTRATO — Tipo de contrato
38 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_TIPO_CONTRATO | integer(4) | PK |  | Codigo |
| NOME | varchar(60) |  |  | Nome |
| PERIODICIDADE | tinyint(1) |  |  | Periodicidade 1 Mensal 2 Bimestral 3 Trimestral 4 Quadrimestral 6 Semestral 12 Anual |
| TIPO_REAJUSTE | tinyint(1) |  |  | Tipo de reajuste 1 Mensal 2 Bimestral 3 Trimestral 4 Quadrimestral 6 Semestral 12 Anual 0 Data base |
| MES_BASE | tinyint(1) |  |  | Mes base 1 Janeiro 2 Fevereiro 3 Marco 4 Abril 5 Maio 6 Junho 7 Julho 8 Agosto 9 Setembro 10 Outubro 11 Novembro 12 Dezembro |
| INDEXADOR | char(1) |  |  | Indexador M Moeda corrente I Indices |
| INDICE | char(8) |  | S | Indice |
| PROPORCIONAL | char(1) |  |  | Proporcional a data do contrato S N |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| I_INDICE_REAJUSTE | integer(4) |  | S | Código do índice do reajuste |
