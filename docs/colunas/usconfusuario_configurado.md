# usconfusuario_configurado — Cadastro de usuário - indica se o usuario esta configurado
2.144 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_confusuario | integer(4) | PK |  | Codigo |
| tipo | smallint(2) | PK |  | Tipo (1=Usuario, 2=Grupo de modulos/menu, 3=Grupo de empresas) |
| modulo | integer(4) | PK |  | Codigo do modulo |
