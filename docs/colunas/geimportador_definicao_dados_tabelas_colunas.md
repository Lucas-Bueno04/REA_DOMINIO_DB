# GEIMPORTADOR_DEFINICAO_DADOS_TABELAS_COLUNAS — Colunas das tabelas da definição de dados
24.631 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_DEFINICAO | integer(4) | PK |  | Código da definição |
| CODI_TABELA | integer(4) | PK |  | Código da tabela |
| CODI_COLUNA | integer(4) | PK |  | Código da coluna |
| NOME_COLUNA | varchar(128) |  | S | Nome da coluna no banco de dados |
| REFERENTE_CODI_DEFINICAO | integer(4) |  | S | Definição de dados que será complementada |
| REFERENTE_CODI_TABELA | integer(4) |  | S | Tabela temporária da definição de dados que será complementada |
| REFERENTE_CODI_COLUNA | integer(4) |  | S | Coluna da tabela temporária que será complementada |
| ORIGEM_COLUNA | char(1) |  |  | Origem da coluna (F = Fixo/I = Importado/V = Variável automática/T = Tabela estrangeira/A = Argumento/R = Regra/C = Calculado/D = Definição de dados/P = Própria definição de dados/M = Manipulação de caracteres/N = Complementar(Nulo)/L = Código de lote automático) |
| VALOR_FIXO | varchar(128) |  | S | Valor fixo (ORIGEM_COLUNA = F) |
| CODI_LEIAUTE | integer(4) |  | S | Código do leiaute (ORIGEM_COLUNA = I) |
| CODI_REGISTRO | integer(4) |  | S | Código do registro (ORIGEM_COLUNA = I) |
| CODI_CAMPO | integer(4) |  | S | Código do campo (ORIGEM_COLUNA = I) |
| VALOR_AUTOMATICO | char(1) |  | S | Valor da variável automática (D = Data atual/E = Empresa atual/U = Usuario atual/S = Sequencial) (ORIGEM_COLUNA = V) |
| COLUNA_QUEBRA | varchar(128) |  | S | Coluna de quebra da variável automática sequencial (VALOR_AUTOMATICO = S) |
| CODI_TABELA_ESTRANGEIRA | integer(4) |  | S | Código da tabela estrangeira (ORIGEM_COLUNA = T) |
| CODI_ARG | integer(4) |  | S | Código do argumento (ORIGEM_COLUNA = A) |
| CODI_REGRA | integer(4) |  | S | Código da regra (ORIGEM_COLUNA = R) |
| CODI_MANIPULACAO | integer(4) |  | S | Código da manipulação de caracteres (ORIGEM_COLUNA = M) |
| DEPENDENTE_CODI_DEFINICAO | integer(4) |  | S | Definição de dados da qual dependente (ORIGEM_COLUNA = D, P) |
| DEPENDENTE_CODI_TABELA | integer(4) |  | S | Tabela da definição de dados da qual dependente (ORIGEM_COLUNA = D, P) |
| DEPENDENTE_CODI_COLUNA | integer(4) |  | S | Coluna da tabela da qual dependentee (ORIGEM_COLUNA = D, P) |
