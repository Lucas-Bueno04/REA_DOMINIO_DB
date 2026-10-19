# GEPARAMETROS_IMPRESSORA — Parâmetros da impressora
786 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| USUARIO | varchar(120) | PK |  |  |
| NOME_IMPRESSORA | varchar(120) | PK |  |  |
| MODELO | varchar(120) |  | S |  |
| CODIGO_COMPACTACAO10CPP | varchar(40) |  | S |  |
| NOME_ESTACAO | varchar(120) | PK |  |  |
| CODIGO_COMPACTACAO17CPP | varchar(40) |  | S |  |
| CODIGO_COMPACTACAO20CPP | varchar(40) |  | S |  |
| CODIGO_COMPACTACAOOITAVOS | varchar(40) |  | S |  |
| CODIGO_COMPACTACAOSEXTOS | varchar(40) |  | S |  |
| NOME_EXECUTAVEL | varchar(40) | PK |  |  |
| MARGEM_DIREITA | integer(4) |  | S |  |
| MARGEM_ESQUERDA | integer(4) |  | S |  |
| MARGEM_SUPERIOR | integer(4) |  | S |  |
| MARGEM_INFERIOR | integer(4) |  | S |  |
| LARGURA_PAPEL | integer(4) |  | S |  |
| PERCENTUAL_ZOOM | integer(4) |  | S |  |
| LARGURA_CARACTER | integer(4) |  | S |  |
| TIPO | smallint(2) |  | S |  |
| PERCENTUAL_AUMENTAR | numeric(13) |  | S |  |
