# GECSPERGUNTAS_SOLUCOES — Perguntas e soluções da Central de Soluções
7.968 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| ID | uniqueidentifier(16) | PK |  |  |
| CODIGO | integer(4) |  |  |  |
| SISTEMA | integer(4) |  |  |  |
| MODULO | integer(4) |  |  |  |
| CLASSIFICACAO | integer(4) |  |  |  |
| PROXIMA_REVISAO | timestamp(8) |  | S |  |
| VALIDO_DE | timestamp(8) |  |  |  |
| VALIDO_ATE | timestamp(8) |  | S |  |
| PERGUNTA | varchar(4000) |  | S |  |
| TITULO | varchar(4000) |  | S |  |
| TIPO | integer(4) |  |  |  |
| TAGS | varchar(4000) |  | S |  |
| QUANTIDADE_ACESSOS | integer(4) |  | S |  |
| QUANTIDADE_TOTAL_ACESSOS | integer(4) |  | S |  |
| IDS_TELAS_CONTABIL | varchar(4000) |  | S |  |
| ULTIMA_ATUALIZACAO | timestamp(8) |  | S |  |
| ATIVO | integer(4) |  |  |  |
