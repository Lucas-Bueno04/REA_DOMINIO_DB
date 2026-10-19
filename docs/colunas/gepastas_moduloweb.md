# GEPASTAS_MODULOWEB — Pastas de publicação do Onvio
261 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| MODULO | integer(4) | PK |  |  |
| DEPARTAMENTO | integer(4) | PK |  |  |
| JANELA | varchar(255) | PK |  |  |
| PASTA | long varchar(32767) | PK |  |  |
| PADRAO | smallint(2) |  | S |  |
| PASTA_ONVIO | bit(1) |  |  | 0 - Pasta do DA Legado, 1 - Pasta do Onvio |
