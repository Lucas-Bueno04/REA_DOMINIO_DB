# GEIMPORTADOR_DEFINICAO_DADOS_TABELAS — Tabelas da definição de dados
4.844 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_DEFINICAO | integer(4) | PK |  | Código da definição |
| CODI_TABELA | integer(4) | PK |  | Código da tabela |
| IDENTIFICACAO | varchar(64) |  |  | Identificação da tabela |
| TIPO_TABELA | char(1) |  |  | Tipo da tabela (D = Dados/C = Complementar/T = Temporária) |
| TABELA | varchar(64) |  | S | Nome da tabela |
| DEPENDENTE_CODI_DEFINICAO | integer(4) |  | S | Definição de dados da qual dependente (TIPO_TABELA = C) |
| DEPENDENTE_CODI_TABELA | integer(4) |  | S | Tabela da definição de dados da qual dependente (TIPO_TABELA = C) |
| ORDEM | integer(4) |  |  | Ordem da tabela |
