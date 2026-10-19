# GEIMPORTADOR_REGRAS_CLAUSULAS_CONDICOES — Condições das cláusulas das regras
15.396 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_LEIAUTE | integer(4) | PK |  | Código do leiaute |
| CODI_REGISTRO | integer(4) | PK |  | Código do registro do leiaute |
| CODI_REGRA | integer(4) | PK |  | Código da regra |
| CODI_CLAUSULA | integer(4) | PK |  | Código da cláusula |
| CODI_CONDICAO | integer(4) | PK |  | Código da condição |
| CODI_CAMPO | integer(4) |  | S | Código do campo do registro |
| CONDICAO | varchar(2) |  |  | Condição do campo (=/</>/<=/>=/<>/BW/VV/VI/LI/LD) |
| VALOR1 | varchar(32) |  | S | Valor da condição |
| VALOR2 | varchar(32) |  | S | Valor2 da condição entre(BW) |
| OPERADOR | char(1) |  | S | Operador lógico (E/O = Ou) |
| ORIGEM_COLUNA | char(1) |  |  | Origem da coluna (I = Importado/P = Definição de dados atual) |
| DEPENDENTE_CODI_DEFINICAO | integer(4) |  | S | Definição de dados da qual dependente (ORIGEM_COLUNA = P) |
| DEPENDENTE_CODI_TABELA | integer(4) |  | S | Tabela da definição de dados da qual dependente (ORIGEM_COLUNA = P) |
| DEPENDENTE_CODI_COLUNA | integer(4) |  | S | Coluna da tabela da qual dependentee (ORIGEM_COLUNA = P) |
