# GEIMPORTADOR_CAMPOS_CALCULADOS — Campos calculados
3.149 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_DEFINICAO | integer(4) | PK |  | Código da definição |
| CODI_TABELA | integer(4) | PK |  | Código da tabela |
| CODI_COLUNA | integer(4) | PK |  | Código da coluna |
| CODI_CALCULADO | integer(4) | PK |  | Código do campo calculado |
| ORIGEM_COLUNA | char(1) |  |  | Origem da coluna (F = Fixo/I = Importado/P = Própria definição de dados) |
| VALOR | numeric(13) |  | S | Valor fixo |
| CODI_LEIAUTE | integer(4) |  | S | Código do leiaute (ORIGEM_COLUNA = I) |
| CODI_REGISTRO | integer(4) |  | S | Código do registro (ORIGEM_COLUNA = I) |
| CODI_CAMPO | integer(4) |  | S | Código do campo do registro (ORIGEM_COLUNA = I) |
| DEPENDENTE_CODI_DEFINICAO | integer(4) |  | S | Definição de dados da qual depende (ORIGEM_COLUNA = P) |
| DEPENDENTE_CODI_TABELA | integer(4) |  | S | Tabela da definição de dados da qual depende (ORIGEM_COLUNA = P) |
| DEPENDENTE_CODI_COLUNA | integer(4) |  | S | Coluna da tabela da qual depende (ORIGEM_COLUNA = P) |
| OPERACAO | char(1) |  | S | Operação aritmética |
| OPERACAO_GRUPO | char(1) |  | S | Operação do grupo |
| GRUPO | integer(4) |  |  | Grupo |
| ORDEM | integer(4) |  |  | Ordem do campo |
