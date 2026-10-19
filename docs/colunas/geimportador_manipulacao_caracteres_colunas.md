# GEIMPORTADOR_MANIPULACAO_CARACTERES_COLUNAS — Colunas da manipulação de caracteres
809 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_LEIAUTE | integer(4) | PK |  | Código do leiaute |
| CODI_REGISTRO | integer(4) | PK |  | Código do registro do leiaute |
| CODI_MANIPULACAO | integer(4) | PK |  | Código da manipulação de caracteres |
| CODI_COLUNA | integer(4) | PK |  | Código da coluna da manipulação |
| CODI_CAMPO | integer(4) |  | S | Código do campo do registro |
| VALOR | varchar(32) |  | S | Valor informado |
| OPERACAO1 | char(2) |  | S | Operação de manipulação (SN = Só numeros/SL = Só letras/MA = Maiúsculo/MI = Minúsculo/ES = À esquerda/DI = À direita) |
| QUANTIDADE1 | integer(4) |  | S | Quantidade de caracteres da operação1 |
| OPERACAO2 | char(2) |  | S | Operação de manipulação (SN = Só numeros/SL = Só letras/MA = Maiúsculo/MI = Minúsculo/ES = À esquerda/DI = À direita) |
| QUANTIDADE2 | integer(4) |  | S | Quantidade de caracteres da operação2 |
| OPERACAO3 | char(2) |  | S | Operação de manipulação (SN = Só numeros/SL = Só letras/MA = Maiúsculo/MI = Minúsculo/ES = À esquerda/DI = À direita) |
| QUANTIDADE3 | integer(4) |  | S | Quantidade de caracteres da operação3 |
| ORDEM | integer(4) |  |  | Ordem da coluna |
