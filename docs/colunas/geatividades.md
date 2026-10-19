# geatividades — Registro de Atividades - Cadastro
19.995 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_atv | integer(4) | PK |  | Codigo sequencial das atividades |
| codi_emp | integer(4) |  |  | Empresa |
| codi_cla | integer(4) |  |  | Codigo da classificacao |
| codi_usu | char(30) |  |  | Usuario |
| data_atv | date(4) |  |  | Data da atividade |
| hori_atv | time(8) |  |  | Hora inicial da atividade |
| fina_atv | char(1) |  |  | Finalizar a atividade(S/N) |
| horf_atv | time(8) |  | S | Hora final da atividade |
| desc_atv | varchar(500) |  | S | Descricao da atividade |
