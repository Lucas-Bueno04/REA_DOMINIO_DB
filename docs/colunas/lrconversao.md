# LRCONVERSAO — Conversão do Lalur
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| STATUS | tinyint(1) |  |  | Indica como esta o processo de conversão (0=Não definido/ 1=Dados convertidos/ 2=Atualizou sem converter/ 3=Convertendo) |
| USUARIO | varchar(128) |  | S | Usuário |
| DATA_HORA | timestamp(8) |  | S | Data e hora |
| CONNECTION_ID | integer(4) |  | S | Identificador da conexao |
