# GECONTROLE_DOMINIO_PROCESSOS — Controla se o escritorio possui ou não permissão para utilizar o Domínio Processos
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | tinyint(1) | PK |  |  |
| TEM_PERMISSAO | integer(4) |  | S | -1 = Erro na requisiÃ§Ã£o 0 = NÃ£o possui acesso ao domÃ­nio processos 1 = Possui acesso ao domÃ­nio processos |
| DATA_HORA_ULTIMA_CONSULTA | timestamp(8) |  | S | Data e hora da Ãºltima consulta feita |
