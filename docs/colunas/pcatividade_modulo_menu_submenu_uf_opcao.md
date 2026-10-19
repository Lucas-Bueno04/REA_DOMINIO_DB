# PCATIVIDADE_MODULO_MENU_SUBMENU_UF_OPCAO — Módulos - Menu - Submenu - UF - Opção
850 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_OPCAO | integer(4) | PK |  | Código |
| I_MODULO | integer(4) |  |  | Módulo |
| I_MENU | integer(4) |  |  | Menu |
| I_SUBMENU | integer(4) |  |  | Submenu |
| I_UF | integer(4) |  | S | UF |
| NOME | varchar(128) |  |  | Nome |
| ORDEM | integer(4) |  |  | Ordem |
| CONFORME_IMPOSTO | char(1) |  |  | A opção representa um imposto (S/N) |
| CODIGO_IMPOSTO | integer(4) |  |  | Código do imposto no sistema |
| INATIVO | char(1) |  |  | Inativo (S/N) |
