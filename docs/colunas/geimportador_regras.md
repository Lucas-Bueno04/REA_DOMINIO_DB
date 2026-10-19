# GEIMPORTADOR_REGRAS — Regras
1.384 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_LEIAUTE | integer(4) | PK |  | Código do leiaute |
| CODI_REGISTRO | integer(4) | PK |  | Código do registro |
| CODI_REGRA | integer(4) | PK |  | Código da regra |
| NOME_REGRA | varchar(64) |  |  | Nome da regra |
| RETORNO_PADRAO | varchar(64) |  |  | Retorno padrão da regra |
| EXIBIR_ADVERTENCIA_RETORNO | char(1) |  |  | Exibir advertências referentes a retorno (S/N) |
| DEPENDENTE_CODI_DEFINICAO | integer(4) |  | S | Definição de dados da qual as cláusulas dependem |
| PADRAO | varchar(20) |  | S | Padrão da Domínio Sistemas |
