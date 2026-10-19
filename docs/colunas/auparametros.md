# auparametros — Parametros da auditoria
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| novas_empresas | tinyint(1) |  |  | Auditar novas empresas |
| novos_usuarios | tinyint(1) |  |  | Auditar novos usuarios |
| novas_tabelas | tinyint(1) |  |  | Auditar novas tabelas |
| filtro_empresa | tinyint(1) |  |  | Filtrar auditoria por empresa |
| filtro_usuario | tinyint(1) |  |  | Filtrar auditoria por usuario |
| filtro_tabela | tinyint(1) |  |  | Filtrar auditoria por tabelas |
| EXCLUIR_DADOS_ANTERIORES_A | integer(4) |  |  | Excluir dados anteriores a: (0 - Nunca excluir / 1 - 3 meses / 2 - 1 Ano / 3 - 5 anos) |
