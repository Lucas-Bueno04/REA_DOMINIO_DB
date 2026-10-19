# GEMENUFAVORITOS — Itens do menu favoritos
431 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_MODULO | integer(4) | PK |  |  |
| I_CONFUSUARIO | integer(4) | PK |  |  |
| I_MENUFAVORITO | integer(4) | PK |  |  |
| I_MENUFAVORITO_PAI | integer(4) |  | S |  |
| NOME | varchar(120) |  |  |  |
| TIPO | smallint(2) |  |  |  |
| I_MODULO_MENU | integer(4) |  |  |  |
| VINCULO | varchar(1000) |  | S |  |
| TIPO_USUARIO | smallint(2) | PK |  |  |
| CAMINHO_MENU | varchar(512) |  | S |  |
| ORDEM | integer(4) |  |  |  |
