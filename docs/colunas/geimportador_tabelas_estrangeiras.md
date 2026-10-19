# GEIMPORTADOR_TABELAS_ESTRANGEIRAS — Tabelas estrangeiras
626 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_LEIAUTE | integer(4) | PK |  | Código do leiaute |
| CODI_REGISTRO | integer(4) | PK |  | Código do registro do leiaute |
| CODI_TABELA_ESTRANGEIRA | integer(4) | PK |  | Código da tabela estrangeira |
| NOME_TABELA_ESTRANGEIRA | varchar(64) |  |  | Nome da tabela estrangeira |
| LOCAL_PESQUISA | char(1) |  |  | Local da pesquisa (S = tabelas do Sistema/T = tabelas Temporárias) |
| TABELA | varchar(64) |  | S | Tabela do sistema pesquisada (LOCAL_PESQUISA = S) |
| COLUNA_RETORNO | varchar(128) |  | S | Coluna retornada da tabela pesquisada (LOCAL_PESQUISA = S) |
| CODI_DEFINICAO | integer(4) |  | S | Definição de dados que contém a tabela temporária (LOCAL_PESQUISA = T) |
| CODI_TABELA | integer(4) |  | S | Tabela temporária pesquisada (LOCAL_PESQUISA = T) |
| CODI_COLUNA | integer(4) |  | S | Coluna da tabela temporária retornada (LOCAL_PESQUISA = T) |
| RETORNO_PADRAO | varchar(64) |  | S | Retorno padrão |
| EXIBIR_ADVERTENCIA_RETORNO | char(1) |  |  | Exibir advertências referentes a retorno (S/N) |
| IDENTIFICADOR_EMPRESA | char(1) |  |  | Tabela estrangeira que identifica a empresa no arquivo |
| DEPENDENTE_CODI_DEFINICAO | integer(4) |  | S | Definição de dados da qual as colunas dependem |
| PADRAO | varchar(20) |  | S | Padrão da Domínio Sistemas |
