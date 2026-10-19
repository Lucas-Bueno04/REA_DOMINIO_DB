# GEIMPORTADOR_REGRAS_CLAUSULAS — Cláusulas das regras
6.538 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_LEIAUTE | integer(4) | PK |  | Código do leiaute |
| CODI_REGISTRO | integer(4) | PK |  | Código do registro |
| CODI_REGRA | integer(4) | PK |  | Código da regra |
| CODI_CLAUSULA | integer(4) | PK |  | Código da cláusula |
| IDENTIFICACAO | varchar(64) |  |  | Identificação da cláusula |
| TIPO_RETORNO | char(1) |  |  | Tipo de retorno (F = Fixo/I = Importado/V = variável automática/A = Argumento/P = Própria definição de dados) |
| VALOR_FIXO | varchar(128) |  | S | Valor fixo (TIPO_RETORNO = F) |
| CODI_CAMPO | integer(4) |  | S | Código do campo do registro (TIPO_RETORNO = I) |
| VALOR_AUTOMATICO | char(1) |  | S | Valor da variável automática (D = Data atual/E = Empresa atual/U = Usuario atual) (TIPO_RETORNO = V) |
| CODI_ARG | integer(4) |  | S | Código do argumento (TIPO_RETORNO = A) |
| DEPENDENTE_CODI_DEFINICAO | integer(4) |  | S | Definição de dados da qual dependente (TIPO_RETORNO = P) |
| DEPENDENTE_CODI_TABELA | integer(4) |  | S | Tabela da definição de dados da qual dependente (TIPO_RETORNO = P) |
| DEPENDENTE_CODI_COLUNA | integer(4) |  | S | Coluna da tabela da qual dependentee (TIPO_RETORNO = P) |
