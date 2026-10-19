# GEPARAMETROS_IMPRESSAO_RELATORIO — Parâmetros de impressao do relatório
2.794 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| USUARIO | varchar(120) | PK |  |  |
| IMPRESSORA_PADRAO | varchar(120) |  | S |  |
| ID_RELATORIO | varchar(120) | PK |  |  |
| NOME_ESTACAO | varchar(120) | PK |  |  |
| PERCENTUAL_ZOOM | integer(4) |  | S |  |
| LARGURA_CARACTER | integer(4) |  | S |  |
| PERCENTUAL_AUMENTAR | numeric(13) |  | S |  |
| ORIENTACAO | smallint(2) |  | S |  |
| ESPACAMENTO_LINHAS | smallint(2) |  | S |  |
| MARGEM_DIREITA | integer(4) |  | S |  |
| MARGEM_ESQUERDA | integer(4) |  | S |  |
| MARGEM_SUPERIOR | integer(4) |  | S |  |
| MARGEM_INFERIOR | integer(4) |  | S |  |
| LARGURA_PAPEL | integer(4) |  | S |  |
| PERSONALIZADAR_MARGEM | smallint(2) |  | S |  |
| PERSONALIZADAR_IMPRESSAO | smallint(2) |  | S |  |
| MODULO | smallint(2) | PK |  |  |
