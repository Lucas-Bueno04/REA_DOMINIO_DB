# FOMENSAGEM_AVISO — Tabela para controle de mensagens e avisos do sistema
18 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| AVISO | integer(4) | PK |  | IDENTIFICAÇÃO DO AVISO |
| USUARIO | char(16) | PK |  | USUÁRIO |
| DATA_AVISO | date(4) |  | S | DATA DO AVISO |
| MOSTRAR | char(1) |  | S | MOSTRAR AVISO NOVAMENTE(S/N) |
