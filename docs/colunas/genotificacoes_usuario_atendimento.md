# GENOTIFICACOES_USUARIO_ATENDIMENTO — Notificações por usuário do Domínio Atendimento
393.561 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| SEQUENCIAL | integer(4) | PK |  |  |
| TIPO_NOTIFICACAO | integer(4) |  |  |  |
| CODIGO | integer(4) |  |  |  |
| USUARIO | integer(4) |  |  |  |
| EMPRESA | integer(4) |  |  |  |
| RESPONSAVEL | integer(4) |  | S |  |
| DEPARTAMENTO | varchar(64) |  | S |  |
| SITUACAO | integer(4) |  |  |  |
| ASSUNTO | varchar(250) |  | S |  |
| TIPO | integer(4) |  | S |  |
| NOME_EMPREGADO | varchar(70) |  | S |  |
| CPF_EMPREGADO | varchar(11) |  | S |  |
| VISUALIZADO | integer(4) |  |  |  |
| ORIGEM_ATENDIMENTO | integer(4) |  |  | Flag que indica se o registro vem do DA(1) ou não (0) |
