# GEIMPORTADOR_LEIAUTES_REGISTROS_CAMPOS — Campos dos registros dos leiautes
23.006 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_LEIAUTE | integer(4) | PK |  | Código do leiaute |
| CODI_REGISTRO | integer(4) | PK |  | Código do registro |
| CODI_CAMPO | integer(4) | PK |  | Código do campo |
| NOME_CAMPO | varchar(64) |  |  | Nome do campo |
| TIPO_CAMPO | char(1) |  |  | Tipo de dado do campo (C = Caractere/R = Decimal/N = Numérico/D = Data/H = Hora/G = Númerico Grande) |
| FORMATO_CAMPO | varchar(32) |  | S | Formato de dado do campo |
| POS_INICIAL | integer(4) |  | S | Posição (inicial) do campo |
| POS_FINAL | integer(4) |  | S | Posição final do campo |
| DEC_INFO | integer(4) |  | S | Casas decimais do campo |
| IDENT_CAMPO | char(1) |  |  | Campo identificador (S/N) / Tipo de elemento (I = Identificador/P = Propriedade/C = Campo/V = Valor) |
| VALOR_CAMPO | varchar(32) |  | S | Valor identificador |
| CODI_EQUIVALENCIA | integer(4) |  | S | Código da tabela de equivalência |
| ORDEM | integer(4) |  |  | Ordem do campo |
| COMENTARIO | varchar(2048) |  | S | Comentário do campo |
| REQUERIDO | char(1) |  | S | Campo requerido (S/N) (Arquivo XML) |
