# GEESTACOES — INFORMAÇÕES SOBRE AS ESTAÇÕES
50 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| ENDERECO_MAC | char(12) | PK |  | ENDEREÇO MAC DA PLACA DE REDE |
| ULTIMA_CONEXAO | timestamp(8) |  |  | DATA E HORA DA ÚLTIMA CONEXÃO |
| SO | tinyint(1) |  |  | SISTEMA OPERACIONAL |
| VERSAO_MAIOR_SO | integer(4) |  |  | VERSÃO MAIOR DO SISTEMA OPERACIONAL |
| VERSAO_MENOR_SO | integer(4) |  |  | VERSÃO MENOR DO SISTEMA OPERACIONAL |
| RESOLUCAO_VIDEO_X | integer(4) |  |  | RESOLUÇÃO DE VÍDEO HORIZONTAL |
| RESOLUCAO_VIDEO_Y | integer(4) |  |  | RESOLUÇÃO DE VÍDEO VERTICAL |
| MAIOR_VERSAO_DOTNET | varchar(255) |  |  | MAIOR VERSÃO DOTNET |
| VERSAO_BANCO | varchar(255) |  |  | VERSÃO DO BANCO |
| TIPO_BANCO | smallint(2) |  |  | 1 = BANCO SYBASE / 2 = BANCO DB2 |
| LISTA_VERSOES_DOTNET | varchar(900) |  |  | Lista de versões .net instaladas na estacao |
