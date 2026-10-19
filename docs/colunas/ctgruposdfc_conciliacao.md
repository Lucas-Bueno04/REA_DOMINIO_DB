# CTGRUPOSDFC_CONCILIACAO — Estrutura DFC - Conciliacao
1.513 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_CONCILIACAO | integer(4) | PK |  | Codigo |
| ORDEM | integer(4) |  |  | Ordem |
| GRUPO | integer(4) |  |  | Grupo |
| DESCRICAO | varchar(128) |  |  | Descricao |
| NATUREZA | char(1) |  |  | Natureza (A=Analitica/S=Sintetica/G=Grupo) |
| TIPO | char(1) |  | S | Tipo (J=Lucro-Prejuizo/P=Saldo Periodo/S=Sub-Total/T=Total/C=Total crédito/D=Total débito/ I=Inverter natureza do saldo) |
