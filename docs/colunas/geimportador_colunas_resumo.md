# GEIMPORTADOR_COLUNAS_RESUMO — Colunas exibidas no resumo do importador
483 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| TABELA | varchar(64) | PK |  | Nome da tabela |
| ORDEM | integer(4) | PK |  | Ordem da coluna |
| NOME_COLUNA | varchar(128) |  |  | Nome da coluna no banco |
| DESCRICAO_CABECALHO | varchar(64) |  |  | Descrição no cabeçalho |
| LARGURA | integer(4) |  |  | Larguna no cabeçalho em caracteres |
| FORMATO | varchar(32) |  | S | Formato do valor exibido |
| ALINHAMENTO | char(1) |  |  | Alinhamento do valor exibido (E = Esquerda/D = Direita/C = Centro) |
| UTILIZA_TRATAMENTO | char(1) |  |  | Utiliza tratamento para exibir valor (S = Sim/N = Não) |
