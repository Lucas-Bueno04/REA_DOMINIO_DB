# GEACOES_SUPORTE_CONFIGURACOES — Tabela de configurações de ações exclusivas do suporte
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Código unico |
| QUANTIDADE_MAXIMA_ARQUIVOS | integer(4) |  |  | Quantidade máxima de arquivos de request log |
| TAMANHO_MAXIMO_ARQUIVO | integer(4) |  |  | Tamanho máximo do arquivo de request log |
| TEMPO_ATIVO | integer(4) |  |  | Tempo em horas que o processo ficará ativo |
| CAMINHO | varchar(512) |  |  | Caminho em que os arquivos serão gravados |
| STATUS_INICIADO | integer(4) |  |  | Status request log inciado (Sim - 1; Não - 0 |
| DATA_HORA_INICIO | timestamp(8) |  | S |  |
