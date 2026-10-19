# FOEMPREGADOS_CHAVE_PIX_ALTERNATIVA — Cadastro de empregados - Chave Pix alternativa
3 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_EMPREGADOS | integer(4) | PK |  | Empregado |
| I_CHAVE_PIX | integer(4) | PK |  | Sequencial |
| TIPO_CHAVE | smallint(2) |  |  | Tipo da Chave alternativa (1=Celular/2=E-mail/3=CPF/4=Chave Aleatória) |
| CHAVE_PIX | varchar(70) |  |  | Valor da chave Pix alternativa |
| CHAVE_ATUAL | char(1) |  |  | Chave Pix alternativa atual (S/N) |
