# FOCONFIGURACOES_ETIQUETAS_CTPS — Configuração das etiquetas de atualização da CTPS.
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CONFIGURACAO | integer(4) | PK |  | Código da configuração. |
| DESCRICAO | varchar(100) |  |  | Descrição. |
| ALTURA | smallint(2) |  |  | Altura. |
| LARGURA | smallint(2) |  |  | Largura. |
| QUANTIDADE_ETIQUETAS_LINHA | smallint(2) |  |  | Quantidade de etiquetas por linha. |
| QUANTIDADE_ETIQUETAS_COLUNA | smallint(2) |  |  | Quantidade de etiquetas por coluna. |
| MARGEM_SUPERIOR | numeric(13) |  |  | Margem superior. |
| MARGEM_INFERIOR | numeric(13) |  |  | Margem inferior. |
| MARGEM_ESQUERDA | numeric(13) |  |  | Margem esquerda. |
| MARGEM_DIREITA | numeric(13) |  |  | Margem direita. |
| ESPACAMENTO_LINHAS | numeric(13) |  |  | Espaçamento entre linhas. |
| ESPACAMENTO_COLUNAS | numeric(13) |  |  | Espaçamento entre colunas. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout) |
