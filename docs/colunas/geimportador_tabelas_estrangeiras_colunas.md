# GEIMPORTADOR_TABELAS_ESTRANGEIRAS_COLUNAS — Colunas das tabelas estrangeiras
1.022 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_LEIAUTE | integer(4) | PK |  | Código do leiaute |
| CODI_REGISTRO | integer(4) | PK |  | Código do registro do leiaute |
| CODI_TABELA_ESTRANGEIRA | integer(4) | PK |  | Código da tabela estrangeira |
| CODI_IDENTIFICACAO | integer(4) | PK |  | Código da identificação |
| CODI_COLUNA_TABELA_ESTRANGEIRA | integer(4) | PK |  | Código da coluna da tabela estrangeira |
| NOME_COLUNA | varchar(128) |  | S | Nome da coluna no banco de dados (Tabelas do sistema) |
| CODI_DEFINICAO | integer(4) |  | S | Definição de dados que contém a tabela temporária (Tabelas temporárias) |
| CODI_TABELA | integer(4) |  | S | Tabela temporária pesquisada (Tabelas temporárias) |
| CODI_COLUNA | integer(4) |  | S | Coluna da tabela temporária comparada (Tabelas temporárias) |
| CONDICAO | varchar(2) |  |  | Condição do campo (=/</>/<=/>=/<>) |
| ORIGEM_COLUNA | char(1) |  |  | Origem da coluna (F = Fixo/I = Importado/V = Variável automática/A = Argumento/P = Própria definição de dados) |
| VALOR_FIXO | varchar(128) |  | S | Valor fixo (ORIGEM_COLUNA = F) |
| CODI_CAMPO | integer(4) |  | S | Código do campo do registro (ORIGEM_COLUNA = I) |
| VALOR_AUTOMATICO | char(1) |  | S | Valor da variável automática (D = Data atual/E = Empresa atual/U = Usuario atual) (ORIGEM_COLUNA = V) |
| CODI_ARG | integer(4) |  | S | Código do argumento (ORIGEM_COLUNA = A) |
| DEPENDENTE_CODI_DEFINICAO | integer(4) |  | S | Definição de dados da qual depende (ORIGEM_COLUNA = P) |
| DEPENDENTE_CODI_TABELA | integer(4) |  | S | Tabela da definição de dados da qual depende (ORIGEM_COLUNA = P) |
| DEPENDENTE_CODI_COLUNA | integer(4) |  | S | Coluna da tabela da qual depende (ORIGEM_COLUNA = P) |
| OPERADOR | char(1) |  |  | Operador lógico (E/O = Ou) |
